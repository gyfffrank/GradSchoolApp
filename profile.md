# Profile
<!-- last updated: 2026-05-26 by profile-builder -->

## Target subfields
<!-- last updated: 2026-07-27 by sop-coach (research-interest sharpening from Materials.docx) -->

- **Primary:** **High-dimensional structured quantum optics** — engineering the spatial, polarization, and orbital-angular-momentum (OAM) degrees of freedom of light together with quantum-state control (single photons and photon pairs). Central interest: geometric phase and topological structure in structured light, and how the large photonic degree-of-freedom space can encode and transport information.
- **Why this cluster (Frank's own framing):** photons carry far more independently encodable degrees of freedom than an electronic circuit, so structured quantum light is a direct attack on the information-capacity bottleneck in optical communication and quantum information processing. The SLM wavefront-shaping already done on classical beams transfers directly to shaping the transverse wavefunction of single photons / photon pairs; the PhD adds the quantum toolchain not yet owned (SPDC sources, heralded single photons, coincidence counting, single-photon detectors, quantum-state tomography).
- **Ranked adjacent clusters (from the PI taxonomy in Materials.docx):**
  1. **Classical structured light & singular / topological optics** (propagation structure, vortices, caustics, critical points) — the fundamental substrate; heavy overlap with the primary cluster.
  2. **Atom–photon quantum interfaces** — the most fundamental cluster; held as the **secondary choice.**
  3. **Ultrafast & nonlinear structured light** (temporal DoF, HHG, strong-field) — adjacent, but requires a technique pivot off free-space SLM.
  4. **Integrated / nanoscale quantum-photonic platforms** (chips, metasurfaces, nanocavities) — promising as a future compute platform but **constrained** (tied to silicon-IC / EUV fabrication and associated export sensitivities).
- **Career-overlap track:** optical / quantum networking — the applied end of high-dimensional photonic encoding.
- **Avoid:** astrophysics and astronomy-focused programs.

## Career goals
Dual-track: academic faculty in experimental quantum optics / AMO physics, or industry role in quantum networking and optical photonics. Post-PhD path is OPT → H-1B; clearance-required positions (most quantum computing hardware roles) are off-table due to citizenship constraints. Whichever track offers the best fit at graduation.

## Geography
- **Primary:** Northeast US — NY lifestyle preferred; girlfriend based in Syracuse area
- **Secondary:** All other US regions and internationally; open to anywhere with strong fit
- **Avoid:** Florida state-funded institutions (SB 846 restricts Chinese nationals from certain state-funded research positions)

## Citizenship and visa status
Chinese citizen. F-1 student visa at Colgate University. Planning OPT (3-year STEM extension) → H-1B post-PhD. NSF GRFP ineligible. Federal clearance-required positions off-table. University RA/TA packages and most private fellowships eligible.

## Application tier strategy
- **Total PhD programs:** 18
- **Reach / Match / Safety:** 6 / 6 / 6
- **MS backups:** 10 programs (U Rochester MS in Optics confirmed; others TBD by program-discovery)
- **Total applications:** 28
- **Estimated budget:** TBD (before waivers)

> The actual program list is maintained separately in `programs.md` at the project root.

## Academic background
- **Institution:** Colgate University, Hamilton, NY | BA | Rising senior, expected May 2027
- **GPA:** 3.92 / 4.00
- **Majors:** Physics and History-Historiography Pathway
- **Notable coursework:** Quantum Mechanics, Nonlinear Dynamics & Chaos, Mathematical Methods of Physics, Classical Mechanics, Electronics, Introduction to Quantum Mechanics, Intro to E&M, Atom and Waves, Planetary Science, Calculus I–III; Stanford Online HS Modern Physics (XP 670 — special/general relativity, quantum computation, quantum information)
- **Awards / honors:**
  - Alumni Memorial Scholar — selective community of 15 per class year; $10,000 for independent research and skill development
  - Dean's Award with Distinction — all semesters

## Research experience

### Gravitational Lensing Optical Analog | Prof. Galvez | Apr 2025 – Present
- **Summary:** Designed and carried out an optical simulation of gravitational lensing using laser beams modulated by a spatial light modulator (SLM) to emulate spacetime curvature. Implemented phase profiles for single and binary Schwarzschild lenses; reproduced interference and fringe patterns analogous to Einstein rings. Quantitatively compared theoretical predictions with measured intensity profiles demonstrating agreement in fringe structure relevant to binary systems and black hole mergers.
- **Methods and skills:** SLM, laser optics, phase profile design, intensity profile measurement and comparison
- **Outcomes:** Presented at OPICA/FIO, Denver, CO (2025). Manuscript **under review** with Gu as lead experimental / co-first author: Moreso Serra, Bulashenko, Gu, et al., "Laboratory observation of lensing diffraction in a binary-lens system for gravitational-wave astrophysics" (2026). Repo: `C:\Users\user\Documents\GitHub\OpticsLab26-27` (MATLAB package; his contributions include the `stationaryLens` caustic/critical-point analysis, `phaseMap` optical-vortex / net-OAM detection, dual-SLM library re-architecture, and ThorLabs automation).

### Optical Analog of Quantum Pendulum Dynamics | Prof. Galvez | Apr 2025 – Present
- **Summary:** Designed and experimentally realized a structured optical beam exploiting the Helmholtz–Schrödinger equation equivalence. Generated a Fourier-plane image encoding a superposition of 11 pendular eigenstates, with ring radii proportional to energy and angular modulation proportional to quantum probability density, including bound and rotor states.
- **Methods and skills:** Structured light, Fourier optics, eigenstate superposition encoding
- **Outcomes:** Submitted to Physics Today (Backscatter) — under review.

### Self-Initiated Optical Project | Prof. Galvez (funding) | Summer 2026 – May 2027
- **Summary:** Self-proposed independent optical research project to be carried out under Galvez lab funding during summer 2026 and continued through senior year. Specific topic TBD — to be updated when defined.
- **Methods and skills:** TBD
- **Outcomes:** In planning; expected in progress at application time.

### Pulsar Timing / NanoGrav | Prof. Lam | Sep 2024 – Jan 2025
- **Summary:** Utilized NanoGrav post-fit data to analyze red noise effects in pulsar timing and attempt to improve gravitational wave detection. Also analyzed radio-frequency-dependent interstellar material effects using irregular auto-regression models and PSD analysis.
- **Methods and skills:** Python (SciPy, AstroPy, Pandas, Matplotlib), auto-regression, PSD analysis
- **Outcomes:** Completed; no publication. Astro direction not being pursued.

### JWST Dark Stars / Dark Matter | Prof. Ilie | Mar 2024 – Aug 2024
- **Summary:** Analyzed archival JWST data using machine learning to identify potential supermassive dark star candidates and investigate dark matter properties.
- **Methods and skills:** Machine learning, JWST archival data analysis, Python
- **Outcomes:** Completed; no publication. Astro direction not being pursued.

### Koopman Operator Analysis of Chua's Circuit | Colgate (course project)
- **Summary:** Applied Koopman operator theory and EDMD in MATLAB to analyze a physical Chua's circuit across four dynamical regimes (fixed point, limit cycle, period-doubled, double-scroll chaos). Compared polynomial, RBF, and piecewise-linear observable dictionaries. Implemented Lyapunov spectrum computation and box-counting fractal dimension algorithms; acquired real-time data via Arduino R4 Minima with custom MATLAB serial interface.
- **Methods and skills:** MATLAB, Koopman operator theory, EDMD, Lyapunov spectrum, fractal dimension, Arduino
- **Outcomes:** Co-authored written report; presented as Nonlinear Dynamics & Chaos course project (Prof. Segall).

### Research Assistant | Chinese Academy of Sciences, Beijing | Apr – Jul 2021
- **Summary:** Assisted PhD students in thermal engineering lab with data collection, analysis, and simulation after completing a 2-month training workshop.
- **Methods and skills:** MATLAB, FLUENT
- **Outcomes:** Supporting role; completed program.

## Technical skills
- **Programming:** MATLAB (proficient), Python — SciPy, AstroPy, NumPy, Pandas, Matplotlib (proficient), Java (proficient), LaTeX (proficient), C++ (basic), Machine Learning (basic)
- **Lab / instrumental:** Spatial light modulator (SLM), laser optics, Arduino (R4 Minima), digital and analog electronics, FLUENT
- **Mathematical / analytical:** Mathematical modeling (HiMCM finalist, MAA/COMAP), Koopman operator theory, EDMD, Lyapunov spectrum, fractal dimension; self-studying: advanced QM (Sakurai), functional analysis (Reed — recommended by Prof. Crotty)

## Publications and presentations
<!-- last updated: 2026-07-27 by sop-coach (added binary-lens manuscript; corrected GL authorship) -->
- **Manuscript under review — lead experimental / co-first author:** A. Moreso Serra, O. Bulashenko, **Y. Gu**, T. Nguyen, K. Kendja, V. Rodríguez-Fajardo, E. J. Galvez, "Laboratory observation of lensing diffraction in a binary-lens system for gravitational-wave astrophysics" (dated 8 June 2026). Gu is the first-listed Colgate (experimental) author; Bulashenko (U. Barcelona) and Galvez (Colgate) are corresponding authors. Reports the first laboratory observation of binary-lens diffraction — caustics modulated by coherent wave interference, quantitative theory–experiment agreement, and a GW-chirp optical analogue. Venue: TBD/confirm. Under review as of July 2026.
- **Conference presentation:** Gravitational-lensing optical analog — OPICA/FIO, Denver, CO, 2025 (with Prof. Galvez)
- **Under review:** Optical analog of quantum pendulum dynamics — submitted to Physics Today (Backscatter) (with Prof. Galvez)

## Recommenders

- **Prof. Enrique Galvez, Colgate University**
  - Relationship: Primary research advisor
  - Projects: Gravitational lensing analog, quantum pendulum analog, planned senior independent project
  - Topics: Experimental design, SLM optics, scientific maturity, publication-quality work
  - Tier: Primary (anchor letter)

- **Prof. Segall, Colgate University**
  - Relationship: Course instructor (PHYS 131, Nonlinear Dynamics & Chaos); directly observed Koopman Operator project
  - Projects: Koopman Operator Analysis of Chua's Circuit
  - Topics: Mathematical physics depth, project-based research ability, nonlinear dynamics
  - Tier: Primary

- **Prof. Adhikari, Colgate University**
  - Relationship: Electronics course instructor; electronics lab supervisor; Engineering Club mentor
  - Projects: Electronics lab work; co-led go-kart build (15-member team)
  - Topics: Hands-on experimental and engineering skills, leadership, initiative
  - Tier: Primary

- **Prof. Levine, Colgate University**
  - Relationship: Course instructor (Classical Mechanics, Planetary Science); known for writing strong letters
  - Projects: Coursework only
  - Topics: Academic performance, physics mastery
  - Tier: Backup

## Self-assessed strengths
- **Experimental design and instrumentation:** Built SLM-based optical analog setups from scratch under Galvez (2025); OPICA/FIO presentation; Physics Today submission
- **Intellectual autonomy:** Self-proposed senior year optical project under Galvez lab funding — initiative beyond assigned research
- **Breadth-to-depth arc:** Computational astro (Ilie, Lam) → experimental optics (Galvez) — deliberate narrowing toward a clear experimental identity
- **Mathematical fluency at depth:** Koopman operator theory and EDMD on physical hardware at undergrad level; active self-directed remediation via Sakurai and Reed
- **Cross-disciplinary identity:** History-Historiography double major — paradigm-shift awareness, source criticism, comfort with contested interpretations; differentiator on faculty track
- **Teaching and communication depth:** TAed/tutored 5 physics courses; co-designed new course PHSY 125 from scratch
- **Leadership with demonstrated outcomes:** Engineering Club co-founder and VP; led 15-person go-kart team; RA in ResLife (community building, conflict mediation)
- **Alumni Memorial Scholar:** Selective award (15/class year); signals institutional recognition of academic excellence

## Gaps and weaknesses to address
- **Math background:** Weaker than peers who double-major or minor in math; no real analysis, abstract algebra, or topology coursework. Actively addressing: self-studying Sakurai and Reed's functional analysis. Should complete at least one graduate-level math text before applications.
- **No graduate-level coursework:** Colgate as undergraduate-only LAC does not offer graduate courses — structural constraint; contextualize in SoP.
- **GRE / Physics GRE:** Neither taken. General GRE: sit Summer/Fall 2026. Physics GRE: assess program-by-program; a strong score directly addresses math gap perception.
- **Single-institution research:** All Colgate; no external REU. CAS Beijing (2021) is older and in a different field.
- **Independent project not yet started:** Will be in progress (not complete) at application time — frame as ongoing with clear scope and preliminary results.

## Hard constraints and deal-breakers
- **Florida state-funded institutions:** SB 846 — Chinese nationals restricted from certain state-funded research positions. Rules out UF, FSU, UCF, etc.
- **Astro-focused programs:** Not pursuing astrophysics; programs centered on astro are out regardless of ranking.
- **No guaranteed multi-year funding for international students:** F-1/OPT/H-1B path makes funding gaps particularly risky; full international PhD funding is a hard requirement.

## Scientific identity narrative
<!-- append-only section, written by sop-coach -->

### Intellectual lineage

#### Session: 2026-06-02 (sop-coach, cluster: intellectual lineage)

My intellectual lineage is still forming — I'm a rising senior, not a second-year PhD student, and I want to be honest about what I've actually absorbed versus what I'm building toward.

The researcher I've engaged with most directly outside my own lab is Michael Berry. I read his work on the nonlinearity of caustic patterns in gravitational lensing — specifically the wavelength-dependent structure of caustics — because it connects directly to observations in the GL project data that may be the subject of a future paper. That encounter was substantive: I found a specific result in Berry's lensing analysis that appears in our own measurements, and verifying that connection is part of the ongoing work. I've read Berry's geometric phase paper much more briefly; it's on my list to read seriously before applications, because the Poincaré sphere problem I want to pursue for my senior project sits squarely inside that tradition and I don't want to reference it without real content.

The tradition I'm most directly working inside is Kiko's (Prof. Galvez's) structured light program at Colgate. Reading his papers taught me how research in this area is constructed — how optical analogs are designed, how phase profiles encode physical states, how to move between theory and tabletop implementation. That's been more formative than any single paper: learning a research style, not just a result.

My self-directed reading program is driven by gaps I identified and decided to fix. Crotty's quantum mechanics course was heavily matrix-based, and while I worked through it, the formalism was opaque in a specific way — the physical content kept disappearing behind the algebra. Sakurai's Modern Quantum Mechanics gave me what was missing: it combines Dirac bra-ket notation with matrix formalism in a way that keeps the physical objects visible throughout. I'm comfortable with mathematics, but I need the mathematical objects to have physical meaning I can track; bra-ket notation gives me that in a way that pure matrix manipulation doesn't. That preference runs through my research approach too — I read the theory before touching the setup, I simulate before building, and I go back to primary papers when the physical picture isn't clear.

Topology is next on the list for a specific reason: the Poincaré sphere, which is the mathematical object at the center of my proposed senior project, is a topological structure — the 2-sphere, S². The higher-order Poincaré spheres I want to extend to are more complex topological spaces, and the polarization optics I already work with daily (half-wave plates, quarter-wave plates) are physically described by transformations on that sphere. I want to understand the mathematics of the physical objects I work with, not use them as black boxes. Abstract algebra is on the list for the same reason — group theory underlies the symmetry structure of quantum states and optical polarization, and I'd rather build that foundation before PhD coursework than catch up during it.

The through-line, honest version: my lineage runs from Kiko's structured light program, through Berry's geometric and lensing work, toward a topology-grounded understanding of geometric phase in higher-dimensional optical state spaces. I haven't read all the foundational papers in this tradition yet — Allen et al. on orbital angular momentum, Pancharatnam on geometric phase in optics, the broader structured light literature — but I know what I need to read and why, and I'm building toward it deliberately rather than waiting for a course to assign it.

### Technical signature

#### Session: 2026-06-01 (sop-coach, cluster: technical signature)

My technical signature has two components — a physical layer and a mathematical layer — and most of what I've learned in research has been figuring out how to move between them.

**Physical layer — optics and instrumentation**

The center of my experimental toolkit is the spatial light modulator. I can program phase profiles from first principles: for the GL project I went back to the original Einstein ring paper to understand how the phase encoding works, then adapted existing code to implement Schwarzschild lens profiles for single and binary lenses. I am able to reconstruct the entire phase profile generator from scratch. The non-trivial part of SLM work isn't the phase encoding itself — it's managing the pixelization artifact. The SLM's pixel grid acts as a diffraction grating, creating a cross-pattern of zero, first, second, and higher diffraction orders in the output. To get a clean image, you have to apply a separate grating in the phase plane to spatially separate the first diffraction order — the signal — from the zero order and higher orders that carry SLM artifacts and interference. Designing that grating requires balancing three parameters: if the grating is too dense or too loose it degrades diffraction quality; if the tilt angle is too steep the beam can't be re-aligned to the optical axis. The working parameter range isn't in any manual — I learned it empirically, through iteration and laser realignment. I can teach this process from scratch, including the physics of why it's necessary, the trade-offs in parameter space, and how to diagnose when the grating is misconfigured from the output beam alone.

Beyond phase programming, I own laser alignment. Prof. Galvez has explicitly endorsed my alignment skill, and I now know my optical setup completely — I can diagnose any misalignment from its signature in the output beam pattern without checking each element in sequence. I can immediately fix any problem that occurs. This mastery came from the quantum pendulum project, my introductory lab assignment: the task was to recreate a pendulum optical setup previously built in the lab, and aligning it for the first time with no experience was genuinely painful. The phase profile was generated by code written by previous students; my contribution was fine-tuning the separations, sizes, and brightnesses of the 11 pendular eigenstates encoded in the Fourier plane — ring radii proportional to energy, angular modulation proportional to quantum probability density, encoding both bound and rotor states. I've since extended that alignment skill to the full GL setup and now operate it independently.

I also built the ThorLabs hardware automation from scratch — MATLAB IO control of the LM300 translation stage and the CMOS camera, including the communication layer that establishes simultaneous contact with both instruments. That code is now used lab-wide by other projects. On top of the automation, I wrote image analysis code for the GL project: alignment and comparison routines for sequential images, and a movie generation script that assembles 1,000+ images into a frame-by-frame visualization of the merger pattern evolution as two Schwarzschild lenses approach each other. Neither the image analysis nor the movie was assigned; I built both because they were better ways to work with the data. Previous lab members working on the GL project had not been able to produce clean, usable images; I was the one who eventually solved the experimental problems and generated the actual data. I do embedded development as a personal hobby project outside the lab — writing firmware and hardware interfaces for microcontrollers — for the same reason I built the ThorLabs automation: the satisfaction of making hardware respond to code you wrote is something I keep seeking out independently.

**Mathematical layer — Fourier methods and operator theory**

My computational background gave me 2D Fourier analysis before I had any optics experience. With Lam, I worked on pulsar timing residuals using PSD methods, red noise analysis, and 2D Fourier transforms in Python — learning the tools at the data analysis level, applied to gravitational wave detection in NanoGrav post-fit datasets. When I moved into Galvez's lab, I recognized that Fourier-plane encoding in optics is the same operation applied to a different substrate: instead of decomposing a time series into frequency components, you encode a spatial eigenstate superposition in the back focal plane of a lens and the optical Fourier transform physically implements the decomposition. The quantum pendulum project was my first explicit use of this equivalence. I didn't experience these as separate skills — they're the same mathematical object instantiated in two different physical contexts.

The Koopman operator framework from the Chua's circuit project is the same idea in a third context. EDMD lifts a nonlinear physical system into a higher-dimensional function space where the dynamics become spectrally analyzable — a Fourier-like decomposition applied to the phase space of a chaotic system. I co-built the full EDMD analysis repository from scratch with a team, applying it to a physical Chua's circuit across four dynamical regimes — fixed point, limit cycle, period-doubled limit cycle, and double-scroll chaos — and comparing polynomial, RBF, and piecewise-linear observable dictionaries. I implemented the Lyapunov spectrum computation and box-counting fractal dimension algorithms, and built a custom MATLAB serial interface to an Arduino R4 Minima for real-time hardware data acquisition. I can give an independent talk on this entire framework; I understand the mathematics well enough to explain why it works, not just how to run it.

**MATLAB is my primary tool.** I've used it for SLM phase programming, ThorLabs hardware IO, image analysis, Koopman EDMD, Arduino serial communication, and parameter simulation across all of my research. Python is my secondary tool — SciPy, AstroPy, NumPy, Pandas, Matplotlib — proficient enough to build working data pipelines, though I rely on documentation for less familiar library functions. I'm also actively self-studying advanced quantum mechanics using Sakurai and Reed's functional analysis text (recommended by Prof. Crotty), which is directly relevant to the operator-theoretic framing I've been developing through the Koopman work. My electronics background (Adhikari's lab) gives me comfort with digital and analog instrumentation; I've built and debugged physical circuits and understand hardware at the component level, not just as black boxes.

**Mathematical modeling** is a separate thread: I was a finalist in HiMCM (MAA/COMAP) — a 36-hour mathematical modeling competition — which required building quantitative models from scratch under time pressure and defending them in writing. That experience trained a different kind of mathematical thinking than lab research: applied, fast, and required to produce usable results quickly.

**Approach to new problems:** When I encounter an unfamiliar problem, I read the relevant texts and papers first to understand the theoretical structure, then run a brief MATLAB or Python simulation to develop intuition for the parameter space, then move to physical implementation. I don't build blind. The GL phase profile work is an example: before I could make the encoding work, I went back to the source paper to understand the Einstein ring geometry from first principles. That habit — tracing the math before touching the setup — is what let me solve the imaging problem that previous workers couldn't.

### Open questions
<!-- COMPLETE — synthesized 2026-06-25; working notes below retained as raw record -->

#### Working notes: 2026-06-02 (sop-coach, cluster: open questions — awaiting synthesis)

**Raw Q&A — do not treat as final prose; synthesize after completing the cluster**

The core problem Frank is working toward: entangled photon states move along geodesics on the Poincaré sphere (S²), but which geodesic they select is unresolved. Bill Luo (Galvez lab, graduated summer 2026) worked on this problem. Frank's instinct: the geodesic choice requires a higher-dimensional state space to explain — the standard Poincaré sphere doesn't capture all the relevant degrees of freedom. His candidate extension: higher-order Poincaré spheres, where OAM modes live, which are directly accessible via the SLM setup he already owns.

Frank's working intuition on why the choice is unresolved: there are missing variables in the current description. The system may need a higher-order topological structure — more degrees of freedom — to fully specify which geodesic is taken. This is the same intellectual move Frank has made in two prior contexts: (1) Koopman operator on Chua's circuit — chaotic dynamics became analyzable by lifting to a higher-dimensional function space; (2) Fourier-plane encoding — hidden eigenstate structure became visible by working in the Fourier plane rather than direct space. He has not yet explicitly recognized this as a recurring pattern.

**Resolved 2026-06-25 — synthesis below.** Frank's answers: (a) the missing-variable question can only be answered once the senior project actually starts (topic still TBD) — candidate is OAM / higher-order Poincaré spheres; the simple topological structure breaks down in complex regimes (multi-mode fiber cited as throwaway example). Held provisionally, not asserted. (b) Confirmed the "lift to higher-dimensional space" move is the same across Koopman, Fourier optics, and the Poincaré problem. His epistemic stance: the patterns are already there in nature; our role is to discover them and the right mathematics is what lets us represent them (scientific realism / Platonism — **deferred to Intellectual Taste cluster** per Frank's instruction).

#### Session: 2026-06-25 (sop-coach, cluster: open questions)

The open problem I actually think about comes from Bill Luo's work in Galvez's lab: entangled photon states evolve along geodesics on the Poincaré sphere, but *which* geodesic the system selects is unresolved. My instinct is that the geodesic is underdetermined because the standard Poincaré sphere — two degrees of freedom, the surface of S² — is too small a state space to carry all the relevant physics. The polarization sphere is adequate for simple cases but breaks down under more complex conditions. My candidate for the missing degree of freedom is orbital angular momentum, which lives naturally on the higher-order Poincaré spheres — and which I can already generate and manipulate with the SLM setup I own. I hold this provisionally. Whether OAM alone fixes the geodesic, or is only the first of several missing axes, is something I expect to answer empirically once my senior project is defined and underway, not something I can settle from the literature now. I'd rather state it as a live hypothesis with a clear test than as a conclusion I haven't earned.

What pulls me toward this problem is a move I've now made three times. With the Koopman operator on the Chua's circuit, I lifted a chaotic system into a higher-dimensional function space and its hidden linear spectral structure became analyzable. In Fourier optics, I moved from direct space to the Fourier plane and a concealed eigenstate superposition became visible and physically decodable. The Poincaré-sphere problem has the same shape: enlarge the state space, and structure that looked arbitrary at the lower level becomes determined. I don't experience these as three separate skills — it's one recurring intellectual reflex, and recognizing it has clarified the kind of physicist I am: I'm drawn to problems where apparent complexity or arbitrariness resolves once you find the right enlarged space to view it in.

#### Session: 2026-07-27 (sop-coach, cluster: open questions — REWORK, supersedes 2026-06-25 above)

My open question has moved. The geodesic-selection problem I described in June — which geodesic an entangled state follows on the Poincaré sphere — I now see as one *instance* of a larger question rather than the headline. What reframed it was reading Gutiérrez-Cuevas, Dennis, and Alonso's 2024 work on the ray and caustic structure of Ince–Gauss beams. They show that the apparent transformation of a beam from LG-like to HG-like is not really a change at all: it is a single object seen from different cuts of a Poincaré-sphere picture. That collapsed something for me — differences I had been treating as distinct phenomena were one topological structure viewed from different angles.

This is the move I keep making — Koopman, Fourier optics, the polarization sphere — but I can now state it more precisely: I am drawn to problems where you elevate the viewpoint until apparent change or complexity dissolves into one simple, elegant topological structure. Elegance, for me, is not decoration; it is the simplicity that appears once you find the right elevated vantage.

The question I actually want to work on is *constructive*. Not only "how do these topological structures emerge," but "what are the rules for building them." I think of it like assembling something from bricks: each degree of freedom you add — polarization, then orbital angular momentum, then radial mode — is another brick that enlarges the state space, and I want the grammar for how those bricks snap together into stable high-dimensional structures. Right now I am on the skeleton of that grammar: working through the group theory (O(n), U(n), SO(n), SU(n), the point groups; the distinction between Lie and Abelian groups) and how it connects to optical polarization and vectorial fields, before I can honestly say anything about construction. A sub-question I am genuinely curious about and cannot yet answer: what makes a topological structure *stable* — what property protects it. I suspect the answer is topological, but I have not earned that claim yet.

Why it matters — the stakes, not the motive: the stability of these structures is exactly what would let information ride on far more degrees of freedom than classical channels use, a direct line on the data-transmission capacity ceiling in modern information technology. But I want to be honest about where I stand. This is foundational for me right now — I am building the mathematics, I do not have an experimental observable or a falsifiable test yet, and I would rather state the question at the level I actually occupy than present it as a finished research program. The skyrmion and quantum-structured-light literature is where I am reading next, because skyrmions are a concrete instance of the stable, buildable topological texture I want to learn to construct.

### Trajectory logic

#### Session: 2026-06-01 (sop-coach, cluster: trajectory logic)

My research path before Galvez's lab was almost entirely computational, and both projects ended without papers. With Ilie, I analyzed JWST archival data using machine learning to identify potential dark matter signatures, but funding constraints kept me at the exploration stage — I never reached real research. With Lam, I went further: he walked me through NanoGrav post-fit datasets and taught me red noise analysis, 2D Fourier transforms, and PSD methods for gravitational wave detection in pulsar timing residuals. I learned Python seriously there — SciPy, AstroPy, Pandas, Matplotlib — and gained real comfort with scientific data pipelines. That project ended when Lam, a visiting professor, left for Massachusetts; the distance made continuation impractical. Neither project pointed toward astrophysics as a career. Both pointed away from it.

The project that changed my direction was the Koopman operator analysis in Segall's Nonlinear Dynamics course. I applied EDMD to a physical Chua's circuit, analyzing it across four dynamical regimes — fixed point, limit cycle, period-doubled limit cycle, and double-scroll chaos — and compared polynomial, RBF, and piecewise-linear observable dictionaries. I implemented Lyapunov spectrum computation and box-counting fractal dimension, and built a custom MATLAB serial interface to an Arduino R4 Minima for real-time hardware data acquisition. The mathematical move that fascinated me: you can find hidden linear spectral structure inside a physically chaotic system by lifting the dynamics into a higher-dimensional function space. The chaos doesn't disappear, but it becomes analyzable. I didn't have language for this at the time, but it's the same intellectual move I keep making — extracting invariant structure from systems that look complex or inaccessible from outside.

My original draw toward quantum physics came from what I'd call the "creepy" nature of QM and chaos — phenomena that are mathematically rigorous but physically counterintuitive, where the rules of everyday intuition simply break down. I was initially interested in quantum computation hardware for this reason. Most of those positions, however, are restricted to US citizens, which ruled out the bulk of the quantum computing hardware programs I had identified. Photonics and quantum optics are not a fallback — my behavior in the lab doesn't match someone who settled — but citizenship constraints were part of the honest calculation that directed my attention here.

Before I entered Galvez's lab, I applied for external research positions at Fermilab, the Perimeter Institute in Canada, and Max Planck in Garching. All three declined. Kiko (Prof. Galvez) knew this and offered me a position on the gravitational lensing project. The GL project — simulating single and binary Schwarzschild lenses using SLM-modulated phase profiles, comparing computed interference patterns to measured intensity profiles, including fringe structures relevant to binary black hole merger signatures — gave me a complete technical education in experimental optics: SLM phase programming in MATLAB, ThorLabs hardware IO control (LM300 translation stage and CMOS camera), laser alignment, and full optical system diagnostics. My role in the Barcelona collaboration phase is limited — parameter adjustment within given ranges, photo acquisition — and I'm honest about that limitation. But the technical skills are entirely my own. I rewrote the ThorLabs LM300 and CMOS camera automation from scratch without being asked; that code is now used lab-wide by other projects and members. I also built, independently, a frame-by-frame movie of the GL merger pattern evolution across 1,000+ images — Kiko hadn't requested it; I built it because a movie was a clearer way to show the data than static frames. Neither of those came from an assignment.

What I've learned about myself in the lab is that I'm most engaged when I own the full stack: optics, control code, data pipeline, visualization. The moment that stands out most is making the computer establish contact with and simultaneously control the CMOS camera and the LM300 translation stage — writing the communication layer from scratch, then watching the hardware respond to commands I had written. I do embedded development as a personal project outside the lab for the same reason. There is a specific and genuine satisfaction in mastery of a physical system: I now know my optical setup well enough that any misalignment reveals itself in the output beam pattern, and I can diagnose and fix it immediately. That mastery is what keeps me in the lab past midnight and over breaks — not obligation, but the pleasure of a system doing exactly what you intend.

The intellectual direction I want to pursue came from Bill Luo, a labmate who graduated this summer. He worked on the geometric phase of entangled photon states on the Poincaré sphere: we know these states move along geodesics, but which geodesic they choose is unresolved. I found this problem open and interesting in a way that the GL project never was — it sits at the intersection of geometry, topology, and quantum state evolution, which connects both to Kiko's structured light program and to the Koopman project's underlying question: what is the invariant structure that governs apparently arbitrary dynamical behavior? My instinct is to extend the framework to higher-order Poincaré spheres, where orbital angular momentum modes live — and those are exactly the beams I already generate with my SLM setup. The technical infrastructure is already mine. Kiko has approved a self-proposed independent project for summer 2026 through senior year; I haven't finalized the specific topic with him yet. The project will become my PHYS 410 senior seminar in fall 2026 and my honors thesis in spring 2027. The specific direction may change with Kiko's guidance, but the general area — geometric phase of structured light on higher-dimensional state spaces — is where I intend to go.

My scientific direction was also shaped by the lab seniors above me. One went to the University of Oregon to study quantum networks; another went to the University of Rochester to study optics — both directly relevant to where I want to go. They helped me technically and were candid with me about graduate school in ways that formal advising rarely is. The three research areas I find most compelling — geometric phase and topology in complex quantum optical systems, quantum chaos as it connects to the Koopman operator framework, and optical quantum circuits — all emerged partly from those conversations, not only from reading papers. The lab culture under Kiko is rigorous in the lab and genuinely relaxed outside it, which is part of why I keep choosing to be there.

### Fit-with-target
[To be developed with sop-coach]

### Intellectual taste

#### Session: 2026-07-27 (sop-coach, cluster: intellectual taste)

What I find elegant is unification through elevation. My clearest example is Gutiérrez-Cuevas, Dennis, and Alonso's 2024 work on Ince–Gauss beams: two beam families that look like different objects turn out to be one structure seen from different cuts of a sphere. I would have loved that result even with no application — the pleasure is in the collapse of apparent difference into a single object, not in what it is good for. This is a form of scientific realism for me: the structure is already there in nature, and the right geometry or group is the lens that brings an existing pattern into focus, not a formalism imposed on top of it. It is why I read the theory before I touch the setup, and why I keep reaching for higher-dimensional or operator-theoretic viewpoints — the elevated vantage is where the simplicity lives.

What I find ugly is mechanism-concealment — and it is not the same as difficulty. I dislike machine-learning approaches to physics: they can produce the right output while discarding the one thing I care about, the underlying mechanism. A method that predicts without exposing an object is a missed chance, not a result. What makes this precise rather than a slogan: I am currently working through the general-relativistic Shapiro-delay theory behind my own lensing project — a Fresnel–Kirchhoff diffraction integral with the time-delay function in the exponent — and it is genuinely hard for me to decode, harder than any ML method, yet I do not find it ugly in the least. Difficulty is an acceptable toll; opacity by design is the sin. My unfashionable-but-deep taste is the wave-optical account of light itself: in the lensing project the caustics are reproduced from just the neighbourhoods of the critical points of the time-delay function, and that picture tells me far more about how the optics works than reducing everything to Snell's law and rays. Most people walk past classical Fresnel/diffractive optics on the way to quantum hardware; I think the structure that appears at the caustics — exactly where the ray picture breaks down — is where the real physics lives.

### Cross-pollination from history-historiography
[To be developed with sop-coach]

## Notes
- Application cycle: Fall 2027 entry (applying Fall 2026)
- GRE General: not yet taken — sit Summer/Fall 2026
- Physics GRE: not yet taken — **must sit for CU Boulder / JILA** (strongly recommended, explicitly flags students from small programs and non-US institutions); also assess for other programs; target Fall 2026; score 750+ would directly address math gap perception across all applications
- Senior year independent project (Summer 2026–May 2027) is a major asset — ensure defined scope and preliminary results by December 2026 for applications
- Alumni Memorial Scholar $10,000: allocated to personal projects and application visit costs (not funding research)
- Prof. Crotty: strong academic relationship (near-perfect quantum score, TA'd 205) but not a recommender per Frank's assessment
- Girlfriend based in Syracuse — soft geographic preference for Northeast
- Recommender full titles to be confirmed before LoR requests
