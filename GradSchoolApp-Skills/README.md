# GradSchoolApp-Skills

A collection of [Claude](https://claude.ai) skills for navigating PhD and MS graduate school applications, originally built for physics / optics / photonics / quantum applications but adaptable to any quantitative science field.

## What's included

| Skill | Purpose |
|---|---|
| **grill-me** | Structured interviewing that walks down the decision tree of a complex multi-part plan, one question at a time, with a recommended answer attached to every question. Field-agnostic. |
| **profile-builder** | Reads the user's CV, then grills them on the forward-looking information a CV doesn't carry, and produces a `profile.md` that the rest of the skill set depends on. |
| **program-discovery** | First-pass triage from the full universe of graduate programs down to a ranked working list of ~20–30 candidates. Writes the target list into `programs.md` at the project root. |
| **program-evaluation** | Deep evaluation of a single program against six weighted criteria, producing a rich scorecard in `programs/{slug}/scorecard.md` and updating the corresponding row in `programs.md`. Creates the `essays/` subfolder per program so essay-coaches can populate it. |
| **sop-coach** | Develops, refines, and critiques Statement of Purpose drafts through probing questions and a six-check critique. Never writes SoP prose for the user — coaches them to write better prose themselves. Reads from and contributes to `profile.md`'s Scientific identity narrative section. |

The skills compose into a workflow:

```
   profile-builder  →  profile.md (the living applicant knowledge base)
         ↓
   program-discovery  →  programs.md (the target program dashboard at root)
         ↓
   program-evaluation  →  programs/{slug}/scorecard.md per program
                         + empty essays/ subfolder per program
                         + updates the row in programs.md
         ↓
   sop-coach  →  core-sop.md at root (user-written, skill-critiqued)
                 + programs/{slug}/essays/sop-tailoring.md per target
                 + appended bio prose into profile.md narrative section
```

`grill-me` is the underlying interview pattern that several skills use internally and that you can invoke directly any time you face a complex multi-decision plan.

## File and folder layout (after running the full workflow)

```
GradSchoolApp/                         ← project root
├── cv.pdf                             ← your input
├── profile.md                         ← applicant knowledge base (about YOU)
├── programs.md                        ← target program dashboard (about your TARGETS)
├── core-sop.md                        ← program-agnostic SoP draft
├── programs/
│   ├── mit-physics/
│   │   ├── scorecard.md
│   │   └── essays/
│   │       └── sop-tailoring.md
│   ├── caltech-physics/
│   │   ├── scorecard.md
│   │   └── essays/
│   ├── ...
└── GradSchoolApp-Skills/              ← these skill files
    ├── README.md
    ├── grill-me/SKILL.md
    ├── profile-builder/SKILL.md
    ├── program-discovery/SKILL.md
    ├── program-evaluation/SKILL.md
    └── sop-coach/SKILL.md
```

## Two living documents, two responsibilities

The skill set keeps two long-lived markdown files at the project root, each with a single responsibility:

- **`profile.md` is about the applicant.** Background, research, recommenders, strengths, constraints, scientific identity narrative. Written by profile-builder and updated by sop-coach (narrative) and any skill that surfaces new facts about the user. Owned by the applicant.

- **`programs.md` is about the targets.** Summary table of every program on the list with tier, top PI, hook, deadline, weighted score, link to scorecard. Plus a chronological deadlines section. Written by program-discovery and updated by program-evaluation. Owned by the program skills.

Keeping these separate makes both files focused as they grow. Essay skills read both; only the program skills write to `programs.md`; only profile-builder and the essay skills write to `profile.md`.

## Write protocols (so skills don't clobber each other)

- **Narrative section in profile.md** is **append-only** — every session adds a timestamped block, never rewrites existing prose.
- **Factual sections in profile.md** (research, recommenders, etc.) get **clean rewrites with audit comments** (`<!-- last updated: YYYY-MM-DD by skill-name -->`) so the next skill can see freshness.
- **programs.md** is row-scoped — program-evaluation only edits the row for the program being evaluated; the rest is preserved.
- **Scorecards** are clean rewrites per evaluation session.

## How to use these skills with Claude

### Option 1 — Claude.ai Projects (easiest)

1. Create a new Project at [claude.ai](https://claude.ai).
2. Upload your CV to the project (PDF or DOCX).
3. Upload the five `SKILL.md` files as project files. (Rename on upload if Claude's UI requires unique filenames, e.g. `grill-me-SKILL.md`, `sop-coach-SKILL.md`.)
4. In any conversation inside the project, invoke skills naturally:
   - *"Build my profile"* → triggers **profile-builder**
   - *"Find me PhD programs matching my profile"* → triggers **program-discovery**
   - *"Evaluate MIT's physics PhD program for me"* → triggers **program-evaluation**
   - *"Help me develop my SoP"* / *"Critique this SoP draft"* → triggers **sop-coach**
   - *"Grill me about [X]"* → triggers **grill-me**

### Option 2 — Claude Code / API with skill auto-discovery and filesystem access

Place the `GradSchoolApp-Skills/` folder somewhere Claude can read it, and ensure Claude has filesystem write access to your project directory. The skills will then read CVs, write `profile.md` and `programs.md`, create program folders and scorecards, and persist essay drafts directly to disk.

### Option 3 — Manual prompting (no setup)

Open the `SKILL.md` file you want, paste the contents at the start of your conversation with Claude, and ask Claude to follow the instructions for your task. Works in any Claude interface but loses file-persistence benefits.

## Suggested workflow

1. **Drop your CV into the project.**
2. **Run `profile-builder`.** Reads CV, grills you on forward-looking gaps, writes `profile.md`.
3. **Run `program-discovery`.** Produces your candidate list, writes `programs.md`.
4. **Iterate the list** — drop programs that don't fit; add ones discovery missed.
5. **Run `program-evaluation` on each finalist.** One conversation per program. Produces a scorecard in `programs/{slug}/scorecard.md`, creates the matching `essays/` subfolder, updates the row in `programs.md`.
6. **Run `sop-coach`.** Starts with cluster grilling that fills the Scientific identity narrative section in `profile.md`; you draft the core SoP at `core-sop.md`; the skill critiques. Later, for each target program, the skill grills on fit specifics and you draft the per-program tailoring block at `programs/{slug}/essays/sop-tailoring.md`.
7. **Use `grill-me` anytime** a decision feels too tangled to think through alone — picking recommenders, deciding application order, choosing between admits.

## Adapting to other fields

The skills were authored for physics / optics / photonics but the structure is general. To adapt:

- **`program-discovery`** and **`program-evaluation`**: edit the "Sources to use" sections — swap Optica rankings for your field's specialty rankings (e.g., CSRankings for CS, US News specialty rankings for chemistry), and swap community sources.
- **`program-evaluation`**: adjust scoring criterion #2 ("Program quality in optics-photonics") to reflect your field's specialty metrics.
- **`sop-coach`**: the seven question clusters are mostly field-agnostic, but cluster #7 (cross-pollination from history-historiography) is specific to one user's pathway. Replace with whatever cross-disciplinary pathway your applicant brings, or drop the cluster if not applicable.
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
- Letting profile.md or programs.md become static documents — both must grow across the application cycle

## Contributing

Pull requests welcome. Natural additions to this skill set:

- **ps-coach** — Personal Statement drafting and critique (different conventions from SoP; more memoir-adjacent)
- **rs-coach** — Research Statement drafting and critique (longer technical document, closer to a research proposal)
- **pi-cold-email** — Pre-application outreach to potential PIs
- **lor-tracking** — Recommender management across N programs
- **application-tracker** — Deadlines, materials, submission status

## License

MIT — feel free to fork, adapt, and redistribute.

## Acknowledgments

Originally built as part of a personal grad school application project for physics PhD admissions, Fall 2026 cycle.
