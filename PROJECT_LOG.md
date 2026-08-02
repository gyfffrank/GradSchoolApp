# Laboratory Astrophysics of Gravitational Lensing — Complete Development Log

**Repository:** `OpticsLab26-27`
**Developer / experimentalist:** Yufeng Gu
**Advisor:** Prof. Enrique (Kiko) Galvez — Department of Physics & Astronomy, Colgate University
**Theory collaboration:** A. Moreso Serra & O. Bulashenko, Institut de Ciències del Cosmos (ICCUB), Universitat de Barcelona
**Funding:** NSF Grant PHY-2409587
**Period covered:** ≈ 2025 (bench work, pre-repository) · **2026-04-27 → 2026-07-30** (this repository)
**Scale of work (repository):** 49 commits · 7,351 lines of MATLAB across 67 source files · 11,675 insertions / 2,817 deletions · 352 file-touches
**Scale of work (bench):** 14 laser wavelengths (403–684 nm) · `r_S` = 0.2–20 µm · `d̂` = 0–4 · hundreds of
recorded diffraction patterns, of which one full 73-frame phase-shifting cycle is archived here

> This document is a reconstructed engineering-and-physics log assembled from the git history,
> the project memory files, the working-session transcripts, the repository documentation, the
> LaTeX poster source, the raw data directories, the submitted manuscript
> (`Optical_Lab_Binary-2.pdf`), and the developer's own written account of the pre-repository
> bench work. It records what was built, what was measured, what broke, how each failure was
> diagnosed, and which conclusions were later overturned. Wrong turns are kept in deliberately —
> the diagnostic chain is the actual content.

**Provenance convention.** Because this log is also the raw-material file for graduate-application
writing, every claim carries a traceable source. Three tags are used where the source is not
obvious:

| Tag | Meaning |
|---|---|
| **[git]** | Verifiable from the repository — commits, code, committed data, committed figures. Default; used only where a paragraph mixes sources. |
| **[ms]** | Taken from the submitted manuscript `Optical_Lab_Binary-2.pdf` (dated 2026-06-08), including its figure numbers, tables, and parameter values. |
| **[account]** | The developer's own written recollection of bench work that predates or lies outside the repository (source: `GradSchoolApp/Materials.docx`, 2026-07-27). Not independently verifiable from this repo; recorded because it is the only record of the physical alignment work, and flagged so that nothing is over-claimed. |

---

## Table of Contents

1. [Scientific goal](#1-scientific-goal)
2. [Physics implemented](#2-physics-implemented)
3. [Hardware inventory](#3-hardware-inventory)
4. [Software architecture](#4-software-architecture)
5. [Chronological development log](#5-chronological-development-log)
6. [Debugging case studies](#6-debugging-case-studies-the-hard-problems)
7. [Verification and validation ledger](#7-verification-and-validation-ledger)
8. [Data products, figures, and deliverables](#8-data-products-figures-and-deliverables)
9. [Dissemination: manuscript, poster, and talks](#9-dissemination-manuscript-poster-and-talks)
10. [Open items and next steps](#10-open-items-and-next-steps)
11. [Skills and competencies demonstrated](#11-skills-and-competencies-demonstrated)
12. [Application-material index (SOP raw material)](#12-application-material-index-sop-raw-material)
13. [Appendix A — commit ledger](#appendix-a--commit-ledger)
14. [Appendix B — working-session ledger](#appendix-b--working-session-ledger)
15. [Appendix C — complete file map](#appendix-c--complete-file-map)

---

## 1. Scientific goal

Build a **tabletop optical analogue of wave-optical gravitational lensing** — specifically of a
**binary mass lens (BML)** — using a phase-only spatial light modulator (SLM), and then extend it
to **polarization** effects in curved spacetime.

The motivation, as stated on the project poster:

- Binary systems (binary stars, binary black holes) are ubiquitous, yet their **wave-optical**
  lensing is essentially unexplored — most lensing work is in the geometric-optics limit.
- Gravitational waves from compact binaries are long-wavelength and coherent, so **diffraction**,
  not just ray deflection, imprints the signal.
- A gravitational-wave detector samples only a **single "pixel"** of a vast diffraction pattern.
  A tabletop optical analogue with an SLM instead images the **entire pattern** at once.

Three research threads emerged over the period:

| # | Thread | Status at 2026-07-29 |
|---|--------|----------------------|
| **A** | **Scalar BML diffraction caustics** — encode the binary Shapiro delay on an SLM, image and measure the caustic, reconstruct the complex field by phase-shifting interferometry | Working end-to-end; data taken; poster presented; theory–experiment agreement with **no adjustable parameters** |
| **B** | **Stationary-phase (geometric-optics) minimal-pixel encoding** — reproduce the caustic using only the SLM area around the stationary points of the Fermat potential | Simulation complete and quantitatively characterized; hologram generator built; hardware run pending |
| **C** | **Gravitational Wigner-Rotation-Angle (WRA) polarimetry** — realize Miller/Noh's WRA as a dual-SLM polarization rotator, so the lensing potential drives a spatially varying polarization rotation | Full general-relativistic pipeline built and verified numerically; bench tutorial written; hardware implementation pending |

**Source papers in the repository root:**
- `Optical_Lab_Binary-2.pdf` — the binary-mass-lens manuscript, *"Laboratory observation of lensing
  diffraction in a binary-lens system for gravitational-wave astrophysics"* (dated 2026-06-08,
  under review). Authors: A. Moreso Serra and O. Bulashenko (ICCUB, Barcelona); **Yufeng Gu**,
  Thao Nguyen, Kwakye Kendja, V. Rodríguez-Fajardo, and E. J. Galvez (Colgate). Corresponding
  authors: Bulashenko and Galvez. The developer is the **first-listed Colgate (experimental)
  author**. Full results and figure-level attribution in §9.1.
- `Millers41598-024-71203-x.pdf` — Noh, Alsing, Miller & Ahn, *"Nonreciprocity in photon polarization based on direction of polarizer under gravitational fields,"* **Sci. Rep. 14, 20801 (2024)**.

### 1.1 How the project began, and what preceded it  **[account]**

Recorded because the repository begins in the middle of the story and shows none of it.

The lab position was not planned. At the end of sophomore year the developer applied to several
Colgate faculty and to external quantum-physics research programs; a funding cut that year meant
every application was declined. The fallback plan was to approach Prof. Galvez — his major advisor
— not for a position in Galvez's own lab, but for an introduction to a colleague, self-funding the
project with an **Alumni Memorial Scholar research award (≈ $10,000)**. Galvez replied that the
gravitational-lensing project had an unfilled slot that had never made it into the summer research
application, and took him on directly.

The on-ramp was a **one-month optical analogue of quantum-pendulum dynamics**, run on the *same*
bench that the lensing project would later use. Physics: the Helmholtz–Schrödinger correspondence
maps paraxial beam propagation onto the Schrödinger equation, so Mathieu / elliptical-beam
solutions are the optical image of pendular eigenstates. A Fourier-plane pattern was generated
encoding a **superposition of 11 pendular eigenstates**, with **ring radius ∝ eigenenergy** and
**angular modulation ∝ quantum probability density**, spanning both **bound (librating)** and
**rotor** states.

**Ownership, stated plainly** (this matters for how the later work is read): the theory-simulation
code and the phase-encode/SLM-control code were both **inherited from previous students**. The
developer's contribution was tuning the separations, sizes, and relative brightnesses of the 11
states in MATLAB until the superposition was physically usable — and, more consequentially,
learning the whole apparatus from zero: laser/lens/aperture/mirror/camera alignment, SLM control,
and the 4f Fourier system. Everything in this log after that point is the same bench, operated
independently.

### 1.2 Division of labour with the theory collaboration

Worth stating explicitly, because the project is a two-institution collaboration and the boundary
is clean:

| | Barcelona (ICCUB) — Moreso Serra & Bulashenko | Colgate — Galvez group, this developer |
|---|---|---|
| **Owns** | Wave-optical lensing theory; the dimensionless formulation (`w`, `d̂`, `y`); the scaling laws connecting lab optics to GW astrophysics; the Airy/Pearcey asymptotics near folds and cusps; the astrophysical parameter mapping (manuscript Table I) | The optical analogue itself: apparatus, alignment, SLM phase encoding, hardware automation, data acquisition, image analysis and reduction, the simulation code in this repository |
| **In this repository** | Appears as *implemented* physics — `optics.field`, `optics.gravityLens`, `optics.stationaryLens`, the poster equations | All of it |

The honest one-line version: **the caustic theory is Barcelona's; the instrument, the code, the
measurements, and the reduction are Colgate's.** No claim in this log should be read as claiming
authorship of the theoretical framework.

---

## 2. Physics implemented

### 2.1 Wave-optical lensing (thread A)

The lensed field is the **Fresnel–Kirchhoff diffraction integral**

```
F(w, y) = (w / 2πi) ∫ exp[ i w T(x, y) ] d²x
```

with dimensionless frequency `w = 4π R_S / λ` (small `w` → diffraction dominated; large `w` → ray
optics). `T` is the **time-delay (Fermat) function**, a geometric path term plus the gravitational
**Shapiro delay**:

```
T(x, y) = ½|x − y|²  −  ψ(x)   ≡   T_geom + T_grav
```

For a **symmetric equal-mass binary** with masses at `(±χ, 0)`:

```
T_grav(x) = −¼ ln[ (x₁² + x₂² + χ²)² − 4 x₁² χ² ]
```

**Key experimental insight — only the gravitational part is programmed.** The SLM imprints the
Shapiro delay as a pointwise phase (paper Eq. 13),

```
φ_SLM(x) = −2 k r_S T_grav(x),        k = 2π/λ
```

and **free-space Fresnel propagation from the SLM to the camera supplies `T_geom` for free**.
`r_S` is an *effective optical Schwarzschild radius* (a phase depth, not a length in the lab);
the scaled separation is `d̂ ≡ d / r_E`.

A crucial structural property that took real work to establish (see §6.2): because the encoded
phase is **metric** (defined in physical metres, not pixels), the caustic morphology and the
caustic distance are **independent of SLM pixel pitch** — but they scale as **1/(phase depth)**.
This single fact resolved the largest hardware discrepancy of the project.

### 2.2 Geometric-optics / stationary-phase limit (thread B)

At large `w` the integral is dominated by the **stationary points** `x_j` of `T` — the solutions of
the lens equation `∇_x T = 0`, i.e. `y = x − ∇ψ(x)`:

```
F_GO = Σ_j |μ_j|^(1/2) exp[ i w T(x_j, y) − i π n_j / 2 ]
```

with magnification `μ_j = [det K̂]^(-1)` (Hessian `K̂_ab = ∂²T/∂x_a∂x_b`) and Morse index `n_j`
labelling minimum / saddle / maximum images. **Caustics** are the curves `det K̂ = 0`, where images
merge and `μ` diverges.

The experimental question: *can the SLM be driven only inside small disks around the `x_j` and
still reproduce the caustic?* Implemented in `+optics/stationaryLens.m`, with a quantitative answer
in §7.2. Sanity checks built into the solver: a single point lens (`β = 0`) yields **2 images**; an
equal-mass binary with the source inside the caustic yields **5 images**.

### 2.3 Gravitational Wigner rotation (thread C)

Noh, Alsing, Miller & Ahn prove that the gravitational **Wigner Rotation Angle** imprinted on a
photon's helicity state is **equivalent to a classical SO(2) rotation of the polarization plane**,
and note it "could be feasible on an optical table … effectively realized using polarizers and
mirrors." The implementation here:

- **Full GR pipeline** (`+optics/wignerRotation.m`): equatorial **Kerr** null geodesic in `M = 1`
  units → analytic static-observer orthonormal **tetrad** → local Lorentz generators
  `Ω_ab = g(e_a, D e_b/dλ)` (Christoffels by finite differencing the analytic metric) →
  Miller Eq. 4 single-path WRA `χ` and Eq. 9/11 relative WRA `Δχ` with the
  **non-reciprocity factor `1/(1 − n₃²)`**.
- **Key design decision:** the solver is **1-D over signed impact parameter `b`**, then mapped to
  2-D. **The SLM plane *is* the impact-parameter plane** (Miller Fig. 1F/1G). A binary lens is the
  sum of two shifted 1-D curves, because angles add. The grid-independent 1-D curve is cached once
  and resampled onto any SLM grid — a large speed win.
- **Bench realization** (`docs/WRA_bench_setup.md`): a phase-only LCOS modulates only the field
  component along its liquid-crystal director. Put SLM1's director at **H** and SLM2's at **V**;
  together they are a variable retarder `diag(e^{iφ_H}, e^{iφ_V})`. Sandwich that between **two
  quarter-wave plates both at +45°** and it becomes a **pure polarization rotator** with
  `θ = (φ_H − φ_V)/2`. Drive `φ_H = Φ + θ`, `φ_V = Φ − θ`: the **differential** part is the WRA
  polarization rotation, and the **common** part `Φ` is the ordinary scalar binary-lens phase —
  so the same beam carries **both the diffraction caustic and a polarization texture on it**.

**Action on input light** (`+optics/applyWRA.m`) splits into two families:
- **Linear inputs (H/V/D/A):** stay linear, azimuth rotates by `θ`; read out by **Malus's law**
  through an analyzer. A D input with a crossed analyzer gives the dark-field null `I = sin²θ` —
  the most sensitive readout.
- **Circular inputs (L/R):** ellipse unchanged, a pure **geometric phase `e^{∓iθ}`** is imprinted →
  the WRA becomes a **diffractive wavefront** (Miller's helicity phase). L and R are conjugates.

An honest scale statement was written into both the code and the tutorial: for `r_S = 3.3 µm` in
this geometry the SLM samples impact parameters `b ~ 2600 M` — deep weak field — so the **true**
physical WRA is `|θ| ≈ 0.13°`, `|Δθ| ≈ 0.73°`. That smallness *is* Miller's point; the
non-reciprocal enhancement is what makes it detectable. For visible demonstrations the code
exposes an `analogue` scale with a `peakDeg` amplitude knob, where the **map shape is physically
faithful and only the amplitude is scaled up**.

---

## 3. Hardware inventory

| Device | Identity / specs | How it is driven | Notes |
|---|---|---|---|
| **SLM 1** | Hamamatsu X10468 phase-only LCOS, 800 × 600, **20 µm** pitch (16.00 × 12.00 mm active) | Extended video monitor, 8-bit grayscale | Reference device — all prior calibration is anchored to it. `modMaxGray` from a measured 16-point table (403–684 nm) |
| **SLM 2** | Holoeye **PLUTO-2.1 NIR-145**, S/N 7020-1 6010-2304, 1920 × 1080, **8.0 µm** pitch (15.36 × 8.64 mm) | Extended video monitor; green channel carries the 8-bit gray (grayscale BMP has R=G=B, so automatic) | Gray→phase CLUT is flashed onto the driver over USB via HOLOEYE Configuration Manager — **not** settable from MATLAB. Config library in `Holoeye/Configs_PLUTO-2.1/` |
| **SLM 3 (attempted revival)** | Boulder Nonlinear Systems **P512**, 512 × 512, **15 µm** pitch (7.68 × 7.68 mm), 8-bit | DVI-D → HDMI; presents to Windows as a 1024×768 monitor | EDID decoded: `"BNS PD 512"`, serial `BNSPD051216 0`, mfr week 20 / 2009. Preferred timing 200 MHz pixel clock ≈ 204 Hz; supports 800×600 and 1024×768 at 60–123 Hz. USB controller present but **no BNS SDK/DLL on the system** → video-only. Not adopted |
| **Camera** | Thorlabs **LP126CU**, S/N **27757**, USB 3.0, colour, **3.45 µm** sensor pitch, native frames **4096 × 3000** | Thorlabs TSI .NET SDK via 37 DLLs in `LibDLL/` | Auto-exposure controller written in-house |
| **Stage** | Thorlabs **LTS300**, S/N `45254754` | Thorlabs Kinesis | For z-scans |
| **Laser** | HeNe, **632.8 nm** (project also supports 403–684 nm via wavelength-aware calibration) | — | |
| **Host** | Windows 11 Pro, MATLAB R2024b | — | Primary display at 125% DPI scaling, SLM monitors at 100% — the source of a subtle bug (§6.1) |

### Bench layouts used

**Dual-SLM 4f relay (thread C / SLM matching work):**
```
SLM1(Ham) ─50 cm─ Lens1 ─50 cm─ iris ─20 cm─ mirror ─30 cm─ Lens2 ─50 cm─ SLM2(Holoeye)
```
The mirror is why the Holoeye is mounted mirror-opposite — a fact that generated a long-running
sign confusion (§6.3).

**Single-SLM free-space caustic imaging (thread A):**
```
SLM ─── 530 mm free space ─── camera        (no lens; 530 mm is a distance, not a focal length)
```
Clarifying that "530 mm" was a **free-space distance and not a lens focal length** was itself a
turning point in one debugging session — the earlier "4f / 1f" language had been misleading.

**Bessel / Fourier test geometry:**
```
SLM ─── L1 (f = 530 mm) ─── camera    (camera found to sit ~35 cm PAST L1's focal plane)
```

**WRA rotator (designed, documented, not yet built):**
```
laser → spatial filter → polarizer → QWP@+45° → SLM1(H) → 4f → SLM2(V) → 4f → QWP@+45° → analyzer → camera
```

---

## 4. Software architecture

### 4.1 Design philosophy

The project began as a pile of flat monolithic scripts (`MakeHologram.m`, `DisplayonSLM.m`,
`CombinedImageAnalysis.m`, `gravitylensbinary.m`, `KikoMarch24image.m`, …) with 37 DLL copies in
the repository root. It was restructured into a **MATLAB package architecture** with explicit
design rules:

- **Function style, not OOP.** `cam = camera.init(hw)` returns a plain struct; the caller does
  `camera.capture(cam, file)`.
- **`onCleanup` discipline for every device.** `cleanup = onCleanup(@() camera.close(cam))` fires
  even on Ctrl+C — this is what prevents the camera/stage from needing a power-cycle after a crash.
  Documented prominently in every `init` function.
- **Pure computation separated from hardware.** Everything in `+optics` except `display`/`close` is
  side-effect-free, so the entire physics stack runs and is testable with no hardware attached.
- **All physics in metres, never pixels.** `optics.coordinates` returns X, Y in metres; every
  lens, aperture, and grating is defined metrically. This is what makes holograms
  automatically size-matched across SLMs of different pitch (§6.2, §6.5).
- **A full hardware simulator** (`+sim/`) mirroring the camera/SLM/stage APIs, so scans can be
  developed and regression-tested with zero hardware.
- **Configuration split in two:** `slm_config.m` (SLM + laser; edited per experiment) and
  `thorlab_hardware_config.m` (device serials and paths; edited once per machine) — so SLM-only
  work never requires Thorlabs configuration.

### 4.2 Code inventory (current)

**`+optics/` — optical computation and SLM output (1,533 lines)**

| File | Lines | Purpose |
|---|---|---|
| `wignerRotation.m` | 445 | Full Kerr-tetrad/Lorentz gravitational WRA map: `θ(x,y)`, `θ_reverse`, `Δθ`, plus cached 1-D `χ(b)` curve. `analogue` and `physical` scale modes |
| `stationaryLens.m` | 419 | Binary-lens hologram restricted to stationary-phase points; analytic dimensionless stationary-point solver, Morse classification, `autoPixPerUnit`, `coreRadiusUnits`, far-field fidelity check |
| `applyWRA.m` | 203 | Acts a WRA map on H/V/D/A/L/R or arbitrary Jones input; rotator/retarder modes; returns Stokes S0–S3, azimuth, ellipticity, Malus intensity, helicity phase, Fresnel diffraction |
| `alignmentHologram.m` | 138 | Blazed grating + optical **vortex** (charge ℓ, default 3) → first order is a doughnut ring with a dark null, cleanly separated from the zero-order ghost. Options: `Vortex`, `Lens`, `Crosshair`, `CrossWidth`, `Aperture`, `GratingNx/Ny` |
| `display.m` | 125 | Fullscreen Java hologram output keyed per monitor index (`slmFrameData(device)`); phase → gray scaling by `modMaxGray`; per-device temp BMP; **`cfg.invertPhase` global phase negation** (§6.4); embeds undersized holograms into a larger screen frame |
| `hologram.m` | 99 | Encode a complex field: `'phase'` (`mod(−∠U + G + A, 2π)`) or `'CAM'` complex-amplitude modulation (Bolduc *et al.* 2013, via `SincInv.mat`) |
| `gravityLens.m` | 99 | High-level pipeline: coordinates → field → grating → aberration → hologram → mask. Name-value `mode`/`ell`/`sigma`/`lensOffset`/`phaseModel`/`pwPhase`/`pwAmplitude` |
| `modMaxGray.m` | 94 | Wavelength → 2π gray level by PCHIP interpolation of a 16-point measured table; linear extrapolation with a warning outside 403–684 nm |
| `listScreens.m` | 88 | Enumerates Java `GraphicsEnvironment` monitors with true unscaled resolution; guesses which is which SLM by resolution |
| `laguerreGauss.m` | 86 | Complex Laguerre–Gaussian `LG_{p,ℓ}` mode field in physical units |
| `field.m` | 76 | Lensed complex field; three phase models: log (`n=1`), power-law (`n>1`), cotangent |
| `aberration.m` | 65 | 9-term Zernike aberration-correction phase map (Noll ordering) |
| `applyMask.m` | 56 | Circular aperture: inside kept, outside replaced with a **beam-dump grating** that steers stray light off-axis |
| `gratingAngle.m` | 47 | Grating specified by incident/diffracted **angles** (Hecht Eq. 10.61); errors out if the required groove pitch is sub-4-pixel |
| `coordinates.m` | 34 | Cartesian + cylindrical grids **in metres**, with pixel-offset origin shift |
| `close.m` | 34 | Release fullscreen device and dispose window |
| `grating.m` | 31 | Blazed grating from line counts |
| `ellipticalCoordinates.m` | 26 | Elliptical coordinates for asymmetric lenses |

**`+analysis/` — post-processing (838 lines)**

| File | Lines | Purpose |
|---|---|---|
| `phaseMap.m` | 501 | **Phase-shifting interferometry reconstruction + optical-vortex detection.** Single-bin temporal DFT per pixel recovers the complex field; net topological charge measured by loop integrals of phase winding; three independent local-core detectors (`circulation`, `zerocross`, `variance`); memory-safe incremental accumulation for 4096×3000 stacks |
| `imageAnalysis.m` | 217 | Merge two z-scan datasets, correct lateral drift interactively, track intensity vs. z at user-clicked points |
| `movie.m` | 120 | Compile a sorted PNG sequence into MP4 with optional parameter-value text overlay and cropping |

**`+camera/` (392 lines)** — `init` (loads all DLLs exclusively from `LibDLL/` by full path and
prepends it to `PATH`), `capture`, `setExposure`, `setGain`, `close`, and **`autoExpose` (185
lines)**: a two-stage controller that drives exposure by proportional control
(`newExp = oldExp × satLevel / peak`) to the saturation boundary, then falls back to a **binary
search on gain** only when exposure hits a limit, and issues a *specific* actionable warning
("add/remove ND filters") when the target is unreachable. "Peak" is defined as the value exceeded
by `satFrac` of pixels, making it robust to hot pixels.

**`+stage/` (101 lines)** — `init`, `moveTo` (blocking absolute move), `home`, `close`.

**`+sim/` (144 lines)** — full mirror of the camera/SLM/stage APIs for hardware-free development.

**Configuration** — `slm_config.m` (218 lines, device-dispatching, wavelength-aware),
`thorlab_hardware_config.m` (31 lines).

**`examples/` — 19 runnable scripts (2,469 lines)**, catalogued in §8.3.

### 4.3 The configuration system

`slm_config(device)` dispatches on `'hamamatsu'` / `'holoeye'`; a no-argument call still returns
the Hamamatsu config, so every pre-existing script kept working. What it auto-computes:

- **`cfg.modMaxGray`** — the gray level for 2π. Hamamatsu: PCHIP interpolation of the measured
  table. Holoeye: derived from the *flashed CLUT config* as
  `round(255 × (2/P) × (λ/λ_cfg))`, where `P` is the phase stroke printed in the config filename
  and `λ_cfg` its design wavelength. **This is the focal-plane knob** (§6.2).
- **`cfg.grating.nx/ny`** — reproduces the Hamamatsu *reference physical spatial frequency* on any
  device: `u_ref = n_ref/(N_ref × px_ref)`, then `n_dev = gainMult × orientMult × waveMult × u_ref × (N_dev × px_dev)`.
  Both SLMs therefore deflect to the **same focal-plane spot** despite different pitch;
  `waveMult = 632.8 nm / λ` preserves the diffraction angle at any wavelength. Verified:
  both devices give `|u| = [10500, 10000]` cycles/m.
- **`cfg.maskRadius_px`** — matched **in metres** across devices: Hamamatsu 214 px × 20 µm =
  Holoeye 535 px × 8 µm = **4.28 mm radius** on both.
- **`cfg.invertPhase`** — per-device CLUT polarity flag (§6.4).

---

## 5. Chronological development log

### Phase −1 — The measurement campaign that predates this repository (≈ 2025 → 2026-04)  **[ms] [account]**

*No commits. This is the work the manuscript reports; the repository begins after it, as the
software rebuild that the second SLM forced.*

**What the apparatus was.** [ms] A laser was coupled into a **single-mode fibre** (uniform
wavefront, and — critically — trivial re-alignment when swapping wavelengths), released by a fibre
collimator, expanded by lenses, steered by mirrors onto the **Hamamatsu LCOS-X10468** phase-only
SLM, and the phase-encoded light imaged onto the camera through a **4f lens pair**. All lenses
achromatic, because the campaign was multi-wavelength by design.

**What was scanned.** [ms]
- **14 wavelengths, 403–684 nm**: 403, 442 (Cd-Ne), 450, 473, 491, 515, 520, 532, 589/590, 633
  (He-Ne), 650, 672, 684 nm — a mix of diode, solid-state, and gas lasers. Most measurements at
  **633 nm**.
- **Effective optical Schwarzschild radius `r_S` = 0.2 – 20 µm**; recording distances **z = 10–30 cm**.
- **Binary separation `d` swept 0 → 4 mm** in **20 µm steps** (one SLM pixel — the pixelation sets
  the quantization), i.e. dimensionless **`d̂` = 0 – 4**.
- Dimensionless frequency **`w = 4π r_S/λ`** covering roughly **40 → 280** across the campaign.

**The craft that made it work — diffraction-order management.** [account] The genuinely difficult
part of SLM work here was not writing the phase; it was defeating the SLM's own pixel grid, which
acts as a 2-D diffraction grating and throws a cross of zero-, first-, second- and higher-order
copies into the output. The signal is the **first order**, so a blazed grating is added *in the
phase plane* to push it clear of the zero order and the artifact-carrying higher orders. That
design is a three-way trade-off with no manual value:
- grating **too dense** → the phase ramp is under-sampled by the pixel pitch and diffraction
  quality collapses (this constraint is now enforced in code — `optics.gratingAngle` errors out
  below a 4-pixel groove pitch);
- grating **too loose** → the orders do not separate and the signal sits on the zero-order ghost;
- **tilt angle too steep** → the deflected beam can no longer be brought back onto the optical axis
  downstream.

The working window was found empirically, by iteration and laser re-alignment. **Previous project
members had not been able to produce clean, usable images; this is the step that produced the
first ones**, and hence the data the manuscript reports.

**The alignment debugging arc (multi-wavelength scan).** [account] Before the takeover, recorded
patterns were consistently **deformed and asymmetric in both shape and intensity**. The diagnostic
chain:
1. Re-align the camera — cheapest hypothesis, and it did **not** fix it.
2. Strip the 4f lenses out of the path to remove them as a variable → revealed that **the laser was
   not aligned to the SLM's first order** in the first place.
3. **Invented a diagnostic that is still in use:** encode an **optical vortex** on the SLM. Its dark
   central null makes it immediately visible whether the beam passes through the *centre* of the
   alignment iris — a null is far more sensitive to judge than the centroid of a bright spot. The
   mirrors were then tuned against that criterion to align the 4f system. *This diagnostic was
   later productized as `optics.alignmentHologram` (grating + charge-3 vortex, §5 Phase 5) — the
   bench trick came first, the function came a year later.*
4. The residual **intensity asymmetry** turned out not to be alignment at all but **uneven source
   brightness (incoherent background) from the beam-splitter arm**; fixed by slightly repositioning
   the beam-splitter lenses.

**Self-initiated infrastructure built during this phase.** [account]
- **ThorLabs hardware automation from scratch** — MATLAB IO control of the **LTS300 translation
  stage** and the **CMOS camera**, including the communication layer that holds simultaneous
  contact with both instruments. **Now used lab-wide by other projects.** (This code is what
  Phase 0 inherited and modularized into `+camera/` and `+stage/`.)
- **Image-analysis routines** — alignment and comparison of sequential images across a scan
  (`analysis.imageAnalysis`).
- **A 1,000+ frame merger movie** assembling the scan into a frame-by-frame visualization of the
  diffraction pattern evolving as the two Schwarzschild lenses approach each other
  (`analysis.movie`).

Neither the image analysis nor the movie was assigned; both were built because they were better
ways to work with the data than the alternatives on offer.

**Phase-profile provenance.** [account] The phase-profile generator was not used as a black box:
the developer went back to the original **Einstein-beam paper** to work out how the phase encoding
is derived, then extended the existing code to single- and binary-Schwarzschild profiles. The
generator can be reconstructed from first principles — which is precisely what `optics.field` +
`optics.gravityLens` + `optics.stationaryLens` in this repository are.

### Phase 0 — Inheritance and restructure (2026-04-27)

*Commits `9d66703` Initial commit, `335cdf7` ThorCam, `3df59b5` CamDepend, `ad6dcb4` Reconstructed,
`d45a3fb`, `c782cec` Integrate SLM and Optics Folder*

**Starting state:** flat scripts, no structure, 37 DLLs in the repository root.

**Work done:**
- Complete modularization. Every flat script was mapped to a package function:
  `captureColorImage.m` → `+camera/`; `moveLTS300.m` → `+stage/`; `DisplayonSLM.m` → `+slm/`
  (later folded into `+optics/`); `CoordinateDef.m` / `EllipticalCoordinateDef.m` →
  `optics.coordinates` / `optics.ellipticalCoordinates`; `FieldGenerator.m` +
  `EinsteinRingEllipse.m` → `optics.field`; `MakeGrating.m` / `MakeGratingAngle.m` →
  `optics.grating` / `optics.gratingAngle`; `MakeAberrationCorrection.m` → `optics.aberration`;
  `MakeHologram.m` → `optics.hologram`; `gravitylensbinary.m` + `gravitylensellipticalkg24.m` →
  `optics.gravityLens`; `CombinedImageAnalysis.m` → `analysis.imageAnalysis`;
  `MovieGeneration.m` → `analysis.movie`. Legacy per-date capture scripts (`Kiko*.m`,
  `parabolicbeamquartic.m`, `ColorProcessing.m`) became `examples/`.
- **Solved: DLL root-corruption hazard.** Root cause: `captureColorImage.m` loaded DLLs from its
  own directory — the repository root — which held 37 DLL copies that could be corrupted by a
  crash mid-load. Fix: all DLLs consolidated into `LibDLL/`, `*.dll` added to `.gitignore` so
  copies can never be re-introduced at root, and `+camera/init.m` rewritten to load **exclusively**
  from `LibDLL/` by full path while prepending that directory to `PATH` so native dependencies
  resolve.
- Dropped `wave_packet_evolution.m` (incomplete, syntax errors) rather than carry dead code.
- Removed all `assignin('base', ...)` side effects from the original `FieldGenerator.m`.
- Wrote `docs/README.md` (589 lines at creation) — full function reference, calibration tables,
  hardware setup, troubleshooting.
- Merged `+slm/` into `+optics/` so all optical output lives in one namespace; renamed
  `hardware_config.m` → `thorlab_hardware_config.m` to make the vendor scope explicit.

### Phase 1 — Automation and the interference scan (2026-04-30 → 2026-06-24)

*Commits `1113602`, `8c63989`, `e44fa05`, `78910a6` Interference Scan, `60013ba` movie,
`f33e127` 3 Features Updated, `b5550a4`, `4a7023a`, `0a2db5b`*

- Built `examples/gravity_lens_scan.m`: sweep `r_s`, display hologram, capture frame, save PNG,
  with optional stage control.
- Built `examples/interference_scan.m`: the **phase-shifting interferometry acquisition**. A fixed
  binary-lens hologram is interfered against a reference plane wave whose phase `pwPhase` is
  stepped over a full 0 → 2π cycle, one frame per step. This is the measurement that gives access
  to **both** phase and intensity of the lensed field.
- Added `pwPhase` / `pwAmplitude` to `optics.gravityLens` to support the above.

  **The idea worth naming: a virtual interferometer encoded inside the SLM.** The reference arm is
  not a second physical path. It is added *in the encoded field* —
  `ER = ER₁·ER₂ + pwAmplitude·exp(i·pwPhase)` (`+optics/gravityLens.m:87`) — so a single
  common-path hologram carries both the lensed wave and its reference, and the phase step is a
  number in a loop rather than a mirror on a piezo. Consequences, all of which matter for the
  reconstruction in Phase 2:
  - **No moving parts** → no mechanical drift between frames of a 73-frame stack;
  - **the phase step is exact by construction**, not calibrated;
  - the two "arms" share every optic downstream, so common-mode aberration and air-path phase
    cancel;
  - arm balance is a scalar (`pwAmplitude`), so fringe visibility is tunable in software.

  This is the "**virtual Mach–Zehnder written into the SLM**" that made phase-resolved analysis of
  the lensed field possible at all — the wavefront's *phase* structure, not just its intensity,
  becomes measurable with no additional hardware. It is the direct enabler of `analysis.phaseMap`
  (Phase 2), of the measured phase maps on the poster, and of the optical-vortex/OAM detection that
  bridges this project toward structured-light work.
- `examples/test_gravityLens.m`: a **12-check automated test suite** over the whole name-value
  interface, output range, mode switching, and error handling.
- Built `analysis.movie` and `ebin0626/make_movie.m`; produced `ebin0626.mp4` from the scan.
- **Fixed a units bug in `lensOffset`** (`e44fa05`, "Metric of LensOffset Updated") — the first of
  two encounters with this class of error (§6.5).
- Cleaned stale `.asv` autosave files out of version control.

**Three features requested and delivered 2026-06-24** (session `36f378da`):
1. **`camera.autoExpose`** — the requirement evolved live across three user messages, from "auto
   exposure and gain" to "must not saturate" to "and be as bright as possible" — settling on
   *"the final output should be just at the boundary of saturation and not saturation."* The
   implementation (exposure by proportional control first, gain by binary search only if exposure
   saturates its range, actionable warning otherwise) reflects exactly that spec.
2. **`optics.applyMask`** — extracted from `gravityLens`'s inline code into a standalone reusable
   function, because the gravitational-lensing configuration needs the grating to deflect **only**
   a central disk (initially 290 px radius), with a beam-dump grating outside. `gravityLens` now
   delegates to it; the mask was also applied to `interference_scan`.
3. **Wavelength-aware calibration** — `optics.modMaxGray(λ)` plus grating auto-scaling by
   `mult = 632.8 nm / λ`, so switching lasers requires editing **one line** (`cfg.lambda`) instead
   of a manual table lookup and several edits.

### Phase 2 — Field reconstruction and vortex detection (2026-06-23 → 2026-06-29)

*Commit `ac0d098` Vortices*

- Acquired the **`ebin0626` dataset**: **73 interferograms at 4096 × 3000 px** (~12 MB each,
  ~880 MB total) plus a compiled movie — one full phase-shifting cycle against a binary
  gravity-lens hologram.
- Wrote **`+analysis/phaseMap.m` (501 lines)** to invert it. Method: each camera pixel sees a
  temporal sinusoid `I_n = a + b·cos(ψ + φ_n)` as the reference phase is stepped; a **single-bin
  temporal DFT over frame index** recovers `U = (b/2)e^{iψ}`, so `angle(U)` is the phase map and
  `|U|` the modulation magnitude.
- **Robustness engineering that mattered:**
  - The **net** topological charge (beam OAM ℓ) is measured by integrating phase winding around
    **circles in the high-contrast fringe zone**, not by counting cores — this tolerates an
    over-exposed/saturated beam core and cancels noise-generated vortex pairs, which always come
    in ± pairs and vanish around any enclosing loop.
  - Because phase stepping is discrete, the winding integral lands slightly short of a full turn,
    so the vortex decision uses the **continuous** winding with a tolerance (`chargeTol = 0.3`
    turn) rather than a brittle exact-integer test.
  - **Three independent local-core detectors** so results can be cross-checked:
    `circulation` (2×2 plaquette loop integrals — topologically exact but noisy in dense fringes),
    `zerocross` (simultaneous zeros of Re *U* and Im *U*, sign from the field Jacobian — clean),
    `variance` (circular phase-variance blobs gated by non-zero circulation — robust candidate
    finder that rejects vortex-free dense fringes).
  - **Never holds the full stack in RAM**: crops, downsamples, and accumulates incrementally, with
    auto-detection of the modulation DFT bin from a coarse low-resolution pass.
- `examples/vortex_analysis.m` as the ready-to-run wrapper.

### Phase 3 — Stationary-phase minimal-pixel encoding (2026-06-29 → 2026-06-30)

*Commits `655417d`, `7695278`, PR #1 `c658657`, `889eedf`, `b1ed857`, `57a2dc6`, `da95eba`,
`5d56565`, `7df9190`, `7f39fc0` Stationary v2, `7d91659`, `b54f028`, `f19646f`, `fa55833`*
*(sessions `c7d05d54`, `bd49cd92`)*

Built `+optics/stationaryLens.m` from the paper's geometric-optics section — the only feature
developed on a **feature branch and merged by pull request**.

**Iteration 1 (2026-06-29).** The task was: *tune `stationary_phase_lens.m` so it encodes the same
hologram as `gravityLens` with `rs = 3.3e-6`, `lensOffset = 70`, defaults elsewhere.* Two
substantive physics questions came out of it:
- *"the image by the stationary phase focuses too close compared to the gravLens images, help me
  explain why"* → traced to the phase-depth/effective-`rs` relationship rather than a coding error.
- *"how do I tune pixel-per-unit and what does it exactly do?"* → exposed the real bug, below.
- A **4-panel phase comparison** was added to the example (stationary with mask / without mask /
  full `gravityLens` at matched parameters) as a permanent A/B diagnostic.

**Iteration 2 (2026-06-30, `stationary_phase_lens_v2.m` + rewritten solver).** Stated goal:
*"create the caustic stated in the paper with minimal pixels"*, and *"the core issue right now is
that pixel-per-unit is influencing the solution to the stationary points."*

**Solved — physics/display coupling.** The stationary points `x_j` are solvable **analytically in
dimensionless units** from `(β, ySource)` alone, so they are *pixPerUnit-independent* by
construction. But the old example tied `beta = 70/pixPerUnit` (a merge-conflict artifact), which
silently changed `d̂ = 2β` and therefore the whole caustic whenever the display resolution changed.
Fix: `beta` (`= d̂/2`) is now set **directly** as physics, and `pixPerUnit` is a **pure display
knob**. Two independent "minimal-pixel" controls were then added:
- **`autoPixPerUnit`** — picks the smallest resolution that Nyquist-samples the displayed phase,
  sizing from the **image neighbourhoods** (radius ≈ 0.25 u) with a 0.08 u guard around the mass
  singularities and a 99.5-percentile cut computed **toolbox-free** (no `prctile` dependency).
  The log singularities at the masses are deliberately left under-resolved — unavoidable on a
  pixelated SLM and negligible in the far field. For `d̂ = 1.2`, `r_S = 7 µm` this gives
  `ppu ≈ 102` at `w = 2 k r_S ≈ 139`.
- **`coreRadiusUnits`** — kept-disk radius in Einstein radii.

**The scientifically interesting negative result.** The GO/stationary-phase sum **breaks down at
caustic scales** — the paper's own caveat. Small disks around isolated images therefore do **not**
reproduce the caustic; the disks must cover the **critical-curve merge regions**. Quantified by
far-field correlation against the full lens (`d̂ = 1.2`, `y = 0`) — see §7.2. Default set to
`coreRadiusUnits = 0.8`.

- Also built `examples/phase_plane_critical_points.m`: filled contours of the Fermat potential,
  critical points classified by Morse index (minimum = green circle, saddle = yellow square,
  maximum = red triangle), the critical curves `det K̂ = 0`, and their image in the source plane —
  the caustic.
- Process note: when the first attempt modified `stationaryLens.m` in place, the change was
  **reverted and moved into a new v2 file** on request, preserving a working version — good
  practice under active experimental use.

### Phase 4 — BNS P512 hardware archaeology (2026-06-30)

*Session `accc677c` — no commit; investigative*

Attempt to revive a **2009-vintage Boulder Nonlinear Systems P512** SLM: DVI-D→HDMI to the laptop,
USB 2.0 controller attached. Work done: decoded the raw **EDID** to confirm identity
(`"BNS PD 512"`, serial `BNSPD051216 0`, week 20 / 2009) and extract every supported video timing;
established that Windows PnP saw *"Generic Monitor (BNS PD 512)" — Status OK* but that it was not
configured as an active extended display; confirmed **no BNS USB SDK/DLL existed on the system**
(only Thorlabs DLLs), so only video-only operation was possible; provisionally reconfigured
`slm_config.m` to 512×512 / 15 µm / `maskRadius_px = 248` and wrote a 6-pattern revival test
script.

**Lasting contribution:** to support a panel smaller than its own video frame, `+optics/display.m`
was changed to **embed an undersized hologram into the screen frame (top-left, zero-padded)**
instead of erroring on a size mismatch. That generalization is still in the code and is what makes
the display path device-agnostic.

**Outcome — honest:** the device did **not** modulate. The user reported *"nothing changed, checked
for polarizations, nothing changed."* The panel was not adopted; effort moved to the Holoeye
PLUTO-2.1 two days later. The EDID/timing/SDK findings are preserved so the decision is
reproducible rather than folkloric.

### Phase 5 — Dual-SLM support (2026-07-02 → 2026-07-07)

*Commits `092cd80` Holoeye-Supported, `355cf28`, `3c0c741` LG Beams* *(session `2684f40e`)*

**Goal:** drive the Holoeye PLUTO-2.1 **and** the Hamamatsu simultaneously, and build an
easy-to-align hologram.

- Rewrote `slm_config.m` as a **device-dispatching function** with `cfg.name` and
  `cfg.modMaxGraySource`, keeping the no-argument call backward compatible.
- Read the PLUTO-2.1 manual (via `pdftotext` — image-rendering the PDF did not work) to confirm
  1920×1080 / 8 µm / phase-only / extended-monitor addressing / green channel carries the 8-bit
  gray level. Established that the gray→phase LUT lives in the `.hec` config flashed over USB by
  the HOLOEYE Configuration Manager and is **not** controllable from MATLAB — a constraint that
  shaped everything downstream.
- **Fixed a latent multi-device bug:** the temporary bitmap used by `optics.display` was a single
  shared filename, so two simultaneous SLM frames clobbered each other. Now per-device
  (`slm_display_%d.bmp`). `optics.display` already keyed windows by monitor index
  (`slmFrameData(device_number)`), so two calls with distinct `cfg.slmScreen` now light both panels
  independently.
- **New `optics.listScreens()`** — enumerates Java `GraphicsEnvironment` monitors with true
  *unscaled* resolution and guesses which SLM is which by resolution. This became the standard
  first step of every bench session.
- **New `optics.alignmentHologram()`** — the alignment strategy went through a design iteration.
  A plain blazed grating gives a first-order **spot**, which is hard to judge. On request, it
  became a grating **+ optical vortex** (spiral phase `ℓ·φ`, matching HOLOEYE's own
  `heds_show_phasefunction_vortex = charge·atan2(y,x)` convention), so the first order forms a
  **doughnut ring with a dark null**, cleanly separated from the zero-order ghost. Alignment then
  becomes "make the ring smooth, round, centred, with a clean dark centre" — a far more sensitive
  criterion. Verified numerically: **winding number = 3.000** on a loop integral, and the FFT
  far-field first order is a ring with centre null ≈ 0.007 and peak at r ≈ 3 px at the grating
  offset. Also fixed on request: everything outside the circular mask is set to phase 0, and the
  aperture was enlarged.
- `examples/align_slms.m` — the working driver: build both configs, print `listScreens`, encode
  both, display simultaneously, close on keypress.
- **Solved: the mixed-DPI "hologram only occupies the corner" bug** — the hardest
  environment-level problem of the project (full case study in §6.1).
- Added `+optics/laguerreGauss.m` and `examples/dual_slm_lg_split_mask.m` — split one circular
  aperture across **two** SLMs (left half on one panel, right half on the other) driven with the
  same physical LG mode, using **CAM complex-amplitude encoding** because an LG mode carries both
  amplitude and phase.

### Phase 6 — Cross-SLM physical matching (2026-07-09 → 2026-07-10)

*Commits `c891f60` Grating, `f35c919` SLMpixelSizeUpdate, `0359267`, `9f1a8e9` Holoeye,
`bd7d6fe` holoeye2.0* *(session `c0f24fce`)*

**Requirement:** both SLMs must produce the **same beam size, same pattern, and the same focal
plane**, using Hamamatsu pixels as the reference, given the bench layout
`SLM1 ─50─ L1 ─50─ iris ─20─ mirror ─30─ L2 ─50─ SLM2`.

- **Established the key structural result:** because all physics is generated in metres, the
  **wavefront is inherently size-matched** regardless of pixel pitch or resolution. Verified
  quantitatively: single-lens, binary, OAM, and power-law fronts agree to **≤ 9° RMS phase**
  when resampled onto a common micrometre grid — and that residual is pure resampling error.
- **Aperture matched in metres:** Hamamatsu `maskRadius_px` changed 298 → **214** so that
  214 × 20 µm = 535 × 8 µm = **4.28 mm** on both.
- **Grating rewritten** to reproduce the reference *physical* spatial frequency on each device
  (§4.3), giving identical `|u| = [10500, 10000]` cycles/m and therefore the same diffraction
  angle and the same focal spot.
- **`examples/compare_slm_holograms.m` (175 lines)** — builds every beam front for both configs,
  resamples onto one micrometre grid, reports RMS phase difference, and plots on µm axes so sizes
  are comparable by eye. All checks pass.
- Simplified `align_slms.m`'s wavelength refresh to rescale the **device-correct** grating from
  `slm_config` by `λ_ref/λ`, instead of re-deriving the raw −140/100 reference counts (which
  ignored both geometry and orientation).
- **Then the big one:** with geometry provably matched, the Holoeye still focused the Einstein ring
  **one focal length early (3f instead of 4f)**. Full case study in §6.2 — the answer was **phase
  depth, not pixel pitch**, and the fix required reading the HOLOEYE Configuration Manager manual
  to derive the `modMaxGray` formula from first principles.
- Built **`examples/holoeye_focus_scan.m`** — sweeps `modMaxGray` (255 : −10 : 140) on a fixed
  gravity-lens ring hologram, capturing a frame per value, to lock the value in **on the bench**
  rather than by argument. Direction rule written into the header: *ring too close → lower
  `modMaxGray`; too far → raise it (cap 255).*

### Phase 7 — Bessel/defocus diagnosis and the phase-inversion root cause (2026-07-13)

*Commits `ffcb7d0` "Holo flipped"* *(sessions `9a510783`, and `c0f24fce` tail)*

The single most instructive debugging day of the project — three nested misdiagnoses ending in a
one-line root cause. Full narrative in §6.3 and §6.4. Artifacts:

- **`examples/bessel_ring_test.m`** — a Durnin-ring Bessel generator + 4f alignment check, with the
  measured `defocusF = −0.80 m` correction as a top-level parameter and the reasoning documented in
  the header.
- **`bessel_ring_capture.png`** (14 MB) — the captured **J0 Bessel** with evenly spaced dark rings
  at 15, 34, 53, 72 px from centre (Δ ≈ 19 px), committed as evidence.
- **`cfg.invertPhase`** in `slm_config` + `optics.display` — the actual root-cause fix.
- Scratch diagnostic scripts written and run through the MATLAB MCP bridge during the session:
  `bessel_diag.m`, `ring_sim.m`, `focus_check.m`, `lens_sweep.m`, `lens_refine.m`, `ring_focused.m`,
  `sign_test.m`.
- A process gotcha found and documented: capture **scripts** run via the MATLAB bridge leave `cam`
  and `cleanup` in the base workspace and their `onCleanup` never fires, so the next `camera.init`
  throws *"TLCameraSDK is already open."* Fix: `camera.close(cam); clear all`, or make capture
  routines **functions** so `onCleanup` fires on return.
- `examples/gravity_lens.m` gained a **metric** `lensSep_m = 1.4e-3` with
  `lensOffset = round(lensSep_m / pixelSize)` → 175 px on the Holoeye (§6.5).

### Phase 8 — Poster: theory, simulation, and measurement in one place (2026-07-15)

*Session `3de7de85` — the largest working session of the project (26 MB transcript)*

Restructured `Lab_GravLensing_Poster_Ver_01` into a **3-column, 35 × 43 in portrait beamerposter**
(XeLaTeX + a Colgate theme), and — more importantly — generated the simulation figures to fill it.
Detail in §9.

**`scratchpad/make_poster_caustics.m`** was written to produce three figures from the real code
path with no hardware touched, at `d̂ = 1.09`, `r_S = 3.3 µm`, `y = 0`, `z = 0.50 m`,
`coreRadiusUnits = 0.80`:
1. `Tfunction_map.png` — the time-delay function `T_grav` over the lens plane on a 900×900
   dimensionless grid, with contours and the two masses marked, over ±1.7 Einstein radii.
2. `Caustic_full.png` — far-field `|F(y)|²` from the **full** lens, via
   `F ~ FFT_x[exp(i(½ w|x|² + φ_SLM))]` with `w = 2 k r_S` (the quadratic term is the
   Fourier-lens/defocus), γ-compressed at 0.4 for display.
3. `Caustic_masked.png` — the same from the **stationary-phase mask**, plus `Stationary_mask.png`
   showing the kept disks themselves.

Quantitative output of that run: `pixPerUnit = 128.5`, **5 images**, Einstein radius
`R_E = 2.569 mm`, and two mask variants — **82.4 %** of aperture pixels → correlation **0.850**
with the full-lens caustic, and **51.4 %** → **0.679**. The poster reports the 51 % / 5-disk
version, i.e. the honest claim *"reproduces the caustic backbone with roughly half the pixels."*

Also in this session: corrected physics errors in the poster against the source paper, added the
governing equations (Fresnel–Kirchhoff integral, Fermat function, symmetric-binary `T_grav`, the
boxed SLM encoding `φ_SLM = −2 k r_S T_grav`, the GO sum with magnification and Morse index), and
made the LaTeX project **reliably compilable from VS Code** — which required forcing XeLaTeX via
`.latexmkrc` and `.vscode/` settings because the theme loads `fontspec`. That last point took six
repeated requests to fully satisfy, which is recorded here plainly.

### Phase 9 — Polarization / WRA simulation (2026-07-21 → 2026-07-22)

*Commits `998370c` Tunned, `bb8996b` WRA* *(session `c70e55e3`)*

Built `examples/polarization_wra_dual_slm.m` (542 lines) for the
**SLM1(H) → 4f → SLM2(V) → 4f** setup with +45° input, tying the two papers together: the BML
potential `Φ = −2 k r_S T_grav`, `T_grav = −Σ mᵢ log|x − xᵢ|`, drives a spatially varying
**polarization-rotation field `θ(x,y)`** — a "lensing WRA map".

Physics results established (all verified in MATLAB to ~1e-14):
- A phase-only LCOS modulates only its own linear component: `SLM1 = diag(e^{iφ_H}, 1)`,
  `SLM2 = diag(1, e^{iφ_V})`. Setting `φ_H = +θ`, `φ_V = −θ` gives differential `δ = 2θ`.
- **Rotator mode** (the Miller-faithful configuration): the H/V SLM pair sandwiched between **two
  QWPs both at +45°** is a pure polarization rotator — output azimuth `= 45° + θ`, ellipticity 0.
  (QWP+45 … QWP−45 also rotates, but by `−θ`; both-at-+45 gives `+θ`.)
- **Retarder mode** (bare SLMs, no QWPs): azimuth stays at 45°, **ellipticity = θ** — circular at
  θ = 45°.
- A **non-obvious quirk** worth recording: for a +45° input, **QWP1 @ +45° is a no-op**, because
  +45° is its fast-axis eigenstate. The rotation physically happens as SLMs (→ elliptical) then
  QWP2 (→ rotated linear).

**Answering *"why is there only H/V polarization when the paper is mostly about L/R?"*** — this
produced one of the clearest conceptual results of the project. H/V is the **hardware** basis (an
LCOS modulates a linear axis); the QWP sandwich **is** the H/V ↔ L/R (helicity) transform. In
rotator mode `|L| = |R|` remain equal and the WRA appears entirely as the **L/R relative phase
= 2θ** — exactly Miller's *"helicity state WRA = phase shift χ."* And since the L/R relative phase
equals −2 × (ellipse azimuth), **the quantum (helicity phase) and classical (azimuth rotation)
faces of the WRA are literally the same number.**

Also added on request: `polarizationStagesFigure` / `jonesStages`, drawing the polarization-ellipse
map at **every element** (Input / After QWP1 / After SLMs / After QWP2 = output), with ellipse
colouring green = linear (`|χ| < 0.5°`, chosen to avoid ±0 S₃ sign noise), blue = RH, red = LH.

Sign convention pinned down and documented: `optics.hologram` (phase-only) displays `−∠U`, so one
must pass `U = exp(−i·φ_intended)` to imprint `+φ`.

### Phase 10 — Full-GR WRA modules (2026-07-29)

*Commit `4073184` WRA* *(session `7328e276`)*

The final and most theory-heavy phase: replace the heuristic rotation field
`ψ = −Σ mᵢ log rᵢ` with a **genuine general-relativistic calculation**. Given a choice between a
paraxial approximation and the full tetrad pipeline, the full pipeline was chosen.

**`+optics/wignerRotation.m` (445 lines)** — equatorial **Kerr** null geodesic (M = 1) →
analytically constructed static-observer orthonormal tetrad → local Lorentz generators
`Ω_ab = g(e_a, D e_b/dλ)` with Christoffels by finite-differencing the analytic metric →
Miller Eq. 4 single-path WRA `χ` and Eq. 9/11 relative WRA `Δχ` including the `1/(1 − n₃²)`
non-reciprocity. Parameters: `mode` (binary/single), `a` (Kerr spin a/M), `r0` (= 9 = 4.5 r_s),
`bMax` (= 8), `sepFrac`, `massRatio`, and `quant.axisAngleDeg` (polarizer tilt from the orbit
normal; 0 = normal, 90 = ∥ momentum → trivial). Returns `theta`, `thetaReverse`, `deltaTheta`,
the 1-D curves `b1d`/`chi1d`/`dchi1d`, and a `checks` struct. Runtime ≈ 28 s on 800×600 at
`nB = 201`, `nR = 1500`; convergence checked at `nR = 4000` (difference 5e-5).

**Bug found and fixed during construction:** the azimuthal tetrad leg norm is
`B = sqrt(gtt/(gtt·gpp − gtp²))` — both numerator and denominator negative, so the result is real —
**not** `sqrt(−gtt/(…))`. `Ω` is also explicitly antisymmetrized to kill finite-difference residue.

**Physical-scale mode** (`opts.scale = 'physical'` + `lens.rs`) maps the SLM plane to the **true**
gravitational impact parameter `b = 2ρ/r_s`. Two subtleties had to be handled: it uses a
**scattering** geodesic (launched just outside periapsis, ×2 for the symmetric legs), and it
**subtracts the flat-space M = 0 frame sweep** — without that subtraction the polar-coordinate
frame rotation contributes a spurious ≈ 172° instead of the real WRA. Metric primitives were
generalized to take mass `M` so that `M = 0` provides the flat reference. Verified: `r_s = 3.3 µm`
single lens → `|θ| ~ 0.01°`, `|Δθ| ~ 0.065°` (same order as the deflection `4M/b = 0.088°`),
scaling ∝ `r_s`; binary at `r_s = 3.3 µm` → `|θ| ~ 0.13°`, `|Δθ| ~ 0.73°`.

**`+optics/applyWRA.m` (203 lines)** — acts the map on input light (§2.3), returning
`Ex, Ey, S0–S3, azimuth, ellipticity, malus, phaseEig, diffraction`.

**Deliverables of this phase:**
- `examples/wigner_rotation_lensing.m` — 3 figures: axis-sweep + Kerr 1-D curves (reproducing the
  character of Miller Fig. 1F/1G); binary `θ` / `θ_reverse` / `Δθ` maps; D-input Malus dark field +
  R/L diffraction.
- `examples/caustic_polarization_z500.m` — the flagship simulation: binary lens `r_s = 3.3 µm`,
  offset 70 px (`d = 2.8 mm`), single-FFT Fresnel propagation to **z = 500 mm**, producing a
  caustic (`d̂ = 1.54`, `w = 65.5`) that **carries a θ polarization texture**; the SLM imprints
  common `Φ(caustic)` + differential `θ(WRA)`; D input; analyzer and azimuth readouts with overlay;
  reports the true physical WRA alongside.
- `examples/dual_slm_phase_maps.m` — builds `HoloH` (SLM1 = Holoeye, H, `Φ + θ`) and `HoloV`
  (SLM2 = Hamamatsu, V, `Φ − θ`) through the **real** encode pipeline (grating + aberration +
  applyMask), with a 2 × 3 phase-map figure and a MATLAB-drawn bench sketch. Both panels use
  **one shared `χ(b)` curve × one global scale**, so `+θ` and `−θ` are guaranteed to be the
  identical field — an important correctness detail for a differential measurement.
- `docs/WRA_bench_setup.md` (248 lines) — a complete build tutorial: beam path diagram, component
  table with settings, the two operating modes and their sign conventions, how to prepare each of
  the six input states, readout strategies (Malus null / interferometric fringe shift / six-shot
  Stokes polarimetry), an 8-step alignment procedure, honest expected magnitudes, and a
  code cross-reference table.
- `docs/figures/WRABenchSetupSketch.png`, `docs/figures/Dual_SLMPhaseMaps.png`.
- `examples/polarization_wra_dual_slm.m` retrofitted: `wraRotationField` now calls
  `optics.wignerRotation` (cached 1-D curve) instead of the old heuristic; the rotator identity
  check still passes at 2.5e-14.

---

## 6. Debugging case studies (the hard problems)

These five are written out in full because the diagnostic reasoning — not the final patch — is the
substance.

### 6.1 The mixed-DPI "hologram only occupies the corner" bug

**Symptom.** Running `examples/align_slms.m` interactively, the hologram appeared shrunk into the
corner of the Hamamatsu panel. But when the same code was driven programmatically through the
MATLAB bridge during debugging, it was **correct**. The user's report captured the frustration
exactly: *"it's been weird — when you try to debug it it's all right, but when I run from
align_slms.m to align the Hamamatsu, it only takes the corner."*

**Diagnosis.** This laptop runs the **primary display at 125 % Windows scaling** while the SLM
monitors run at 100 %. Verified directly: DPI-unaware processes see the primary as 1536×960 while
Java reports the physical 1920×1200 (exactly 1.25×); the SLM reads 800×600 either way. With a plain
windowed `JFrame`, Windows **DPI-virtualizes** the window and shrinks it. The behaviour is
*state- and DPI-awareness-dependent*, which is precisely why it reproduced from an interactive
session but not from the bridge — that JVM saw physical pixels. This is the kind of bug that looks
like flakiness and is usually blamed on the hardware.

**Fix.** `optics.display` / `slm_fullscreen` were moved to **fullscreen EXCLUSIVE mode**
(`dev.setFullScreenWindow(frame)`), which owns the physical panel at true resolution and bypasses
DPI virtualization entirely, guarded so that frame reuse only does `icon.setImage` + `repaint`, and
falling back to explicit fullscreen `setBounds` when `isFullScreenSupported()` is false.
`optics.close` calls `dev.setFullScreenWindow([])` before `dispose()` to release the device. An
earlier interim fix (`pack()` → `setBounds`) was necessary but **insufficient** — recorded so it
isn't retried.

**Verification.** `java.awt.Robot` screen-capture of monitor 2 confirmed the image fills the full
panel, that frame reuse updates in place, and that closing restores the desktop. Also noted: a
circular aperture on an 800×600 landscape panel necessarily leaves flat left/right bars — pass
`'Aperture', false` to `alignmentHologram` to fill edge-to-edge (confirmed rows 1..600,
cols 1..800).

**Honest follow-up recorded in the log:** the `setFullScreenWindow` fix was later found **not** to
be present in the committed `+optics/display.m` (`git log -S setFullScreenWindow` shows it was never
committed). It is flagged as a real outstanding regression (§10) — though it was correctly ruled
out as a cause of the 3f-ring bug, since window management cannot move a lens's focal plane.

### 6.2 "The Holoeye focuses the Einstein ring at 3f instead of 4f"

**Symptom.** After geometry, aperture, and grating were provably matched between the two SLMs, the
Holoeye *still* formed the gravity-lens Einstein ring **one focal length early** in the
`SLM1─50─L1─50─iris─50─L2─50─SLM2` relay. The natural suspicion — pixel pitch — had already been
eliminated.

**Diagnosis, done numerically before touching the bench.** For the log lens
`φ = −2 k r_S ln(ρ/σ)`, the ray-crossing (caustic) distance is `z(ρ) = ρ/|θ|` with
`θ = (1/k) dφ/dρ = −2 r_S/ρ`. Evaluating this for both devices with the **same physical φ**:
Hamamatsu at 20 µm and Holoeye at 8 µm both give `z = 0.2857 m` at `ρ = 2 mm`, `r_S = 7 µm`. So the
caustic distance is **pixel-pitch invariant** — pitch genuinely cannot be the cause. But
over-modulating φ by 255/190 moved `z` to `0.2129 m` — a ratio of **0.745 ≈ 190/255 ≈ 3f/4f**.
That is the observed error, exactly. **The caustic distance scales as 1/(phase depth).**

Mechanism: `optics.display` sends `gray = φ/(2π) × modMaxGray`, so the panel's actual phase is
`φ × (modMaxGray / gray_2π)`. `slm_config` had **hard-coded Holoeye `modMaxGray = 255`**, assuming a
perfect 2π-at-λ config was flashed. If a config with a different stroke or a different design
wavelength is loaded, 255 **over-modulates**, the lens is too strong, and the ring forms early.

**Getting the authoritative calibration.** Rather than fit the number, the HOLOEYE Configuration
Manager manual was read (again via `pdftotext`) and the formula derived from the physics:
1. The flashed CLUT is **phase-linear over gray**: gray 0..255 → phase 0..(P·π) at the config's
   design wavelength `λ_cfg`, where `P` is the stroke printed in the filename.
2. LC retardance (OPD) is approximately fixed, so phase ∝ 1/λ: at the actual laser wavelength the
   stroke becomes `P·(λ_cfg/λ)·π`.

Hence **`modMaxGray = round(255 × (2/P) × (λ/λ_cfg))`**, reducing to `255 × 2/P` when the config
matches the laser. `slm_config`'s Holoeye branch was rewritten to be wavelength-aware, exposing
`holoConfigPi` and `holoConfigLambda` and clamping to 1..255.

**Also corrected during this investigation:**
- The unit was confirmed to be a **PLUTO-2.1 NIR-145** (matching
  `Wavefront_Correction_Function/U.14-…-2304.h5`) — earlier notes had said VIS-016, which was
  **wrong**.
- `Holoeye/Configs_PLUTO-2.1/NIR 145/` was inventoried: 450/520/635/800/1070 nm configs,
  **2π-family only** (2.00/2.10/2.20/2.23 π → 255/243/232/228 when matched) and **no 4π config** —
  which **killed the earlier "4π over-modulation" hypothesis** outright. Within-band mismatch caps
  at ~10 %.
- **Most likely real cause therefore: a wavelength mismatch.** An 800 nm config used at 635 nm
  over-modulates by 1.26× → `modMaxGray ≈ 202` → ring at ≈ 3f. A 1064 nm config at 635 nm would
  give ≈ 2.4f.
- Clarified that the per-unit `.h5` file is a **separate wavefront-flatness calibration** (an
  additive phase map), *not* a `modMaxGray` source.

**Best fix (documented) vs. workaround (built):** flash the NIR-145 config whose wavelength matches
the laser, then `modMaxGray = 255`. Until then, `examples/holoeye_focus_scan.m` sweeps the value on
the bench with the camera fixed at the plane where the Hamamatsu gives a sharp ring.

### 6.3 "The SLM won't show a Bessel beam" — a chain of three misdiagnoses

**Reported symptom (2026-07-13).** With the camera at the 4f system's 1f plane, the pattern should
be concentric circles (a Bessel beam); instead a single ring appeared at the Fourier plane, and
something Bessel-like appeared only ~1 cm from the SLM plane.

**First finding — the SLM was healthy, and the premise was wrong.** `slm_config('holoeye')` gave
`modMaxGray = 254` for the 635 nm 2.0π NIR-145 config at 632.8 nm — essentially perfect 2π, no
over-modulation — so the §6.2 hypothesis did **not** apply on this bench. More importantly, the
displayed pattern was `examples/gravity_lens.m`: a **binary twin log-axicon** (`rs = 3.3 µm`,
offset 70 px) — an Einstein-ring lensing demo, **not a Bessel generator**. Simulation
(`bessel_diag.m`, `ring_sim.m`) confirmed the log-axicon caustic is **chirped**,
`z(ρ) = ρ²/(2 r_s,eff)`, spreading the "Bessel" over z ≈ 1 cm … 136 cm — dim and non-uniform. Wrong
tool for a clean Bessel. A **linear** axicon (`φ = −kαρ`) gives a uniform Bessel over `[0, R/α]`;
a **ring/annulus** on the SLM gives a J0 Bessel at the **lens focal plane** (Durnin) — which is
what actually puts concentric circles on a camera at that plane.

**Second finding — the camera was not where everyone assumed.** Displaying a *plain deflected spot*
(flat phase + grating, full aperture) should give a ~50 µm point at the Fourier plane. It gave a
**~5 mm disk full of concentric Fresnel aperture rings**, plus two fainter copies (other
diffraction orders). So every prior "Fourier plane" observation had actually been a **defocused
aperture disk**. Both original observations were then textbook-correct: an axicon puts the real
Bessel in the **near field** and a ring at the Fourier plane; the camera simply was not at that
plane.

**Quantified by an SLM-lens sweep.** Adding a lens `φ = −k/(2F)ρ²` on the SLM and sweeping F on the
plain spot gave rms spot width: `F = −0.55 m → 0.48 mm`, `−0.80 m → 0.198 mm`, `−1.05 m → 0.38 mm`
— a clean parabolic minimum at **F = −0.80 m**. Converging F did nothing, proving the camera sits
**past** focus. Displacement `Δz ≈ f²/F = 0.53²/0.80 ≈ **35 cm past** L1's focal plane`.

**Result — a real Bessel, on demand.** Writing the blazed grating **only on an annulus**
(`ρ_r = 3.0 mm`, ±16 px, beam-dump elsewhere) sends the ring's light into the first order as a
flat-phase ring → J0 Bessel at L1's focal plane; adding the measured `F = −0.80 m` defocus
correction pulls that plane onto the sensor. Captured: a sharp, centred J0 with dark rings at
**15, 34, 53, 72 px** (Δ ≈ 19 px — the Bessel signature). Residual cross-hatch identified as
grating × Bayer-filter moiré plus overlapping orders — cosmetic. Committed as
`bessel_ring_capture.png` and productized as `examples/bessel_ring_test.m`.

**Third finding — the "Ham works, Holoeye doesn't" difference.** The user then reported that the
*same* `gravity_lens.m` gives clean concentric circles on the Hamamatsu but not the Holoeye. Two
real differences were found:
1. The bench language had been misleading: **both arms are SLM → free space → camera with no lens**,
   separation **530 mm** — "530 mm" and "4f/1f" had been a *distance*, not a focal length. Since the
   gravity-lens phase is metric, the caustic is pixel-pitch-independent, so the same code must give
   the same caustic at the same distance **if the incident beam curvature matches**. It was then
   measured that a `−0.80 m` SLM lens moves the flat-phase focus onto the 530 mm camera, i.e.
   `1/530 = 1/R_c − 1/800` → `R_c ≈ 319 mm`: the beam hitting the Holoeye appeared to **converge**
   ~319 mm in front of it, which would add to the gravity lens and drag the caustic in toward the
   SLM — matching the original "Bessel at ~1 cm". Setting `collimateF = −0.319 m` did produce the
   compact in-focus **binary-lensing caustic** (four-cusp diamond/astroid + central
   multiple-imaging lattice) on the 530 mm camera, expanding past focus by `F = −0.75`.
2. The `lensOffset` pixel-vs-metric bug (§6.5).

**And then the actual root cause superseded all of it** — §6.4.

### 6.4 Root cause: the PLUTO-2.1 imprints the *negative* of the addressed phase

**The observation that cracked it**, from the user: *"somehow the same phase encode on the two SLMs
does exactly the opposite thing — the same phase difference deflects the laser in opposite
directions … it is also probably why the grating needs to be flipped."* Followed by the empirical
fix: *"I need to flip the grating with a −1 multiplier **and** flip the hologram value:
`holo = 2π − holo`."*

**Root cause (user-confirmed on hardware).** This PLUTO-2.1's flashed CLUT is
**phase-DESCENDING** — gray → phase has a reversed slope, so the panel imprints the **negative** of
the addressed phase. Consequences: the same hologram deflects the opposite way, **and** a
converging lens becomes diverging — which is why the gravity-lens caustic could not form at all.

**The elegant part.** The user's two empirical operations — flip the grating sign *and* negate the
hologram — are algebraically **one** operation: negating the **full** hologram, grating included,
when it is built with natural (Hamamatsu-sign) grating counts. So the fix is a single global
negation applied at the output stage:

```matlab
if cfg.invertPhase
    Holo = mod(2*pi - Holo, 2*pi);   % in optics.display
end
```

with `slm_config('holoeye')` setting `invertPhase = true` and returning `orientMult` to `+1` —
because a `−1` there would **double-flip** the grating back to wrong. One negation simultaneously
corrects gratings, lenses, gravity lenses, **and** OAM charge (`exp(iℓθ) → exp(−iℓθ)` is
pre-compensated). **No per-feature `ell` or `orientMult` flips are needed anywhere.** The
alternative root fix — reflash an ascending-polarity CLUT via the HOLOEYE Configuration Manager,
then set `invertPhase = false` — is documented in the config.

**Two earlier conclusions were retracted in writing.** Both the *"geometric flip / mirror-opposite
mounting"* explanation and the *"converging incident beam, R_c = −0.319 m collimation"* measurement
were **confounded by the unrecognized phase inversion**: a `−0.319 m` command became `+0.319 m`
*converging* on the panel and produced its own caustic, convincingly faking a "normal lens." The
`collimateF` block in `examples/gravity_lens.m` was therefore commented out — not deleted — with a
header explaining precisely why the numbers must not be trusted and that the incident-beam
curvature has to be **re-measured after** the `invertPhase` fix. The dual-SLM note claiming
*"mirror-opposite mounting → orientMult = −1"* was likewise flagged as almost certainly the same
misdiagnosis.

Keeping the retraction, the reasoning, and the superseded numbers in the repository — rather than
quietly overwriting them — is the practice this project settled on.

### 6.5 The `lensOffset` pixel-vs-metric bug (encountered twice)

`lensOffset` specifies the twin-lens separation of the binary lens in **pixels**. A fixed count is
therefore a **different physical separation on every device**: 70 px is 70 × 20 µm = **1.40 mm** on
the Hamamatsu but 70 × 8 µm = **0.56 mm** on the Holoeye — a different binary, and a different
Einstein-ring structure. The grating and aperture had already been metric-matched in Phase 6; this
one was missed and surfaced during the Phase 7 hardware comparison.

**Fix:** specify the separation in metres and convert per device —
`lensSep_m = 1.40e-3; lensOffset = round(lensSep_m / cfg.slmPixelSize)` → **175 px on the
Holoeye** to match 70 px on the Hamamatsu. An earlier instance of the same class of error was fixed
in commit `e44fa05` ("Metric of LensOffset Updated"), which is why the general principle —
**never let a pixel count carry physics** — is now written into the design rules and enforced by
`optics.coordinates` returning metres.

### 6.6 The same phase-inversion bug, seen from the bench: a four-hypothesis elimination  **[account]**

§6.4 records the *code* root cause and the one-line fix. This is how it was actually found at the
optical table, and it is the cleanest controlled-elimination arc in the project — worth keeping
separate because the reasoning, not the patch, is the content.

**Expected.** With the new Holoeye PLUTO-2.1 installed, a **Bessel-beam** test pattern should show
**concentric rings** at the output of the 4f system.

**Observed.** A single **large ring** — the far-field signature — as though the beam were coming to
focus very close to the SLM plane. Not a subtle discrepancy: the pattern was in the wrong *regime*,
so it could not be tuned away and could not be ignored.

**Hypothesis 1 — the input beam is not collimated** (an uncollimated input adds curvature and would
pull the focus in toward the SLM). Test: a **shearing interferometer** after the beam expander,
adjusting the separation of the expander lenses until the shear fringes ran parallel — the standard
collimation null. Collimation achieved. **Symptom unchanged → eliminated.**

**Hypothesis 2 — the gray→phase LUT is wrong.** The Holoeye's look-up table maps gray 0–255 onto
0–2π; a wrong table means the addressed phase is not the imprinted phase. Test: read the PLUTO-2.1
documentation, identify and load the correct LUT/config for the device and wavelength. **Symptom
unchanged → eliminated.** (This is the same knob that §6.2 later shows *does* control the caustic
distance — so eliminating it here was not wasted: it fixed the depth while leaving the sign wrong.)

**Hypothesis 3 — the phase encoding itself.** Designed the decisive controlled test: give **both
SLMs the same, simplest possible pattern** — a plain blazed grating, whose only job is to deflect
light from the zero into the first order — and compare. **The new SLM deflected the first order in
the opposite direction from the Hamamatsu.** That single observation localizes the fault to the
sign of the imprinted phase, independently of lenses, collimation, alignment, or the lensing physics.

**Fix and result.** Multiply the entire phase map by −1. Rings appeared. The algebraic consolidation
of that empirical fix into `cfg.invertPhase` — and the two earlier conclusions it forced to be
retracted — are in §6.4.

**Why this arc is the good one:** each hypothesis was killed by an *independent measurement* rather
than by a parameter tweak (an interferometer for collimation; the vendor's own calibration for the
LUT; a null-physics pattern for the encoding), and the decisive test was chosen because it removed
every variable except the one under suspicion.

### 6.7 Series alignment and the oblique-incidence deformation  **[account]**

The last bench problem of the dual-SLM build, and the one that resisted analysis entirely.

**Step 1 — the alignment test that passed.** To verify that the 4f relay images SLM1 onto SLM2
faithfully, a **cross phase-mask** was displayed on *both* panels. If the relay is correct, the
cross arriving from SLM1 and the cross written on SLM2 must **overlap and be the same size**. After
several iterations of mirror and lens adjustment, it passed. *(This is the physical-optics
counterpart of the numerical cross-SLM matching in §6.5/§7.1 — the two checks were developed
independently and agree.)*

**Step 2 — the failure it did not catch.** With a grating on SLM1 (deflecting into the first order)
and a **Bessel** wavefront on SLM2, the first-order light arriving at SLM2 carried **extra phase**:
instead of clean concentric rings, the output showed **fragmented curves and cusps** — a deformed,
caustic-like breakup of the ring structure.

**Elimination.** Removing the 4f lenses did **not** remove the deformation, which excluded the lens
pair and left only the **mirror between the iris and the second lens** as the source. The mirror
was taken off its mount and moved by hand through the space of positions and angles, looking for a
configuration with no deformation. (In the developer's own words: *"That was the messiest station
I've ever had — tools, lenses, irises all over the table. But I'm not afraid of making such a mess;
I believe this is the necessary step."*)

**The observation that resolved it.** The deformation **vanished only at one specific angle of
incidence of the beam on the SLM** — not at a specific position. The final geometry was found by
re-centring the beam on the panel *while holding that incidence angle fixed*, which is a
two-constraint alignment rather than the usual one.

**Physical reading.** A phase-only LCOS is a reflective device with finite liquid-crystal
thickness; at oblique incidence the optical path through the LC layer, the effective pixel pitch
seen by the beam, and the geometric wavefront tilt all change, so the imprinted phase acquires an
incidence-dependent aberration on top of the intended map. The empirical result — one good angle —
is consistent with that, but **it was not modelled or parameterized**, and this is recorded as
resolved-in-practice, not explained. Quantifying it (measured deformation vs. incidence angle,
against an LC-thickness model) is a genuine open item.

---

## 7. Verification and validation ledger

Everything below was actually computed and checked, mostly through the MATLAB bridge during the
working sessions.

### 7.1 Cross-SLM matching

| Quantity | Result |
|---|---|
| Wavefront agreement, all beam types (single / binary / OAM / power-law) resampled to a common µm grid | **≤ 9° RMS phase** difference — pure resampling error |
| Physical grating frequency, both devices | `|u| = [10500, 10000]` cycles/m (identical) |
| Aperture radius, both devices | 214 px × 20 µm = 535 px × 8 µm = **4.28 mm** |
| Log-lens caustic distance, 20 µm vs 8 µm pitch, same physical φ | Both **z = 0.2857 m** at ρ = 2 mm, `r_S = 7 µm` → pitch-invariant, as predicted |
| Same lens with φ over-modulated by 255/190 | z → **0.2129 m** (ratio 0.745 ≈ 3f/4f) → reproduces the observed bug |

### 7.2 Stationary-phase caustic fidelity (`d̂ = 1.2`, `y = 0`)

Far-field correlation of the masked hologram's caustic against the full lens, vs. kept-disk radius:

| `coreRadiusUnits` | Correlation | Note |
|---|---|---|
| 0.3 u | 0.43 | Disks cover only isolated images — GO sum fails at caustic scales |
| 0.6 u | 0.78 | |
| **0.8 u** | **0.95** | **at ~30 % of aperture pixels (~3× fewer)** — the chosen default |
| 1.0 u | 0.99 | |

Poster configuration (`d̂ = 1.09`, `r_S = 3.3 µm`, `z = 0.50 m`, `coreU = 0.80`,
`pixPerUnit = 128.5`, **5 images**, `R_E = 2.569 mm`):

| Kept fraction of aperture | Active pixels | Correlation with full-lens caustic |
|---|---|---|
| 82.4 % | 118,485 | 0.850 |
| **51.4 %** | **74,003** | **0.679** ← the version shown on the poster |

Structural sanity checks built into the solver: single point lens (`β = 0`) → **2 images**;
equal-mass binary with source inside the caustic → **5 images**.

### 7.3 WRA / GR pipeline invariants

| Check | Result |
|---|---|
| Null condition on the Kerr geodesic | **2e-15** |
| Tetrad orthonormality | **4e-16** |
| `Ω_ab` antisymmetry | **2e-11** (explicitly antisymmetrized to remove FD residue) |
| Miller trivial-WRA recovery at `α = 90°` (axis ∥ momentum) | `Δχ = 3e-11 ≈ 0` |
| Schwarzschild (`a = 0`) → antisymmetric `Δχ(±b)`; Kerr (`a > 0`) breaks it | Confirmed — frame dragging |
| Radial-grid convergence, `nR = 1500` vs `4000` | **5e-5** |
| Rotator identity `QWP(+45)·[SLM_H·SLM_V]·QWP(+45) = R(θ)` | **1e-14** (retained at 2.5e-14 after the `wignerRotation` retrofit) |
| Malus readout, D input + crossed analyzer → `I = sin²θ` | **2e-16** |
| Physical WRA, single lens `r_s = 3.3 µm` | `|θ| ~ 0.01°`, `|Δθ| ~ 0.065°` (cf. deflection `4M/b = 0.088°`), scales ∝ `r_s` |
| Physical WRA, binary `r_s = 3.3 µm` | `|θ| ~ 0.13°`, `|Δθ| ~ 0.73°` |

### 7.4 Alignment hologram

| Check | Result |
|---|---|
| Topological charge by loop integral | **3.000** (requested ℓ = 3) |
| FFT far-field first order | Ring at the grating offset; centre null ≈ **0.007**; peak at r ≈ 3 px |
| Fullscreen output (via `java.awt.Robot` capture of monitor 2) | Fills rows 1..600, cols 1..800; frame reuse updates in place; close restores |

### 7.5 Bessel / defocus measurements

| Measurement | Result |
|---|---|
| SLM-lens F sweep on a plain focused spot (rms width) | −0.55 m → 0.48 mm; **−0.80 m → 0.198 mm**; −1.05 m → 0.38 mm (parabolic minimum) |
| Inferred camera displacement from L1's focal plane | `Δz ≈ f²/F = 0.53²/0.80 ≈` **35 cm past focus** |
| Captured J0 dark-ring radii | **15, 34, 53, 72 px** (Δ ≈ 19 px — Bessel signature) |
| Defocused plain spot (before correction) | ~5 mm disk of concentric Fresnel aperture rings + 2 fainter diffraction orders (expected ~50 µm point) |

### 7.6 Regression suite

`examples/test_gravityLens.m` — 12 automated checks over the `optics.gravityLens` name-value
interface: default call, every option, mode switching, output size, `[0, 2π]` range, and error
handling. `examples/simulation.m` (310 lines) exercises **every layer** of the package on synthetic
data with no hardware: optics unit tests → a full scan loop through `+sim/camera`, `+sim/optics`,
`+sim/stage` → movie compilation.

---

## 8. Data products, figures, and deliverables

### 8.1 Raw experimental data

| Dataset | Contents | Purpose |
|---|---|---|
| `ebin0626/` | **73 PNG interferograms at 4096 × 3000** (~12 MB each, ~880 MB) + `ebin0626.mp4` (20 MB) | Phase-shifting interferometry: one full 0→2π reference-phase cycle against a fixed binary gravity-lens hologram. Input to `analysis.phaseMap` |
| `bessel_ring_capture.png` | 14 MB camera frame | Captured J0 Bessel with measured ring spacing — evidence for the defocus diagnosis (§6.3) |
| `CapturedImage.png` | 9 MB | Sample camera output retained from the original codebase |

Raw image sequences and generated data (`data/`, `sim_output/`, `*.mp4`, `ebin0626/*.png`) are
deliberately git-ignored; the code that produces and consumes them is versioned instead.

### 8.2 Figures generated

**Simulation figures (from `scratchpad/make_poster_caustics.m`, in the poster directory):**
- `Tfunction_map.png` — the Shapiro/time-delay function `T_grav` in the lens plane, 900×900
  dimensionless grid over ±1.7 Einstein radii, 12 contour levels, masses marked with ×.
- `Caustic_full.png` — far-field `|F(y)|²` from the full binary lens (γ = 0.4, hot colormap).
- `Caustic_masked.png` — the same from the stationary-phase mask.
- `Stationary_mask.png` — the kept stationary-phase disks themselves.

**Measured figures (in the poster directory):**
- `PhaseBinaryCausticd0p8.png`, `PhaseBinaryCausticd1p1.png`, `PhaseBinaryCausticd1p6.png` —
  **measured** field phase wrapped to [0, 2π] reconstructed from interference scans, at binary
  separations `d̂ = 0.8, 1.1, 1.6`.
- `Cutsthroughdatak40.png` — measured intensity cuts overlaid on the wave-optical prediction.
- `Changersdydhatconst.png` (15 MB) — `r_s` / `d_y` variation at constant `d̂`.
- `App.png` — apparatus photograph/diagram; `BinaryLensing.png` — geometry schematic;
  `LRG3-757.png` — Hubble image of the Einstein ring in LRG 3-757 (z = 2.4).

**Documentation figures (versioned in `docs/figures/`):**
- `WRABenchSetupSketch.png` — MATLAB-drawn WRA bench layout.
- `Dual_SLMPhaseMaps.png` — the 2 × 3 dual-SLM phase-map panel.

**Interactive diagnostic figures produced by the example scripts:** the Fermat phase plane with
Morse-classified critical points, critical curves and the source-plane caustic; the 4-panel
`phaseMap` diagnostic (mean interferogram / wrapped phase / modulation magnitude /
enclosed-charge-vs-radius plateau); the 3-figure WRA demo; the per-element polarization-ellipse
stage map; the cross-SLM micrometre-axis hologram comparison.

### 8.3 Example script catalogue (19 scripts, 2,469 lines)

| Script | Lines | What it does |
|---|---|---|
| `polarization_wra_dual_slm.m` | 542 | Full dual-SLM WRA polarization simulation with rotator/retarder modes, per-stage Jones analysis, and hardware display subfunction |
| `simulation.m` | 310 | Hardware-free end-to-end package test (optics → scan → movie) |
| `stationary_phase_lens_v2.m` | 300 | Minimal-pixel stationary-phase hologram with caustic-fidelity check and phase-plane plot |
| `rainbow_droplet.m` | 233 | Rainbow scattering from a water droplet as a **fold catastrophe**; encodes the geometric-optics phase to probe vortices in the blue/violet supernumerary bows (Nussenzveig; Berry; Lee & Hernández-Andrés) |
| `dual_slm_phase_maps.m` | 230 | Builds and displays both WRA SLM phase maps + bench sketch |
| `test_gravityLens.m` | 205 | 12-check regression suite |
| `dual_slm_lg_split_mask.m` | 181 | Splits one aperture across two SLMs with a shared physical LG mode (CAM encoding) |
| `compare_slm_holograms.m` | 175 | Quantitative cross-SLM hologram comparison on a common µm grid |
| `phase_plane_critical_points.m` | 152 | Fermat potential, Morse-classified critical points, critical curves, caustic |
| `wigner_rotation_lensing.m` | 140 | 3-figure WRA demo (Kerr 1-D curves, binary maps, per-input readouts) |
| `caustic_polarization_z500.m` | 139 | Caustic with polarization texture Fresnel-propagated to z = 500 mm |
| `align_slms.m` | 139 | Simultaneous dual-SLM vortex alignment driver |
| `stationary_phase_lens.m` | 122 | Original stationary-phase example (v1) |
| `gravity_lens_scan.m` | 104 | Automated `r_s` sweep with camera capture (optional stage) |
| `interference_scan.m` | 100 | Phase-shifting acquisition — produces the `ebin0626`-style dataset |
| `holoeye_focus_scan.m` | 95 | On-bench `modMaxGray` calibration sweep |
| `bessel_ring_test.m` | 83 | Durnin-ring Bessel + 4f alignment check with defocus correction |
| `vortex_analysis.m` | 63 | Phase reconstruction + vortex/OAM decision wrapper |
| `gravity_lens.m` | 50 | Single binary-lens display with metric `lensSep_m` |
| `parabolic_beam.m` | 34 | Power-law (n = 2, quartic-potential) beam |
| `test_camera.m` | 26 | Camera connectivity + auto-exposure check |
| `grating.m`, `alignment_bessel.m` | 17 each | Minimal bench scratch drivers |

### 8.4 Documentation written

| Document | Size | Contents |
|---|---|---|
| `docs/README.md` | ~850 lines | Full user guide: repository structure, quick start, both config files with complete field tables, the 16-point `modMaxGray` calibration table, every function signature with options tables, the 3 phase models, the 9 Zernike terms, the 3 vortex-detection methods, dual-SLM setup, alignment procedure, hardware notes, and an 8-entry troubleshooting section keyed to real failures |
| `docs/WRA_bench_setup.md` | 248 lines | The WRA bench-build tutorial (§5, Phase 10) |
| `docs/PROJECT_LOG.md` | this file | Development log |
| `README.md` | 40 lines | Repository entry point and quick start |
| In-code documentation | throughout | Every module carries a full help block; the difficult files (`slm_config`, `holoeye_focus_scan`, `bessel_ring_test`, `gravity_lens`, `stationaryLens`) carry the **physics reasoning and the retracted hypotheses** inline, so the bench context travels with the code |

---

## 9. Dissemination: manuscript, poster, and talks

### 9.1 The manuscript — results, parameters, and figure-level attribution  **[ms]**

> **A. Moreso Serra, O. Bulashenko, Y. Gu, T. Nguyen, K. Kendja, V. Rodríguez-Fajardo, and
> E. J. Galvez**, *"Laboratory observation of lensing diffraction in a binary-lens system for
> gravitational-wave astrophysics"*, dated 2026-06-08, **under review**.
> Corresponding authors: Bulashenko (ICCUB) and Galvez (Colgate).
> **Gu is the first-listed Colgate author — the lead experimental author on the paper.**

**The claim of the paper.** Diffraction of gravitationally lensed light has never been directly
observed: astrophysical sources are too incoherent and optical wavelengths too short. A phase-only
SLM lets the binary Shapiro delay be imprinted on a fully coherent laboratory beam, so the entire
wave-optical diffraction pattern of a binary lens — caustics *decorated by interference* — can be
imaged at once. The measurements reproduce both the predicted caustic morphologies **and**,
for the first time, the **fine interference structure**, with **no adjustable parameters**, across
a disparity of many orders of magnitude in length scale.

**Structure of the results, and what was measured for each:**

| § | Result | Measurement behind it |
|---|---|---|
| IV.A | **Caustic morphology vs. separation.** Six stages of the metamorphosis at λ = 633 nm: `d̂ = 0` (concentric rings — the single point lens, a 2-D confluent hypergeometric pattern well approximated by a Bessel function), `0.64` (symmetry breaks → central astroid), `0.88` (deltoids merge into a vertically elongated hypocycloid), `1.13`, `1.63`, `1.84` (two astroids joined by a thin caustic bridge, which then breaks) | A `d̂` scan at fixed wavelength — Fig. 5 |
| IV.A | **Achromatic caustic, chromatic fringes.** The caustic geometry is set by `d̂` alone and does **not** move with wavelength; the interference fringes on it do. Fringe spacing scales as **√λ** away from the caustic and as **λ^(2/3)** near a fold. The composite reveals a highly symmetric **crosshatched network of interference minima** extending well *beyond* the caustic boundary | **Composite of 14 wavelengths, 403–684 nm, at fixed `d̂` = 1.09** — Fig. 6 |
| IV.A | **Quantitative theory–experiment comparison with no free parameters.** Four characteristic lengths defined from the first intensity maxima measured normal to the critical curve: `ℓ₁` (central cusp pair), `ℓ₂` (upper cusps), `s₁` (folds on the vertical axis), `s₂` (opposite cusps), tracked across `d̂`. Theory from Airy (fold) and Pearcey (cusp) asymptotics with the universal constants `X_cusp = 2.1986`, `X_fold = 1.0188` | λ = 633 nm, `r_S` = 12 µm → **w = 238**; insets at 532 nm — Figs. 7, 8 |
| IV.B | **Agreement at the level of the diffraction fine structure — the paper's headline novelty.** Point-by-point comparison of measured and computed patterns, plus intensity cuts along **pixel columns 205 and 267**, comparing both positions *and* relative amplitudes of the maxima. Previous experiments confirmed caustic *morphology*; this demonstrates agreement in the **detailed interference structure** for the first time | **w = 80, `d̂` = 1.07** — Fig. 9 |
| IV.C | **Mapping lab → astrophysics.** Each optical `(r_S, z, d_exp)` maps to a family of GW-lensing scenarios with the same `(d̂, w)`: Galactic B-star / O-star / SOBH / WR binaries lensing extragalactic sources (kHz — Einstein Telescope, NEMO, high-frequency KAGRA; and LVK-band inspiral), primordial-black-hole pairs, and SMBH/IMBH binaries in a common host galaxy (mHz — LISA) | Table I |
| IV.D | **The GW chirp reproduced in the lab.** Because `w ∝ r_S` and the wavelength range only spans a factor ≈ 2, the frequency sweep of an inspiral is instead emulated **by scaling `r_S` and `z` together at fixed `λ` and fixed `d̂`**, so the caustic shape is frozen while the diffraction pattern evolves. Six panels: `(r_S, z)` = (2 µm, 150.1 cm), (3, 98.2), (3.5, 83.2), (5, 56.1), (8, 31.5), (14, 17.0) → **w = 39.7, 59.6, 69.5, 99.3, 158.8, 277.9** → for a 5×10³ M☉ lens, **f = 63.9, 95.9, 111.9, 159.9, 255.8, 447.6 Hz**. **GW150914 swept 35 → 250 Hz — a range these configurations cover.** The lab images are then read as *snapshots of the diffraction pattern that would sweep across a detector during a chirp* | λ = 633 nm, `d_exp` = 2.8 mm (`d̂` ≈ 1.2) — Fig. 10, Table II |

**Scale relations used throughout** (they are what make the analogy quantitative):
`R_E = 2.86 au · (M_Lz/M☉)^{1/2} (d_L/1 kpc)^{1/2}` astrophysically, versus
`r_E = 0.14 mm · (r_S/1 µm)^{1/2} (z/1 cm)^{1/2}` on the bench — same dimensionless physics,
~10¹⁵ apart in length.

**Attribution — what is safe to claim.** The developer is the lead **experimental** author and
produced the diffraction data behind the results above; the multi-wavelength composite (Fig. 6),
the fine-structure comparison (Fig. 9), and the chirp sequence (Fig. 10) are the ones most directly
his. Data acquisition on a shared bench across a year involves the other Colgate co-authors
(Nguyen, Kendja, Rodríguez-Fajardo) and Galvez, and the theory, scaling laws, and asymptotics are
Barcelona's. The accurate phrasing is **"co-first / lead experimental author"** or **"first-listed
Colgate author"** — not sole first author, and never authorship of the theory.

### 9.2 The conference poster

`Lab_GravLensing_Poster_Ver_01` — **"Laboratory Astrophysics of Gravitational Lensing"**,
Yufeng Gu and Enrique (Kiko) Galvez, Department of Physics & Astronomy, Colgate University.
Credits theory collaborators A. Moreso Serra & O. Bulashenko (ICCUB, Barcelona) and NSF grant
PHY-2409587.

**Format:** 35 × 43 in portrait beamerposter, three columns, XeLaTeX with a custom Colgate theme
(`beamerthemecolgate.sty`, `beamercolorthemecolgateColor.sty`).

**Column 1 — Background & wave-optical theory:** what gravitational lensing is, the Einstein radius
`R_E = sqrt((4GM_L/c²)(d_LS d_L/d_S))` with the Hubble LRG 3-757 Einstein ring; the motivation
(binary wave-optical lensing is unexplored; a GW detector samples one pixel of a huge diffraction
pattern while the SLM analogue images all of it); and the theory — the Fresnel–Kirchhoff integral,
the Fermat time-delay decomposition, and the symmetric-binary `T_grav`.

**Column 2 — Method:** the apparatus; the boxed SLM encoding `φ_SLM(x) = −2 k r_S T_grav(x)` with
the crucial note that **only the gravitational part is programmed** and free-space propagation
supplies `T_geom`; the `T_grav` map that is literally the phase written to the SLM; and the
stationary-phase/GO limit with the image sum, magnification `μ_j = [det K̂]^{-1}`, Morse index, and
caustics as `det K̂ = 0`.

**Column 3 — Results:** the full-lens vs. stationary-phase-mask caustic comparison (5 disks,
~51 % of the aperture, `d̂ = 1.09`) demonstrating that the masked hologram recovers the same
fold/cusp structure; the measured interference-scan phase maps at `d̂ = 0.8, 1.1, 1.6` showing the
caustic and its interference decoration evolving with separation; and **theory vs. experiment** —
measured intensity cuts overlaying the wave-optical prediction with maxima and minima aligning
**with no adjustable parameters**, validating the analogue across many orders of magnitude in
length scale.

**Engineering note:** making the project build reliably from VS Code required forcing XeLaTeX
through `.latexmkrc` plus `.vscode/` settings, because the theme loads `fontspec` and the default
pdfLaTeX recipe fails on it.

### 9.3 Full dissemination ledger

| Output | Venue / status | Role |
|---|---|---|
| **Binary-lens manuscript** (§9.1) | Under review, dated 2026-06-08 | **Lead experimental author** (first-listed Colgate author) |
| **"Laboratory Astrophysics of Gravitational Lensing"** poster (§9.2) | Conference poster, 35 × 43 in, 2026-07 | First author; built the poster and generated its simulation figures |
| **OPICA / FIO presentation** *(2025)* | Conference presentation | Presenter — *outside this repository; listed for completeness* |
| **Physics Today "Backscatter"** submission — quantum-pendulum optical analogue | Under review | *Outside this repository; from the Phase −1 warm-up project (§1.1)* |
| **Senior thesis project** | Self-initiated, funded through Galvez; Summer 2026 → May 2027 | The WRA / polarization thread (§5 Phases 9–10) is its technical foundation |

---

## 10. Open items and next steps

**Immediate / known regressions**
1. **Restore the fullscreen-exclusive display fix.** The `dev.setFullScreenWindow` change (§6.1) is
   documented and verified but **not in committed `+optics/display.m`** — `git log -S` confirms it
   was never committed. It affects grating steering and geometric fidelity on this mixed-DPI
   machine.
2. **`orientMult` for the Holoeye is currently `−1.8`** in `slm_config.m` (from the 2026-07-21
   "Tunned" commit) while the surrounding comment states it should be `+1` now that
   `cfg.invertPhase` handles the sign globally. The value is an empirical steering tune; the
   discrepancy between code and comment should be resolved deliberately — either document `−1.8`
   as a measured steering gain or restore `+1`.
3. **Confirm the flashed Holoeye CLUT.** `slm_config` still assumes `holoConfigPi = 2.0` and
   `holoConfigLambda = 635 nm`. The actual flashed config filename should be read off the
   Configuration Manager and entered, or — better — the wavelength-matched NIR-145 2.00π config
   should be flashed so `modMaxGray = 255` exactly.
4. **Re-measure the incident-beam curvature on the Holoeye arm** now that `invertPhase` is
   corrected. Every `collimateF`/`R_c = 319 mm` number predates the fix and is explicitly
   untrustworthy (§6.4). Run `scratchpad/sign_test.m` once the camera USB is re-seated — it dropped
   frames mid-session (opens, then *"No frame received within 10 s"*; needs replug / `imaqreset`).

4b. **Parameterize the oblique-incidence deformation (§6.7).** The Bessel-ring breakup on SLM2 was
   cured empirically by finding the one working angle of incidence; it was never measured or
   modelled. A deformation-vs-angle scan against a liquid-crystal-thickness / effective-pitch model
   would turn a piece of bench folklore into an alignment specification — and the current setup can
   take that data.

**Physics goals not yet reached**
5. **The original stated goal remains open:** observe the **binary gravitational-lensing pattern at
   "1f + z" after the 4f relay**. The camera cannot reach the true plane because **SLM2 physically
   occupies that space**. The lensing caustic is a near-field object, so it needs either the camera
   at the right plane or the same SLM-lens defocus relay trick — and the `−0.80 m` value is
   specific to the Bessel test geometry, so the full path with SLM2 needs its own calibration via
   the plain-spot sweep.
6. **Run the stationary-phase hologram on hardware.** The simulation is characterized (§7.2); the
   masked hologram has not yet been displayed and imaged for a direct A/B against the full lens.
7. **Build the WRA bench.** `docs/WRA_bench_setup.md` gives the complete component list, QWP
   settings, alignment procedure, and readout strategies. Expect sub-degree true signals, so the
   crossed-analyzer null plus a reference interferometer arm is the route to a quantitative result;
   `peakDeg = 20–45°` gives a visible demonstration with a physically faithful map shape.
8. **Measure the non-reciprocity `Δθ`** by swapping `θ → θ_reverse` and differencing — Miller's
   Mach–Zehnder proposal, and the effect whose `1/(1 − n₃²)` enhancement makes the WRA detectable
   at all.

---

## 11. Skills and competencies demonstrated

*Compiled for application material — every item is traceable to a specific artifact above.*

**Experimental optics.** Phase-only LCOS SLM hologram design and encoding (phase-only and complex
amplitude/CAM); blazed-grating beam steering and diffraction-order separation; 4f relay design and
alignment; Fourier-plane vs. near-field diagnosis; Durnin-ring Bessel-beam generation; optical
vortices and OAM; phase-shifting interferometry; polarimetry and Jones/Stokes analysis;
quarter-wave-plate rotator design; camera photometry and exposure control; Zernike aberration
correction; multi-device (dual-SLM) bench integration.

**Theory and computation.** Fresnel–Kirchhoff diffraction; Fermat/time-delay potentials and
gravitational lensing; catastrophe optics (folds, cusps, caustics, Morse classification);
stationary-phase/geometric-optics asymptotics *including where they break down*; Kerr geodesics,
orthonormal tetrads, local Lorentz generators, and Wigner rotation; FFT-based Fresnel propagation;
Nyquist sampling analysis for hologram design.

**Scientific software engineering.** Refactoring a legacy monolith into a documented, testable
package architecture; API design with explicit resource-safety patterns (`onCleanup`); building a
hardware simulator to enable hardware-free development and regression testing; automated test
suites; memory-bounded processing of ~880 MB image stacks; hardware SDK integration via .NET/DLL;
Java/AWT display control including fullscreen-exclusive mode and DPI virtualization;
backward-compatible configuration refactors; documentation as a first-class deliverable.

**Physics-driven debugging — the through-line.** Every hard bug in this project was solved by
deriving the expected physical scaling first and only then touching the bench:
proving the caustic distance is pitch-invariant but depth-dependent (§6.2); recognizing a
"defocused aperture disk" for what it was and locating the plane by a parabolic sweep (§6.3);
collapsing two empirical sign flips into one algebraic negation (§6.4); tracing a
"flaky" corner-hologram to Windows DPI virtualization by comparing what two different JVMs reported
as the screen size (§6.1). Equally: **writing down which conclusions were wrong** — the retracted
collimation measurement, the dead 4π hypothesis, the VIS-016 misidentification, the
mirror-mounting misdiagnosis — and keeping the superseded numbers in the repository with
explanations of why they can't be trusted.

**Measurement campaign execution.** Running a **multi-wavelength (14 lasers, 403–684 nm),
multi-parameter (`r_S` = 0.2–20 µm, `d̂` = 0–4, z = 10–30 cm) imaging campaign** to publication
standard: fibre-coupled source swapping without re-alignment, achromatic-path design, the
empirically-found grating working window that made clean first-order imaging possible at all, and
reduction of the resulting patterns into four caustic observables compared against parameter-free
theory (§9.1).

**Communication.** A 3-column research poster combining theory, simulation, and measurement;
a 248-line bench-build tutorial written so another person could reproduce the setup; ~1,100 lines
of user documentation; and inline physics reasoning kept with the code that depends on it.

**Research output.** Lead experimental author on a manuscript under review (§9.1); first author on
the conference poster (§9.2); conference presentation and a *Physics Today* Backscatter submission
from the warm-up project (§9.3); a self-initiated, funded senior thesis project growing out of the
WRA thread.

---

## 12. Application-material index (SOP raw material)

*This section exists because the log is also the evidence base for graduate-application writing.
It selects and cross-references — it invents nothing. Every row points at a section above.
It is deliberately **not prose**: the statement of purpose gets written by hand, from these.*

### 12.1 The three narrative arcs worth telling

Each is a complete *expected → anomaly → competing causes → decisive test → fix → consequence*
chain, which is the only shape a research story needs.

**Arc A — "The new SLM imprints the negative of what you tell it."** (§6.6 bench, §6.4 code)
Expected concentric Bessel rings; saw a far-field ring. Killed collimation with a **shearing
interferometer**, killed the **LUT** with the vendor's own calibration, then a controlled test —
*the same plain grating on both devices* — showed the new panel deflecting the first order the
wrong way. Fixed by one global sign. **The consequence is the interesting half:** two earlier
"results" (a measured incident-beam curvature `R_c ≈ 319 mm`, and a geometric mirror-mounting
explanation) had been *confounded* by the unrecognized inversion and had to be **retracted in
writing**, with the superseded numbers kept in the repository and marked untrustworthy.
*Why it's the strongest arc:* every hypothesis was eliminated by an independent instrument, not by
tuning; the decisive test was designed to isolate exactly one variable; and the ending is about
recognizing that earlier conclusions were wrong.

**Arc B — "Pixel pitch cannot be the problem; phase depth can."** (§6.2)
The Holoeye formed the Einstein ring one focal length early after geometry, aperture, and grating
had all been provably matched. Instead of tuning on the bench, the caustic distance was derived:
`z(ρ) = ρ/|θ|` with `θ = (1/k)dφ/dρ` gives **z = 0.2857 m for both 20 µm and 8 µm pitch** — pitch is
provably irrelevant — while over-modulating the phase by 255/190 gives **z = 0.2129 m, a ratio of
0.745 ≈ 3f/4f, exactly the observed error**. The fix then required deriving the calibration from
the vendor manual's physics — `modMaxGray = round(255 × (2/P) × (λ/λ_cfg))` — rather than fitting a
number. Along the way the "4π over-modulation" hypothesis was **killed by inventory** (no 4π config
exists for this device) and the device was **re-identified** (NIR-145, not VIS-016 as previously
recorded).
*Why it matters:* it is the clearest instance of the working method — **derive the expected physical
scaling first, and only then touch the bench.**

**Arc C — "The camera was never where everyone thought it was."** (§6.3)
Three nested misdiagnoses. First, the premise was wrong — the pattern being displayed was a binary
*log-axicon*, whose caustic is **chirped** (`z(ρ) = ρ²/2r_S,eff`, smeared over z ≈ 1–136 cm), i.e.
the wrong tool for a clean Bessel. Second, a plain deflected spot that should have been ~50 µm at
the Fourier plane came out as a **5 mm disk of Fresnel aperture rings** — so every previous
"Fourier-plane" observation had been a *defocused aperture disk*. The plane was then **located
quantitatively**: sweeping an SLM-encoded lens gave rms spot widths 0.48 / **0.198** / 0.38 mm at
F = −0.55 / −0.80 / −1.05 m, a parabolic minimum at F = −0.80 m → **camera 35 cm past focus**.
Third, writing the grating **only on an annulus** produced a real Durnin J₀ Bessel with dark rings
at 15, 34, 53, 72 px (Δ ≈ 19 px), committed as evidence.
*Why it matters:* it converts "the SLM is broken" into a measured number, and the measurement
technique (encode a lens, sweep it, fit the minimum) is reusable.

**Supporting beat, if a grit moment is wanted:** the oblique-incidence hunt (§6.7) — dismantling the
relay, hand-searching mirror positions, and finding that the deformation vanishes only at one
specific angle of incidence. Honest ending: fixed in practice, never modelled.

### 12.2 Claim → evidence table

*Left column: a claim an application might make. Right: where it is substantiated. Nothing here
requires the reader to take a word on trust.*

| Claim | Evidence |
|---|---|
| Lead experimental author on a manuscript under review | §9.1 — title, author order, corresponding authors, and which results the data supports |
| Produced the first quantitative agreement between wave-optical lensing theory and a laboratory analogue at the level of the **fine diffraction structure**, with no adjustable parameters | §9.1 (Figs. 8, 9); manuscript §IV.A–B |
| Reproduced a **GW chirp** in the lab by scaling `r_S` and `z` at fixed caustic shape, spanning 64–448 Hz for a 5×10³ M☉ lens — covering GW150914's 35→250 Hz sweep | §9.1 (Fig. 10, Table II); manuscript §IV.D |
| Solved the imaging problem previous project members could not, producing the first clean, usable data | §5 Phase −1 — the grating density / tilt-angle working window, found empirically |
| Invented and later productized a **vortex-null alignment diagnostic** | §5 Phase −1 (bench origin) → `optics.alignmentHologram`, §5 Phase 5, verified winding number **3.000** (§7.4) |
| Built a **virtual interferometer inside the hologram** — a common-path, zero-moving-part, exactly-stepped reference arm | §5 Phase 1; `+optics/gravityLens.m:87`; the 73-frame `ebin0626` dataset |
| Reconstructed the complex field and detected optical vortices / net OAM from a saturated-core beam | `analysis.phaseMap` (501 lines), §5 Phase 2 — single-bin temporal DFT, loop-integral charge, three independent core detectors, memory-bounded over ~880 MB |
| Built lab infrastructure now used beyond this project | §5 Phase −1 — ThorLabs stage + camera automation, **now used lab-wide** |
| Re-architected a legacy codebase into a device-agnostic library | §4 — package architecture, config-driven dual-SLM support; a new SLM is a new config function |
| Derives physics before touching hardware | §6.2, §6.3 — pitch-invariance proof; parabolic focus sweep |
| Retracts wrong conclusions in writing rather than overwriting them | §6.4 — the `collimateF` block commented out, not deleted, with a header explaining why the numbers cannot be trusted |
| Full-stack ownership: optics, control code, data pipeline, visualization, theory implementation, and writing | §3 (bench), §4 (code), §7 (validation), §8 (data), §9 (manuscript + poster) |
| Independent general-relativistic implementation from a paper, verified to machine precision | `optics.wignerRotation` — Kerr geodesic + tetrad + Lorentz generators; null condition 2e-15, tetrad orthonormality 4e-16, Miller's trivial-WRA limit recovered at 3e-11 (§7.3) |
| Understands where an approximation *breaks* | §7.2 — the stationary-phase/GO sum fails at caustic scales; quantified as correlation vs. kept-disk radius (0.43 → 0.99) |

### 12.3 Numbers that are safe to quote

| Number | Meaning | Source |
|---|---|---|
| **14** wavelengths, **403–684 nm** | Multi-wavelength campaign span | §9.1 |
| **`d̂` = 0–4**, in 20 µm (one-pixel) steps of separation | Binary-separation scan range | §9.1 |
| **w = 238** (λ = 633 nm, `r_S` = 12 µm) | Regime of the no-free-parameter caustic-dimension comparison | §9.1 |
| **w = 80, `d̂` = 1.07** | The fine-structure agreement figure | §9.1 |
| **64 → 448 Hz** | GW frequencies spanned by the lab chirp sequence | §9.1 |
| **73 frames × 4096 × 3000 px (~880 MB)** | The phase-shifting dataset reconstructed in software | §8.1 |
| **≤ 9° RMS phase** | Cross-SLM wavefront agreement after metric matching | §7.1 |
| **0.745 ≈ 3f/4f** | Predicted-and-observed ratio that identified phase depth as the 3f-ring cause | §6.2 |
| **35 cm** | Measured camera displacement past the focal plane | §6.3 |
| **≈ 51 % of aperture pixels → 0.679 correlation**; **0.8 u disks → 0.95 at ~30 % of pixels** | Stationary-phase minimal-pixel fidelity | §7.2 |
| **1,000+ frames** | The self-initiated merger movie | §5 Phase −1 |
| **7,351 lines / 67 files / 49 commits** | Repository scale | header |
| **2e-15, 4e-16, 3e-11, 1e-14, 2e-16** | GR-pipeline and Jones-optics invariants | §7.3 |

### 12.4 The intellectual through-line

Stated once, because it is what an application actually has to argue — and each step below is a
section of this log, not a retrofit:

> **Enlarge the representation until the hidden structure becomes analyzable.**

- The lensing caustics are **critical points of the time-delay function** — the structure lives
  exactly where the ray picture breaks down (§2.2, §7.2). The interesting object is not the ray;
  it is the catastrophe.
- The **phase**, not just the intensity, is made measurable by co-encoding a reference wave into
  the hologram (§5 Phase 1) — enlarging the observable from |U|² to U.
- From the reconstructed field, **topological charge** is extracted by loop integrals: an
  integer-valued invariant that survives a saturated core and cancels noise-generated vortex pairs
  (§5 Phase 2). Local data → global invariant.
- The **WRA thread** adds a second degree of freedom on top of the same beam: the common part of
  the dual-SLM phase carries the diffraction caustic, the differential part carries a polarization
  texture (§2.3, §5 Phases 9–10). One beam, two independent structures.
- And the clearest single result of that thread: in the rotator configuration the **helicity-basis
  phase and the classical azimuth rotation are literally the same number** (§5 Phase 9) — the
  quantum and classical faces of one quantity, visible only after changing basis.

**Honesty guardrails to carry into any application text.** (a) The lensing *theory* is Barcelona's;
the instrument, code, data, and reduction are the Colgate side's (§1.2). (b) The quantum-pendulum
warm-up ran on inherited code; the contribution there was tuning and learning the apparatus (§1.1).
(c) The dual-SLM/WRA platform is **built and verified in simulation but has produced no
measurements** — it is capability and intent, never a finding (§10). (d) "Lead experimental /
first-listed Colgate author," not sole first author (§9.1).

### 12.5 Gaps a reader would probe — and the honest answer

| Likely question | Answer as it stands today |
|---|---|
| Did the stationary-phase (minimal-pixel) hologram ever run on hardware? | **No.** Simulation is fully characterized (§7.2); the hardware A/B is open item 6 (§10). |
| Has the WRA polarimetry produced data? | **No.** Full GR pipeline verified numerically, bench tutorial written, hardware not built (§10, items 7–8). |
| Was the oblique-incidence deformation explained? | **No** — resolved empirically at one working angle, never modelled (§6.7, open item 4b). |
| Is everything in this log verifiable from the repository? | **No** — pre-repository bench work is tagged **[account]** and is the developer's own recollection; manuscript values are tagged **[ms]**. The tagging exists precisely so the boundary is legible. |
| Any known regressions in the committed code? | **Yes, documented:** the fullscreen-exclusive display fix was verified but never committed (§6.1, §10 item 1), and `orientMult = −1.8` contradicts its own comment (§10 item 2). |

---

## Appendix A — commit ledger

| Date | Hash | Message | Substance |
|---|---|---|---|
| 2026-04-27 18:23 | `9d66703` | Initial commit | Repository created |
| 2026-04-27 18:25 | `335cdf7` | ThorCam | Thorlabs camera code |
| 2026-04-27 18:27 | `3df59b5` | CamDepend | Camera DLL dependencies |
| 2026-04-27 19:57 | `ad6dcb4` | Reconstructed | **The restructure**: 32 package functions created, ~25 flat scripts deleted, 37 root DLLs removed, `docs/README.md` written (589 lines) |
| 2026-04-27 20:02 | `d45a3fb` | Delete .claude directory | Housekeeping |
| 2026-04-27 20:16 | `c782cec` | Integrate SLM and Optics Folder | `+slm` → `+optics`; `hardware_config` → `thorlab_hardware_config` |
| 2026-04-30 14:16 | `1113602` | Uodated | `gravityLens` rework + `test_gravityLens.m` (132 lines) |
| 2026-04-30 17:03 | `8c63989` | Integrated | Scan + parabolic-beam integration |
| 2026-06-17 10:39 | `e44fa05` | Metric of LensOffset Updated | First `lensOffset` metric fix; `.asv` cleanup |
| 2026-06-22 14:51 | `78910a6` | Interference Scan | **`interference_scan.m`** (88 lines) + `pwPhase` support |
| 2026-06-23 11:00 | `60013ba` | movie | `ebin0626/make_movie.m`; movie pipeline |
| 2026-06-24 11:37 | `f33e127` | 3 Features Updated | **`camera.autoExpose`** (185), **`optics.applyMask`** (55), **`optics.modMaxGray`** (94), `rainbow_droplet.m` (235), docs |
| 2026-06-24 12:06–12:13 | `b5550a4`, `4a7023a`, `0a2db5b` | tuning | autoExpose parameters; examples updated to new APIs |
| 2026-06-29 00:23 | `ac0d098` | Vortices | **`analysis.phaseMap`** (501 lines) + `vortex_analysis.m` |
| 2026-06-29 00:45 | `655417d` | Add stationary-phase binary-lens generator | **`optics.stationaryLens`** (264 lines) + example |
| 2026-06-29 00:55 | `7695278`, `c658657` | Stationary Code Solver / **PR #1 merge** | Solver improvements; only PR-merged feature |
| 2026-06-29 01:13 → 15:09 | `889eedf`, `b1ed857`, `57a2dc6`, `da95eba`, `5d56565`, `7df9190` | tuning | Parameter matching against `gravityLens`; 4-panel phase comparison |
| 2026-06-30 16:37 | `7f39fc0` | Stationary v2 | **Physics/pixel decoupling**; `stationary_phase_lens_v2.m` (289) + `phase_plane_critical_points.m` (148) |
| 2026-06-30 17:20–17:48 | `7d91659`, `b54f028`, `f19646f`, `fa55833` | v2 refinement | `autoPixPerUnit`, `coreRadiusUnits`, fidelity sweep |
| 2026-07-06 15:48 | `092cd80` | Holoeye-Supported | **`optics.alignmentHologram`** (138), **`optics.listScreens`** (88), `align_slms.m` (131), device-dispatching `slm_config` |
| 2026-07-07 11:34 | `355cf28` | Create alignment_bessel.m | Bench scratch driver |
| 2026-07-07 13:56 | `3c0c741` | LG Beams | **`optics.laguerreGauss`** (86) + `dual_slm_lg_split_mask.m` (181) |
| 2026-07-09 12:36 | `c891f60` | Grating | Grating experiments |
| 2026-07-10 15:36 | `f35c919` | SLMpixelSizeUpdate | **Metric grating/aperture matching** + `compare_slm_holograms.m` (175) |
| 2026-07-10 15:37 | `0359267` | Update applyMask.m | Mask fix |
| 2026-07-10 16:40 | `9f1a8e9` | Holoeye | **`holoeye_focus_scan.m`** (95) — 3f-ring calibration sweep |
| 2026-07-10 17:29 | `bd7d6fe` | holoeye2.0 | **Wavelength-aware `modMaxGray`** formula from the CLUT manual |
| 2026-07-13 17:26 | `ffcb7d0` | Holo filpped | **`cfg.invertPhase`** root-cause fix; `bessel_ring_test.m` (83); `bessel_ring_capture.png`; metric `lensSep_m` |
| 2026-07-21 12:00 | `998370c` | Tunned | Bench parameter tuning (`orientMult`, grating, alignment) |
| 2026-07-27 17:09 | `bb8996b` | WRA | **`polarization_wra_dual_slm.m`** (523 lines) |
| 2026-07-29 16:47 | `4073184` | WRA | **`optics.wignerRotation`** (445), **`optics.applyWRA`** (203), `wigner_rotation_lensing.m` (140), `caustic_polarization_z500.m` (139), `dual_slm_phase_maps.m` (230), `docs/WRA_bench_setup.md` (248), 2 figures |

| 2026-07-29 17:38 | `e3c6b10` | Create PROJECT_LOG.md | This log committed |

Plus 6 merge commits synchronizing with the GitHub remote (and one PR merge, `c658657`).

## Appendix B — working-session ledger

| Session date(s) | Topic | Principal outcome |
|---|---|---|
| ≈ 2025 → 2026-04 | **Pre-repository bench campaign** (no transcripts; §5 Phase −1) | Quantum-pendulum warm-up; grating/diffraction-order working window found; vortex-null alignment diagnostic invented; ThorLabs automation, image analysis, and merger movie built; the multi-wavelength `d̂` and `r_S` scans that the manuscript reports |
| 2026-06-24 | Three-feature request | `autoExpose`, `applyMask`, wavelength-aware calibration; requirements refined live across 5 exchanges |
| 2026-06-29 | Stationary-phase parameter matching | Explained why the stationary-phase image focused closer than `gravityLens`; added the 4-panel A/B comparison; surfaced the `pixPerUnit` question |
| 2026-06-30 (day) | BNS P512 revival | EDID decoded, timings and SDK status established; device did not modulate; `display.m` generalized to embed undersized holograms |
| 2026-06-30 (evening) | Stationary-phase v2 | Physics decoupled from `pixPerUnit`; minimal-pixel design; caustic-fidelity sweep; GO breakdown quantified |
| 2026-07-02 → 07-06 | Dual-SLM support | Device-dispatching config; vortex alignment hologram (winding = 3.000); per-device temp bitmap; mixed-DPI fullscreen fix |
| 2026-07-10 | Cross-SLM matching + 3f ring | Metric grating/aperture matching (≤ 9° RMS); phase-depth diagnosis; `modMaxGray` formula derived from the CLUT manual; NIR-145 identified; 4π hypothesis killed |
| 2026-07-13 | Bessel / defocus / phase inversion | SLM cleared; camera located 35 cm past focus; J0 Bessel captured; **phase-inversion root cause found and two earlier conclusions retracted** |
| 2026-07-15 | Poster (largest session) | 3-column poster restructured; equations corrected against the paper; caustic figures generated (`corr = 0.850` at 82.4 %, `0.679` at 51.4 %); VS Code XeLaTeX build fixed |
| 2026-07-22 | Polarization / WRA simulation | Dual-SLM Jones model; rotator vs retarder; H/V ↔ L/R equivalence explained; per-element ellipse figure |
| 2026-07-29 | Full-GR WRA modules | Kerr tetrad pipeline with verified invariants; physical-scale mode with flat-frame subtraction; caustic-with-polarization at z = 500 mm; bench tutorial |

## Appendix C — complete file map

```
OpticsLab26-27/
├── slm_config.m                     218   device-dispatching, wavelength-aware SLM config
├── thorlab_hardware_config.m         31   device serials and paths
├── SincInv.mat                            sinc-inverse LUT for CAM encoding
│
├── +optics/                        1533   optical computation + SLM output (18 files)
│   ├── wignerRotation.m             445   Kerr tetrad/Lorentz WRA pipeline
│   ├── stationaryLens.m             419   stationary-phase binary-lens hologram
│   ├── applyWRA.m                   203   WRA acting on input polarization
│   ├── alignmentHologram.m          138   grating + vortex alignment pattern
│   ├── display.m                    125   fullscreen output, per-monitor, invertPhase
│   ├── hologram.m / gravityLens.m 99/99   encoding / high-level lens pipeline
│   ├── modMaxGray.m                  94   λ → 2π gray level (PCHIP)
│   ├── listScreens.m                 88   monitor enumeration
│   ├── laguerreGauss.m               86   LG modes
│   ├── field.m                       76   lensed field, 3 phase models
│   ├── aberration.m                  65   Zernike correction
│   ├── applyMask.m                   56   aperture + beam dump
│   ├── gratingAngle.m                47   angle-specified grating
│   └── coordinates.m, close.m, grating.m, ellipticalCoordinates.m
│
├── +analysis/                       838   post-processing (3 files)
│   ├── phaseMap.m                   501   phase-shifting reconstruction + vortex detection
│   ├── imageAnalysis.m              217   z-scan merge, drift correction, intensity tracking
│   └── movie.m                      120   PNG sequence → MP4 with overlays
│
├── +camera/                         392   init, capture, setExposure, setGain, autoExpose, close
├── +stage/                          101   init, moveTo, home, close
├── +sim/                            144   hardware simulator (camera / optics / stage)
├── examples/                       2469   19 runnable experiment and test scripts
│
├── docs/
│   ├── README.md                          full user guide
│   ├── WRA_bench_setup.md           248   WRA bench-build tutorial
│   ├── PROJECT_LOG.md                     this file
│   └── figures/                           WRABenchSetupSketch.png, Dual_SLMPhaseMaps.png
│
├── Lab_GravLensing_Poster_Ver_01/         3-column XeLaTeX poster + 12 figures
├── Holoeye/                               PLUTO-2.1 manuals, CLUT config library, SDK, per-unit .h5
├── LibDLL/                                37 Thorlabs SDK DLLs (isolated; root must stay clean)
├── ebin0626/                              73 × 4096×3000 interferograms + movie (git-ignored)
├── Optical_Lab_Binary-2.pdf               BML paper (Moreso Serra, Bulashenko, Gu et al. 2026)
├── Millers41598-024-71203-x.pdf           Noh, Alsing, Miller & Ahn, Sci. Rep. 14, 20801 (2024)
├── bessel_ring_capture.png                captured J0 Bessel (defocus-diagnosis evidence)
└── CapturedImage.png                      sample camera frame
```

---

*Log compiled 2026-07-29 from git history, project memory, session transcripts, repository
documentation, LaTeX poster source, and data directories.*
*Extended 2026-07-30 with the pre-repository bench campaign, the two bench-side debugging case
studies (§6.6–6.7), the manuscript results and figure-level attribution (§9.1), the full
dissemination ledger (§9.3), and the application-material index (§12) — sources tagged **[ms]**
(submitted manuscript) and **[account]** (the developer's own written record of bench work outside
this repository).*
