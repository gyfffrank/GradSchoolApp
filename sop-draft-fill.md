# SOP Scaffold — FILLED with source sentences

<!--
HOW TO USE THIS FILE
- Every bullet under "SENTENCES" is lifted VERBATIM from a source file. Nothing here is invented.
- Source tag after each sentence:
    [M]   = Materials.docx  (primary, as requested)
    [P]   = profile.md
    [CN]  = SOP_contribution_notes.md
    [LOG] = PROJECT_LOG.md
  Sentences with NO tag do not exist in any source — they are marked <!-- GAP --> for you to fill.
- Verbatim means verbatim: grammar/typos from Materials.docx are preserved so you can see exactly
  what is yours. Trimmed fragments are marked [M, trimmed].
- Assembled word counts are given per paragraph against the scaffold target so you can see how much
  to cut. Every paragraph is currently OVER target — that is deliberate; select, don't expand.
- Generated 2026-07-31 against sop-scaffold.md (2026-07-27 version).
-->

---

## ¶1 — Opening / research goal — target 100–150 w · assembled ≈ 300 w (cut ~half)

**Claim this ¶ must serve:** live problem → your recurring reflex → doctoral direction. Three sentences of work.

### Beat A — the hook (a real unresolved problem, constructive framing)

> My open question has moved. The geodesic-selection problem I described in June — which geodesic an entangled state follows on the Poincaré sphere — I now see as one *instance* of a larger question rather than the headline. **[P]**

> What reframed it was reading Gutiérrez-Cuevas, Dennis, and Alonso's 2024 work on the ray and caustic structure of Ince–Gauss beams. They show that the apparent transformation of a beam from LG-like to HG-like is not really a change at all: it is a single object seen from different cuts of a Poincaré-sphere picture. **[P]**

> The question I actually want to work on is *constructive*. Not only "how do these topological structures emerge," but "what are the rules for building them." **[P]**

> I think of it like assembling something from bricks: each degree of freedom you add — polarization, then orbital angular momentum, then radial mode — is another brick that enlarges the state space, and I want the grammar for how those bricks snap together into stable high-dimensional structures. **[P]**

> A sub-question I am genuinely curious about and cannot yet answer: what makes a topological structure *stable* — what property protects it. **[P]**

<!-- NOTE: the Ince–Gauss hook exists ONLY in profile.md, not in Materials.docx. Materials.docx's
     closest equivalent is the Task-2 "Research Objects" sentence below, which is vaguer. Decide which
     one leads. Scaffold recommends the Ince–Gauss version. -->

### Beat B — the reflex (your differentiator)

> I am drawn to problems where you elevate the viewpoint until apparent change or complexity dissolves into one simple, elegant topological structure. **[P]**

> Elegance, for me, is not decoration; it is the simplicity that appears once you find the right elevated vantage. **[P]**

> The mathematical move that fascinated me: you can find hidden linear spectral structure inside a physically chaotic system by lifting the dynamics into a higher-dimensional function space. **[M]**

<!-- GAP — ¶1 needs ONE compressed sentence naming all three instances of the reflex (Koopman →
     Fourier-plane encoding → Ince-Gauss/Poincaré). Every source states them separately; none states
     them as a single list. You write that sentence. -->

### Beat C — the direction (doctoral field + stakes, stakes SECOND)

> I hope to research certain complex optical structures in high dimensional spaces, around singularities, or under topological perspectives. **[M]**

> I especially interested in finding properties in complex or even chaotic conditions, and how these properties contribute to understanding structures of photons, the ways of their propagation, and how they potentially contribute to development in quantum/classical optical networks. **[M]**

> I think high dimensional quantum structured light would be my current top interest and best fit. **[M]**

> I am pretty interested in the topological structures entailed in this field and I think this is a promising field to solve information-capacity bottlenecks in communication and quantum information processing, as comparing to electronical circuit, photons have way more degrees of freedom to allow the information to be encoded. **[M]**  ← *stakes sentence; scaffold says state this SECOND, not as the motive*

> the stability of these structures is exactly what would let information ride on far more degrees of freedom than classical channels use, a direct line on the data-transmission capacity ceiling in modern information technology. **[P, trimmed]**

**Materials.docx's own opening template (Task 8.2) — for reference while you write:**
> My research experiences have led me to ask how ____. By using spatial light modulators to ____ in projects on gravitational lensing and quantum pendulum dynamics, I became interested not only in reproducing complex physical phenomena optically, but also in understanding ____. I now hope to pursue doctoral research in ____, with particular interest in ____. **[M]**

<!-- UNRESOLVED TENSION flagged in scaffold, still unresolved: your taste pulls fundamental/classical
     (Alonso/Dennis geometric structured light) while your stated field is quantum. No source resolves
     this. Suggested framing to write yourself: classical topological structure = the substrate you
     enter at; quantum = the extension where the stakes live. -->

---

## ¶2 — Quantum pendulum (entry into experimental optics) — target 180–250 w · assembled ≈ 260 w

**Role:** the honest on-ramp. Helmholtz–Schrödinger bridge + first physical Fourier-plane encoding + precision about what was yours.

### Beat A — how you got there (optional; cut first if over length)

> The reason why I join this lab is an accident. **[M]**

> At the end of the sophomore year, I was trying to apply researches by other colgate faculties as well as trying to look for an external research opportunity in quantum physics, but due to the funding cut that year, all of the professors and institutions that I applied for rejected my application. **[M]**

> But turns out prof. Galvez got back to me saying this gravitational project had an open position which haven't been solidified in the Summer Research Application, and he's happy to take me. **[M]**

### Beat B — the physics

> This research started by the simple project about optical analog of quantum pendulum dynamics. **[M]**

> I designed and experimentally achieved a structured optical beam exploiting the resemblance between the Helmholtz–Schrödinger equation equivalence and the wave function of a Matheiu/Eliptical Beams. **[M]**

> Generated a Fourier-plane image encoding a superposition of 11 pendular eigenstates, with ring radii proportional to energy and angular modulation proportional to quantum probability density, including bound and rotor states. **[M]**

### Beat C — honest ownership (the beat that makes ¶3 land)

> All major codes are written by previous people, including one that generates a theoretical simulation of the eigenstates and another one that generate the phase encode and controls the SLM. **[M]**

> My contribution to this project was fine-tuning the separations, sizes, and brightnesses of the 11 pendular eigenstates encoded in the Fourier plane through MATLAB. **[M, trimmed]**

> Prof. Galvez first taught me how to align the lasers, lens, apertures, mirrors, and cameras. **[M]**

> We created a few really cool pictures, and I learned how the entire set up works, including the laser alignment, SLM controls, and 4-f Fourier Lens System. **[M]**

> I've since extended that alignment skill to the full GL setup and now operate it independently. **[M]**

### Beat D — the conceptual bridge (Fourier: computational → physical)

> With Lam, I went further: he walked me through NanoGrav post-fit datasets and taught me red noise analysis, 2D Fourier transforms, and PSD methods for gravitational wave detection in pulsar timing residuals. **[M]**

> When I moved into Galvez's lab, I recognized that Fourier-plane encoding in optics is the same operation applied to a different substrate: instead of decomposing a time series into frequency components, you encode a spatial eigenstate superposition in the back focal plane of a lens and the optical Fourier transform physically implements the decomposition. **[P]**

> The quantum pendulum project was my first explicit use of this equivalence. I didn't experience these as separate skills — they're the same mathematical object instantiated in two different physical contexts. **[P]**

<!-- GAPS — the four scaffold holes for ¶2 are STILL EMPTY in every source. Nothing exists to lift:
     Q11: what output pattern first told you the alignment / eigenstate weighting was wrong?
     Q12: how did you tune AND VALIDATE the 11-state pattern — visual? quantitative fit? theoretical
          ratios? iterative comparison to a target image?
     Q13: the hardest conceptual step in making Helmholtz–Schrödinger physically meaningful.
     Q14: what this taught you about structured light BEYOND generating a pretty image.
     You need at least Q12 or Q14 — without one of them this ¶ is a description, not an experience. -->

---

## ¶3 — Gravitational lensing (THE ANCHOR) — target 250–350 w · assembled ≈ 700 w (cut ~half)

**Claim this ¶ argues:** *I built the instrument and the code that turned a theoretical caustic picture into the first quantitative wave-optical measurement of it — and then extended that rig into a platform for adding degrees of freedom, which is the question I want my PhD to be about.*

### BEAT 1 — Credential + taste hook (2 sentences)

**Credential:**
> The paper referred to throughout is A. Moreso Serra, O. Bulashenko, Y. Gu, T. Nguyen, K. Kendja, V. Rodríguez-Fajardo and E. J. Galvez, "Laboratory observation of lensing diffraction in a binary-lens system for gravitational-wave astrophysics," dated 8 June 2026, a collaboration between the Institut de Ciències del Cosmos in Barcelona, which supplied the theory, and the Colgate University optics laboratory, where the experiment was done. **[CN]**

> I am the first-listed author of the Colgate experimental group and the third author overall. **[CN]**

> I built and calibrated the modulator-based optical platform, the automated acquisition and the complex-field analysis used to make the first laboratory observation of gravitational-lensing diffraction from a binary-mass system, and extended it to geometric-optics, polarization and cosmic-string analogues. **[CN]** ← *this is the single best one-sentence version; CN calls it a "drafted passage I can lift directly"*

> In the past whole year, I designed and carried out an optical simulation of gravitational lensing using laser beams modulated by a spatial light modulator to emulate spacetime curvature. **[M]**

> Quantitatively compared theoretical predictions with measured intensity profiles demonstrating agreement in fringe structure relevant to binary systems and black hole mergers. **[M]**

> earlier experiments had confirmed caustic morphologies, whereas agreement at the level of the detailed diffraction structure is a qualitatively new level of validation. **[CN, trimmed]** ← *the actual novelty claim*

**Taste hook (1 line — pick one):**
> the caustics are reproduced from just the neighbourhoods of the critical points of the time-delay function, and that picture tells me far more about how the optics works than reducing everything to Snell's law and rays. **[P, trimmed]**

> I think the structure that appears at the caustics — exactly where the ray picture breaks down — is where the real physics lives. **[P]**

> Independently coded and analyzed the areas in the phase encode of the gravitational lensing which contributed the most to the caustic patterns of the interference images, which potentially contribute to understanding of optics around singular areas and critical points. **[M]**

<!-- HONESTY GUARDRAIL (a): the caustic THEORY is Barcelona's. Your ownership = experiment, code,
     data, reduction. CN's own wording if you want it verbatim: "the accurate way for me to describe
     my role is that I built and calibrated the platform and the analysis, and took the
     interference-scan and caustic data that I personally acquired, rather than claiming every
     published figure." [CN]
     Also unresolved per CN: confirm publication status/venue and whether you may cite the preprint. -->

### BEAT 2 — The challenge: integrating the second SLM (the sign-flip elimination arc) — 3–4 sentences

**Setup:**
> One of the biggest challenges that I have confronted is configuring the new spatial light modulator. This summer, prof. Galvez decided to introduce a new Holoeye Pluto 2.1 NIR145 LCOS-SLM into the current setup. This new SLM should connected with the Hamamatsu LCOS-SLM in series. **[M]**

**Expected → anomaly:**
> After setting up the SLM, I first tried to encode a Bessel Beam on the new SLM to see if the 4-f system is able to function correctly with the second Hamamatsu SLM. I am intending to see the concentric circles at the end of the 4-f system, but turns out I saw a big circle which should only appear at the far field of the beam. **[M]**

**Hypothesis 1 — collimation — eliminated:**
> I originally thought it's the input beam of the SLM not collimated so it brought an angle to make thing focus very close to the SLM plane. I tried using the Shearing Interferometers to verify the collimation of the laser beams after the beam expander (composed by 2 apertures), by changing the separation between the lenses I have collimated the lasers but the issue was still there. **[M]**

**Hypothesis 2 — LUT — eliminated:**
> Then, I thought it could be the LUT issue, which is the dictionary which governed how the gray-scale image ranging 0 to 255 to be translated in to 0 to 2pi phase delay on the SLM. I digged through the document of the Holoeye Pluto 2.1 and configure the SLM with correct LUT file, the issue is still not solved. **[M]**

**Decisive controlled test → root cause → fix:**
> Then I started suspecting I encode the SLM wrong, I compared the effect of the same phase encode on the both SLMs, I gave them a plain grating to deflect light from zero order to the first order. I found the new slm simply deflect the light to opposite direction from the old Hamamatsu one. I realized this is the actual issue, and I suspecting the new slm just deflect lights in the opposite way compared to the old SLM. Then I add a -1 multitude to the entire phase map, and the issue been fixed. **[M]**

> recognizing that let me replace two empirical sign corrections with a single global negation that fixes gratings, lenses and orbital-angular-momentum charge simultaneously. I documented the hypotheses that turned out to be wrong, and why they had been convincing. **[CN, trimmed]** ← *the generalization; stronger than "the issue been fixed"*

**Materials.docx's requested "specific moment" template (Task 3.2), still blank:**
> 当我发现____时，我意识到原来的假设____可能不成立。为区分____和____，我设计了____。 **[M]**
<!-- GAP — fill this in English: "When I found [the new SLM deflected the first order the opposite
     way], I realized my assumption that [both devices encode phase with the same polarity] could not
     hold. To distinguish [X] from [Y], I designed [the same-grating-on-both-devices control test]."
     The pieces exist; the single sentence does not. -->

**Grit beat (1 line — compress to a clause if over length):**
> I've found the deformation disappears only when the laser beam enters the SLM at a certain angle. I tried to center the beams while keeping the angle between the laser and the SLM and it finally works. **[M]**

> That was the messiest station I've ever had, tools, lenses, irises are all over the table. But I am not around of making such as ness, I believe this is the necessary step. **[M]** <!-- typo in source: "not around of making such as ness" = "not afraid of making such a mess" -->

**Architecture (1 line, optional — scaffold says CUT THIS FIRST if over length):**
> Instead of simply adding more functions or variables to create mess, I reconstruct the repository in a format like a python library, which I use a configuration function to control the initiation and configuration of both SLM and generate a configuration matrix for both of them, and re-write the functions to allow them to read the configurations to avoid writing a redundant and essentially the same code base for the new SLM, and this would make the future adding more and different SLMs much easier by writing a new configuration function. **[M]**

### BEAT 3 — Payoff / bridge to the PhD (2–3 sentences)

**Honesty (keep):**
> The stationary-phase minimal-pixel result and the Wigner-rotation and cosmic-string modules are simulation and design work that has been verified numerically but not yet measured on the bench, and I should say so plainly, because the numerical verification is strong enough to stand on its own merits. **[CN]**

> Full general-relativistic pipeline built and verified numerically; bench tutorial written; hardware implementation pending. **[LOG, trimmed]**

**What the platform is for:**
> Noh, Alsing, Miller & Ahn prove that the gravitational Wigner Rotation Angle imprinted on a photon's helicity state is equivalent to a classical SO(2) rotation of the polarization plane. **[LOG, trimmed]**

> the polarization work extends analogue gravity beyond scalar diffraction, making a gravitationally induced polarization rotation, and its non-reciprocity, into a bench-measurable quantity. **[CN, trimmed]**

> the deeper point is that a spatial light modulator is a programmable spacetime. Any thin-lens gravitational potential can be written as a phase mask, so the same apparatus that makes a binary black-hole lens can make a cosmic string or a Kerr Wigner rotation without changing a single optical component, and I have now implemented all three. **[CN, trimmed]**

**The bridge that the ¶ exists for:**
> each degree of freedom you add — polarization, then orbital angular momentum, then radial mode — is another brick that enlarges the state space, and I want the grammar for how those bricks snap together into stable high-dimensional structures. **[P, trimmed]**

> The skyrmion and quantum-structured-light literature is where I am reading next, because skyrmions are a concrete instance of the stable, buildable topological texture I want to learn to construct. **[P]**

<!-- GAP — the ONE sentence that makes Beat 3 work does not exist in any source: "a second SLM is a
     second degree of freedom, so the rig is the physical form of the question I most want to pursue."
     Materials.docx describes the two-SLM build purely as an engineering problem; profile.md describes
     the bricks/DoF question purely as an intellectual one. Nothing joins them. Write that join —
     scaffold says this and the −1 arc are the paragraph's whole reason to exist. -->

### Independent contributions — name, don't bury (fold into Beat 1 or 2, ~1 sentence total)

> I also built the ThorLabs hardware automation from scratch — MATLAB IO control of the LM300 translation stage and the CMOS camera, including the communication layer that establishes simultaneous contact with both instruments. That code is now used lab-wide by other projects. **[M]**

> Neither the image analysis nor the movie was assigned; I built both just because they were better ways to work with the data. **[M]**

> Previous lab members working on the GL project had not been able to produce clean, usable images; I was the one who eventually solved the experimental problems and generated the actual data. **[M]**

> for the GL project I went back to the original Einstein ring paper to understand how the phase encoding works, then adapted existing code to implement Schwarzschild lens profiles for single and binary lenses. I am able to reconstruct the entire phase profile generator from scratch. **[M]**

> Independently coded and analyzed the phase structure of the lensed interference pattern by encoding a virtual Mach-Zehnder interferometer in SLM which allows further research in complex optical structures in it. **[M]**

> I wrote a complete MATLAB instrument-control and analysis platform, currently about eight thousand lines across roughly seventy source files and forty-eight commits. **[CN]**

> The part that I enjoy the most in the lab is that I'm most engaged when I own the full stack: optics, control code, data pipeline, visualization. **[M]**

<!-- ALTERNATIVE SPINE, if you decide the sign-flip arc is too narrow: the multi-wavelength alignment
     arc is equally complete in Materials.docx and shows IMPACT (solved what others could not):
     "Before I took over the setup, the images we took is always kind of deformed and asymmetrical in
     shape and intensity. I first try align the camera as it's the easiest fix, but its not quite
     working. Then, I started remove the lenses of the 4-f Fourier system, and I found the laser is
     not quite aligned with the first order of the SLM output, then I encode the SLM with an optical
     vortex (the benefit is to be able to see if the laser passes the center of the iris used for
     aligning the system) and then we tune the mirrors to align the 4 f system. The uneven intensity
     of the pattern turns out to be caused by incoherent brightness of the laser source, the issue is
     solved by slightly move the lenses of the beam splitter." [M]
     Scaffold picked the sign-flip arc; this is here so the choice stays yours. -->

---

## ¶4 — Supporting capabilities — ONE integrated paragraph — target 120–180 w · assembled ≈ 280 w

**Role:** organize by *capability*, not chronology. Combine, don't enumerate.

> My research path before Galvez's lab was almost entirely computational, and both projects ended without papers. **[M]**

**JWST (compress to one clause at most, or cut):**
> With Ilie, I analyzed JWST archival data using machine learning to identify potential dark matter signatures, but funding constraints kept me at the exploration stage — I never reached real research. **[M]**

**NanoGrav = Fourier/PSD continuity:**
> With Lam, I went further: he walked me through NanoGrav post-fit datasets and taught me red noise analysis, 2D Fourier transforms, and PSD methods for gravitational wave detection in pulsar timing residuals. I learned Python seriously there — SciPy, AstroPy, Pandas, Matplotlib — and gained real comfort with scientific data pipelines. **[M]**

**Koopman = the enlarged-space theme in its purest form:**
> The project that changed my direction was the Koopman operator analysis in Segall's Nonlinear Dynamics course. I applied EDMD to a physical Chua's circuit, analyzing it across four dynamical regimes — fixed point, limit cycle, period-doubled limit cycle, and double-scroll chaos — and compared polynomial, RBF, and piecewise-linear observable dictionaries. **[M]**

> I implemented Lyapunov spectrum computation and box-counting fractal dimension, and built a custom MATLAB serial interface to an Arduino R4 Minima for real-time hardware data acquisition. **[M]**

> The mathematical move that fascinated me: you can find hidden linear spectral structure inside a physically chaotic system by lifting the dynamics into a higher-dimensional function space. The chaos doesn't disappear, but it becomes analyzable. **[M]**

> I didn't have language for this at the time, but it's the same intellectual move I keep making — extracting invariant structure from systems that look complex or inaccessible from outside. **[M]**

**The unifying sentence:**
> MATLAB is my primary tool. I've used it for SLM phase programming, ThorLabs hardware IO, image analysis, Koopman EDMD, Arduino serial communication, and parameter simulation across all of my research. **[M]**

**Materials.docx's own integration template (Task 6.4), still blank:**
> 我在 NANOGrav、JWST 数据分析和 Chua 电路研究中的经历，使我从不同角度学习了如何____。NANOGrav 培养了我处理____的能力；JWST 项目让我学习了____；Chua 电路则让我将____与____结合。这些能力现在直接影响了我研究光学问题的方式：我不仅关注是否能够产生一个光学现象，也关注如何____。 **[M]**

<!-- GAPS still open in ¶4:
     Q17 (decision): NanoGrav vs Koopman vs both in the main SOP? Recommend Koopman as the spine
          (it carries the enlarged-space reflex) and NanoGrav as one clause of Fourier continuity;
          JWST cut entirely.
     Q18: your SPECIFIC slice of the Koopman TEAM project, and the lesson from comparing
          polynomial / RBF / piecewise-linear dictionaries (model choice vs physical interpretability).
          Sources say you "co-built" and "implemented Lyapunov + fractal dimension" but never state
          what the dictionary comparison TAUGHT you.
     Q19: shortest POSITIVE framing for why computational astro narrowed you toward experimental
          optics. Materials.docx only has the negative version ("Neither project pointed toward
          astrophysics as a career. Both pointed away from it."). That line is honest but it argues
          exclusion, not attraction. -->

---

## ¶5 — Conclusion — target 2 sentences · assembled ≈ 0 usable

<!-- LARGEST GAP IN THE DOCUMENT. Nothing in Materials.docx answers Task 9.1 (博士阶段我希望建立什么能力 /
     我希望从"能够执行实验"成长为什么类型的研究者 / 我希望最终能够独立提出怎样的问题). The scaffold's
     talkpoint — "an experimentalist who moves fluently between mathematical representation,
     programmable light fields, instrumentation, and quantum-state questions" — is the SCAFFOLD's
     phrasing, not yours. You must write these two sentences from scratch.
     The ending test: make a claim the OPENING could not. Not a restatement, not a hope-list. -->

**Fragments that exist and could seed it:**

> but quantum experiments require additional tools such as heralded single-photon or SPDC sources, coincidence counting, single-photon detectors, and quantum-state tomography, and then research about quantum features of those structured light beams. **[M, trimmed]** ← *what you need to LEARN*

> Currently, I am using SLM to modulate classical light beams, and in PhD, I can advance toward quantum states and scalable devices. **[M]**

> Right now I am on the skeleton of that grammar: working through the group theory (O(n), U(n), SO(n), SU(n), the point groups; the distinction between Lie and Abelian groups) and how it connects to optical polarization and vectorial fields, before I can honestly say anything about construction. **[P]**

> This is foundational for me right now — I am building the mathematics, I do not have an experimental observable or a falsifiable test yet. **[P, trimmed]** <!-- honest, but do NOT end the SOP on it -->

<!-- Career track: profile.md records dual-track (academic faculty in experimental quantum optics/AMO,
     or industry in quantum networking and optical photonics). Scaffold says keep it dual-track without
     over-committing. Not in Materials.docx — your call whether it appears at all. -->

---

## Per-school fit block — 3 sentences each — lives in `programs/{slug}/essays/sop-tailoring.md`, NOT the core SOP

**Materials.docx template (Task 9.2), verbatim:**
> Professor ______'s work on ______ is particularly relevant to my interest in ______. My experience with ______ has prepared me to contribute to ______, while I hope to develop deeper expertise in ______. I am especially interested in exploring whether/how ______. **[M]**

**Slot 2 — what you contribute immediately (reusable across schools):**
> I am currently able to set-up, configure, and utilize Spatial Light Modulator easily. **[M]**

> High Dimensional Quantum Structured Light experiments would also use SLMs, thus my skill set built from the Lab Gravitational Lensing project can be straightly transferred to this field because the same wavefront-shaping principles can be applied to the transverse wavefunction of single photons or photon pairs. **[M, trimmed]**

**Slot 3 — what you need to learn (reusable):**
> quantum experiments require additional tools such as heralded single-photon or SPDC sources, coincidence counting, single-photon detectors, and quantum-state tomography. **[M, trimmed]**

**Cluster → PI map, verbatim from Materials.docx Task 1:**

| # | Cluster | PIs **[M]** | Frank's own verdict **[M]** |
|---|---|---|---|
| 1 | High dimensional Structured Quantum Optics — "the intersection of spatial, polarization, OAM, and other degrees of freedom with quantum-state engineering" | Otte, Feng, Kwiat, Sergienko, Mehta; Capasso, Litchinitser, Bigelow | "my current top interest and best fit" |
| 2 | Classical Structured Light and Singular/Topological Optics — "complex phase, polarization, vortices, caustics, and propagation structures" | Alonso, Otte, Swartzlander, Litchinitser, Milchberg, Murnane/Kapteyn | "a more fundamental field of research compared to others… faculty in this field tends to collaborate other people in field structured light/quantum structured light" |
| 3 | Integrated/Nanoscale Quantum-Photonic Platforms | Feng, Mehta, Vamivakas, Alaeian, Capasso, Dimitrova, Otte | "Interesting field, but probably restricted since it is closely related to silicone ICs and EUV" |
| 4 | Atom–Photon Quantum Interfaces | Bigelow, Panda, Dimitrova, Mehta | "the most fundamental one among all five. Make this as the secondary choice" |
| 5 | Ultrafast and Nonlinear Structured Light | Milchberg, Murnane/Kapteyn, Moses, Litchinitser, Alaeian, Feng | *(no verdict recorded)* |

<!-- Alonso (Rochester) is in Cluster 2 and is an author of the Ince–Gauss paper that supplies your ¶1
     hook — the hook and the Rochester fit block are the same paper. Noted in the scaffold; the
     connection is not stated anywhere in Materials.docx. -->

<!-- GAP per school: slot 1 (2 PIs + ONE shared scientific question, not shared equipment/keywords)
     and slot 4 (a plausible next question growing from their recent work). Nothing school-specific
     exists in any source — Materials.docx has only the cluster table above. -->

---

## Sections of the scaffold NOT filled, and why

| Scaffold item | Status |
|---|---|
| ¶2 holes Q11–Q14 | **No source material exists.** Only you can answer. |
| ¶3 "specific moment" sentence (Task 3.2 template) | Pieces exist; the sentence does not. |
| ¶3 Beat-3 join (2nd SLM = 2nd degree of freedom) | **No source material.** Highest-value single sentence in the SOP. |
| ¶4 Q18 dictionary-comparison lesson | **No source material.** |
| ¶4 Q19 positive framing of the astro→optics turn | Only the negative framing exists **[M]**. |
| ¶5 entire paragraph | **No source material.** |
| Per-school slots 1 and 4 | **No source material** beyond the cluster table. |
| Teaching / Engineering Club (Task 7) | Materials.docx Task 7 is questions only, no answers. profile.md has facts (TA'd 5 courses, co-designed PHSY 125, Engineering Club co-founder/VP, 15-person go-kart team) but the scaffold allocates them no paragraph. Left out deliberately. |
| Prompt 3.5 "研究成长" fill-ins | Blank in Materials.docx; no answers anywhere. These four sentences would strengthen ¶3→¶1 if you write them. |
| Prompt 5.1–5.3 (two-project progression) | Blank in Materials.docx. Scaffold folds this into ¶2→¶3 transition, which you said you'd write. Note the honesty check Materials.docx raises itself: "两个项目在时间上是否真的具有先后关系?" — yes, the pendulum ran ~1 month and preceded GL **[M]**. |
