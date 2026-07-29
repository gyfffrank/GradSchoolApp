# SOP Scaffold — Structure & Per-Paragraph Talkpoints
<!-- working document maintained with sop-coach. Talkpoints only — NOT submittable prose. You write the SOP. -->
<!-- created 2026-07-27 -->

## The one claim every paragraph must serve

> "I developed from a computational data analyst into an experimental structured-light researcher whose signature move is **enlarging the state space so hidden structure becomes analyzable** — and I want to carry that move into high-dimensional structured *quantum* optics."

The reader should finish the SOP able to say what kind of *scientist* you are, not just that you were a strong physics student. Every selected fact must advance the claim above; if a fact is true but doesn't, it goes in the CV, not the SOP.

## Target lengths (from the evidence map)

| ¶ | Section | Length |
|---|---|---|
| 1 | Opening / research goal | 100–150 w |
| 2 | Quantum-pendulum (entry into optics) | 180–250 w |
| 3 | GL project — the ONE anchor challenge | 250–350 w |
| 4 | Supporting capabilities (integrated, not 4 mini-stories) | 120–180 w |
| 5 | Conclusion (researcher-you-intend-to-become) | 2 sentences |
| — | Per-school fit block (tailoring file, not core) | 3 sentences each |

---

## ¶1 — Opening / research goal  *(the hook)*

**Role:** replace any childhood-wonder / "light is beautiful" opening with a live scientific problem → your recurring reflex → doctoral direction. Three sentences of work.

**Talkpoints you already own:**
- **Hook sentence** = a real unresolved problem — **REWORKED 2026-07-27**: the *constructive* question — *what are the (group-theoretic) rules for building stable high-dimensional topological structures in structured light?* — catalyzed by the **Gutiérrez-Cuevas / Dennis / Alonso** Ince–Gauss result (LG-like ↔ HG-like beams are one object seen from different *cuts* of a sphere). This replaces the old geodesic-selection hook as the headline; geodesic selection is now one *instance* inside it. **Bonus:** Alonso is at Rochester (your prime target) — the hook and the lead fit block are the same paper.
- **Reflex sentence** = the "enlarge the state space" move, now sharpened to *"elevate the viewpoint until apparent difference dissolves into one topological structure"*: Koopman → Fourier optics → Ince–Gauss/Poincaré. Your differentiator — a scientist with a *position*, not a student with a skill list.
- **Direction sentence** = high-dimensional structured quantum optics; broad enough for free-space, integrated, and AMO faculty (evidence-map Task 2 Q6). Capacity/networking is the *stakes*, stated second — not the motive.

**HOLES:**
- ~~Open-question rework~~ **DONE 2026-07-27** — see `profile.md` → Open Questions (2026-07-27 block) and Intellectual Taste (2026-07-27 block).
- Density decision (evidence-map Task 8 Q2): how much S² / OAM / higher-order-Poincaré vocabulary before the opening gets too dense. Recommend: name the *problem* (Ince–Gauss unification → construction rules) concretely, defer the group-theory machinery to the body.
- One live tension to resolve in drafting: your *taste* pulls fundamental/classical (Alonso/Dennis geometric structured light) while your *stated field* is quantum. Frame the classical topological structure as the substrate you enter at, quantum as the extension where the stakes live — don't let the opening commit you to only one.

---

## ¶2 — Quantum-pendulum  *(entry point into experimental optics)*

**Role:** the honest on-ramp. Establishes the Helmholtz–Schrödinger bridge and your first physical Fourier-plane encoding — and models intellectual honesty by being precise about what was *yours*.

**Talkpoints you already own:**
- Equation-level analogy: Helmholtz–Schrödinger equivalence ↔ Mathieu / elliptical-beam wavefunctions. 11 pendular eigenstates encoded in the Fourier plane — ring radii ∝ energy, angular modulation ∝ probability density, bound + rotor states.
- **Honest ownership:** the theory-simulation code and the phase-encode/SLM-control code were inherited from previous students. *Your* contribution = fine-tuning separations, sizes, brightnesses in MATLAB to reach a *physically usable* superposition, and learning alignment / SLM control / the 4-f Fourier system from zero. Say this plainly — it makes ¶3 (where the work becomes yours) land harder.
- Conceptual bridge: this is where 2D Fourier analysis (learned computationally with Lam) became *physical* Fourier optics — same mathematical object, different substrate.

**HOLES (from evidence-map Task 4 / questionnaire C):**
- Q11: what output pattern first told you the alignment / eigenstate weighting was wrong?
- Q12: how did you *tune and validate* the 11-state pattern — visual, quantitative fit, theoretical ratios, iterative comparison to target?
- Q13: the hardest conceptual step in making Helmholtz–Schrödinger physically meaningful.
- Q14: what did this teach you about structured light *beyond* generating a pretty image?

---

## ¶3 — Gravitational-lensing project  *(the anchor — your strongest paragraph)*

**Role:** prove experimental identity through ONE challenge reconstructed as a scientific arc (expected → anomaly → competing causes → decisive test → fix → result), then land a scientific payoff. Not a tour of everything you built.

**Confirmed from the repo `OpticsLab26-27` (2026-07-27) — all three candidates are real, your own MATLAB code:**
- The project is a **manuscript under review** with you as **lead experimental / co-first author**: Moreso Serra, Bulashenko, **Gu**, et al., *"Laboratory observation of lensing diffraction in a binary-lens system for gravitational-wave astrophysics"* (2026). This is a *citable authorship* — the single biggest upgrade to the paragraph; the SOP can say "under review" with your name.
- Candidate (A) dual-SLM rebuild: verified — MATLAB **package namespaces** (`+optics/+camera/+stage/+analysis/+sim`), wavelength-aware `slm_config('hamamatsu'|'holoeye')`, `optics.modMaxGray` PCHIP calibration, independent per-monitor display. Hamamatsu 800×600/20 µm + Holoeye PLUTO-2.1 1920×1080/8 µm.
- Candidate (B) `optics.stationaryLens`: verified — builds the lens phase from the **stationary points of the Fermat/time-delay function** `T = ½|x−y|² − ψ(x)`, keeps phase only around each image (Morse min/saddle/max, signed magnification). This *is* your "Fresnel > Snell" taste in code, and it's the paper's §IV.A caustic morphology + appendix "interference maxima near critical points."
- Candidate (C) `analysis.phaseMap`: verified — phase-shifting reconstruction + **optical-vortex / net-OAM (topological charge ℓ) detection** via a phase-winding integral robust to a saturated core. This is the cleanest *bridge* from GL into your structured-light/OAM/Poincaré goal.

**Challenge candidates (pick ONE as the spine — see decision fork):**
- **(A) Dual-SLM library rebuild** — new Holoeye Pluto 2.1 NIR145 in series with the Hamamatsu; different pixel size/resolution broke the inherited phase-encode code. Rather than bolt on functions, you **re-architected the repo as a library** with a configuration function that initializes/configures *both* SLMs and emits a config matrix per device. Shows software architecture + initiative. *(Your Materials.docx sentence is cut off at "then the f…" — this story is unfinished.)*
- **(B) The imaging problem previous members couldn't solve** — diffraction-order/grating artifact management; you found the empirical parameter window (grating density vs. tilt-angle vs. re-alignability) that no manual gives, and produced the first clean, usable data on the project. Best fits the challenge-arc format and shows *impact* (solved what others couldn't).
- **(C) Caustic / virtual-Mach-Zehnder analysis** — you encoded a *virtual Mach-Zehnder interferometer in the SLM* to analyze the phase structure, and independently isolated which regions of the phase encode contribute most to the caustic patterns (i.e., optics around singular points / critical points). Weakest as a "challenge" but **strongest thematic link to your research goal** (singularities, topology).

**Scientific payoff to land regardless of which spine you pick (new in Materials.docx):**
- Binary-lensing interference vs. **GW chirp** — as the GW frequency sweeps upward, the interference pattern evolves; you flagged this as potentially observable by LIGO-class detectors. *This is a real scientific result, not "the apparatus worked."*
- The caustic-contribution map → understanding optics near singularities → **directly seeds your PhD goal.**

**Independent contributions (name them; don't bury them — evidence-map Task 3 Q5/Q8):**
- ThorLabs automation from scratch (MATLAB IO for LM300 stage + CMOS camera, simultaneous-contact comm layer) — *now used lab-wide.*
- Image-analysis + 1,000-frame merger movie — *unassigned; built because they were better ways to work the data.*
- Full phase-profile generator reconstructable from first principles (went back to the original Einstein-ring paper).

**Boundary to draw (evidence-map Task 3 Q6):** your independent technical + analysis work vs. the Barcelona collaborators' theory/parameter-selection. State it cleanly — the honesty is a feature.

**HOLES:** the full challenge arc for whichever spine you pick (expected result → observed anomaly → why it couldn't be ignored → hypotheses → elimination → decisive observation → what you modified → degree of resolution). This is **drafting priority #1** in the evidence map.

### Raw challenge material — Frank's words, 2026-07-27 (working notes, pre-synthesis)

*Four real debugging arcs surfaced. The dual-SLM integration (2–4) is his most-owned, richest challenge; the sign-flip (3) is the cleanest single elimination arc. Candidate restructure: dual-SLM integration = challenge body; caustic/critical-point + co-first-author paper = establishing credential + taste hook; payoff = a two-SLM platform is the physical machine for **adding degrees of freedom** → bridges straight to the reworked open question ("bricks = DoF").*

1. **Initial alignment (multi-wavelength setup; pre-takeover images deformed/asymmetric).** Camera realign didn't fix it. Removed the 4-f lenses → laser not aligned to the SLM's first order. **Invented a diagnostic: encoded an optical vortex on the SLM** — its dark core reveals whether the beam passes the iris center — then tuned mirrors to align the 4-f. Uneven intensity turned out to be incoherent source brightness → fixed by nudging the beam-splitter lenses.
2. **Dual-SLM code re-architecture (A).** New Holoeye Pluto 2.1 NIR145 in series with the Hamamatsu; different pixel size/resolution broke the inherited code. Rebuilt the repo as a library: one config function initializes/configures both SLMs and emits a per-device config matrix; functions read the config instead of duplicating code; adding a future SLM = writing a new config function.
3. **New-SLM debugging — systematic hypothesis elimination.** Bessel-beam test → saw a far-field big circle instead of concentric rings at the 4-f output. H1 collimation → verified with a **shearing interferometer**, adjusted expander-lens separation → still broken. H2 LUT (grayscale→phase map) → set the correct Holoeye LUT → still broken. H3 encoding → **gave both SLMs the same plain grating; the new SLM deflected the first order the *opposite* way** → added a −1 to the whole phase map → fixed. *(Decisive controlled test = the clean arc.)*
4. **Series alignment + the oblique-incidence fix.** Cross phase-mask on both SLMs → overlapped equal crosses = aligned (passed). Then grating on SLM1 + Bessel on SLM2 → first-order light carried extra phase; Bessel rings deformed into fragmented curves/cusps. Removed 4-f lenses (issue persisted) → isolated it to the mirror between iris and 2nd lens; pulled the mirror and hunted the position ("messiest station I've had — but I'm not afraid of the mess, it's the necessary step"). **Deformation vanished only at a specific beam-incidence angle on the SLM** → centered the beam while preserving that angle → works. *(Best grit/character beat.)*

### ✅ FINALIZED ¶3 STRUCTURE (2026-07-27) — talkpoints, ~300 w, you write the prose

**One claim ¶3 argues:** *I built the instrument and the code that turned a theoretical caustic picture into the first quantitative wave-optical measurement of it — and then extended that rig into a platform for adding degrees of freedom, which is the question I want my PhD to be about.*

**Beat 1 — Establishing credential + taste hook (2 sentences).**
- Credential (concrete, not vague): co-first / lead-experimental author on the binary-lens gravitational-lensing manuscript under review; *you* produced the experimental diffraction data behind **Figs. 6, 9, 10** (the 14-wavelength composite; the first-ever theory–experiment agreement at the level of the *fine diffraction structure*, not just caustic morphology; the chirp analogue). More scan data (stationary-lens, image-plane phase-map) in the conference poster.
- Taste hook (1 line): what drew you in — the caustics are born at the *critical points of the time-delay function*, i.e. the structure lives exactly where the ray picture breaks down. (Ties to your Taste block; do NOT claim the theory — it's Barcelona's; you implemented/visualized/measured it.)

**Beat 2 — The challenge: integrating the second SLM (the sign-flip elimination arc) (3–4 sentences).**
- Setup: this summer a second SLM (Holoeye PLUTO-2.1) was added in series with the Hamamatsu — the move from one spatial-phase DoF toward controlling more.
- The arc (your cleanest): a Bessel test beam should have given concentric rings at the 4-f output; you saw a far-field ring — as if the beam were focusing near the SLM. You eliminated collimation (verified with a **shearing interferometer**) and the phase **LUT**, then a *controlled test* — the same grating on both SLMs — showed the new device deflected the first order the *opposite* way; a sign flip (−1 on the phase map) fixed it.
- Grit beat (1 line): a later Bessel deformation resolved only at one specific beam-incidence angle, found by pulling the setup apart and hunting the geometry — "the messy but necessary step."
- Architecture (1 line, optional): rather than duplicate code per device, you rebuilt the repo as a config-driven library, so a new SLM is just a new config function.

**Beat 3 — Payoff / bridge to the PhD (2–3 sentences).**
- Honesty (keep it): the platform works, but it has produced no results yet (end of summer); its first intended use — testing how photon polarization transforms under a *simulated* gravitational field, motivated by Noh/Alsing/Miller/Ahn (2024) — is just beginning.
- Bridge (the payoff that matters): a second SLM is a second **degree of freedom** — the rig is the physical form of the question you most want to pursue, *how to build stable high-dimensional structures by adding degrees of freedom one at a time*, and it is the platform you would use to construct and study topological textures like **optical skyrmions**.

**Trim priority if over length:** cut the architecture line first, then compress the grit beat to a clause. Never cut: the −1 controlled-test arc (Beat 2) or the DoF/skyrmion bridge (Beat 3) — those two are the paragraph's whole reason to exist.

**Honesty guardrails:** (a) caustic *theory* = Barcelona's, your ownership = experiment/code/data; (b) dual-SLM platform = built, *no results yet* — frame as capability + intent, never as a finding; (c) "co-first / lead experimental author" is accurate (first-listed Colgate author) — don't inflate to sole first author.

---

## ¶4 — Supporting capabilities  *(ONE integrated paragraph, not four projects)*

**Role:** convert pre-Galvez work into evidence for the optics goal, organized by *capability*, not chronology. The evidence map is explicit: combine, don't enumerate.

**Talkpoints you already own:**
- **NanoGrav (Lam)** = Fourier/PSD/red-noise continuity — you had 2D Fourier analysis *before* optics; physical Fourier optics was the same tool on a new substrate.
- **Koopman/Chua (Segall)** = the enlarged-space theme in its purest form — lift chaotic dynamics into a higher-dimensional function space → hidden linear spectral structure becomes analyzable. This is the through-line to the Poincaré problem.
- **JWST (Ilie)** = compress to one clause at most, or cut (evidence-map Task 6 Q5).
- The unifying sentence: you no longer care only whether an optical phenomenon can be *produced* — you care how enlarging the representation *reveals its structure*.

**HOLES (evidence-map Task 6 / questionnaire E):**
- Q17: NanoGrav vs. Koopman vs. both in the main SOP? (decision fork)
- Q18: your specific slice of the Koopman team project + the lesson from comparing polynomial/RBF/piecewise-linear dictionaries (model choice vs. physical interpretability).
- Q19: shortest *positive* framing for why computational astro narrowed you toward experimental optics (not "astro failed").

---

## ¶5 — Conclusion  *(2 sentences)*

**Role:** make a claim the opening couldn't (the "ending test"). Not a restatement, not a hope-list.
**Talkpoints:** the researcher you intend to *become* — an experimentalist who moves fluently between mathematical representation, programmable light fields, instrumentation, and quantum-state questions; career kept dual-track (academia / photonics-networking industry) without over-committing.

---

## Per-school fit block  *(lives in `programs/{slug}/essays/sop-tailoring.md`, NOT the core SOP)*

**Template of talkpoints per school (evidence-map Task 9 / questionnaire G):**
1. Name **2 PIs** + **one shared scientific question** (not shared equipment/keywords).
2. What you contribute **immediately**: SLM phase engineering, laser alignment, MATLAB hardware control, Fourier-plane analysis.
3. What you need to **learn** from them: SPDC/heralded sources, coincidence counting, single-photon detection, quantum-state tomography, or (per lab) integrated photonics / cavity QED / ultrafast.
4. One **plausible next question** that grows from their recent work without inventing expertise.

**Cluster → PI map (from Materials.docx, to reconcile with `programs/` scorecards):**
- Cluster 1 (primary): Otte, Kwiat, Bigelow, Litchinitser, Capasso, Feng, Sergienko, Mehta
- Cluster 2: Alonso, Otte, Swartzlander, Litchinitser, Milchberg, Murnane/Kapteyn
- Cluster 4 (secondary): Bigelow, Panda, Dimitrova, Mehta
- ⚠️ Some names here (Sergienko, Mehta, Vamivakas, Alaeian, Dimitrova, Panda, Moses) are **not yet in the 12-PI scorecard set** — the live `GradSchoolApp.xlsx` is ahead of `programs/`. Fit-block work should re-sync these first.

---

## Task 2 — Open-questions REWORK — ✅ DONE 2026-07-27

Reworked via sop-coach grilling and written to `profile.md` (append-only; supersedes the 2026-06-25 geodesic block, which stays as a record). Outcome:
- **New open question (constructive):** what are the group-theoretic rules for *building* stable high-dimensional topological structures in structured light — bricks = degrees of freedom, grammar = group theory. Catalyzed by the Ince–Gauss unification (Gutiérrez-Cuevas/Dennis/Alonso 2024).
- **Identity confirmed:** engine = *unification through elevation* (fundamental); capacity/communication = stakes, not motive.
- **Taste block also filled:** elegant = unification through elevation (scientific realism); ugly = *mechanism-concealment* (ML), explicitly distinguished from difficulty (GR Shapiro-delay math is hard but not ugly); unfashionable-but-deep = wave-optical/Fresnel caustics-from-critical-points over Snell rays.
- **Honest stance kept:** foundational stage, no experimental observable / falsifiable test yet; skyrmions named as next reading.

---

## Live holes checklist (ranked by the evidence map's drafting priority)

1. **GL challenge arc** — pick the spine, reconstruct expected→anomaly→test→resolution. *(¶3)*
2. **Quantum-pendulum validation** — how the 11-state pattern was tuned + confirmed. *(¶2)*
3. **Research-goal calibration** — observable, falsifiability, senior-project vs. PhD scope. *(¶1)*
4. **Faculty fit** — contribution + learning + next-question per school. *(fit blocks)*
5. **Supporting-experience selection** — which of NanoGrav / Koopman / history / teaching earns main-SOP space. *(¶4)*
