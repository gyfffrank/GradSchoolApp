# SOP Source Book — everything usable for the Statement of Purpose, in one place

<!--
WHAT THIS IS
One consolidated file holding every piece of raw material that is used, or could plausibly be used,
in the SOP — pulled from Materials.docx, profile.md, SOP_contribution_notes.md, PROJECT_LOG.md and
sop-scaffold.md.

RULES FOLLOWED IN BUILDING IT
- Everything in a blockquote is VERBATIM. Original words, diction, phrasing and tone are preserved
  exactly, including non-native grammar and typos from Materials.docx. Nothing was smoothed.
- Nothing is invented. Text outside blockquotes is only headings, source tags, and navigation.
- Source tag on every quote:
    [M]   Materials.docx           (your own drafting document — the primary voice)
    [P]   profile.md               (sop-coach sessions — your own words, transcribed)
    [CN]  SOP_contribution_notes.md (your own first-person contribution notes)
    [LOG] PROJECT_LOG.md           (engineering log; [account] passages inside it are your recollection)
    [S]   sop-scaffold.md          (coaching structure — NOT your voice; use as instruction only)
- Where two sources carry the same content in different registers, both are kept and the difference
  is noted, because the register is part of what you're choosing between.
- Assembled 2026-07-31.

ORGANIZATION
  Part 0  Source register and voice notes
  Part 1  Research identity — the open question, taste, lineage, direction
  Part 2  Target field and PI taxonomy
  Part 3  Project 1 — quantum pendulum
  Part 4  Project 2 — gravitational lensing: origin, physics, ownership
  Part 5  Project 2 — the challenge arcs (four, in full)
  Part 6  Project 2 — results, significance, and what was reproduced
  Part 7  Credentials, dissemination, numbers safe to quote
  Part 8  Supporting research — NanoGrav, JWST, Koopman
  Part 9  Technical signature and skills
  Part 10 Background, constraints, recommenders, career
  Part 11 Teaching, engineering, leadership (currently unallocated)
  Part 12 Honesty guardrails and things to verify before submitting
  Part 13 Structural instructions from the scaffold
  Part 14 Prompts and templates still unanswered — the real gap list
-->

---

# Part 0 — Source register and voice notes

| Tag | File | What it is | Voice |
|---|---|---|---|
| **[M]** | `Materials.docx` | Your own Chinese-scaffolded drafting doc. The prompts are in Chinese; your answers are in English. | **Your primary voice.** Direct, unpolished, concrete. First choice for lifting. |
| **[P]** | `profile.md` | Transcribed sop-coach sessions, append-only. | Your voice, but *spoken* and then written up — more reflective and more fluent than [M]. |
| **[CN]** | `SOP_contribution_notes.md` | First-person contribution notes, written expressly so sentences could be lifted. | Your voice at its most formal and most precise. Best for the credential/technical sentences. |
| **[LOG]** | `PROJECT_LOG.md` | Engineering log. Third-person except passages tagged `[account]`, which are your recollection. | **Not your voice.** Use for facts, numbers, and the diagnostic chains — rewrite before use. |
| **[S]** | `sop-scaffold.md` | Coaching structure and talkpoints. | **Not your voice at all.** Instructions only. Never lift prose from it. |

**Register note worth deciding on early.** The same events exist in three registers. Example — the sign-flip fix:

> Then I add a -1 multitude to the entire phase map, and the issue been fixed. **[M]** — raw, yours

> recognizing that let me replace two empirical sign corrections with a single global negation that fixes gratings, lenses and orbital-angular-momentum charge simultaneously. **[CN]** — formal, yours

> The user's two empirical operations — flip the grating sign *and* negate the hologram — are algebraically **one** operation. **[LOG]** — third person, not yours

Pick a register and hold it. Mixing [M] and [CN] sentences in one paragraph reads as two people.

---

# Part 1 — Research identity: the open question, taste, lineage, direction

## 1.1 The current open question — the 2026-07-27 rework (this supersedes the June geodesic framing)

> My open question has moved. The geodesic-selection problem I described in June — which geodesic an entangled state follows on the Poincaré sphere — I now see as one *instance* of a larger question rather than the headline. What reframed it was reading Gutiérrez-Cuevas, Dennis, and Alonso's 2024 work on the ray and caustic structure of Ince–Gauss beams. They show that the apparent transformation of a beam from LG-like to HG-like is not really a change at all: it is a single object seen from different cuts of a Poincaré-sphere picture. That collapsed something for me — differences I had been treating as distinct phenomena were one topological structure viewed from different angles. **[P]**

> This is the move I keep making — Koopman, Fourier optics, the polarization sphere — but I can now state it more precisely: I am drawn to problems where you elevate the viewpoint until apparent change or complexity dissolves into one simple, elegant topological structure. Elegance, for me, is not decoration; it is the simplicity that appears once you find the right elevated vantage. **[P]**

> The question I actually want to work on is *constructive*. Not only "how do these topological structures emerge," but "what are the rules for building them." I think of it like assembling something from bricks: each degree of freedom you add — polarization, then orbital angular momentum, then radial mode — is another brick that enlarges the state space, and I want the grammar for how those bricks snap together into stable high-dimensional structures. Right now I am on the skeleton of that grammar: working through the group theory (O(n), U(n), SO(n), SU(n), the point groups; the distinction between Lie and Abelian groups) and how it connects to optical polarization and vectorial fields, before I can honestly say anything about construction. A sub-question I am genuinely curious about and cannot yet answer: what makes a topological structure *stable* — what property protects it. I suspect the answer is topological, but I have not earned that claim yet. **[P]**

> Why it matters — the stakes, not the motive: the stability of these structures is exactly what would let information ride on far more degrees of freedom than classical channels use, a direct line on the data-transmission capacity ceiling in modern information technology. But I want to be honest about where I stand. This is foundational for me right now — I am building the mathematics, I do not have an experimental observable or a falsifiable test yet, and I would rather state the question at the level I actually occupy than present it as a finished research program. The skyrmion and quantum-structured-light literature is where I am reading next, because skyrmions are a concrete instance of the stable, buildable topological texture I want to learn to construct. **[P]**

## 1.2 The superseded June version — kept because the geodesic problem is still a usable concrete instance

> The open problem I actually think about comes from Bill Luo's work in Galvez's lab: entangled photon states evolve along geodesics on the Poincaré sphere, but *which* geodesic the system selects is unresolved. My instinct is that the geodesic is underdetermined because the standard Poincaré sphere — two degrees of freedom, the surface of S² — is too small a state space to carry all the relevant physics. The polarization sphere is adequate for simple cases but breaks down under more complex conditions. My candidate for the missing degree of freedom is orbital angular momentum, which lives naturally on the higher-order Poincaré spheres — and which I can already generate and manipulate with the SLM setup I own. I hold this provisionally. Whether OAM alone fixes the geodesic, or is only the first of several missing axes, is something I expect to answer empirically once my senior project is defined and underway, not something I can settle from the literature now. I'd rather state it as a live hypothesis with a clear test than as a conclusion I haven't earned. **[P]**

> What pulls me toward this problem is a move I've now made three times. With the Koopman operator on the Chua's circuit, I lifted a chaotic system into a higher-dimensional function space and its hidden linear spectral structure became analyzable. In Fourier optics, I moved from direct space to the Fourier plane and a concealed eigenstate superposition became visible and physically decodable. The Poincaré-sphere problem has the same shape: enlarge the state space, and structure that looked arbitrary at the lower level becomes determined. I don't experience these as three separate skills — it's one recurring intellectual reflex, and recognizing it has clarified the kind of physicist I am: I'm drawn to problems where apparent complexity or arbitrariness resolves once you find the right enlarged space to view it in. **[P]**

## 1.3 The plainer version of the same goal, in the Materials.docx register

> I hope to research certain complex optical structures in high dimensional spaces, around singularities, or under topological perspectives. I especially interested in finding properties in complex or even chaotic conditions, and how these properties contribute to understanding structures of photons, the ways of their propagation, and how they potentially contribute to development in quantum/classical optical networks. **[M]**

## 1.4 Intellectual taste — what you find elegant and what you find ugly

> What I find elegant is unification through elevation. My clearest example is Gutiérrez-Cuevas, Dennis, and Alonso's 2024 work on Ince–Gauss beams: two beam families that look like different objects turn out to be one structure seen from different cuts of a sphere. I would have loved that result even with no application — the pleasure is in the collapse of apparent difference into a single object, not in what it is good for. This is a form of scientific realism for me: the structure is already there in nature, and the right geometry or group is the lens that brings an existing pattern into focus, not a formalism imposed on top of it. It is why I read the theory before I touch the setup, and why I keep reaching for higher-dimensional or operator-theoretic viewpoints — the elevated vantage is where the simplicity lives. **[P]**

> What I find ugly is mechanism-concealment — and it is not the same as difficulty. I dislike machine-learning approaches to physics: they can produce the right output while discarding the one thing I care about, the underlying mechanism. A method that predicts without exposing an object is a missed chance, not a result. What makes this precise rather than a slogan: I am currently working through the general-relativistic Shapiro-delay theory behind my own lensing project — a Fresnel–Kirchhoff diffraction integral with the time-delay function in the exponent — and it is genuinely hard for me to decode, harder than any ML method, yet I do not find it ugly in the least. Difficulty is an acceptable toll; opacity by design is the sin. **[P]**

> My unfashionable-but-deep taste is the wave-optical account of light itself: in the lensing project the caustics are reproduced from just the neighbourhoods of the critical points of the time-delay function, and that picture tells me far more about how the optics works than reducing everything to Snell's law and rays. Most people walk past classical Fresnel/diffractive optics on the way to quantum hardware; I think the structure that appears at the caustics — exactly where the ray picture breaks down — is where the real physics lives. **[P]**

## 1.5 Intellectual lineage

> My intellectual lineage is still forming — I'm a rising senior, not a second-year PhD student, and I want to be honest about what I've actually absorbed versus what I'm building toward. **[P]**

> The researcher I've engaged with most directly outside my own lab is Michael Berry. I read his work on the nonlinearity of caustic patterns in gravitational lensing — specifically the wavelength-dependent structure of caustics — because it connects directly to observations in the GL project data that may be the subject of a future paper. That encounter was substantive: I found a specific result in Berry's lensing analysis that appears in our own measurements, and verifying that connection is part of the ongoing work. I've read Berry's geometric phase paper much more briefly; it's on my list to read seriously before applications, because the Poincaré sphere problem I want to pursue for my senior project sits squarely inside that tradition and I don't want to reference it without real content. **[P]**

> The tradition I'm most directly working inside is Kiko's (Prof. Galvez's) structured light program at Colgate. Reading his papers taught me how research in this area is constructed — how optical analogs are designed, how phase profiles encode physical states, how to move between theory and tabletop implementation. That's been more formative than any single paper: learning a research style, not just a result. **[P]**

> My self-directed reading program is driven by gaps I identified and decided to fix. Crotty's quantum mechanics course was heavily matrix-based, and while I worked through it, the formalism was opaque in a specific way — the physical content kept disappearing behind the algebra. Sakurai's Modern Quantum Mechanics gave me what was missing: it combines Dirac bra-ket notation with matrix formalism in a way that keeps the physical objects visible throughout. I'm comfortable with mathematics, but I need the mathematical objects to have physical meaning I can track; bra-ket notation gives me that in a way that pure matrix manipulation doesn't. That preference runs through my research approach too — I read the theory before touching the setup, I simulate before building, and I go back to primary papers when the physical picture isn't clear. **[P]**

> Topology is next on the list for a specific reason: the Poincaré sphere, which is the mathematical object at the center of my proposed senior project, is a topological structure — the 2-sphere, S². The higher-order Poincaré spheres I want to extend to are more complex topological spaces, and the polarization optics I already work with daily (half-wave plates, quarter-wave plates) are physically described by transformations on that sphere. I want to understand the mathematics of the physical objects I work with, not use them as black boxes. Abstract algebra is on the list for the same reason — group theory underlies the symmetry structure of quantum states and optical polarization, and I'd rather build that foundation before PhD coursework than catch up during it. **[P]**

> The through-line, honest version: my lineage runs from Kiko's structured light program, through Berry's geometric and lensing work, toward a topology-grounded understanding of geometric phase in higher-dimensional optical state spaces. I haven't read all the foundational papers in this tradition yet — Allen et al. on orbital angular momentum, Pancharatnam on geometric phase in optics, the broader structured light literature — but I know what I need to read and why, and I'm building toward it deliberately rather than waiting for a course to assign it. **[P]**

## 1.6 Why quantum optics, honestly — including the citizenship calculation

> My original draw toward quantum physics came from what I'd call the "creepy" nature of QM and chaos — phenomena that are mathematically rigorous but physically counterintuitive, where the rules of everyday intuition simply break down. I was initially interested in quantum computation hardware for this reason. Most of those positions, however, are restricted to US citizens, which ruled out the bulk of the quantum computing hardware programs I had identified. Photonics and quantum optics are not a fallback — my behavior in the lab doesn't match someone who settled — but citizenship constraints were part of the honest calculation that directed my attention here. **[P]**

## 1.7 Where the direction came from — labmates and lab seniors

> The intellectual direction I want to pursue came from Bill Luo, a labmate who graduated this summer. He worked on the geometric phase of entangled photon states on the Poincaré sphere: we know these states move along geodesics, but which geodesic they choose is unresolved. I found this problem open and interesting in a way that the GL project never was — it sits at the intersection of geometry, topology, and quantum state evolution, which connects both to Kiko's structured light program and to the Koopman project's underlying question: what is the invariant structure that governs apparently arbitrary dynamical behavior? My instinct is to extend the framework to higher-order Poincaré spheres, where orbital angular momentum modes live — and those are exactly the beams I already generate with my SLM setup. The technical infrastructure is already mine. **[P]**

> Kiko has approved a self-proposed independent project for summer 2026 through senior year; I haven't finalized the specific topic with him yet. The project will become my PHYS 410 senior seminar in fall 2026 and my honors thesis in spring 2027. The specific direction may change with Kiko's guidance, but the general area — geometric phase of structured light on higher-dimensional state spaces — is where I intend to go. **[P]**

> My scientific direction was also shaped by the lab seniors above me. One went to the University of Oregon to study quantum networks; another went to the University of Rochester to study optics — both directly relevant to where I want to go. They helped me technically and were candid with me about graduate school in ways that formal advising rarely is. The three research areas I find most compelling — geometric phase and topology in complex quantum optical systems, quantum chaos as it connects to the Koopman operator framework, and optical quantum circuits — all emerged partly from those conversations, not only from reading papers. The lab culture under Kiko is rigorous in the lab and genuinely relaxed outside it, which is part of why I keep choosing to be there. **[P]**

---

# Part 2 — Target field and PI taxonomy

## 2.1 The five clusters, verbatim, with your own verdicts

> In current spreadsheet of potential PIs, most of the PIs falls into the following categories: 1. **High dimensional Structured Quantum Optics**, which features the intersection of spatial, polarization, OAM, and other degrees of freedom with quantum-state engineering; this cluster includes Otte, Feng, Kwiat, Sergienko, Mehta; Capasso, Litchinitser, and Bigelow. Currently, I am using SLM to modulate classical light beams, and in PhD, I can advance toward quantum states and scalable devices. I am pretty interested in the topological structures entailed in this field and I think this is a promising field to solve information-capacity bottlenecks in communication and quantum information processing, as comparing to electronical circuit, photons have way more degrees of freedom to allow the information to be encoded. **[M]**

> 2. **Classical Structured Light and Singular/Topological Optics**, which features complex phase, polarization, vortices, caustics, and propagation structures. This cluster includes Alonso, Otte, Swartzlander, Litchinitser, Milchberg and Murnane/Kapteyn. This is a more fundamental field of research compared to others, it's mainly focusing on the propagation structure of beams and optical structures. Also faculty in this field tends to collaborate other people in field structured light/quantum structured light. **[M]**

> 3. **Integrated/Nanoscale Quantum-Photonic Platforms**, which implement quantum-optical functions in chips, nanocavities, or metasurfaces. This cluster includes Feng, Mehta, Vamivakas, Alaeian, Capasso, Dimitrova, and Otte. Integrated Photonics Chip is a promising option for future computational platform. Interesting field, but probably restricted since it is closely related to silicone ICs and EUV. **[M]**

> 4. **Atom–Photon Quantum Interfaces**, which use structured light, cavities, or integrated devices to control atomic quantum states. This cluster includes Bigelow, Panda, Dimitrova, and Mehta. This field of research is the most fundamental one among all five. Make this as the secondary choice. **[M]**

> 5. **Ultrafast and Nonlinear Structured Light**, which features temporal degrees of freedom, HHG, strong-field propagation, and nonlinear frequency conversion. This cluster includes Milchberg, Murnane/Kapteyn, Moses, Litchinitser, Alaeian, and Feng. **[M]**

## 2.2 The choice, and the transferability argument — the single most reusable passage for fit blocks

> I think high dimensional quantum structured light would be my current top interest and best fit. My previous work was about using spatial light modulator to encode the phases to a classical laser beam. I am currently able to set-up, configure, and utilize Spatial Light Modulator easily. High Dimensional Quantum Structured Light experiments would also use SLMs, thus my skill set built from the Lab Gravitational Lensing project can be straightly transferred to this field because the same wavefront-shaping principles can be applied to the transverse wavefunction of single photons or photon pairs, but quantum experiments require additional tools such as heralded single-photon or SPDC sources, coincidence counting, single-photon detectors, and quantum-state tomography, and then research about quantum features of those structured light beams. **[M]**

## 2.3 The same taxonomy as ranked in profile.md (compressed, with the constraint noted)

> **Primary:** High-dimensional structured quantum optics — engineering the spatial, polarization, and orbital-angular-momentum (OAM) degrees of freedom of light together with quantum-state control (single photons and photon pairs). Central interest: geometric phase and topological structure in structured light, and how the large photonic degree-of-freedom space can encode and transport information. **[P]**

> **Career-overlap track:** optical / quantum networking — the applied end of high-dimensional photonic encoding. **Avoid:** astrophysics and astronomy-focused programs. **[P]**

**Note for fit blocks:** Alonso (Rochester) sits in Cluster 2 and is a co-author of the Ince–Gauss paper that supplies the §1.1 hook. That connection is not stated in any source — it is the scaffold's observation **[S]** — but it is factually checkable and worth using.

---

# Part 3 — Project 1: the optical analogue of quantum pendulum dynamics

## 3.1 How it started, and the accident that produced the lab position

> The reason why I join this lab is an accident. At the end of the sophomore year, I was trying to apply researches by other colgate faculties as well as trying to look for an external research opportunity in quantum physics, but due to the funding cut that year, all of the professors and institutions that I applied for rejected my application. After a brief period of frustration, I started trying to reach out to prof. Galvez, my physics major advisor, to look for chances to send me to his colleagues and use my Alumni Memorial Scholar's funding, about 10000USD, to fund myself a research project. But turns out prof. Galvez got back to me saying this gravitational project had an open position which haven't been solidified in the Summer Research Application, and he's happy to take me. This is how I got this project. **[M]**

> Before I entered Galvez's lab, I applied for external research positions at Fermilab, the Perimeter Institute in Canada, and Max Planck in Garching. All three declined. Kiko (Prof. Galvez) knew this and offered me a position on the gravitational lensing project. **[P]**

## 3.2 The project itself

> This research started by the simple project about optical analog of quantum pendulum dynamics. Prof. Galvez first taught me how to align the lasers, lens, apertures, mirrors, and cameras. And then he showed me how the lab set-up for the analog of quantum pendulum (which is the same as the gravitational lensing project). This project is like a warm-up to the actual research project. I designed and experimentally achieved a structured optical beam exploiting the resemblance between the Helmholtz–Schrödinger equation equivalence and the wave function of a Matheiu/Eliptical Beams. Generated a Fourier-plane image encoding a superposition of 11 pendular eigenstates, with ring radii proportional to energy and angular modulation proportional to quantum probability density, including bound and rotor states. **[M]**

> Physics: the Helmholtz–Schrödinger correspondence maps paraxial beam propagation onto the Schrödinger equation, so Mathieu / elliptical-beam solutions are the optical image of pendular eigenstates. **[LOG, account]**

## 3.3 Ownership — stated plainly, in three registers

> All major codes are written by previous people, including one that generates a theoretical simulation of the eigenstates and another one that generate the phase encode and controls the SLM. My contribution to this project was fine-tuning the separations, sizes, and brightnesses of the 11 pendular eigenstates encoded in the Fourier plane through MATLAB — ring radii proportional to energy, angular modulation proportional to quantum probability density, encoding both bound and rotor states. We created a few really cool pictures, and I learned how the entire set up works, including the laser alignment, SLM controls, and 4-f Fourier Lens System. I've since extended that alignment skill to the full GL setup and now operate it independently. **[M]**

> **Ownership, stated plainly** (this matters for how the later work is read): the theory-simulation code and the phase-encode/SLM-control code were both **inherited from previous students**. The developer's contribution was tuning the separations, sizes, and relative brightnesses of the 11 states in MATLAB until the superposition was physically usable — and, more consequentially, learning the whole apparatus from zero: laser/lens/aperture/mirror/camera alignment, SLM control, and the 4f Fourier system. Everything in this log after that point is the same bench, operated independently. **[LOG, account]**

> This mastery came from the quantum pendulum project, my introductory lab assignment: the task was to recreate a pendulum optical setup previously built in the lab, and aligning it for the first time with no experience was genuinely painful. **[P]**

## 3.4 The Fourier bridge — computational to physical

> My computational background gave me 2D Fourier analysis before I had any optics experience. With Lam, I worked on pulsar timing residuals using PSD methods, red noise analysis, and 2D Fourier transforms in Python — learning the tools at the data analysis level, applied to gravitational wave detection in NanoGrav post-fit datasets. When I moved into Galvez's lab, I recognized that Fourier-plane encoding in optics is the same operation applied to a different substrate: instead of decomposing a time series into frequency components, you encode a spatial eigenstate superposition in the back focal plane of a lens and the optical Fourier transform physically implements the decomposition. The quantum pendulum project was my first explicit use of this equivalence. I didn't experience these as separate skills — they're the same mathematical object instantiated in two different physical contexts. **[P]**

## 3.5 Status

> **Under review:** Optical analog of quantum pendulum dynamics — submitted to Physics Today (Backscatter) (with Prof. Galvez) **[P]**

<!-- GAP — nothing in any source answers: what output pattern first told you the eigenstate weighting
     was wrong; how you validated the 11-state pattern (visual? quantitative fit? theoretical ratios?);
     the hardest conceptual step in making Helmholtz-Schrödinger physically meaningful; what this
     taught you about structured light beyond a pretty image. -->

---

# Part 4 — Project 2: gravitational lensing — physics, scope, and ownership

## 4.1 The project in your own summary sentences

> The quantum pendulum project continued about 1 month and we moved onto the gravitational project, which extended all the way to this summer. In the past whole year, I designed and carried out an optical simulation of gravitational lensing using laser beams modulated by a spatial light modulator to emulate spacetime curvature. Implemented phase profiles for single and binary Schwarzschild lenses; reproduced interference and fringe patterns analogous to Einstein rings. Quantitatively compared theoretical predictions with measured intensity profiles demonstrating agreement in fringe structure relevant to binary systems and black hole mergers. Simulated the impact on the interference pattern of this binary lensing effect by the change of the frequencies in gravitational wave (which the frequencies is continuously getting higher and then stated the potential phenomenon maybe been observed by gravitational wave observatories such as LIGO project. Independently coded and analyzed the phase structure of the lensed interference pattern by encoding a virtual Mach-Zehnder interferometer in SLM which allows further research in complex optical structures in it. Independently coded and analyzed the areas in the phase encode of the gravitational lensing which contributed the most to the caustic patterns of the interference images, which potentially contribute to understanding of optics around singular areas and critical points. **[M]**

> The part that I enjoy the most in the lab is that I'm most engaged when I own the full stack: optics, control code, data pipeline, visualization. **[M]**

> What I've learned about myself in the lab is that I'm most engaged when I own the full stack: optics, control code, data pipeline, visualization. The moment that stands out most is making the computer establish contact with and simultaneously control the CMOS camera and the LM300 translation stage — writing the communication layer from scratch, then watching the hardware respond to commands I had written. I do embedded development as a personal project outside the lab for the same reason. There is a specific and genuine satisfaction in mastery of a physical system: I now know my optical setup well enough that any misalignment reveals itself in the output beam pattern, and I can diagnose and fix it immediately. That mastery is what keeps me in the lab past midnight and over breaks — not obligation, but the pleasure of a system doing exactly what you intend. **[P]**

## 4.2 The scientific goal, as stated on the poster

> Build a **tabletop optical analogue of wave-optical gravitational lensing** — specifically of a **binary mass lens (BML)** — using a phase-only spatial light modulator (SLM), and then extend it to **polarization** effects in curved spacetime. **[LOG]**

> - Binary systems (binary stars, binary black holes) are ubiquitous, yet their **wave-optical** lensing is essentially unexplored — most lensing work is in the geometric-optics limit.
> - Gravitational waves from compact binaries are long-wavelength and coherent, so **diffraction**, not just ray deflection, imprints the signal.
> - A gravitational-wave detector samples only a **single "pixel"** of a vast diffraction pattern. A tabletop optical analogue with an SLM instead images the **entire pattern** at once. **[LOG]**

## 4.3 The physics, in one paragraph of your own

> The central one is the binary point-mass lens, in which the spatial light modulator imprints the gravitational Shapiro delay as a pointwise phase, φ_SLM(x) = −2k·r_S·T_grav(x), with T_grav = −Σ mᵢ log|x − xᵢ|, which is Equation 13 of the paper. **[CN]**

> **Key experimental insight — only the gravitational part is programmed.** The SLM imprints the Shapiro delay as a pointwise phase, and **free-space Fresnel propagation from the SLM to the camera supplies `T_geom` for free**. **[LOG]**

## 4.4 The three research threads

| Thread | What it is | Status **[LOG]** |
|---|---|---|
| **A** | Scalar BML diffraction caustics — encode the binary Shapiro delay on an SLM, image and measure the caustic, reconstruct the complex field by phase-shifting interferometry | Working end-to-end; data taken; poster presented; theory–experiment agreement with **no adjustable parameters** |
| **B** | Stationary-phase (geometric-optics) minimal-pixel encoding — reproduce the caustic using only the SLM area around the stationary points of the Fermat potential | Simulation complete and quantitatively characterized; hologram generator built; **hardware run pending** |
| **C** | Gravitational Wigner-Rotation-Angle (WRA) polarimetry — realize Miller/Noh's WRA as a dual-SLM polarization rotator, so the lensing potential drives a spatially varying polarization rotation | Full general-relativistic pipeline built and verified numerically; bench tutorial written; **hardware implementation pending** |

## 4.5 The division of labour with Barcelona — the boundary to draw

> The honest one-line version: **the caustic theory is Barcelona's; the instrument, the code, the measurements, and the reduction are Colgate's.** No claim in this log should be read as claiming authorship of the theoretical framework. **[LOG]**

> I should be careful about scope here. The caustic-morphology and multi-wavelength datasets that appear as the paper's principal experimental figures span more work, and more people, than my own involvement; there are five experimental authors. The accurate way for me to describe my role is that I built and calibrated the platform and the analysis, and took the interference-scan and caustic data that I personally acquired, rather than claiming every published figure. **[CN]**

> My role in the Barcelona collaboration phase is limited — parameter adjustment within given ranges, photo acquisition — and I'm honest about that limitation. But the technical skills are entirely my own. **[P]**

## 4.6 What you built that was not assigned

> I also built the ThorLabs hardware automation from scratch — MATLAB IO control of the LM300 translation stage and the CMOS camera, including the communication layer that establishes simultaneous contact with both instruments. That code is now used lab-wide by other projects. On top of the automation, I wrote image analysis code for the GL project: alignment and comparison routines for sequential images, and a movie generation script that assembles 1,000+ images into a frame-by-frame visualization of the merger pattern evolution as two Schwarzschild lenses approach each other. Neither the image analysis nor the movie was assigned; I built both just because they were better ways to work with the data. Previous lab members working on the GL project had not been able to produce clean, usable images; I was the one who eventually solved the experimental problems and generated the actual data. **[M]**

> I rewrote the ThorLabs LM300 and CMOS camera automation from scratch without being asked; that code is now used lab-wide by other projects and members. I also built, independently, a frame-by-frame movie of the GL merger pattern evolution across 1,000+ images — Kiko hadn't requested it; I built it because a movie was a clearer way to show the data than static frames. Neither of those came from an assignment. **[P]**

## 4.7 The virtual interferometer — the idea worth naming

> **The idea worth naming: a virtual interferometer encoded inside the SLM.** The reference arm is not a second physical path. It is added *in the encoded field* — so a single common-path hologram carries both the lensed wave and its reference, and the phase step is a number in a loop rather than a mirror on a piezo. Consequences: **No moving parts** → no mechanical drift between frames of a 73-frame stack; **the phase step is exact by construction**, not calibrated; the two "arms" share every optic downstream, so common-mode aberration and air-path phase cancel; arm balance is a scalar, so fringe visibility is tunable in software. **[LOG]**

> This is the "**virtual Mach–Zehnder written into the SLM**" that made phase-resolved analysis of the lensed field possible at all — the wavefront's *phase* structure, not just its intensity, becomes measurable with no additional hardware. It is the direct enabler of `analysis.phaseMap`, of the measured phase maps on the poster, and of the optical-vortex/OAM detection that bridges this project toward structured-light work. **[LOG]**

## 4.8 Phase profiles implemented — the full inventory, your words

> I built the phase-encoding layer of this experiment, and by now it covers essentially every phase profile the laboratory uses. **[CN]**

> Alongside it I implemented the single point-mass logarithmic lens, φ = −2kβ·ln(ρ/σ), which is the zero-separation limit that produces the Einstein ring and which I used constantly as a calibration case; a power-law potential for exponents greater than one, giving the quartic-potential and parabolic beams; a cotangent potential; and an elliptical variant built on elliptical rather than circular coordinates, for asymmetric lenses. On top of these I wrote a stationary-phase version of the binary lens, in which the same gravitational phase is retained only inside small disks surrounding the stationary points of the Fermat potential and every other pixel is set to zero phase — this is my own extension of the paper's geometric-optics section. **[CN]**

> A second family is beam shaping and structured light. I implemented optical vortices carrying orbital angular momentum, exp(iℓφ), which can be added on top of any lens phase and which I also use on its own as the alignment pattern, since a vortex first order forms a doughnut with a dark null that is far more sensitive to misalignment than a bright spot. I implemented Laguerre–Gaussian modes, which because they carry amplitude as well as phase had to be encoded with complex-amplitude modulation rather than phase-only encoding. I implemented blazed gratings to steer the signal into the first diffraction order away from the undiffracted zero-order ghost, including a variant specified by incident and diffracted angles rather than line counts, and a beam-dump grating outside the aperture so that stray light is thrown off the camera instead of contaminating the measurement. I implemented a quadratic lens phase, which I ended up using less as a beam-shaping element than as a diagnostic instrument, sweeping its focal length to locate the camera relative to the Fourier plane. I implemented a flat-phase annulus, the Durnin ring, which a lens Fourier-transforms into a J₀ Bessel beam. I implemented nine-term Zernike aberration correction. And I implemented a coherent plane-wave reference with a tunable phase offset, which is the element that makes phase-shifting interferometry possible on this setup at all. **[CN]**

> A third family goes beyond the published paper into two further analogue spacetimes. The first is a gravitational Wigner rotation field, a spatially varying rotation of the polarization plane driven by the lensing potential and computed from a full Kerr geodesic and tetrad calculation, which is encoded not as a scalar phase but as a differential phase across two modulators, one receiving Φ + θ and the other Φ − θ. The second is a cosmic string, whose spacetime is locally flat but globally conical, so that light deflection is a purely topological effect independent of impact parameter and the string behaves as a perfect gravitational Fresnel biprism. **[CN]**

> There are also profiles I did not invent but substantially corrected. The most consequential is the binary separation itself, which had been specified in pixels. A fixed count of seventy pixels is 1.40 mm on our twenty-micron Hamamatsu modulator but only 0.56 mm on the eight-micron Holoeye, so the same number silently encodes a physically different binary on each device. I changed the interface to take a separation in metres and convert per device, which is what guarantees that a stated dimensionless separation corresponds to the intended physical one. I also made every phase profile wavelength-aware, so the encoded physics stays correct when the laser changes, and I added a global phase-polarity correction after discovering that one of our modulators imprints the negative of the addressed phase. **[CN]**

## 4.9 Experiments completed on the single- and binary-lens systems

> The single lens, the zero-separation limit, is circularly symmetric and produces concentric diffraction rings — the Einstein ring and its wave-optical decoration. I used it throughout as the validation and calibration case, because its symmetry makes any encoding error immediately visible. Concretely I ran automated scans over the effective Schwarzschild radius with camera capture at each step, displayed single-lens holograms with and without added orbital angular momentum, and compared the same single-lens wavefront encoded on two different modulators to confirm they were doing identical physics. **[CN]**

> The binary lens is the physics of the paper: a caustic that evolves through a sequence of shapes as the mass separation grows, decorated everywhere by wave interference. On it I built the automated parameter scan that computes a hologram, displays it, auto-exposes the camera, captures, and saves one frame per parameter value, with optional translation-stage motion, which is the acquisition loop behind a caustic-morphology series. I built the phase-shifting interference scan, in which the binary lens is held fixed while a coherent reference plane wave is stepped through a full cycle from zero to 2π, one frame per step; this is what gives access to the complex field rather than to intensity alone, and I acquired a seventy-three-frame dataset at 4096 by 3000 pixels with it. From those scans I reconstructed measured phase maps of the binary caustic at three separations and located the phase singularities in the reconstructed field. I extended the binary lens into the geometric-optics regime by implementing the stationary-point solver, classifying each image by Morse index as minimum, saddle or maximum, computing its signed magnification from the inverse determinant of the Hessian, and plotting the critical curves where that determinant vanishes together with their image in the source plane, which is the caustic; I then tested quantitatively whether driving the modulator only around those stationary points still reproduces the caustic. I ran the binary lens on two different modulators and proved the encodings physically equivalent, which is the precondition for the two-modulator polarization experiment. And I diagnosed and fixed the reason the binary caustic would not form on the second device at all. **[CN]**

## 4.10 Acquisition, organization and comparison of images

> For acquisition I wrote an auto-exposure controller that drives the camera to the boundary of saturation — as bright as it can be without clipping. It adjusts exposure first by proportional control, scaling the current exposure by the ratio of the target level to the measured peak, and falls back to a binary search on gain only when exposure has reached the limit of its range; if neither can reach the target it stops and tells the user specifically to add or remove neutral-density filters rather than silently returning an unusable frame. The peak is defined as the level exceeded by the brightest one percent of pixels, so a handful of hot pixels cannot fool it. This matters more than it sounds: a saturated core destroys the phase reconstruction, while an underexposed frame loses the faint interference structure outside the caustic, which is precisely where the diffractive physics lives. **[CN]**

> For organization, every scan writes one image per parameter value with a systematic indexed filename, so a dataset is self-describing and the parameter axis is recoverable from the files themselves. I kept raw image sequences out of version control and versioned instead the code that produces and consumes them, since the sequences run to hundreds of megabytes. **[CN]**

> For comparison I wrote several tools, each answering a different question. One compiles a scan into a movie with the parameter value overlaid on each frame, so that a morphological evolution can be watched as a continuous sequence rather than inspected frame by frame. Another merges two depth-scan datasets, corrects lateral beam drift by registering clicked beam centres on the first and last frames of each set, and tracks intensity at chosen points across depth. A third resamples holograms from two modulators of different pixel pitch onto a common micrometre grid and reports the root-mean-square phase difference, which turns the question of whether two devices are doing the same physics into a number instead of an opinion. And the examples themselves carry built-in A/B diagnostic panels. Underlying all of this is a piece of memory engineering that was necessary rather than elegant: raw frames are twelve megabytes each and a scan approaches nine hundred megabytes, so the reconstruction never holds the stack in memory, instead cropping, downsampling and accumulating the transform incrementally, with the modulation frequency auto-detected from a coarse low-resolution pass first. **[CN]**

## 4.11 The software platform

> I wrote a complete MATLAB instrument-control and analysis platform, currently about eight thousand lines across roughly seventy source files and forty-eight commits. It replaced a set of flat, undocumented scripts that had thirty-seven copies of vendor libraries sitting loose in the repository root, where a crash during loading could corrupt them. **[CN]**

> The architecture I designed separates optical computation, which is pure and side-effect-free, from hardware control, so that the entire physics stack runs and can be tested with no hardware attached at all. Around that sit camera and translation-stage control written with a cleanup discipline that releases devices safely even on an interrupt or a crash — before this, a crash meant power-cycling the camera to recover it. There is a post-processing layer for phase reconstruction, depth-scan merging and movie compilation; a full hardware simulator mirroring the camera, modulator and stage interfaces so that scans can be written and regression-tested without occupying the optical table; twenty-one runnable experiment scripts; and about eleven hundred lines of user documentation together with a bench-build tutorial for the polarization experiment. **[CN]**

> The individual pieces I would single out are these. The phase reconstruction, at five hundred lines, recovers the complex field from a phase-shifting sequence by a single-bin temporal transform at each pixel and then detects optical vortices in the result; the net topological charge is measured by integrating phase winding around circles in the high-contrast fringe zone rather than by counting cores, which makes it immune to a saturated beam centre and cancels noise-generated vortex pairs, since those always appear in pairs of opposite sign and vanish around any enclosing loop. Three independent core detectors, based respectively on loop circulation, on simultaneous zeros of the real and imaginary parts of the field, and on circular phase variance, let me cross-check a result three ways. The Wigner-rotation module, at four hundred and forty-five lines, carries a Kerr null geodesic through an analytically constructed orthonormal tetrad to the local Lorentz generators and thence to the rotation angle and its non-reciprocal part; it is a genuine general-relativistic calculation rather than a paraxial approximation. The stationary-phase module, at four hundred and nineteen lines, contains the analytic stationary-point solver, the Morse classification and a Nyquist-driven automatic choice of display resolution. The cosmic-string module is four hundred and twenty-four lines. The auto-exposure controller is one hundred and eighty-five. There is also test infrastructure: a twelve-check regression suite on the hologram interface and a three-hundred-line end-to-end simulation that exercises every layer of the package on synthetic data. **[CN]**

> One contribution I want to name explicitly because it never appears in a figure is that I made the calibration wavelength-aware. Previously, changing lasers required a manual table lookup and several hand edits, with a genuine risk of encoding the wrong phase depth and therefore the wrong physics. I implemented an interpolation of the phase calibration over the range from 403 to 684 nanometres, with a warning on extrapolation beyond it, and made the grating auto-scale so that the diffraction angle is preserved as the wavelength changes. Now only the wavelength itself needs to be edited. The paper's multi-wavelength result — a composite of fourteen wavelengths from 403 to 684 nanometres, showing that the caustic geometry is achromatic while the interference fringes disperse — is exactly the kind of measurement this turns from error-prone into routine. **[CN]**

---

# Part 5 — The challenge arcs, in full

*Four complete arcs exist. Materials.docx has all four in your own words; PROJECT_LOG has three of them reconstructed with more technical precision. Both versions are given for the two that matter most.*

## 5.1 ARC 1 — The initial alignment problem (multi-wavelength setup)

**Your version:**

> The challenges that I have met during the multi-wavelength scan is the alignment of the setup. Before I took over the setup, the images we took is always kind of deformed and asymmetrical in shape and intensity. I first try align the camera as it's the easiest fix, but its not quite working. Then, I started remove the lenses of the 4-f Fourier system, and I found the laser is not quite aligned with the first order of the SLM output, then I encode the SLM with an optical vortex (the benefit is to be able to see if the laser passes the center of the iris used for aligning the system) and then we tune the mirrors to align the 4 f system. The uneven intensity of the pattern turns out to be caused by incoherent brightness of the laser source, the issue is solved by slightly move the lenses of the beam splitter. **[M]**

**The log's reconstruction, with the diagnostic chain numbered:**

> 1. Re-align the camera — cheapest hypothesis, and it did **not** fix it.
> 2. Strip the 4f lenses out of the path to remove them as a variable → revealed that **the laser was not aligned to the SLM's first order** in the first place.
> 3. **Invented a diagnostic that is still in use:** encode an **optical vortex** on the SLM. Its dark central null makes it immediately visible whether the beam passes through the *centre* of the alignment iris — a null is far more sensitive to judge than the centroid of a bright spot. The mirrors were then tuned against that criterion to align the 4f system. *This diagnostic was later productized as `optics.alignmentHologram` (grating + charge-3 vortex) — the bench trick came first, the function came a year later.*
> 4. The residual **intensity asymmetry** turned out not to be alignment at all but **uneven source brightness (incoherent background) from the beam-splitter arm**; fixed by slightly repositioning the beam-splitter lenses. **[LOG, account]**

**The related craft passage — diffraction-order management:**

> The non-trivial part of SLM work isn't the phase encoding itself — it's managing the pixelization artifact. The SLM's pixel grid acts as a diffraction grating, creating a cross-pattern of zero, first, second, and higher diffraction orders in the output. To get a clean image, you have to apply a separate grating in the phase plane to spatially separate the first diffraction order — the signal — from the zero order and higher orders that carry SLM artifacts and interference. Designing that grating requires balancing three parameters: if the grating is too dense or too loose it degrades diffraction quality; if the tilt angle is too steep the beam can't be re-aligned to the optical axis. The working parameter range isn't in any manual — I learned it empirically, through iteration and laser realignment. I can teach this process from scratch, including the physics of why it's necessary, the trade-offs in parameter space, and how to diagnose when the grating is misconfigured from the output beam alone. **[M]**

> **Previous project members had not been able to produce clean, usable images; this is the step that produced the first ones**, and hence the data the manuscript reports. **[LOG, account]**

## 5.2 ARC 2 — The dual-SLM code re-architecture

> One of the biggest challenges that I have confronted is configuring the new spatial light modulator. This summer, prof. Galvez decided to introduce a new Holoeye Pluto 2.1 NIR145 LCOS-SLM into the current setup. This new SLM should connected with the Hamamatsu LCOS-SLM in series. The first problem arises is a coding one. The code we used before are adapted to the Hamammatsu SLM which have different pixels size and resolution from the new Pluto 2.1 on which the functions to generate the phase encodes rely, therefore I will need to adapt the code to allow the current code to control and configure the new SLM correctly while able to control the old device in the same file. Instead of simply adding more functions or variables to create mess, I reconstruct the repository in a format like a python library, which I use a configuration function to control the initiation and configuration of both SLM and generate a configuration matrix for both of them, and re-write the functions to allow them to read the configurations to avoid writing a redundant and essentially the same code base for the new SLM, and this would make the future adding more and different SLMs much easier by writing a new configuration function. **[M]**

## 5.3 ARC 3 — The sign flip (the cleanest elimination arc)

**Your version, in full:**

> After the coding issue, I then confronted several issues with the SLM. After setting up the SLM, I first tried to encode a Bessel Beam on the new SLM to see if the 4-f system is able to function correctly with the second Hamamatsu SLM. I am intending to see the concentric circles at the end of the 4-f system, but turns out I saw a big circle which should only appear at the far field of the beam. I originally thought it's the input beam of the SLM not collimated so it brought an angle to make thing focus very close to the SLM plane. I tried using the Shearing Interferometers to verify the collimation of the laser beams after the beam expander (composed by 2 apertures), by changing the separation between the lenses I have collimated the lasers but the issue was still there. Then, I thought it could be the LUT issue, which is the dictionary which governed how the gray-scale image ranging 0 to 255 to be translated in to 0 to 2pi phase delay on the SLM. I digged through the document of the Holoeye Pluto 2.1 and configure the SLM with correct LUT file, the issue is still not solved. Then I started suspecting I encode the SLM wrong, I compared the effect of the same phase encode on the both SLMs, I gave them a plain grating to deflect light from zero order to the first order. I found the new slm simply deflect the light to opposite direction from the old Hamamatsu one. I realized this is the actual issue, and I suspecting the new slm just deflect lights in the opposite way compared to the old SLM. Then I add a -1 multitude to the entire phase map, and the issue been fixed. **[M]**

**The log's reconstruction of the same arc, structured as hypothesis elimination:**

> **Expected.** With the new Holoeye PLUTO-2.1 installed, a **Bessel-beam** test pattern should show **concentric rings** at the output of the 4f system.
>
> **Observed.** A single **large ring** — the far-field signature — as though the beam were coming to focus very close to the SLM plane. Not a subtle discrepancy: the pattern was in the wrong *regime*, so it could not be tuned away and could not be ignored.
>
> **Hypothesis 1 — the input beam is not collimated** (an uncollimated input adds curvature and would pull the focus in toward the SLM). Test: a **shearing interferometer** after the beam expander, adjusting the separation of the expander lenses until the shear fringes ran parallel — the standard collimation null. Collimation achieved. **Symptom unchanged → eliminated.**
>
> **Hypothesis 2 — the gray→phase LUT is wrong.** The Holoeye's look-up table maps gray 0–255 onto 0–2π; a wrong table means the addressed phase is not the imprinted phase. Test: read the PLUTO-2.1 documentation, identify and load the correct LUT/config for the device and wavelength. **Symptom unchanged → eliminated.**
>
> **Hypothesis 3 — the phase encoding itself.** Designed the decisive controlled test: give **both SLMs the same, simplest possible pattern** — a plain blazed grating, whose only job is to deflect light from the zero into the first order — and compare. **The new SLM deflected the first order in the opposite direction from the Hamamatsu.** That single observation localizes the fault to the sign of the imprinted phase, independently of lenses, collimation, alignment, or the lensing physics.
>
> **Fix and result.** Multiply the entire phase map by −1. Rings appeared.
>
> **Why this arc is the good one:** each hypothesis was killed by an *independent measurement* rather than by a parameter tweak (an interferometer for collimation; the vendor's own calibration for the LUT; a null-physics pattern for the encoding), and the decisive test was chosen because it removed every variable except the one under suspicion. **[LOG, account]**

**The consequence — what the fix generalized to, and what it forced you to retract:**

> The most consequential is diagnostic. When our second modulator refused to form a lensing caustic, I first proved numerically that the caustic distance is independent of pixel pitch but scales inversely with phase depth, which reframed an apparent geometry problem as a calibration problem. Later, displaying a plain focused spot revealed that the camera was sitting thirty-five centimetres past the Fourier plane, so several earlier anomalous patterns had simply been defocused aperture disks. The true root cause turned out to be that the panel imprints the negative of the addressed phase, and recognizing that let me replace two empirical sign corrections with a single global negation that fixes gratings, lenses and orbital-angular-momentum charge simultaneously. I documented the hypotheses that turned out to be wrong, and why they had been convincing. **[CN — this is CN's own "Emphasizing problem-solving" drafted passage, marked there as liftable]**

> **Two earlier conclusions were retracted in writing.** Both the *"geometric flip / mirror-opposite mounting"* explanation and the *"converging incident beam, R_c = −0.319 m collimation"* measurement were **confounded by the unrecognized phase inversion**. The `collimateF` block was therefore commented out — not deleted — with a header explaining precisely why the numbers must not be trusted. Keeping the retraction, the reasoning, and the superseded numbers in the repository — rather than quietly overwriting them — is the practice this project settled on. **[LOG]**

## 5.4 ARC 4 — Series alignment and the oblique-incidence fix (the grit beat)

**Your version:**

> After all these issue been fixed, I started align the first and second slm in series. I coded a phase mask with a cross in the center and put it on both of the SLMs, this test have two goals: 1. To ensure the 4-f system on the first slm which the beam hits the second slm should be the same as when its just come out from the first slm which you will expect to see overlapped crosses with the same size if its correctly aligned and setup. It passes this test after several tries. But when I started put grating on the first slm to deflect light to the first order, and encode the second slm with the Bessel beam front, problems emerged. The first order light hitting the second slm turns out containing the some extra phase which deformed the entire Bessel rings. Rather than seeing elegant concentric circles, I observed fragmented curves and cusps. Then I started remove the lenses to see if the extra phases are introduced by the 4-f system, but the issue stays there, then issue can only be the mirror between the iris and the second lenses. I then took off the mirror and try move around to see if theres any position creating images without deformation. That was the messiest station I've ever had, tools, lenses, irises are all over the table. But I am not around of making such as ness, I believe this is the necessary step. I've found the deformation disappears only when the laser beam enters the SLM at a certain angle. I tried to center the beams while keeping the angle between the laser and the SLM and it finally works. **[M]**
> <!-- typo in source: "I am not around of making such as ness" = "I am not afraid of making such a mess" -->

**The log's cleaned quotation of the same moment, and the honest ending:**

> *"That was the messiest station I've ever had — tools, lenses, irises all over the table. But I'm not afraid of making such a mess; I believe this is the necessary step."* **[LOG, account]**

> **The observation that resolved it.** The deformation **vanished only at one specific angle of incidence of the beam on the SLM** — not at a specific position. The final geometry was found by re-centring the beam on the panel *while holding that incidence angle fixed*, which is a two-constraint alignment rather than the usual one.
>
> **Physical reading.** A phase-only LCOS is a reflective device with finite liquid-crystal thickness; at oblique incidence the optical path through the LC layer, the effective pixel pitch seen by the beam, and the geometric wavefront tilt all change, so the imprinted phase acquires an incidence-dependent aberration on top of the intended map. The empirical result — one good angle — is consistent with that, but **it was not modelled or parameterized**, and this is recorded as resolved-in-practice, not explained. **[LOG, account]**

## 5.5 The log's own ranking of the arcs

> **Arc A — "The new SLM imprints the negative of what you tell it."** *Why it's the strongest arc:* every hypothesis was eliminated by an independent instrument, not by tuning; the decisive test was designed to isolate exactly one variable; and the ending is about recognizing that earlier conclusions were wrong.
>
> **Arc B — "Pixel pitch cannot be the problem; phase depth can."** *Why it matters:* it is the clearest instance of the working method — **derive the expected physical scaling first, and only then touch the bench.**
>
> **Arc C — "The camera was never where everyone thought it was."** *Why it matters:* it converts "the SLM is broken" into a measured number, and the measurement technique (encode a lens, sweep it, fit the minimum) is reusable.
>
> **Supporting beat, if a grit moment is wanted:** the oblique-incidence hunt — dismantling the relay, hand-searching mirror positions, and finding that the deformation vanishes only at one specific angle of incidence. Honest ending: fixed in practice, never modelled. **[LOG]**

---

# Part 6 — Results, significance, and what was reproduced

## 6.1 The phenomenon reproduced

> The wave-optical diffraction pattern of a gravitationally lensed source — a phenomenon that has never been directly observed in astronomy. Specifically, we reproduced the binary-lens caustic together with its full morphological metamorphosis as the scaled separation grows: at zero separation the pattern is the circularly symmetric ring system of a single point mass; the moment symmetry is broken it becomes a central astroid; that astroid merges with the deltoid caustics above and below it into a vertically elongated hypocycloid; the structure then re-elongates in the orthogonal direction until it splits into two distinct astroids joined by a thin caustic bridge, which finally breaks and leaves two separated asymmetric astroids. Crucially, what appears on the camera is not the sharp skeleton that ray optics would predict but a diffraction catastrophe: folds and cusps dressed everywhere in interference fringes, with a symmetric crosshatched network of minima extending well beyond the geometric caustic boundary. I also reproduced the complex field rather than merely its intensity, recovering measured phase maps of the caustic and locating its phase singularities. Along the way, as validation of the platform, I reproduced Einstein rings in the single-lens limit, J₀ Bessel beams, optical vortices of known topological charge, and Laguerre–Gaussian modes. In simulation and beyond the scope of the paper, I reproduced a gravitational Wigner rotation imposed on the caustic as a polarization texture, and the interference pattern of a cosmic-string conical spacetime. **[CN]**

## 6.2 Agreement with theory — three levels

> At three progressively more demanding levels, and it is the third that constitutes the new result. At the first level, the caustic geometry agrees: the four characteristic dimensions measured between the cusps and folds track the theoretical curves as the scaled separation varies, with no adjustable parameters, across the enormous gap in length scale between the laboratory and astrophysics. At the second level, the wavelength behaviour agrees in a way that is doubly informative, because the caustic geometry is fixed by the dimensionless separation alone and is therefore identical at every wavelength, while the fringes superimposed on it are governed by the dimensionless frequency and therefore disperse; both behaviours were confirmed across the full 403 to 684 nanometre range, with fringe spacing scaling linearly in wavelength away from the caustic and as the two-thirds power near a fold, which is the Airy scaling. At the third level, the fine interference structure itself agrees: a point-by-point comparison at a dimensionless frequency of eighty and a scaled separation of 1.07 matched the theoretical centroids of the diffraction maxima onto the measured image, and intensity cuts agreed in both position and relative amplitude. This last point is the paper's central novelty claim, and it is worth stating precisely: earlier experiments had confirmed caustic morphologies, whereas agreement at the level of the detailed diffraction structure is a qualitatively new level of validation. **[CN]**

> Where agreement is imperfect I should say so honestly. Absolute intensity levels differ between experiment and theory because the backgrounds differ, so profiles are compared relative to their respective means. And the geometric image sum degrades near caustics, which is expected, because that is exactly the regime in which the stationary-phase approximation is known to fail; rather than paper over that, I quantified it. **[CN]**

## 6.3 Quantitative theory–experiment comparison

> Yes, and quantitative comparison is really the habit I built the entire toolchain around. The most important instance is the one that reaches the paper: from the interference scans I reconstructed the complex field of the binary caustic at scaled separations of 0.8, 1.1 and 1.6, and measured intensity cuts overlay the wave-optical prediction with maxima and minima aligning with no adjustable parameters whatsoever, across length scales that differ between the laboratory and astrophysics by many orders of magnitude. **[CN]**

> Beyond that, I quantified where the geometric-optics approximation fails, which is a comparison of an approximation against a full wave calculation rather than against data, but is the same discipline. Correlating the far-field pattern of the stationary-phase hologram against that of the full lens as a function of the retained disk radius gave 0.43 at three-tenths of an Einstein radius, 0.78 at six-tenths, 0.95 at eight-tenths while using only about thirty percent of the aperture pixels, and 0.99 at one full radius. The interesting content of that curve is the failure at small radii: it confirms the theoretical caveat that the stationary-phase sum breaks down at caustic scales, so the retained disks must cover the regions where critical curves merge, not merely the isolated images. **[CN]**

> Several diagnostic comparisons followed the same pattern of predicting a number before measuring it. I measured the dark-ring radii of a generated Bessel beam at fifteen, thirty-four, fifty-three and seventy-two pixels, a spacing of about nineteen pixels, and checked them against the predicted core radius. I located the camera relative to the Fourier plane by sweeping an added lens phase and fitting the parabolic minimum of the spot width, which fell at minus 0.80 metres between measurements of 0.48, 0.198 and 0.38 millimetres, and from that predicted a displacement of about thirty-five centimetres past focus. I predicted that over-modulating the phase by a factor of 255 over 190 would move a caustic to 0.745 times its proper distance, which is the ratio of three focal lengths to four, and that was exactly the discrepancy observed on the bench. I showed that holograms encoded on two modulators of different pixel pitch agree to nine degrees root-mean-square in phase, the residual being pure resampling error. For the cosmic-string module I measured the fringe period from direct Fresnel propagation and showed it to be independent of propagation distance for collimated illumination, which falsified a formula in the design guide I had been given. And for the general-relativistic pipeline I verified the invariants that must hold if the calculation is right: the null condition to two parts in ten to the fifteenth, tetrad orthonormality to four parts in ten to the sixteenth, antisymmetry of the Lorentz generators to two parts in ten to the eleventh, and recovery of the known trivial case when the quantization axis is aligned with the momentum. **[CN]**

## 6.4 Which features are physically meaningful

> The Einstein ring at zero separation is the perfectly aligned single-mass limit, and its concentric diffraction rings are the wave-optical fingerprint of a point-mass lens. The folds and cusps of the binary caustic are not incidental shapes but universal ones: catastrophe theory guarantees that only these two singularity types are structurally stable in two dimensions, and the diffraction local to each is described by the Airy function at a fold and the Pearcey integral at a cusp, with the positions of the first intensity maxima following universal scaling laws in the dimensionless frequency, as the minus two-thirds power at a fold and the minus one-half power at a cusp. That universality is the reason a tabletop measurement transfers to astrophysics at all. The caustic itself is where the magnification diverges, since it is defined by the vanishing of the Hessian determinant, and crossing it changes the number of images by two, so caustics are precisely where a lensed signal is most strongly amplified and where a lensed gravitational-wave event would be most detectable. The fringes lying beyond the caustic boundary matter for the opposite reason: ray optics predicts nothing at all there, so their existence, and the fact that they form regular arcs of alternating maxima and minima, is a direct signature that the wave description rather than the ray description is required. The phase singularities I detected in the reconstructed field are points of undefined phase and zero intensity carrying quantized topological charge, and they are a structural feature of the lensed field that only a complex-field measurement can reveal. Finally, the breaking of the caustic bridge as the separation grows is the topological transition of the binary lens, and it is the observable that most directly encodes the mass separation. **[CN]**

## 6.5 The problem the project solved

> Gravitational-lensing diffraction has never been directly observed, and for light it probably cannot be. Astrophysical sources are spatially extended and incoherent, optical wavelengths are far too short, and coherence does not survive cosmological distances, so the wave-optical regime of lensing has remained almost entirely theoretical. Gravitational waves are the exception, since they are long in wavelength, phase-coherent over cosmological distances, and emitted by effectively point-like sources, so diffraction ought to be imprinted on them. But we cannot image a lensed gravitational wave either: a detector samples a single point of a diffraction pattern that extends across light-years, and any signature must be inferred indirectly from modulations of the detected waveform. **[CN]**

> This project solves the observability problem by substituting a controllable analogue for the inaccessible system. A spatial light modulator imprints the gravitational Shapiro delay onto a coherent laser beam, free-space propagation supplies the geometric part of the time delay for free, and a camera images the entire diffraction pattern at once — in minutes, repeatably, with every dimensionless parameter under direct control. It converts a regime that is unobservable in the sky into a bench measurement. **[CN]**

## 6.6 Value to the field — and the programmable-spacetime idea

> For gravitational-wave astrophysics, it provides experimentally validated ground truth for wave-optical lensing calculations, and does so at the level of the fine interference structure rather than merely the caustic outline, which is a direct check on the modelling that lensed-wave searches depend on. Because the physics is governed entirely by dimensionless parameters, each measured optical pattern maps onto a whole family of astrophysical scenarios sharing the same wave optics. We also reproduced the chirp: by scaling the effective Schwarzschild radius and the propagation distance while holding the scaled separation fixed, a sequence of laboratory patterns emulates the frequency sweep of an inspiral over a range that includes the thirty-five to two-hundred-fifty hertz sweep of the first detected gravitational-wave signal, so the analogue can show how a lensed chirp's diffraction signature would evolve. Practically, the structure near caustics, with its sharp rapidly varying fringes and strong constructive amplification, is directly relevant to the data-analysis pipelines that would have to identify a lensing event. **[CN]**

> For laboratory analogue simulation, the deeper point is that a spatial light modulator is a programmable spacetime. Any thin-lens gravitational potential can be written as a phase mask, so the same apparatus that makes a binary black-hole lens can make a cosmic string or a Kerr Wigner rotation without changing a single optical component, and I have now implemented all three. The platform is also agnostic to the astrophysical origin of the lens, since wave-optical lensing depends only on the projected mass distribution and not on the dynamical state of the system, so bound binaries, unbound pairs and primordial objects are all covered equally. And the polarization work extends analogue gravity beyond scalar diffraction, making a gravitationally induced polarization rotation, and its non-reciprocity, into a bench-measurable quantity. **[CN]**

## 6.7 Proof of concept and platform

> It provided both, and I would argue those are the two things a young field most needs. As a proof of concept it establishes something that could not be established observationally: that the wave-optical lensing formalism is correct at the level of the detailed diffraction pattern, verified with no free parameters across an enormous gap in scale. Before anyone can trust a lensing-diffraction signature extracted from a noisy gravitational-wave signal, the underlying physics should be confirmed somewhere it can actually be imaged in full, and this is that confirmation. **[CN]**

> As a platform, what I built outlasts any single result. It is a programmable, wavelength-agile, automated instrument in which the lens potential is software, the acquisition is scripted and the analysis recovers the complex field, so adding a new spacetime amounts to writing a new phase function — which is exactly how the cosmic-string and Wigner-rotation modules came to exist. It also serves as a testbed for questions that would be expensive to investigate any other way; the stationary-phase encoding, for instance, asks how much of a lens one actually needs in order to reproduce its caustic, and answers it quantitatively at disks of eight-tenths of an Einstein radius, about thirty percent of the pixels, for a correlation of 0.95. And it is a training platform, in that it makes a regime of general relativity which is otherwise entirely inaccessible into something a student can align, measure and compare against theory in an afternoon. **[CN]**

## 6.8 The intellectual through-line, as the log states it

> **Enlarge the representation until the hidden structure becomes analyzable.**
>
> - The lensing caustics are **critical points of the time-delay function** — the structure lives exactly where the ray picture breaks down. The interesting object is not the ray; it is the catastrophe.
> - The **phase**, not just the intensity, is made measurable by co-encoding a reference wave into the hologram — enlarging the observable from |U|² to U.
> - From the reconstructed field, **topological charge** is extracted by loop integrals: an integer-valued invariant that survives a saturated core and cancels noise-generated vortex pairs. Local data → global invariant.
> - The **WRA thread** adds a second degree of freedom on top of the same beam: the common part of the dual-SLM phase carries the diffraction caustic, the differential part carries a polarization texture. One beam, two independent structures.
> - And the clearest single result of that thread: in the rotator configuration the **helicity-basis phase and the classical azimuth rotation are literally the same number** — the quantum and classical faces of one quantity, visible only after changing basis. **[LOG]**

---

# Part 7 — Credentials, dissemination, and numbers safe to quote

## 7.1 The manuscript

> The paper referred to throughout is A. Moreso Serra, O. Bulashenko, Y. Gu, T. Nguyen, K. Kendja, V. Rodríguez-Fajardo and E. J. Galvez, "Laboratory observation of lensing diffraction in a binary-lens system for gravitational-wave astrophysics," dated 8 June 2026, a collaboration between the Institut de Ciències del Cosmos in Barcelona, which supplied the theory, and the Colgate University optics laboratory, where the experiment was done. I am the first-listed author of the Colgate experimental group and the third author overall. **[CN]**

> **Gu is the first-listed Colgate author — the lead experimental author on the paper.** Corresponding authors: Bulashenko (ICCUB) and Galvez (Colgate). **[LOG]**

> The accurate phrasing is **"co-first / lead experimental author"** or **"first-listed Colgate author"** — not sole first author, and never authorship of the theory. **[LOG]**

## 7.2 The six defensible attributions

> Six things I can defend from artifacts I own. First, the experimental control and acquisition software for the whole optical platform, covering hologram generation, modulator display, camera control, automated parameter scans and the data pipeline behind the recorded diffraction patterns. Second, the wavelength-dependent phase calibration and grating scaling that makes the fourteen-wavelength study reproducible rather than a series of hand re-calibrations. Third, the phase-shifting interference-scan method and its reconstruction, which measures the complex lensed field, phase as well as intensity, together with the associated optical-vortex analysis; this goes beyond intensity imaging. Fourth, the metric-correct encoding of the binary separation, which is what guarantees that a quoted dimensionless separation corresponds to the intended physical one on any device. Fifth, the geometric-optics extension, in which I implemented the paper's image-sum, Hessian-magnification and Morse-index equations as a working hologram generator and then quantified where the approximation fails. Sixth, the poster presenting the work, including its simulation figures. **[CN]**

> What I must not claim without checking is authorship of specific published figures, or of the original measurements behind the phase calibration table. **[CN]**

## 7.3 The poster

> For the poster, titled "Laboratory Astrophysics of Gravitational Lensing" and authored with Professor Galvez, I restructured the layout into three columns and generated its simulation figures. Those are a density map of the Shapiro time-delay function over the lens plane, which is literally the phase written to the modulator; a side-by-side comparison of the far-field caustic produced by the full binary lens against the one produced by the stationary-phase mask at a scaled separation of 1.09, showing that five disks covering about half the aperture recover the same fold and cusp structure; and an image of the retained disks themselves. The poster also carries the measured phase maps at three separations reconstructed from my interference scans, and the theory-versus-experiment intensity cuts. I additionally corrected the poster's physics against the source paper and added the governing equations, namely the Fresnel–Kirchhoff diffraction integral, the decomposition of the Fermat time-delay function into geometric and gravitational parts, the boxed encoding relation, and the geometric-optics image sum with its magnification and Morse index. **[CN]**

## 7.4 Full dissemination ledger

| Output | Venue / status | Role **[LOG]** |
|---|---|---|
| Binary-lens manuscript | Under review, dated 2026-06-08 | **Lead experimental author** (first-listed Colgate author) |
| "Laboratory Astrophysics of Gravitational Lensing" poster | Conference poster, 35 × 43 in, 2026-07 | First author; built the poster and generated its simulation figures |
| OPICA / FIO presentation (2025) | Conference presentation | Presenter |
| *Physics Today* "Backscatter" submission — quantum-pendulum optical analogue | Under review | From the warm-up project |
| Senior thesis project | Self-initiated, funded through Galvez; Summer 2026 → May 2027 | The WRA / polarization thread is its technical foundation |

## 7.5 Numbers safe to quote

| Number | Meaning **[LOG]** |
|---|---|
| **14** wavelengths, **403–684 nm** | Multi-wavelength campaign span |
| **`d̂` = 0–4**, in 20 µm (one-pixel) steps | Binary-separation scan range |
| **w = 238** (λ = 633 nm, `r_S` = 12 µm) | Regime of the no-free-parameter caustic-dimension comparison |
| **w = 80, `d̂` = 1.07** | The fine-structure agreement figure |
| **64 → 448 Hz** | GW frequencies spanned by the lab chirp sequence (GW150914 swept 35 → 250 Hz) |
| **73 frames × 4096 × 3000 px (~880 MB)** | The phase-shifting dataset reconstructed in software |
| **≤ 9° RMS phase** | Cross-SLM wavefront agreement after metric matching |
| **0.745 ≈ 3f/4f** | Predicted-and-observed ratio that identified phase depth as the 3f-ring cause |
| **35 cm** | Measured camera displacement past the focal plane |
| **≈ 51 % of aperture pixels → 0.679 correlation**; **0.8 u disks → 0.95 at ~30 % of pixels** | Stationary-phase minimal-pixel fidelity |
| **1,000+ frames** | The self-initiated merger movie |
| **7,351 lines / 67 files / 49 commits** | Repository scale (CN says "about eight thousand lines across roughly seventy source files and forty-eight commits") |
| **2e-15, 4e-16, 3e-11, 1e-14, 2e-16** | GR-pipeline and Jones-optics invariants |

## 7.6 The two pre-drafted liftable passages from SOP_contribution_notes

**One sentence:**

> I built and calibrated the modulator-based optical platform, the automated acquisition and the complex-field analysis used to make the first laboratory observation of gravitational-lensing diffraction from a binary-mass system, and extended it to geometric-optics, polarization and cosmic-string analogues. **[CN]**

**At greater length:**

> Gravitational-lensing diffraction has never been directly observed, because starlight is too incoherent and too short in wavelength, and because a gravitational-wave detector samples only a single point of a pattern spanning light-years. In Professor Galvez's laboratory at Colgate I helped solve this by building a tabletop analogue in which a phase-only spatial light modulator imprints the gravitational Shapiro delay onto a coherent laser beam and free-space propagation supplies the rest. I wrote the control and analysis platform — roughly eight thousand lines of MATLAB spanning hologram generation, wavelength-aware phase calibration, automated parameter scans, and phase-shifting interferometry that recovers the complex lensed field. Our measured caustics and their interference decoration agree with wave-optical theory with no adjustable parameters, across length scales differing by many orders of magnitude. **[CN]**

---

# Part 8 — Supporting research: NanoGrav, JWST, Koopman

## 8.1 The pre-Galvez computational path

> My research path before Galvez's lab was almost entirely computational, and both projects ended without papers. With Ilie, I analyzed JWST archival data using machine learning to identify potential dark matter signatures, but funding constraints kept me at the exploration stage — I never reached real research. With Lam, I went further: he walked me through NanoGrav post-fit datasets and taught me red noise analysis, 2D Fourier transforms, and PSD methods for gravitational wave detection in pulsar timing residuals. I learned Python seriously there — SciPy, AstroPy, Pandas, Matplotlib — and gained real comfort with scientific data pipelines. That project ended when Lam, a visiting professor, left for Massachusetts; the distance made continuation impractical. Neither project pointed toward astrophysics as a career. Both pointed away from it. **[M, and identically in P]**

## 8.2 Koopman / Chua — the project that changed direction

> The project that changed my direction was the Koopman operator analysis in Segall's Nonlinear Dynamics course. I applied EDMD to a physical Chua's circuit, analyzing it across four dynamical regimes — fixed point, limit cycle, period-doubled limit cycle, and double-scroll chaos — and compared polynomial, RBF, and piecewise-linear observable dictionaries. I implemented Lyapunov spectrum computation and box-counting fractal dimension, and built a custom MATLAB serial interface to an Arduino R4 Minima for real-time hardware data acquisition. The mathematical move that fascinated me: you can find hidden linear spectral structure inside a physically chaotic system by lifting the dynamics into a higher-dimensional function space. The chaos doesn't disappear, but it becomes analyzable. I didn't have language for this at the time, but it's the same intellectual move I keep making — extracting invariant structure from systems that look complex or inaccessible from outside. **[M, and identically in P]**

> The Koopman operator framework from the Chua's circuit project is the same idea in a third context. EDMD lifts a nonlinear physical system into a higher-dimensional function space where the dynamics become spectrally analyzable — a Fourier-like decomposition applied to the phase space of a chaotic system. I co-built the full EDMD analysis repository from scratch with a team. I can give an independent talk on this entire framework; I understand the mathematics well enough to explain why it works, not just how to run it. **[P]**

## 8.3 The tool statement

> MATLAB is my primary tool. I've used it for SLM phase programming, ThorLabs hardware IO, image analysis, Koopman EDMD, Arduino serial communication, and parameter simulation across all of my research. **[M]**

> Python is my secondary tool — SciPy, AstroPy, NumPy, Pandas, Matplotlib — proficient enough to build working data pipelines, though I rely on documentation for less familiar library functions. **[P]**

## 8.4 Mathematical modeling — a separate thread

> **Mathematical modeling** is a separate thread: I was a finalist in HiMCM (MAA/COMAP) — a 36-hour mathematical modeling competition — which required building quantitative models from scratch under time pressure and defending them in writing. That experience trained a different kind of mathematical thinking than lab research: applied, fast, and required to produce usable results quickly. **[P]**

## 8.5 Older experience

> **Research Assistant | Chinese Academy of Sciences, Beijing | Apr – Jul 2021** — Assisted PhD students in thermal engineering lab with data collection, analysis, and simulation after completing a 2-month training workshop. Methods: MATLAB, FLUENT. Supporting role; completed program. **[P]**

<!-- GAPS in Part 8 — nothing anywhere answers: your specific slice of the Koopman TEAM project; what
     the polynomial / RBF / piecewise-linear dictionary comparison TAUGHT you (model choice vs.
     physical interpretability); a POSITIVE framing for why computational astro narrowed you toward
     experimental optics. Only the negative framing exists ("Both pointed away from it"). -->

---

# Part 9 — Technical signature and skills

## 9.1 The signature, in your own framing

> My technical signature has two components — a physical layer and a mathematical layer — and most of what I've learned in research has been figuring out how to move between them. **[P]**

## 9.2 Physical layer

> The center of my experimental toolkit is the spatial light modulator. I can program phase profiles from first principles: for the GL project I went back to the original Einstein ring paper to understand how the phase encoding works, then adapted existing code to implement Schwarzschild lens profiles for single and binary lenses. I am able to reconstruct the entire phase profile generator from scratch. **[M and P — identical]**

> Beyond phase programming, I own laser alignment. Prof. Galvez has explicitly endorsed my alignment skill, and I now know my optical setup completely — I can diagnose any misalignment from its signature in the output beam pattern without checking each element in sequence. I can immediately fix any problem that occurs. **[P]**

> I do embedded development as a personal hobby project outside the lab — writing firmware and hardware interfaces for microcontrollers — for the same reason I built the ThorLabs automation: the satisfaction of making hardware respond to code you wrote is something I keep seeking out independently. **[P]**

> My electronics background (Adhikari's lab) gives me comfort with digital and analog instrumentation; I've built and debugged physical circuits and understand hardware at the component level, not just as black boxes. **[P]**

## 9.3 Approach to new problems

> When I encounter an unfamiliar problem, I read the relevant texts and papers first to understand the theoretical structure, then run a brief MATLAB or Python simulation to develop intuition for the parameter space, then move to physical implementation. I don't build blind. The GL phase profile work is an example: before I could make the encoding work, I went back to the source paper to understand the Einstein ring geometry from first principles. That habit — tracing the math before touching the setup — is what let me solve the imaging problem that previous workers couldn't. **[P]**

## 9.4 The skills ledger from the log

> **Experimental optics.** Phase-only LCOS SLM hologram design and encoding (phase-only and complex amplitude/CAM); blazed-grating beam steering and diffraction-order separation; 4f relay design and alignment; Fourier-plane vs. near-field diagnosis; Durnin-ring Bessel-beam generation; optical vortices and OAM; phase-shifting interferometry; polarimetry and Jones/Stokes analysis; quarter-wave-plate rotator design; camera photometry and exposure control; Zernike aberration correction; multi-device (dual-SLM) bench integration. **[LOG]**

> **Theory and computation.** Fresnel–Kirchhoff diffraction; Fermat/time-delay potentials and gravitational lensing; catastrophe optics (folds, cusps, caustics, Morse classification); stationary-phase/geometric-optics asymptotics *including where they break down*; Kerr geodesics, orthonormal tetrads, local Lorentz generators, and Wigner rotation; FFT-based Fresnel propagation; Nyquist sampling analysis for hologram design. **[LOG]**

> **Scientific software engineering.** Refactoring a legacy monolith into a documented, testable package architecture; API design with explicit resource-safety patterns; building a hardware simulator to enable hardware-free development and regression testing; automated test suites; memory-bounded processing of ~880 MB image stacks; hardware SDK integration via .NET/DLL; backward-compatible configuration refactors; documentation as a first-class deliverable. **[LOG]**

> **Physics-driven debugging — the through-line.** Every hard bug in this project was solved by deriving the expected physical scaling first and only then touching the bench. Equally: **writing down which conclusions were wrong** — the retracted collimation measurement, the dead 4π hypothesis, the VIS-016 misidentification, the mirror-mounting misdiagnosis — and keeping the superseded numbers in the repository with explanations of why they can't be trusted. **[LOG]**

> **Measurement campaign execution.** Running a **multi-wavelength (14 lasers, 403–684 nm), multi-parameter (`r_S` = 0.2–20 µm, `d̂` = 0–4, z = 10–30 cm) imaging campaign** to publication standard: fibre-coupled source swapping without re-alignment, achromatic-path design, the empirically-found grating working window that made clean first-order imaging possible at all, and reduction of the resulting patterns into four caustic observables compared against parameter-free theory. **[LOG]**

> **Communication.** A 3-column research poster combining theory, simulation, and measurement; a 248-line bench-build tutorial written so another person could reproduce the setup; ~1,100 lines of user documentation; and inline physics reasoning kept with the code that depends on it. **[LOG]**

## 9.5 Skills list from profile

> **Programming:** MATLAB (proficient), Python — SciPy, AstroPy, NumPy, Pandas, Matplotlib (proficient), Java (proficient), LaTeX (proficient), C++ (basic), Machine Learning (basic)
> **Lab / instrumental:** Spatial light modulator (SLM), laser optics, Arduino (R4 Minima), digital and analog electronics, FLUENT
> **Mathematical / analytical:** Mathematical modeling (HiMCM finalist, MAA/COMAP), Koopman operator theory, EDMD, Lyapunov spectrum, fractal dimension; self-studying: advanced QM (Sakurai), functional analysis (Reed — recommended by Prof. Crotty) **[P]**

---

# Part 10 — Background, constraints, career

## 10.1 Academic

> **Institution:** Colgate University, Hamilton, NY | BA | Rising senior, expected May 2027
> **GPA:** 3.92 / 4.00
> **Majors:** Physics and History-Historiography Pathway
> **Notable coursework:** Quantum Mechanics, Nonlinear Dynamics & Chaos, Mathematical Methods of Physics, Classical Mechanics, Electronics, Introduction to Quantum Mechanics, Intro to E&M, Atom and Waves, Planetary Science, Calculus I–III; Stanford Online HS Modern Physics (XP 670 — special/general relativity, quantum computation, quantum information)
> **Awards / honors:** Alumni Memorial Scholar — selective community of 15 per class year; $10,000 for independent research and skill development. Dean's Award with Distinction — all semesters **[P]**

## 10.2 Career goals

> Dual-track: academic faculty in experimental quantum optics / AMO physics, or industry role in quantum networking and optical photonics. Post-PhD path is OPT → H-1B; clearance-required positions (most quantum computing hardware roles) are off-table due to citizenship constraints. Whichever track offers the best fit at graduation. **[P]**

## 10.3 Constraints (context only — most do not belong in the SOP)

> Chinese citizen. F-1 student visa at Colgate University. Planning OPT (3-year STEM extension) → H-1B post-PhD. NSF GRFP ineligible. Federal clearance-required positions off-table. University RA/TA packages and most private fellowships eligible. **[P]**

> **Florida state-funded institutions:** SB 846 — Chinese nationals restricted from certain state-funded research positions. **Astro-focused programs:** Not pursuing astrophysics. **No guaranteed multi-year funding for international students:** full international PhD funding is a hard requirement. **[P]**

## 10.4 Gaps you have named yourself — relevant because the SOP may need to contextualize one

> **Math background:** Weaker than peers who double-major or minor in math; no real analysis, abstract algebra, or topology coursework. Actively addressing: self-studying Sakurai and Reed's functional analysis.
> **No graduate-level coursework:** Colgate as undergraduate-only LAC does not offer graduate courses — structural constraint; contextualize in SoP.
> **Single-institution research:** All Colgate; no external REU.
> **Independent project not yet started:** Will be in progress (not complete) at application time — frame as ongoing with clear scope and preliminary results. **[P]**

## 10.5 Recommenders

> **Prof. Enrique Galvez** — Primary research advisor; GL analog, quantum pendulum analog, planned senior project; experimental design, SLM optics, scientific maturity, publication-quality work. Tier: Primary (anchor letter).
> **Prof. Segall** — Course instructor (Nonlinear Dynamics & Chaos); directly observed the Koopman project; mathematical physics depth. Tier: Primary.
> **Prof. Adhikari** — Electronics course instructor; electronics lab supervisor; Engineering Club mentor; hands-on experimental and engineering skills, leadership, initiative. Tier: Primary.
> **Prof. Levine** — Course instructor (Classical Mechanics, Planetary Science). Tier: Backup. **[P]**

## 10.6 Self-assessed strengths

> - **Experimental design and instrumentation:** Built SLM-based optical analog setups from scratch under Galvez (2025); OPICA/FIO presentation; Physics Today submission
> - **Intellectual autonomy:** Self-proposed senior year optical project under Galvez lab funding — initiative beyond assigned research
> - **Breadth-to-depth arc:** Computational astro (Ilie, Lam) → experimental optics (Galvez) — deliberate narrowing toward a clear experimental identity
> - **Mathematical fluency at depth:** Koopman operator theory and EDMD on physical hardware at undergrad level; active self-directed remediation via Sakurai and Reed
> - **Cross-disciplinary identity:** History-Historiography double major — paradigm-shift awareness, source criticism, comfort with contested interpretations; differentiator on faculty track
> - **Teaching and communication depth:** TAed/tutored 5 physics courses; co-designed new course PHSY 125 from scratch
> - **Leadership with demonstrated outcomes:** Engineering Club co-founder and VP; led 15-person go-kart team; RA in ResLife
> - **Alumni Memorial Scholar:** Selective award (15/class year) **[P]**

---

# Part 11 — Teaching, engineering, leadership

*The scaffold allocates these no paragraph. Facts exist; no narrative does. Kept here in case you decide ¶4 or ¶5 should carry one line.*

**Facts available [P]:** TAed/tutored 5 physics courses; co-designed new course PHSY 125 from scratch; Engineering Club co-founder and VP; led a 15-person go-kart build team; RA in ResLife (community building, conflict mediation). Prof. Adhikari is a recommender partly on this basis.

**Materials.docx's own gate on whether any of it goes in:**

> 只有当这些经历能够支持下列内容时才写入：独立性 / 协作能力 / 技术沟通 / 项目领导 / 实验设计 / 对开放式问题的耐心。不要只写职位名称或活动数量。 **[M]**
> *(Only include these if they support: independence / collaboration / technical communication / project leadership / experimental design / patience with open-ended problems. Do not just write job titles or activity counts.)*

<!-- GAP — every Task 7 prompt in Materials.docx is unanswered. There is no story here yet, only a
     list of roles. If you want teaching or the go-kart in the SOP, that story has to be written. -->

---

# Part 12 — Honesty guardrails and things to verify

## 12.1 The four guardrails, as the log states them

> (a) The lensing *theory* is Barcelona's; the instrument, code, data, and reduction are the Colgate side's. (b) The quantum-pendulum warm-up ran on inherited code; the contribution there was tuning and learning the apparatus. (c) The dual-SLM/WRA platform is **built and verified in simulation but has produced no measurements** — it is capability and intent, never a finding. (d) "Lead experimental / first-listed Colgate author," not sole first author. **[LOG]**

## 12.2 What must be verified before submitting

> There are five experimental authors on the paper, and the principal experimental figures span more work than my own involvement, so I should ask Professor Galvez which datasets are mine and phrase everything else as work the platform and analysis I built supported. I should confirm whether I measured the phase calibration table or inherited it; I certainly implemented the interpolation, the wavelength scaling and the automatic computation, which is safe to claim, but the underlying sixteen-point measurement may predate me, which is why I say "implemented" rather than "measured." I should ask what my contribution statement in the manuscript will say and mirror it. I should confirm the publication status and venue as of the time I apply, and whether I may cite the preprint. And I should record the conference and date at which the poster was presented, since I have the source file but not the venue. **[CN]**

## 12.3 What not to overclaim

> The stationary-phase minimal-pixel result and the Wigner-rotation and cosmic-string modules are simulation and design work that has been verified numerically but not yet measured on the bench, and I should say so plainly, because the numerical verification is strong enough to stand on its own merits. The binary caustic was genuinely observed on hardware, but the specific collimation numbers I once measured were confounded by the phase-inversion problem and have been retracted, so I should not quote them. The phrase "first laboratory observation" belongs to the collaboration's result and not to me individually. And the apparatus reproduces the mathematics of lensing rather than gravity itself; it is an analogue, the paper is careful about that, and I should be too. **[CN]**

## 12.4 Questions a reader will probe — and the honest answer

| Likely question | Answer as it stands today **[LOG]** |
|---|---|
| Did the stationary-phase (minimal-pixel) hologram ever run on hardware? | **No.** Simulation is fully characterized; the hardware A/B is open. |
| Has the WRA polarimetry produced data? | **No.** Full GR pipeline verified numerically, bench tutorial written, hardware not built. |
| Was the oblique-incidence deformation explained? | **No** — resolved empirically at one working angle, never modelled. |

---

# Part 13 — Structural instructions from the scaffold

*Not source material — the shape the above is meant to be poured into. **[S]** throughout.*

**The one claim every paragraph must serve:**

> "I developed from a computational data analyst into an experimental structured-light researcher whose signature move is **enlarging the state space so hidden structure becomes analyzable** — and I want to carry that move into high-dimensional structured *quantum* optics."

> The reader should finish the SOP able to say what kind of *scientist* you are, not just that you were a strong physics student. Every selected fact must advance the claim above; if a fact is true but doesn't, it goes in the CV, not the SOP.

| ¶ | Section | Length |
|---|---|---|
| 1 | Opening / research goal | 100–150 w |
| 2 | Quantum-pendulum (entry into optics) | 180–250 w |
| 3 | GL project — the ONE anchor challenge | 250–350 w |
| 4 | Supporting capabilities (integrated, not 4 mini-stories) | 120–180 w |
| 5 | Conclusion (researcher-you-intend-to-become) | 2 sentences |
| — | Per-school fit block (tailoring file, not core) | 3 sentences each |

**¶3 finalized structure:** Beat 1 credential + taste hook (2 sentences) → Beat 2 the sign-flip elimination arc (3–4 sentences) → Beat 3 payoff/bridge to the PhD (2–3 sentences).

> **Trim priority if over length:** cut the architecture line first, then compress the grit beat to a clause. Never cut: the −1 controlled-test arc (Beat 2) or the DoF/skyrmion bridge (Beat 3) — those two are the paragraph's whole reason to exist.

**Per-school fit block template:**
> 1. Name **2 PIs** + **one shared scientific question** (not shared equipment/keywords).
> 2. What you contribute **immediately**: SLM phase engineering, laser alignment, MATLAB hardware control, Fourier-plane analysis.
> 3. What you need to **learn** from them: SPDC/heralded sources, coincidence counting, single-photon detection, quantum-state tomography, or (per lab) integrated photonics / cavity QED / ultrafast.
> 4. One **plausible next question** that grows from their recent work without inventing expertise.

**Forbidden openings, per Materials.docx:**
> 开头不要从童年、仰望星空或"光很美"开始。填写时避免：fascinating / passion since childhood / optics is everywhere / I have always dreamed / change the world **[M]**

---

# Part 14 — Prompts and templates still unanswered

*These are the actual gaps. Every one is a question Materials.docx asks and no source answers. Verbatim, so the original framing is preserved.*

## 14.1 The GL challenge, deepened (Materials Task 3.2)

> 选择一个最能体现研究能力的挑战，详细回答：
> 当时预期看到什么结果？／实际观察到了什么异常？／为什么这个异常不能被简单忽略？／我最初提出了哪些可能原因？／我如何逐项排除 SLM、镜子、透镜、对准、相位编码、零级衍射或数据处理的问题？／我设计了哪些控制实验？／哪个观察最终帮助我定位问题？／我是否修改了光路、编码、数据分析程序或理论模型？／最终问题是否完全解决？如果没有，解决到了什么程度？ **[M]**

> 写作时尽量加入一个具体瞬间：
> 当我发现________________时，我意识到原来的假设________________可能不成立。为区分________________和________________，我设计了________________。 **[M]**

*(Most of these ARE answered by §5.3 above; the one genuinely missing piece is the single "specific moment" sentence.)*

## 14.2 Research growth (Materials Prompt 3.5) — entirely blank

> 这个项目最初让我把 SLM 看作________________；后来我逐渐意识到，它实际上可以________________。
> 我最重要的成长不是学会了某个软件，而是学会了如何________________。
> 这段经历让我开始关注的更一般问题是________________。
> 它推动我从"使用光学复现现象"转向思考"________________"。 **[M]**

<!-- These four sentences, if answered, would supply the ¶2→¶3→¶1 connective tissue that is currently
     the weakest part of the whole document. Highest-value blanks in the file. -->

## 14.3 The two-project progression (Materials Prompt 5.1–5.3) — blank

> 两个项目是否都使用了 SLM？／两个项目是否都通过 phase engineering 将数学模型转化为可观测光场？／两个项目是否都利用光学系统模拟另一个物理系统？／两个项目的主要区别是什么？／第一个项目让我掌握了什么，第二个项目让我进一步理解了什么？／哪个项目更偏向实验验证，哪个项目更偏向光场设计？／它们共同让我对哪一个更一般的科学问题产生兴趣？ **[M]**

> 两个项目在时间上是否真的具有先后关系？／后一个项目是否真的使用了前一个项目学到的方法？／哪些联系是事实，哪些只是为了 SOP 强行建立的？ **[M]**

*(Factual answer available: the pendulum ran about one month and preceded GL — "The quantum pendulum project continued about 1 month and we moved onto the gravitational project" **[M]**. Note that Materials Prompt 5.2's template has the two projects in the reverse order, GL first then pendulum — that ordering is wrong and should not be used.)*

## 14.4 NanoGrav / JWST / Koopman deepening (Materials 6.1–6.3) — blank

> 我处理的 pulsar timing 数据有什么困难？／irregular sampling、red noise 或 radio-frequency-dependent effects 为什么难以分析？／分析没有得到预期结果时，我学到了什么？／这段经历如何帮助我处理复杂的光学实验数据？ **[M]**

> polynomial、RBF 和 piecewise-linear dictionaries 有什么区别？／最大挑战是硬件采集、算法选择还是物理解释？／Lyapunov spectrum 和 fractal dimension 帮助我理解了什么？／这段经历如何支持我未来研究复杂光场、非线性光学或 optical dynamics？ **[M]**

## 14.5 The integration template (Materials 6.4) — blank

> 我在 NANOGrav、JWST 数据分析和 Chua 电路研究中的经历，使我从不同角度学习了如何________________。NANOGrav 培养了我处理________________的能力；JWST 项目让我学习了________________；Chua 电路则让我将________________与________________结合。这些能力现在直接影响了我研究光学问题的方式：我不仅关注是否能够产生一个光学现象，也关注如何________________。 **[M]**

## 14.6 The opening template (Materials 8.2) — blank

> My research experiences have led me to ask how ________________________________. By using spatial light modulators to __________________ in projects on gravitational lensing and quantum pendulum dynamics, I became interested not only in reproducing complex physical phenomena optically, but also in understanding ________________________________. I now hope to pursue doctoral research in __________________, with particular interest in ________________________________. **[M]**

## 14.7 The conclusion (Materials 9.1) — blank, and this is the largest gap in the SOP

> 博士阶段我希望建立什么能力？／我希望从"能够执行实验"成长为什么类型的研究者？／我可以为实验室立即提供哪些能力？／哪些能力需要在博士阶段继续加强？／我的长期目标是学术研究、国家实验室还是其他方向？／我希望最终能够独立提出怎样的问题？ **[M]**

**The only fragments that exist to seed it:**

> Currently, I am using SLM to modulate classical light beams, and in PhD, I can advance toward quantum states and scalable devices. **[M]**

> quantum experiments require additional tools such as heralded single-photon or SPDC sources, coincidence counting, single-photon detectors, and quantum-state tomography **[M]**

## 14.8 The per-mentor template (Materials 9.2) — blank per school

> 这位导师的哪个具体项目与我的 Goal 最相关？／我过去的哪一段经历证明我能够进入这个项目？／我能使用哪些已有技能立即做贡献？／我希望向这位导师学习什么新的方法？／我能否提出一个自然的未来研究问题，而不是重复导师网站上的介绍？／除单个导师外，这个系还有哪些设备、合作或研究群体支持我的目标？ **[M]**

> Professor ______'s work on ______ is particularly relevant to my interest in ______. My experience with ______ has prepared me to contribute to ______, while I hope to develop deeper expertise in ______. I am especially interested in exploring whether/how ______. **[M]**

---

# Appendix — the five-blank gap list, ranked

1. **¶5 conclusion** — nothing exists. Two sentences, written cold. *(Part 14.7)*
2. **"SLM as ___ → actually ___" growth sentences** — nothing exists; would supply the connective tissue for ¶2→¶3→¶1. *(Part 14.2)*
3. **The "second SLM = second degree of freedom" join** — the two halves exist in different files and are never connected. *(¶3 Beat 3)*
4. **Quantum-pendulum validation** — how the 11-state pattern was tuned *and confirmed*. *(Part 3, gap note)*
5. **Per-school slots 1 and 4** — 2 PIs + one shared question; one plausible next question. *(Part 14.8)*
