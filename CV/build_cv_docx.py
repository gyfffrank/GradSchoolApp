#!/usr/bin/env python3
"""Generate CV/cv.docx from the structured CV content."""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

LINK = RGBColor(0x00, 0x33, 0x99)
DARK = RGBColor(0x1a, 0x1a, 0x1a)

doc = Document()

# ---- base style ----
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10.5)
normal.paragraph_format.space_after = Pt(0)
normal.paragraph_format.space_before = Pt(0)

sec = doc.sections[0]
sec.top_margin = Inches(0.6)
sec.bottom_margin = Inches(0.6)
sec.left_margin = Inches(0.7)
sec.right_margin = Inches(0.7)

RIGHT_TAB = Inches(7.1)  # page width minus margins


def add_bottom_border(paragraph):
    p = paragraph._p
    pPr = p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "888888")
    pbdr.append(bottom)
    pPr.append(pbdr)


def name_heading(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    r.font.size = Pt(22)
    r.font.bold = True
    r.font.color.rgb = DARK
    return p


def contact_line(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(8)
    r = p.add_run(text)
    r.font.size = Pt(9.5)
    r.font.color.rgb = DARK
    return p


def section(title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(title.upper())
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = DARK
    r.font.name = "Calibri"
    # letter spacing
    rPr = r._element.get_or_add_rPr()
    spc = OxmlElement("w:spacing")
    spc.set(qn("w:val"), "30")
    rPr.append(spc)
    add_bottom_border(p)
    return p


def entry(left, right=None, extra=None):
    """Bold role line with optional right-aligned date and optional plain extra (e.g. GPA)."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(1)
    if right:
        p.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB, WD_TAB_ALIGNMENT.RIGHT)
    rb = p.add_run(left)
    rb.font.bold = True
    rb.font.size = Pt(10.5)
    if extra:
        re = p.add_run("  " + extra)
        re.font.italic = True
        re.font.size = Pt(10)
    if right:
        rr = p.add_run("\t" + right)
        rr.font.italic = True
        rr.font.size = Pt(10)
    return p


def bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    r.font.size = Pt(10)
    return p


def plain(text, before=0, after=2):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    r = p.add_run(text)
    r.font.size = Pt(10)
    return r, p


# ============================ CONTENT ============================

name_heading("Yufeng (Frank) Gu")
contact_line(
    "Colgate University  |  13 Oak Drive  |  ygu1@colgate.edu  |  "
    "GitHub: gyfffrank  |  LinkedIn: yufeng-gu-gyf04"
)

# ---- Education ----
section("Education")
entry("Colgate University, Hamilton, NY | Bachelor of Arts",
      right="May 2027", extra="(GPA: 3.92/4.00)")
bullet("Majors: Physics and History-Historiography Pathway")
bullet("Alumni Memorial Scholar, a selective student community of 15 members in each class year, "
       "recognizing dedication to scholarship and academic excellence. Selectees are granted "
       "10,000 USD for independent research and skill development.")
bullet("Dean's Award with Distinction (All semesters)")
bullet("Relevant Coursework: Atom and Waves, Intro to Mechanics, Intro to Electricity and "
       "Magnetism, Electronics, Introduction to Quantum Mechanics, Mathematical Methods of "
       "Physics, Classical Mechanics, Planetary Science, Quantum Mechanics, Nonlinear Dynamics "
       "& Chaos, Calculus I-III.")

entry("Stanford Online High School: Modern Physics (XP 670)",
      right="Aug-Dec 2022", extra="(Grade: 80/100)")
bullet("Completed semester-long coursework in special and general relativity, experimental "
       "quantum mechanics, quantum computation, and quantum information")

# ---- Research Experiences ----
section("Research Experiences")
entry("Student Researcher | Department of Physics | Colgate University", right="Apr 2025 - Present")
bullet("Laboratory Astrophysics of Gravitational Lensing - Working with Professor Galvez, "
       "designed and carried out an optical simulation of gravitational lensing using laser beams "
       "modulated by a spatial light modulator (SLM) to emulate spacetime curvature. Implemented "
       "phase profiles corresponding to single and binary Schwarzschild lenses and experimentally "
       "reproduced interference and fringe patterns analogous to Einstein rings. Quantitatively "
       "compared theoretical predictions with measured intensity profiles, demonstrating "
       "agreement in fringe structure and evolution relevant to binary systems and black hole "
       "mergers. Relative work was presented during the OPICA/FIO conference in Denver, CO, and "
       "is currently being prepared for publication.")
bullet("Optical Analog of Quantum Pendulum Dynamics - Working with Professor Galvez, designed "
       "and experimentally realized a structured optical beam exploiting the equivalence between "
       "the Helmholtz and Schrödinger equations. Generated a Fourier-plane image encoding a "
       "superposition of 11 pendular eigenstates, with ring radii proportional to energy and "
       "angular modulation proportional to quantum probability density, including bound and rotor "
       "states. This work has been submitted to Physics Today (Backscatter) for review.")

entry("Student Researcher | Department of Physics | Colgate University", right="Sep 2024 - Jan 2025")
bullet("Collaborate with Professor Lam, utilizing post-fit data of NanoGrav program, analyzing "
       "red noise effects in pulsar timing by Python Libraries including SciPy, AstroPy, Pandas, "
       "and Matplotlib to attempt to improve gravitational wave detection.")
bullet("Utilize currently available data sets to analyze unidentified radio-frequency-dependent "
       "effects of interstellar materials with Python by irregular auto-regression model and "
       "corresponding power spectral density graph.")

entry("Student Researcher | Department of Physics | Colgate University", right="Mar 2024 - Aug 2024")
bullet("Analyzed archival data from JWST and used machine learning in collaboration with Prof. "
       "Ilie to identify potential supermassive dark star candidates and investigate properties "
       "of Dark Matter.")

entry("Research Assistant | Chinese Academy of Sciences | Beijing, China", right="Apr 2021 - Jul 2021")
bullet("Performed data collection, analysis with Matlab, simulation with FLUENT, and experiment "
       "report writing to assist researchers and Ph.D. students in the thermal engineering lab "
       "after completing a 2-month training workshop.")

# ---- Campus Community Involvement ----
section("Campus Community Involvement")
entry("Co-founder & VP | Engineering and Design Club | Colgate University", right="Sep 2024 - Present")
bullet("Collaborate with peers and faculty of the physics department, founding a club that allows "
       "members to propose their own engineering projects and provides access for these "
       "interested students to funds and gear that facilitate their creativity.")
bullet("Assume the leadership role of vice president in the club, assisting the President in "
       "leading the club by contributing to project proposal reviews, strategic initiatives, "
       "discussions, collaborations, and outreach with student organizations and staff. Also, "
       "oversee key administrative functions including elections, leadership transitions, and "
       "appeals committees.")
bullet("Successfully proposed, fundarised, and led the first project of the club, which is to "
       "design and build an off-raod go kart from scratch, and currently co-leading a team of 15 "
       "members to work on the project by organizing weekly meetings, delegating tasks, and "
       "providing technical guidance.")

entry("Secretary | Ski and Snowboard Club | Colgate University", right="Jan 2025 - Present")
bullet("Collaborate with other club leaders and trip leaders to ensure the safety of the club "
       "outreach activities to Greek, Song, and Labrador Mountains, coordinate with school's "
       "accounting office for funding on outreach meals, and get ready to answer any kind of "
       "questions.")
bullet("Designed and coded an automated online sign-up form for members which has been used for "
       "the club's outreach activities and has significantly improved the efficiency of trip "
       "organization and member management.")

entry("Residential Assistance | ResLife Office | Colgate University", right="Aug 2025 - May 2025")
bullet("Facilitated community meetings, supported residents' academic and personal well-being "
       "through resource referrals, mediated conflicts, and upheld community standards.")
bullet("Collaborated with Residential Life staff on orientation, hall operations, and safety "
       "protocols while serving as a liaison between residents and university offices")

entry("Tutor for PHSY 343 | Department of Physics | Colgate University", right="Jan 2026 - May 2026")
bullet("Assist Professor Enrique Galvez in setting up the electronics lab, clarifying lab "
       "instructions, helping and inspiring students to design digital and analog circuits to "
       "solve certain problems.")

entry("Tutor for PHSY 205 | Department of Physics | Colgate University", right="Jan 2026 - May 2026")
bullet("Assist professor Patrick Crotty by organizing homework help sessions for PHSY 205, "
       "clarifying concepts on differential equations, complex algebra, Fourier transformation, "
       "and other mathematical tools for physicists, answering questions on the homework "
       "problems, and helping peers to prepare for the exams.")

entry("Tutor for PHSY 125 | Department of Physics | Colgate University", right="Aug 2025 - Dec 2025")
bullet("Assist the department in designing this new course, and help students with broad topics "
       "from nanophysics, biophysics, to planetary sciences.")

entry("Tutor for PHSY 232 | Department of Physics | Colgate University", right="Jan 2025 - May 2025")
bullet("Assist professor Michael Lam to organize recitation sessions for PHSY 232 Intro to "
       "Mechanics two hours per week, clarifying concepts on mechanics and astronomy, answering "
       "questions on the recitation problems, and sharing my experience of study and research "
       "with peers.")
bullet("Assist lab manager Hans Benze to organize Lab sessions for three hours per week, "
       "clarifying lab instructions and helping students with theoretical, instrumental, and "
       "coding problems they have.")

entry("Tutor for PHSY 131 | Department of Physics | Colgate University", right="Aug 2024 - Dec 2024")
bullet("Organize tutoring sessions for two to five hours per week for PHSY 131 Atoms and Waves, "
       "clarifying key concepts and helping students with coursework and homework about extensive "
       "topics from classical mechanics to modern relativity and quantum physics.")

entry("Bassist | Colgate Jazz Band | Colgate University", right="Sep 2023 - May 2024")
bullet("Studied jazz theory and performed improvisational classical jazz music to showcase skills "
       "and provide entertainment for peers at Donovan's Pub.")

entry("Student Worker | Chobani Cafe | Colgate University", right="Jan 2024 - May 2024")
bullet("Developed proficiency in preparing a variety of sandwiches, yogurt, salads, coffee, and "
       "drinks to ensure accurate order based on preferences and dietary constraints.")

# ---- Program ----
section("Program")
entry("Researcher, Co-developer | Koopman Operator Analysis of Chua's Circuit | Colgate University",
      right="Apr 2026 - May 2026")
bullet("Applied Koopman operator theory and Extended Dynamic Mode Decomposition (EDMD) in MATLAB "
       "to analyze a physical Chua's circuit across four dynamical regimes (fixed point, limit "
       "cycle, period-doubled, and double-scroll chaos), comparing polynomial, radial basis "
       "function, and piecewise-linear observable dictionaries to optimize spectral accuracy.")
bullet("Implemented Lyapunov spectrum computation and box-counting fractal dimension algorithms "
       "to characterize attractor geometry; developed Koopman eigenfunction visualizations that "
       "revealed hidden geometric structure within the chaotic double-scroll attractor.")
bullet("Acquired real-time experimental data from a hardware Chua circuit via Arduino R4 Minima "
       "with a custom MATLAB serial interface; co-authored a written report and presented "
       "findings as a Nonlinear Dynamics & Chaos course project.")

entry("Modeler, Research Organizer | China Thinks Big | Chengdu No.7 High School", right="Oct 2022")
bullet("Conducted a linguistic philosophical-based double-blind experiment to test the "
       "correlation between popular short video screening and intellectual abilities in "
       "collaboration with peers of different interests.")
bullet("Created an Analytic Hierarchy Process with Matlab based on Ludwig Wittgenstein's "
       "linguistic philosophy and proved the negative correlation between reading speed and short "
       "video screening time.")
bullet("Wrote a script in the style of Faulkner's stream of consciousness for a hand-made anime "
       "to warn the potential danger of short video screening which was viewed 5,000 times "
       "online.")

# ---- Technical Skills ----
section("Technical Skills")
r, p = plain("", before=2, after=2)
rb = p.add_run("Proficient: ")
rb.font.bold = True
rb.font.size = Pt(10)
rt = p.add_run("MATLAB, Java, Python (SciPy, AstroPy, NumPy, Pandas, and Matplotlib), LaTeX, "
               "Mathematical Modeling (Finalist in the High School Mathematical Contest in "
               "Modeling (HiMCM) hosted by MAA and COMAP)")
rt.font.size = Pt(10)

r2, p2 = plain("", before=2, after=2)
rb2 = p2.add_run("Basic: ")
rb2.font.bold = True
rb2.font.size = Pt(10)
rt2 = p2.add_run("C++, Machine Learning, Fluent.")
rt2.font.size = Pt(10)

out = r"C:\Users\user\Documents\GitHub\GradSchoolApp\CV\cv.docx"
doc.save(out)
print("Saved", out)
