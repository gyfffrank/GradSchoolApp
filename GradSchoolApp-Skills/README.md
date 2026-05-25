# GradSchoolApp-Skills

A collection of [Claude](https://claude.ai) skills for navigating PhD and MS graduate school applications, originally built for physics / optics / photonics / quantum applications but adaptable to any quantitative science field.

## What's included

| Skill | Purpose |
|---|---|
| **grill-me** | Structured interviewing that walks down the decision tree of a complex multi-part plan, one question at a time, with a recommended answer attached to every question. Field-agnostic. |
| **profile-builder** | Reads the user's CV, then grills them on the forward-looking information a CV doesn't carry, and produces a `profile.md` that the rest of the skill set depends on. |
| **program-discovery** | First-pass triage from the full universe of graduate programs down to a ranked working list of ~20–30 candidates. Writes the target list into `programs.md` at the project root. |
| **program-evaluation** | Deep evaluation of a single program against six weighted criteria, producing a rich scorecard in `programs/{slug}/scorecard.md` and updating the corresponding row in `programs.md`. Creates the `essays/` subfolder per program so essay-coaches can populate it. |
| **sop-coach** | Develops, refines, and critiques Statement of Purpose drafts through probing questions and a six-check critique. Never writes SoP prose for the user. Reads from and contributes to `profile.md`'s Scientific identity narrative section. |
| **pi-cold-email** | Drafts and critiques outreach emails to potential PhD advisors. Three modes: initial outreach, reply, and follow-up bump. Enforces four required inputs, runs an eight-check critique, and bakes in physics-specific conventions (timing, follow-up cadence, per-program caps, attachment etiquette). Maintains a root-level contact log. |

The skills compose into a workflow:

```
   profile-builder   →  profile.md (the living applicant knowledge base)
         ↓
   program-discovery →  programs.md (the target program dashboard)
         ↓
   program-evaluation →  programs/{slug}/scorecard.md per program
                        + empty essays/ and outreach/ subfolders per program
                        + updates the row in programs.md
         ↓                                         ↓
   sop-coach  →  core-sop.md at root         pi-cold-email  →  per-program
                 + sop-tailoring.md             outreach drafts under
                   per target program           programs/{slug}/outreach/
                 + appended bio prose into      + root-level pi-contacts.md
                   profile.md narrative          log tracking all contacts
```

`grill-me` is the underlying interview pattern that several skills use internally and that you can invoke directly any time you face a complex multi-decision plan.

## File and folder layout (after running the full workflow)

```
GradSchoolApp/                         ← project root
├── cv.pdf                             ← your input
├── profile.md                         ← applicant knowledge base (about YOU)
├── programs.md                        ← target program dashboard (your TARGETS)
├── pi-contacts.md                     ← PI outreach log (cross-program tracking)
├── core-sop.md                        ← program-agnostic SoP draft
├── programs/
│   ├── mit-physics/
│   │   ├── scorecard.md
│   │   ├── essays/
│   │   │   └── sop-tailoring.md
│   │   └── outreach/
│   │       ├── vuletic-v-initial-2026-08-12.md
│   │       └── vuletic-v-followup-2026-08-26.md
│   ├── caltech-physics/
│   │   ├── scorecard.md
│   │   ├── essays/
│   │   └── outreach/
│   ├── ...
└── GradSchoolApp-Skills/              ← these skill files
    ├── README.md
    ├── grill-me/SKILL.md
    ├── profile-builder/SKILL.md
    ├── program-discovery/SKILL.md
    ├── program-evaluation/SKILL.md
    ├── sop-coach/SKILL.md
    └── pi-cold-email/SKILL.md
```

## Three living documents, three responsibilities

The skill set keeps three long-lived markdown files at the project root, each with a single responsibility:

- **`profile.md` is about the applicant.** Background, research, recommenders, strengths, constraints, scientific identity narrative. Written by profile-builder and updated by sop-coach (narrative) and any skill that surfaces new facts about the user.

- **`programs.md` is about the targets.** Summary table of every program on the list with tier, top PI, hook, deadline, weighted score, link to scorecard. Plus a chronological deadlines section. Written by program-discovery and updated by program-evaluation.

- **`pi-contacts.md` is about the outreach state.** Cross-program log of every PI contacted, when, what mode, current state, next action. Written and updated only by pi-cold-email.

Keeping these separate makes all three files focused as they grow. Essay and outreach skills read each other's files; ownership is clean.

## Write protocols (so skills don't clobber each other)

- **Narrative section in `profile.md`** is **append-only** — every session adds a timestamped block.
- **Factual sections in `profile.md`** (research, recommenders) use **clean rewrites with audit comments** (`<!-- last updated: YYYY-MM-DD by skill-name -->`).
- **`programs.md`** is row-scoped — program-evaluation only edits the row for the program being evaluated; the Summary and Deadlines sections are regenerated.
- **`pi-contacts.md`** is owned by pi-cold-email — no other skill writes to it.
- **Scorecards** are clean rewrites per evaluation session.
- **Outreach drafts** are immutable per send (`{pi-slug}-{type}-{date}.md` is a record of what was sent on that date).

## How to use these skills with Claude

### Option 1 — Claude.ai Projects (easiest)

1. Create a new Project at [claude.ai](https://claude.ai).
2. Upload your CV to the project (PDF or DOCX).
3. Upload the six `SKILL.md` files as project files. (Rename on upload if Claude's UI requires unique filenames, e.g. `grill-me-SKILL.md`, `pi-cold-email-SKILL.md`.)
4. In any conversation inside the project, invoke skills naturally:
   - *"Build my profile"* → **profile-builder**
   - *"Find me PhD programs matching my profile"* → **program-discovery**
   - *"Evaluate MIT's physics PhD program for me"* → **program-evaluation**
   - *"Help me develop my SoP"* / *"Critique this SoP draft"* → **sop-coach**
   - *"Draft a cold email to Vuletic at MIT"* / *"Should I follow up with X?"* → **pi-cold-email**
   - *"Grill me about [X]"* → **grill-me**

### Option 2 — Claude Code / API with skill auto-discovery and filesystem access

Place the `GradSchoolApp-Skills/` folder somewhere Claude can read it, and ensure Claude has filesystem write access to your project directory. The skills will then read CVs, write `profile.md`, `programs.md`, `pi-contacts.md`, create program folders with scorecards, essay drafts, and outreach drafts directly to disk.

### Option 3 — Manual prompting (no setup)

Open the `SKILL.md` file you want, paste the contents at the start of your conversation with Claude, and ask Claude to follow the instructions for your task. Works in any Claude interface but loses file-persistence benefits.

## Suggested workflow

1. **Drop your CV into the project.**
2. **Run `profile-builder`.** Reads CV, grills you on forward-looking gaps, writes `profile.md`.
3. **Run `program-discovery`.** Produces your candidate list, writes `programs.md`.
4. **Iterate the list** — drop programs that don't fit; add ones discovery missed.
5. **Run `program-evaluation` on each finalist.** One conversation per program. Produces a scorecard, creates `essays/` and `outreach/` subfolders, updates the row in `programs.md`.
6. **Run `pi-cold-email` for summer outreach (July–October).** One PI at a time. Produces ready-to-revise drafts; tracks contact state across all PIs in `pi-contacts.md`.
7. **Run `sop-coach`.** Cluster grilling fills `profile.md`'s narrative section; you draft `core-sop.md`; the skill critiques. Later, you draft per-program tailoring blocks at `programs/{slug}/essays/sop-tailoring.md`; the skill critiques those too.
8. **Use `grill-me` anytime** a decision feels too tangled — picking recommenders, deciding application order, choosing between admits.

## Adapting to other fields

The skills were authored for physics / optics / photonics but the structure is general. To adapt:

- **`program-discovery`** and **`program-evaluation`**: edit the "Sources to use" sections — swap Optica rankings for your field's specialty rankings (e.g., CSRankings for CS), and swap community sources.
- **`program-evaluation`**: adjust scoring criterion #2 to reflect your field's specialty metrics.
- **`sop-coach`**: the seven question clusters are mostly field-agnostic, but cluster #7 (cross-pollination from history-historiography) is specific to one user. Replace or drop.
- **`pi-cold-email`**: physics-specific conventions (season, per-program cap, no-attachment etiquette) may need adjusting for other fields. CS, for example, has a different outreach culture.
- **`profile-builder`** and **`grill-me`**: field-agnostic — use as-is.

## Anti-patterns these skills are designed to avoid

- Generic ranking advice that ignores PI-level research fit
- Confident-sounding guesses about facts (funding terms, admit rates, PI activity) without verification
- Treating Reddit hot takes as program-quality verdicts
- Question-asking without recommendations attached
- Bundling 5+ questions into a single turn
- Asking the user for information that's already in their CV
- Writing SoP prose for the user (sop-coach scaffolds and critiques only)
- Padding essays with clichés ("passion for physics", "since childhood", "fascinated by the universe")
- Sending AI-stilted cold emails verbatim without user revision
- Cold-emailing PIs at programs not yet evaluated
- Letting profile.md, programs.md, or pi-contacts.md become static — all three must grow across the application cycle

## Contributing

Pull requests welcome. Natural additions to this skill set:

- **ps-coach** — Personal Statement drafting and critique (different conventions from SoP; more memoir-adjacent)
- **rs-coach** — Research Statement drafting and critique (longer technical document, closer to a research proposal)
- **lor-tracking** — Recommender management across N programs
- **application-tracker** — Deadlines, materials, submission status, fee waivers

## License

MIT — feel free to fork, adapt, and redistribute.

## Acknowledgments

Originally built as part of a personal grad school application project for physics PhD admissions, Fall 2026 cycle.
