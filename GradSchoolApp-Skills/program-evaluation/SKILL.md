# Program Evaluation

## When to use

Trigger when the user wants a deep evaluation of a single program already on their candidate list — a rich scorecard supporting go/no-go and SoP-tailoring decisions. Phrases: "evaluate [program]", "deep dive on X", "scorecard for Y", "is [program] worth applying to".

For first-pass discovery of which programs belong on the list, use the Program Discovery skill instead.

## Behavior

Read `profile.md` from the project before searching. Produce a structured scorecard for one program at a time. Mandatory web search for every field — flag any field that couldn't be verified rather than guessing.

After producing the scorecard, write it to disk inside a per-program folder under `programs/`, and create the matching `essays/` subfolder so essay-coach skills (sop-coach, future ps-coach and rs-coach) can drop tailoring blocks there.

## Output folder structure

For a program named e.g. "MIT-physics", produce:

```
programs/
└── MIT-physics/
    ├── scorecard.md     ← this skill writes here
    └── essays/          ← empty folder created here, populated later by essay skills
```

Folder names use kebab-case, lowercase, university-first when ambiguous (e.g. `mit-physics`, `rochester-optics`, `boulder-jila`, `delft-qutech`).

## Scoring criteria (weighted)

| Criterion | Weight | What it measures |
|---|---|---|
| PI fit | 40% | How directly the user's target PIs work on the user's stated subfields, and whether they're actively taking students |
| Program quality in optics-photonics | 15% | Specialty strength, not general USNews rank |
| Funding security for international students | 15% | Years guaranteed, stipend level, international eligibility for top-up fellowships |
| Location and cost-of-living | 10% | Geography preference fit and stipend-to-COL ratio |
| Placement record | 10% | Recent PhD alumni outcomes from target PIs' groups |
| Application feasibility | 10% | Admit rate, deadline pressure, materials match to user's profile |

Each criterion scored 1–10 with a one-sentence justification. Weighted total at the bottom.

## Output format (scorecard.md contents)

### Program: [name] | Tier: [reach/match/safety]

#### Scorecard
Six criteria with 1–10 scores and one-sentence justifications. Weighted total.

#### Target PIs (top 3)
For each:
- Name, title, and group/lab name
- Group size (current PhDs + postdocs, if findable)
- 2–3 recent papers (last 3 years) with one-line summaries
- Recent PhD alumni placements (2–4 most recent if findable)
- The user's specific hook into this PI's work, tied back to a concrete project from `profile.md`

#### Funding details
- Years of guaranteed funding
- Annual stipend, with source (TA / RA / fellowship)
- Summer support policy
- Fellowship match / top-up policy
- International-student eligibility for internal fellowships

#### Application logistics
- Deadline
- Application fee + fee waiver policy
- GRE policy (required / optional / not accepted)
- Required materials (SoP, PS, research statement, writing sample, transcripts, LoR count)
- International-student application contact or office

#### Program quirks
- Cohort size (recent years)
- Admit rate (public number if available, community-estimated otherwise — flag the source)
- Qualifier exam style (oral / written / coursework-only / candidacy paper)
- Coursework load and time-to-candidacy
- Rotations vs. direct admit
- Anything unusual (master's en route, distribution requirements, language requirements, etc.)

#### Community signal
2–4 bullet points from community sources (Reddit, GradCafe, PhysicsGRE, 1point3acres). Quote briefly when useful and attribute by source type (not username). Frame as signal, not verdict.

#### Red flags
Any concerns: funding cuts, PI leaving, group shrinking, state policy issues affecting international students (e.g., FL SB 846), recent climate or culture issues. Leave empty if none found — don't invent.

#### Unknowns
List every field that couldn't be verified during search. Always include this section, even when empty (write "None — all fields verified" in that case). Never fill unknowns with guesses.

#### Audit
```
<!-- last updated: YYYY-MM-DD by program-evaluation -->
```

## Update profile.md Target programs summary

After writing the scorecard, also update the **Target programs** section in `profile.md` — add or refresh a row for this program with:

- Program name | tier | weighted total | top PI | one-line fit | relative path to scorecard (e.g., `programs/mit-physics/scorecard.md`)

This keeps `profile.md` usable as a dashboard. Use the clean-rewrite-with-audit-comment protocol for this section.

## Sources to use

- Program website (faculty pages, grad handbook PDF, financial support page) — always primary
- Google Scholar / arXiv / Optica publications for PI work
- LinkedIn for alumni placement signal where accessible
- GradCafe results page for the program (acceptance/rejection dates, profile signals)
- r/PhysicsGradSchool, r/GradSchool, PhysicsGRE forum
- 1point3acres.com for international-student-specific signal (partial access expected)

## Anti-patterns

- Filling unknown fields with confident-sounding guesses
- Scoring without a justification sentence
- Quoting community sources as if they were verdicts
- Skipping the Unknowns section when everything checked out — write "None" explicitly
- Evaluating a PI who hasn't published in the user's subfield in the last 3 years without flagging that as a concern
- Recommending the program based on prestige when PI fit scores low
- Writing the scorecard without also updating profile.md's Target programs section
- Forgetting to create the `essays/` subfolder — essay skills depend on it existing
