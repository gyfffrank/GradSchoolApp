# Program Discovery

## When to use

Trigger when the user wants to identify candidate programs for their PhD or MS applications — the first-pass triage from a broad universe down to a working list of ~20–30 candidates. Phrases: "find me programs", "what schools should I apply to", "build my target list", "discover candidates".

For deep evaluation of a single program already on the list, use the Program Evaluation skill instead.

## Behavior

Read `profile.md` from the project before searching. If `profile.md` is missing, ask the user to run profile-builder first — discovery without a profile produces generic ranking advice, not useful triage.

Produce a ranked candidate list (default 20–30 PhD programs, plus a separate MS section if MS is part of the user's strategy) calibrated to:
- Target subfields
- Geographic preferences
- Citizenship and funding eligibility
- Tier strategy (reach/match/safety counts from profile)
- Profile strength (GPA, publications, research experience)

Show the list to the user inline first. After the user has confirmed or edited the list, write it into `profile.md`'s **Target programs** section so downstream skills (program-evaluation, sop-coach) can read it.

Use web search aggressively. Do not rely on training-data knowledge for program quality, faculty roster, or current research focus — these change.

## Process

1. Read `profile.md`. Confirm subfields, geography, citizenship, MS-vs-PhD scope, tier counts before searching.
2. Search broadly for programs in the relevant subfields. Combine queries: "[subfield] PhD programs", "[subfield] faculty [region]", "best optics graduate programs". Cross-reference USNews physics specialty rankings and Optica rankings as inputs, not as the basis.
3. For each candidate, identify 1–2 specific PIs whose recent work (last 3 years) matches the user's interests. A program without PI alignment does not belong on the list — drop it.
4. Tag each candidate by tier:
   - **Reach:** top-tier programs, or programs with very low international-student admit rates
   - **Match:** solid fit with reasonable admission odds given the user's profile
   - **Safety:** programs where the user's profile clearly exceeds typical admits
5. Flag any community red flags surfaced during search (program shrinking, funding cuts, PI leaving, state policy issues for international students) — but only as flags, not as verdicts.
6. Show the inline list to the user, get edits, then write to profile.md.

## Inline output format

Group by tier. For each program:
- Program name + university + tier tag
- 1–2 PIs of interest, each with a one-line research summary
- One-line fit justification tying back to the user's profile ("Galvez-style optical analog work aligns with X's structured-light group")
- Any flagged concerns

End with:
- Total count by tier vs. target ratio
- A 2–3 sentence summary of how the list addresses the user's stated strategy
- Any tier that came up short and why

## Write-back to profile.md

After user confirmation, write the **Target programs** section in `profile.md` using clean-rewrite with audit comment:

```markdown
## Target programs
<!-- last updated: YYYY-MM-DD by program-discovery -->

### PhD programs

| Program | Tier | Weighted score | Top PI | One-line fit | Scorecard |
|---|---|---|---|---|---|
| [Name + university] | reach | _pending_ | [PI name] | [one-line hook] | _not yet evaluated_ |
| ... | ... | ... | ... | ... | ... |

### MS backups

| Program | Tier | Weighted score | Top PI | One-line fit | Scorecard |
|---|---|---|---|---|---|
| ... | ms-backup | _pending_ | ... | ... | _not yet evaluated_ |
```

Scorecard column shows `_not yet evaluated_` until program-evaluation produces one; weighted score shows `_pending_` for the same reason. The program-evaluation skill replaces both values when it runs.

Folder slug for each program is derived as kebab-case (e.g., `mit-physics`, `rochester-optics`, `boulder-jila`). The Scorecard column will eventually link to `programs/{slug}/scorecard.md`.

## Sources to use

- Program websites and faculty pages (always primary)
- Google Scholar / arXiv for recent PI publications
- USNews and Optica rankings as cross-references only
- GradCafe results pages for admit-rate signal
- r/PhysicsGradSchool, r/GradSchool, PhysicsGRE forum for community comments
- 1point3acres.com for international-student-specific signal (note: often requires login; partial access expected)

## Anti-patterns

- Returning prestige rankings without PI-level fit (the user can find USNews themselves)
- Listing programs without naming specific PIs
- Citing community comments as verdicts rather than signals
- Failing to read `profile.md` before searching
- Padding the list to hit the target count when fewer programs genuinely fit — better to flag the shortage
- Writing to profile.md silently — always show the user the inline list first and get explicit confirmation before the write-back
- Forgetting to write the Target programs section at all — downstream skills depend on it being there
