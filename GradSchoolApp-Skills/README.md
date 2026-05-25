# GradSchoolApp-Skills

A collection of [Claude](https://claude.ai) skills for navigating PhD and MS graduate school applications, originally built for physics / optics / photonics / quantum applications but adaptable to any quantitative science field.

## What's included

| Skill | Purpose |
|---|---|
| **grill-me** | Structured interviewing that walks down the decision tree of a complex multi-part plan, one question at a time, with a recommended answer attached to every question. Field-agnostic. |
| **profile-builder** | Reads the user's CV, then grills them on the forward-looking information a CV doesn't carry, and produces a `profile.md` that the rest of the skill set depends on. |
| **program-discovery** | First-pass triage from the full universe of graduate programs down to a ranked working list of ~20–30 candidates. Writes the target list into `profile.md`. |
| **program-evaluation** | Deep evaluation of a single program against six weighted criteria, producing a rich scorecard. Creates per-program folders with an `essays/` subfolder for essay-coaching skills to populate. |
| **sop-coach** | Develops, refines, and critiques Statement of Purpose drafts through probing questions and a six-check critique. Never writes SoP prose for the user — coaches them to write better prose themselves. Reads from and contributes to `profile.md`'s Scientific identity narrative section. |

The skills compose into a workflow:

```
   profile-builder  →  profile.md (the living knowledge base)
         ↓
   program-discovery  →  candidate list (written into profile.md)
         ↓
   program-evaluation  →  per-program scorecards (programs/{slug}/scorecard.md)
                         + empty essays/ subfolder created per program
         ↓
   sop-coach  →  core-sop.md (at root)
                 + programs/{slug}/essays/sop-tailoring.md per target
                 + appended bio prose into profile.md narrative section
```

`grill-me` is the underlying interview pattern that several other skills use internally and that you can invoke directly any time you face a complex multi-decision plan.

## File and folder layout (after running the full workflow)

```
GradSchoolApp/                         ← project root
├── cv.pdf                             ← your input
├── profile.md                         ← living knowledge base
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

## The living-document model

`profile.md` is a **living document**, not a static input. Multiple skills read from it and write back to it:

- **profile-builder** initializes the file structure, including empty `Target programs` and `Scientific identity narrative` sections that other skills will fill.
- **program-discovery** writes the candidate list into the `Target programs` section.
- **program-evaluation** updates rows in `Target programs` (scores, scorecard links) as it produces individual scorecards.
- **sop-coach** (and future `ps-coach`, `rs-coach`) appends timestamped session blocks of bio-style prose into the `Scientific identity narrative` section as the user articulates their scientific identity through essay work.

Two write protocols protect against skills clobbering each other:

- **Narrative section** is **append-only** — every session adds a timestamped block, never rewrites existing prose.
- **Factual sections** (research, recommenders, etc.) get **clean rewrites with audit comments** (`<!-- last updated: YYYY-MM-DD by skill-name -->`) so the next skill can see freshness.

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

Place the `GradSchoolApp-Skills/` folder somewhere Claude can read it, and ensure Claude has filesystem write access to your project directory. The skills will then read CVs, write `profile.md`, create program folders and scorecards, and persist essay drafts directly to disk.

### Option 3 — Manual prompting (no setup)

Open the `SKILL.md` file you want, paste the contents at the start of your conversation with Claude, and ask Claude to follow the instructions for your task. Works in any Claude interface but loses the file-persistence benefits.

## Suggested workflow

1. **Drop your CV into the project.**
2. **Run `profile-builder`.** Reads CV, grills you on forward-looking gaps, writes `profile.md` with all sections initialized.
3. **Run `program-discovery`.** Produces your candidate list (20–30 programs), writes it into `profile.md`'s Target programs section.
4. **Iterate the list** — drop programs that don't fit; add ones discovery missed.
5. **Run `program-evaluation` on each finalist.** One conversation per program. Produces a scorecard in `programs/{slug}/scorecard.md`, creates the matching `essays/` subfolder, updates the row in `profile.md`.
6. **Run `sop-coach`.** Starts with cluster grilling that fills the Scientific identity narrative section in `profile.md`; you draft the core SoP at `core-sop.md`; the skill critiques. Later, for each target program, the skill grills on fit specifics and you draft the per-program tailoring block at `programs/{slug}/essays/sop-tailoring.md`.
7. **Use `grill-me` anytime** a decision feels too tangled to think through alone — picking recommenders, deciding application order, choosing between admits.

## Adapting to other fields

The skills were authored for physics / optics / photonics but the structure is general. To adapt:

- **`program-discovery`** and **`program-evaluation`**: edit the "Sources to use" sections — swap Optica rankings for your field's specialty rankings (e.g., CSRankings for CS, US News specialty rankings for chemistry), and swap community sources (e.g., add CS-specific subreddits).
- **`program-evaluation`**: adjust scoring criterion #2 ("Program quality in optics-photonics") to reflect your field's specialty metrics.
- **`sop-coach`**: the seven question clusters are mostly field-agnostic, but cluster #7 (cross-pollination from history-historiography) is specific to one user's pathway. Replace with whatever cross-disciplinary or unconventional pathway your applicant brings, or drop the cluster if not applicable.
- **`profile-builder`**: field-agnostic — use as-is.
- **`grill-me`**: field-agnostic — use as-is.

## Anti-patterns these skills are designed to avoid

- Generic ranking advice that ignores PI-level research fit
- Confident-sounding guesses about facts (funding terms, admit rates, PI activity) without verification
- Treating Reddit hot takes as program-quality verdicts
- Question-asking without recommendations attached
- Bundling 5+ questions into a single turn
- Asking the user for information that's already in their CV
- Writing SoP prose for the user (sop-coach scaffolds and critiques only)
- Padding essays with clichés ("passion for physics", "since childhood", "fascinated by the universe")
- Letting profile.md become a static document — it must grow across the application cycle

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
