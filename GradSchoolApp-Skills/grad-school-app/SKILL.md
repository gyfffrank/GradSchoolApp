# Grad School App

## When to use

Trigger when the user wants a cross-cutting view of their application state, a recommendation on what to work on next, or an updated calendar of upcoming dates. Phrases: "what should I work on this week", "where am I in the process", "give me a status update", "regenerate my calendar", "what's coming up", "am I on track".

Also trigger when the user has 30 minutes or an hour and doesn't know where to spend it — this skill answers that.

## Scope (deliberately narrow)

This skill does **not** do essay work, program research, outreach drafting, or evaluation. Those are owned by the specialist skills. This skill is the **orchestrator** — it reads every other artifact, computes state, surfaces the most time-sensitive or highest-leverage next actions, and produces two outputs at root:

1. `application-status.md` — human-readable dashboard, regenerated each invocation
2. `calendar.ics` — importable calendar file with deadlines, outreach milestones, and recommended check-ins, regenerated each invocation

Scope creep into specialist territory is the primary failure mode. If the user asks "should this paragraph be tighter?" — that's sop-coach. "Is the MIT scorecard up to date?" — that's program-evaluation. This skill points to the right specialist; it doesn't do their work.

## Inputs

Read all of the following before producing any output:

- `profile.md` — applicant context, target tier strategy, citizenship constraints
- `programs.md` — full target list with deadlines, tiers, evaluation status, fit hooks
- `pi-contacts.md` — every PI contact, state (sent / replied / no-reply-N-days / closed / declined), next action
- All `programs/{slug}/scorecard.md` files — to detect missing or stale scorecards
- All `programs/{slug}/essays/sop-tailoring.md` files — to detect missing or stale tailoring drafts
- All `programs/{slug}/outreach/*.md` files — to count contacts per program and detect overdue follow-ups
- `core-sop.md` — to detect whether the core draft exists yet

If a required file is missing entirely, the dashboard notes the missing piece as a blocker and recommends the upstream skill to run.

## Optional grilling at session start

If the user invoked the skill without context, ask **at most two** questions before producing output:

1. *"How much time do you have for application work this week — under 5 hours, 5–10, 10+?"*
2. *"Any specific focus this week — essays, outreach, program research, or open?"*

If the user gives the focus inline ("plan my essay work this week"), skip the questions. If the user says "just give me the status", skip the questions and produce the full dashboard.

## Prioritization heuristics for the weekly planner

When ranking action items, weight by:

1. **Hard deadline proximity** — every action chained to a fixed deadline (application due date, recommender LoR deadline) gets priority over flexible ones. Within deadlines, sort earliest-first.
2. **Time-decaying opportunity** — PI cold-email season (July–early October) is a depreciating asset. After mid-October, outreach drops priority sharply. Surface this explicitly.
3. **Tier weighting** — actions for reach programs get a small bump over match, match over safety. Don't overweight this — a missed safety deadline still loses the slot.
4. **Blocking-chain depth** — actions that unblock other actions get bumped. "MIT scorecard missing" blocks the MIT SoP tailoring, which blocks the final MIT application; that chain rate-limits MIT entirely, so the scorecard is high priority.
5. **Staleness** — items not progressed in 14+ days get a "stalled" flag even if not formally blocking anything. Stale items signal where the user is avoiding work — sometimes there's a real reason (waiting on a recommender) and sometimes there isn't.
6. **Cost-to-progress** — actions that move state with under 30 min of work are surfaced separately as "quick wins" so the user can knock out housekeeping when low on energy.

## application-status.md format

Regenerated cleanly on each invocation (full rewrite, not append). Structure:

```markdown
# Application status
<!-- last updated: YYYY-MM-DD by grad-school-app -->

## Top 5 actions this week
[Ranked by the prioritization heuristics above. Each item:
- One line action with the program/PI named
- One-line rationale (why this is top-5 right now)
- Estimated time
- The specialist skill to invoke for it]

## Time pressure
- **Days to earliest deadline:** N ([program])
- **Days to PI cold-email window close (Oct 15):** N
- **Days to most reach deadlines:** ~N (cluster around [date])

## State by program
| Program | Tier | Scorecard | Core SoP applies | Tailoring | Outreach | Deadline | Days |
|---|---|---|---|---|---|---|---|
| [name] | reach | ✓ / missing / stale | ✓ | ✓ / missing | N PIs contacted | YYYY-MM-DD | N |
| ... | ... | ... | ... | ... | ... | ... | ... |

## Outreach state
- **PIs contacted:** N total, across M programs
- **Awaiting reply:** N (oldest: [PI], [N] days)
- **Follow-up due this week:** [list with dates]
- **Per-program counts:** [flag any approaching the 3-PI soft cap]

## Stalled items (no progress in 14+ days)
- [item] — last touched YYYY-MM-DD
- ...

## Quick wins (<30 min each)
- [item]
- ...

## Blockers
[Items waiting on something external: recommender response, program info request, etc.]
- [item] — waiting on [whom/what] since YYYY-MM-DD

## Recommendations
[Free-form: 2–4 sentences calling out anything the user should think about that doesn't fit the structured sections — e.g. "Your reach tier has 4 deadlines in a 5-day window in December; consider drafting tailoring blocks for all 4 by mid-November rather than treating them sequentially."]
```

## calendar.ics format

Regenerated cleanly on each invocation. Standard iCalendar 2.0 file at project root.

Cover these event types, with stable UIDs so re-importing updates existing events rather than duplicating:

### 1. Application deadlines (all-day)
- One VEVENT per program with a known deadline
- UID format: `deadline-{program-slug}@gradschoolapp`
- SUMMARY: `[Program name] — application deadline`
- DESCRIPTION: tier, top PI, link to scorecard path
- CATEGORIES: `Deadline`
- VALARM 14 days prior + VALARM 2 days prior

### 2. Recommended submission buffer (all-day, 7 days before deadline)
- UID format: `submit-{program-slug}@gradschoolapp`
- SUMMARY: `[Program name] — target submission date (7-day buffer)`
- CATEGORIES: `Buffer`
- VALARM 7 days prior

### 3. Outreach send windows (timed, Tue/Wed/Thu morning)
- One VEVENT per pending initial outreach in `pi-contacts.md` with `next action: send-initial`
- UID format: `outreach-{pi-slug}-{program-slug}-initial-{date}@gradschoolapp`
- DTSTART: 09:00 floating local time on the planned send date
- DURATION: 30 minutes
- SUMMARY: `Send initial outreach to [PI] ([program])`
- DESCRIPTION: link to draft path, paper to reference, hook
- CATEGORIES: `Outreach`

### 4. Follow-up windows (timed, when 10-day minimum elapses)
- One VEVENT per pending follow-up
- UID format: `outreach-{pi-slug}-{program-slug}-followup-{date}@gradschoolapp`
- DTSTART: morning of day 12 after initial send (sweet spot in 10–14 window)
- SUMMARY: `Follow-up window opens: [PI] ([program])`
- CATEGORIES: `Outreach`

### 5. Cold-email season close (single all-day event Oct 15)
- UID format: `outreach-season-close-{year}@gradschoolapp`
- SUMMARY: `PI cold-email season closing — last call`
- VALARM 14 days prior
- CATEGORIES: `Milestone`

### 6. Skill check-in milestones (all-day, derived)
- "Run program-evaluation on all reach programs" — 90 days before earliest reach deadline
- "Draft core SoP" — 75 days before earliest deadline
- "Complete tailoring blocks for all reaches" — 30 days before earliest reach deadline
- "Confirm recommenders have everything" — 21 days before each deadline
- UID format: `milestone-{name}-{date}@gradschoolapp`
- CATEGORIES: `Milestone`

### Calendar structure

Wrap in standard VCALENDAR envelope:

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//GradSchoolApp//Skills//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Grad School Application
X-WR-CALDESC:Deadlines, outreach milestones, and check-ins for the Fall 2026 application cycle

[VEVENT blocks]

END:VCALENDAR
```

Every VEVENT must include DTSTAMP (the regeneration timestamp). All-day events use `DTSTART;VALUE=DATE:YYYYMMDD`. Timed events use floating local time as `DTSTART:YYYYMMDDTHHMMSS`. Use CRLF line endings if filesystem write allows; otherwise LF is acceptable for modern clients.

The user imports `calendar.ics` into their calendar app. Stable UIDs mean re-importing after regeneration updates existing events in place rather than creating duplicates — Google Calendar, Apple Calendar, and Outlook all honor this.

## Anti-patterns

- **Doing specialist work.** If the user asks about essay craft, program quality, or outreach phrasing during a status session, point to the specialist skill rather than answering directly.
- **Generating a status report longer than the user will read.** The Top 5 actions section is the most-read part; everything else is reference. Keep prose minimal.
- **Inventing actions not grounded in the artifacts.** Every action item must trace to an actual file state — a missing scorecard, an overdue follow-up, a deadline, a stale item. Don't recommend "research more programs" if discovery is complete.
- **Treating the calendar as a one-time generation.** It's regenerated every invocation. Tell the user to re-import after each regen.
- **Asking more than two grilling questions at session start.** This skill should be fast. Heavy interrogation belongs in grill-me, not here.
- **Ignoring time-decay.** Outreach season closes mid-October. Mid-September with no outreach activity is a flag, not a neutral state.
- **Writing to anything other than `application-status.md` and `calendar.ics`.** Every other file is owned by another skill.
- **Surfacing only what's going well.** Stalled items, blockers, and unmet target counts are higher-signal than progress made. Lead with what needs attention.
