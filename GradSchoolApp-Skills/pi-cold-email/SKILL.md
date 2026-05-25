# PI Cold Email

## When to use

Trigger when the user wants to draft, refine, or track outreach to a potential PhD advisor. Phrases: "draft a cold email to [PI]", "email [PI] about my application", "reply to [PI]", "follow up with [PI]", "should I follow up with X yet".

Also trigger when the user asks about outreach status, who hasn't replied, or what to send next.

## Core principle

A cold email's job is not to sell yourself — it is to make the PI's decision to spend three minutes on your CV feel obviously worth their time. PIs receive dozens of these per cycle; the failure modes are predictable (generic subject, no specific paper cited, vague hook, weak ask, AI-stilt voice, etiquette violations). The skill is engineered to catch every one of those failures before the email leaves your outbox.

## Behavior

Three modes, user-driven selection.

**Initial outreach.** First contact with a PI. Skill enforces four required inputs, generates a draft, runs the self-critique, requires user revision before saving as ready-to-send.

**Reply.** Response to a PI who replied to a prior outreach (positive, neutral, or asking a question). Skill reads the prior exchange, generates a draft response, runs critique with adjusted weights.

**Follow-up bump.** Short courteous nudge after a non-reply. Skill enforces the minimum wait window, generates a brief draft, runs the abbreviated critique.

Before drafting anything, the skill reads `pi-contacts.md` (if it exists) to detect prior contact with this PI. If found, the skill warns the user and recommends the appropriate mode rather than starting a new initial outreach.

## Required inputs (enforced before any draft is generated)

For **initial outreach mode**, all four inputs must be present before drafting. If any is missing or vague, grill for it before generating:

1. **PI name and program.** Look up `programs/{slug}/scorecard.md` if it exists for context (group size, recent papers, hook). Grill if the program isn't on the user's list yet — there's a reason program-discovery is upstream.

2. **One specific recent paper of theirs you've actually read.** Not skimmed, not the abstract, read. The user must be able to discuss it if the PI replies. Grill: "Which paper? What was the core claim? What surprised you about it?" If the user can't answer the second two, push back — you're not ready to email yet.

3. **The specific hook from your work that connects to theirs.** Drawn from `profile.md` and the scorecard's "user's specific hook" field. Must be specific: "I built an SLM-based optical analog for binary Schwarzschild lensing under Galvez" is a hook; "I'm interested in optics" is not.

4. **The concrete ask.** Calibrated to first contact:
   - "Could you confirm you're considering students for Fall 2027?" (low ask, high info value)
   - "Could I send my SoP draft when ready in case it would inform your read?" (medium)
   - "Would a 15-minute conversation about fit be possible in September?" (higher, only with a strong hook)
   - **Never:** "Can I join your lab?", "Can you interview me?", "Could you guarantee admission?"

For **reply mode**, required inputs are: the PI's exact reply text (pasted in), plus what the user wants to convey (answer their question, accept a meeting, share materials, gracefully exit, etc.).

For **follow-up bump mode**, required inputs are: the date of the prior email and confirmation no reply has been received. The skill enforces the 10-14 day minimum wait.

## Eight-check critique

Run on every draft before it's marked ready-to-send. Mode adjustments noted per check.

1. **Subject line specificity.** Initial: must reference shared work, specific topic, or a clear identity marker. Examples that pass: "Prospective PhD student — optical analogs of gravitational lensing", "On your 2024 PRX paper about entangled-photon networks". Examples that fail: "Prospective PhD student", "Inquiry about PhD program", "Interested in your lab". *Reply: relaxed (subject inherited from thread).* *Follow-up: relaxed (carries from initial).*

2. **Specific paper citation in body.** Must name the paper or its specific result, not "your work" or "your research". Format: "Your 2024 *Nature Photonics* paper on continuous-variable cluster states" or "the result in your recent PRL showing X". *Reply: relaxed if paper was already cited in initial.* *Follow-up: relaxed — short bump doesn't re-cite.*

3. **Hook articulated with evidence.** The connection from your work to theirs must cite a CV-grade specific (project name, technique, advisor, outcome). "I've worked on optical analogs of curved spacetime under Galvez, using SLMs to encode Schwarzschild phase profiles" passes. "I have research experience in optics" fails. *Reply and follow-up: relaxed.*

4. **Concrete ask calibrated to first contact.** Ask must match the relationship stage. Initial outreach with no prior contact cannot ask for a meeting commitment or admission discussion. Flag overreach. *Reply: ask can escalate based on what the PI invited.* *Follow-up: just re-state the original ask, lightly.*

5. **Length within target.**
   - Initial: 120–180 words. Flag if under 100 (insufficient signal) or over 220 (too much for first contact).
   - Reply: 80–150 words.
   - Follow-up: 50–80 words. Hard cap 100.

6. **No begging or apologetic language.** Flag and demand replacement: "sorry to bother you", "I know you're very busy", "I hope this isn't an imposition", "if you have time" (when used as preface, not modifier on the ask), "I apologize for", "I would be honored if". These signal low status and make the PI's mental cost of replying feel higher.

7. **No pseudo-flattery.** Flag and demand replacement: "your groundbreaking work", "your incredible papers", "your fascinating research", "I greatly admire", "world-renowned", "leading expert". Replace with specific claims about a specific result. *Follow-up: relaxed — short bump skips flattery entirely, so this check rarely fires.*

8. **Signature includes affiliation plus one credibility marker.** Affiliation is your current school + program + year. Credibility marker is one of: research advisor, key publication (in prep / under review / published), notable fellowship or scholarship, conference presentation. Not all of them — one. Flag bare-name signatures as weak; flag CV-paste signatures as overdone.

For each finding: location (quoted phrase), what's wrong (which check failed), and a concrete revision direction.

## Physics-specific conventions (baked in)

The skill warns or refuses based on these conventions before drafting:

1. **Season.** July through early October is peak outreach. Mid-October onward is weak — PIs are buried in applications and your email gets lost. The skill warns if the current month is November–June and asks if there's a specific reason (e.g., already admitted, post-rejection inquiry, late-cycle gap).

2. **Day-of-week for send.** The skill recommends Tuesday, Wednesday, or Thursday morning in the PI's local time. Mondays drown in weekend backlog; Fridays get postponed to Monday and lose freshness. The draft output includes a recommended send time.

3. **Follow-up delay.** Minimum 10 calendar days, ideal 12–14, after the initial. The skill computes elapsed days from `pi-contacts.md` and refuses to draft a follow-up before 10 days have passed (suggesting the user wait). Maximum one follow-up. The skill refuses to draft a second follow-up — if the PI hasn't replied after one bump, treat as a no.

4. **Per-program soft cap of 3 PIs.** Physics departments are small and faculty compare notes. The skill warns at 3 contacts within a single program and refuses without explicit override at 4+. Tracks count via `pi-contacts.md`.

5. **Attachments.** Initial emails should not attach SoP, CV, or transcripts. Offer to share them if the PI is interested. The skill flags any draft mentioning an attachment in initial mode. *Reply mode:* attaching is fine if the PI asked.

## Output protocol

After the user has revised the draft to their satisfaction, save two artifacts.

### Per-program draft file

Path: `programs/{program-slug}/outreach/{pi-slug}-{type}-{YYYY-MM-DD}.md`

PI slug is `lastname-firstinitial` in kebab-case (e.g., `vuletic-v`, `yamamoto-y`, `wehner-s`). Type is `initial`, `reply`, or `followup`. Date is the planned send date in ISO format.

File contents:

```markdown
# Outreach to [Full PI Name] | [Program full name] | [Type] | [Date]

## Recommended send time
[Day of week + morning + PI's local time, e.g. "Tuesday or Wednesday morning, Cambridge MA time"]

## Subject
[Subject line]

## Body
[Body text]

## Critique findings (resolved before save)
[List of issues caught during self-critique and how each was resolved. This is for your future reference — e.g. "Replaced 'your groundbreaking work' with specific reference to 2024 PRX paper on CV cluster states".]

## Notes
[Any context the user wants to preserve — why this PI, what specific reply you're hoping for, etc.]
```

### Root contact log

Path: `pi-contacts.md` (project root).

If the file doesn't exist, create it with the template below. If it exists, update the row for this PI (or add a new row).

```markdown
# PI Outreach Log
<!-- last updated: YYYY-MM-DD by pi-cold-email -->

## Quick view: next actions (next 14 days)
[Auto-derived from the table below — list each upcoming action sorted by date.]
- 2026-08-15: Follow up with Vuletic (MIT) — initial sent 2026-08-01, no reply yet
- 2026-08-18: Send initial to Yamamoto (Stanford)

## All contacts

| PI | Program | Last contact | Type | State | Days since | Next action | Draft path |
|---|---|---|---|---|---|---|---|
| [Full name] | [program slug] | [YYYY-MM-DD] | initial/reply/followup | sent / replied / no-reply / closed / declined | N | send-initial / follow-up / await-reply / none | [link to draft] |

## Per-program PI counts
[Track count per program to enforce the soft cap of 3.]
- mit-physics: 2 contacts
- stanford-physics: 1 contact
- ...

## Notes
[Cross-PI observations. E.g. "Vuletic and Schuster are co-PIs on a recent paper — coordinate timing." or "Three Princeton PIs would trigger the soft cap — pick the top 3."]
```

## Cross-skill behavior

- **Reads `programs.md`** to know which programs are in scope. Will not draft outreach to a PI at a program not on the target list — recommends running program-evaluation first.
- **Reads `programs/{slug}/scorecard.md`** to look up the PI's group, recent papers, and the user's pre-articulated hook.
- **Reads `profile.md`** for the user's background, technical signature, and credibility markers for the signature.
- **Does not write to `profile.md` or `programs.md`.** Those files are owned by other skills.
- **Owns `pi-contacts.md`** and `programs/{slug}/outreach/*.md`. No other skill writes to these.

## Anti-patterns

- **Drafting before all four required inputs are confirmed.** No exceptions — generic inputs produce generic emails which produce no replies.
- **Letting the user skip revision after generation.** The draft is a starting point, not a sendable artifact. Make this explicit: "Revise this into your own voice before sending. AI-stilted phrasing is the most common reason cold emails get ignored."
- **Ignoring the prior-contact check.** Always read `pi-contacts.md` first. Starting a fresh initial outreach to someone already contacted is a serious error.
- **Drafting a second follow-up.** One bump max. Train the user to accept silence as a no.
- **Generating outreach for a PI not on the program list.** Run program-evaluation first. Outreach without evaluation is uncalibrated.
- **Generic critique findings.** "This could be more specific" is not a finding. Point to the exact phrase and propose the exact direction of revision.
- **Bypassing the seasonal warning for off-cycle outreach.** Warn explicitly and require user acknowledgment before proceeding.
- **Padding the contact log with notes that should be in `profile.md` or scorecards.** The log tracks outreach state. Cross-program observations are fine; PI-evaluation notes belong in the scorecard.
