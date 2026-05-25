# Profile Builder

## When to use

Trigger when the user wants to create or update a `profile.md` for their grad school application project. Phrases: "build my profile", "create profile.md", "set up my profile", "update my profile". Also trigger automatically when another skill (program-discovery, program-evaluation, sop-coach, etc.) tries to read `profile.md` and finds it missing or critically incomplete.

`profile.md` is the foundational document the rest of the grad-school-app skill set depends on. It is a **living document** — built once here, then continuously updated by sop-coach (narrative section) and by any skill that surfaces new facts (research, recommenders, etc.). The target program list lives in a separate file (`programs.md`) maintained by the program skills.

## Behavior

Two phases, in order.

**Phase 1 — Extract from the CV.** Read the user's CV from project files (PDF, DOCX, or markdown). Pull out everything already documented and put it straight into the draft without asking: education, GPA, coursework, research projects, technical skills, publications, awards, community involvement. Time spent reading is cheaper than the user's time spent typing.

**Phase 2 — Grill for the gaps.** A CV documents the past; `profile.md` needs forward-looking and self-assessment information the CV doesn't carry: target subfields, career goals, geographic preferences, citizenship/visa, application tier strategy, recommender list, strengths/weaknesses, hard constraints. Apply the **grill-me skill's rules**: one question at a time, every question paired with a recommended answer based on what the CV showed, push back on vague answers, finish each branch before opening another.

End by drafting `profile.md`, showing it to the user, accepting edits, and writing the final version to the project root.

## Process

1. **Locate the CV.** Check project files. If missing, ask the user to upload one — grilling without a CV produces generic recommendations and wastes the user's time.

2. **Read the CV thoroughly.** Note the following before asking anything:
   - Strongest research projects (most recent, longest, deepest involvement, publications attached)
   - Methodological signature (theory / experiment / computation / instrumentation / data analysis)
   - Subfields touched (these inform target-subfield recommendations but are not assumed to BE the target)
   - Likely recommenders (advisors named in research entries, course instructors for tutoring roles)
   - GPA, school standing, fellowships/awards

3. **Begin grilling in this order** (upstream dependencies resolved first):
   1. Target subfields (primary, plus open-to set)
   2. Career goals (academic faculty / industry research / national lab / quantum-tech startup / unsure)
   3. Geographic preferences (primary region, secondary, avoid)
   4. Citizenship and visa status (affects fellowships and some state-level restrictions)
   5. Application tier strategy (total PhD count, reach/match/safety ratio)
   6. MS backup strategy (yes/no, count, US/EU mix)
   7. Recommender list (3–5 names, relationship, which project they'd speak to, primary vs. backup tier)
   8. Self-assessed strengths (corroborate with CV; push back on claims without evidence)
   9. Gaps and weaknesses to address before applying
   10. Hard constraints and deal-breakers

   Use the grill-me format: one sentence framing, recommendation with one-sentence reason rooted in the CV, then the question. Keep each turn under ~6 sentences.

4. **Draft `profile.md`** using the template below. CV-extracted fields filled in directly; grilled fields filled from user answers. Quote specific CV evidence for strengths.

5. **Show the draft to the user** and ask for edits or additions. Don't assume silence is approval.

6. **Once approved, write `profile.md` to the project root.**

## profile.md template

```markdown
# Profile
<!-- last updated: YYYY-MM-DD by profile-builder -->

## Target subfields
- **Primary:** [e.g., quantum optics, quantum photonics, quantum networks]
- **Open to:** [adjacent areas, e.g., AMO physics, integrated photonics, nonlinear optics]

## Career goals
[1–3 sentences: what they want to do post-PhD and why]

## Geography
- **Primary:** [region + reason]
- **Secondary:** [region + reason]
- **Avoid:** [region + reason, e.g., FL state-funded institutions for Chinese nationals due to SB 846]

## Citizenship and visa status
[Citizenship; current visa; implications for fellowships]

## Application tier strategy
- **Total PhD programs:** N
- **Reach / Match / Safety:** a / b / c
- **MS backups:** N programs ([list specific schools if decided])
- **Total applications:** N
- **Estimated budget:** $X for fees (before waivers)

> The actual program list is maintained separately in `programs.md` at the project root.

## Academic background
- **Institution:** [school, current year, expected graduation]
- **GPA:** X.XX / 4.00
- **Notable coursework:** [graduate-level or signal-rich classes]
- **Awards / honors:** [pull from CV]

## Research experience
[Reverse chronological. For each significant project:]

### [Project name] | [Advisor] | [Dates]
- **Summary:** [one-paragraph in user's own words — what was done and why it matters]
- **Methods and skills:** [techniques, instruments, software]
- **Outcomes:** [publications, presentations, status — be specific about which conference, which journal, submitted vs. under review vs. published]

## Technical skills
- **Programming:** [languages + proficiency level + relevant libraries]
- **Lab / instrumental:** [equipment, techniques]
- **Mathematical / analytical:** [methods, modeling]

## Publications and presentations
[Specific list with venue, date, status]

## Recommenders
[For each — 3 to 5 entries]
- **[Name], [title], [institution]**
  - Relationship: [advisor, course instructor, etc.]
  - Projects together: [which CV entries this maps to]
  - Topics they would speak to: [specific strengths they witnessed]
  - Tier: primary / backup

## Self-assessed strengths
[Each bullet backed by specific CV evidence]
- ...

## Gaps and weaknesses to address
[Honest list — what's missing or weak]
- ...

## Hard constraints and deal-breakers
[Things that disqualify a program regardless of fit]
- ...

## Scientific identity narrative
<!-- append-only section, written by sop-coach and future ps-coach / rs-coach -->
<!-- Each subsection accumulates timestamped session blocks as the user articulates their scientific identity through essay work. -->

### Intellectual lineage
[bio-style prose paragraphs added over time]

### Technical signature
[bio-style prose paragraphs added over time]

### Open questions
[bio-style prose paragraphs added over time]

### Trajectory logic
[bio-style prose paragraphs added over time]

### Fit-with-target
[bio-style prose paragraphs added over time]

### Intellectual taste
[bio-style prose paragraphs added over time]

### Cross-pollination from history-historiography
[bio-style prose paragraphs added over time, where applicable to this user]

## Notes
[Anything that doesn't fit above but matters: timing constraints, family considerations, specific labs/PIs already in mind, advisor relationships to preserve, etc.]
```

## Notes on the living-document nature

- **Scientific identity narrative section** is initialized with empty subsections by profile-builder. It gets filled across sessions as the user works with sop-coach (and later ps-coach / rs-coach). Subsections accumulate timestamped session blocks; nothing is ever overwritten.
- **Factual sections** (research experience, recommenders, etc.) can be updated by any skill that surfaces new facts during grilling, using the clean-rewrite-with-audit-comment protocol.
- **Program target list does NOT live here.** It lives in `programs.md` at the root, written by program-discovery and maintained by program-evaluation. profile.md is about the applicant; programs.md is about the targets.

## Anti-patterns

- **Asking what's already in the CV.** "What's your GPA?" when it's right there. Read first, ask second.
- **Generic profiles.** Every field should be specific to this user. If a field reads like it could apply to anyone, push for specifics.
- **Writing profile.md silently** without showing the draft. The user must approve before the file is written.
- **Padding the strengths section** with self-assessment that isn't backed by CV evidence. Push back on weak claims.
- **Skipping the recommender section** because it's awkward. This is critical info for LoR management later.
- **Treating the CV's subfields as the target subfields.** Past research doesn't equal future direction — ask.
- **Accepting "I don't know" as a final answer on career goals.** Push for at least a leaning; mark tentative if genuinely unsettled.
- **Omitting the Scientific identity narrative section** because it's "empty". sop-coach depends on it existing — initialize it with the template structure even when there's no content yet.
- **Putting program-specific information in profile.md.** That goes in `programs.md`. Keep profile.md focused on the applicant.
