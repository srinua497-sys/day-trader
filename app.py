import streamlit as st
from datetime import datetime

# ==========================================
# JEE AI PRO - COMPLETE APPLICATION
# Run with:  streamlit run app.py
# ==========================================

st.set_page_config(page_title="JEE AI PRO", page_icon="🎓", layout="wide")

st.markdown("""
<style>
.main { background-color: #0e1117; }
.stButton>button { width: 100%; border-radius: 10px; font-weight: bold; }
.card {
    background: #1c2433;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE
# ==========================================
DEFAULT_STATE = {
    "score": 0,
    "attempts": 0,
    "history": [],
    "mock_submitted": False,
    "mock_result": 0,
    "mock_questions": None,
    "study_selection": {},
    "practice_checked": {},
}
for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ==========================================
# DATA
# ==========================================
SUBJECTS = {
    "Physics": [
        "Units and Dimensions", "Kinematics", "Laws of Motion",
        "Work Energy Power", "Rotational Motion", "Gravitation",
        "Thermodynamics", "Electrostatics", "Current Electricity",
        "Magnetism", "Optics", "Modern Physics",
    ],
    "Chemistry": [
        "Some Basic Concepts", "Atomic Structure", "Chemical Bonding",
        "Thermodynamics", "Equilibrium", "Electrochemistry",
        "Chemical Kinetics", "Organic Chemistry", "Hydrocarbons",
        "Aldehydes and Ketones", "Coordination Compounds",
    ],
    "Mathematics": [
        "Sets and Relations", "Complex Numbers", "Quadratic Equations",
        "Sequences and Series", "Straight Lines", "Circle",
        "Conic Sections", "Limits", "Continuity", "Differentiation",
        "Integration", "Matrices and Determinants", "Probability",
    ],
}

LEARNING_SECTIONS = [
    "Theory",
    "Important Formulas",
    "Solved Examples",
    "Practice Problems",
    "Most Important Questions",
]

# ------------------------------------------
# STUDY MATERIAL (all chapters)
# ------------------------------------------
def _bul(items):
    return "\n".join(f"- {i}" for i in items)


def _num(items):
    return "\n".join(f"{n}. {t}" for n, t in enumerate(items, 1))


def _build(theory, formulas, example, practice, answers, focus):
    return {
        "Theory": _bul(theory),
        "Important Formulas": _bul(formulas),
        "Solved Examples": example,
        "Practice Problems": _num(practice) + "\n\n**Answers:** " + answers,
        "Most Important Questions": (
            "**Frequently tested in JEE Main / Advanced:**\n\n" + _bul(focus) +
            "\n\nFor exact past-paper questions, use the official papers at "
            "jeemain.nta.nic.in and jeeadv.ac.in and add verified questions here."
        ),
    }


STUDY_CONTENT = {}

# ======================== PHYSICS ========================

STUDY_CONTENT[("Physics", "Units and Dimensions")] = _build(
    theory=[
        "Seven SI base quantities: length (m), mass (kg), time (s), current (A), temperature (K), amount of substance (mol), luminous intensity (cd).",
        "Dimensions show how a quantity depends on base quantities, e.g. force = [M L T⁻²].",
        "Principle of homogeneity: every term in a valid physical equation has the same dimensions.",
        "Uses: checking equations, deriving relations, converting units. Limits: cannot find dimensionless constants, and fails for sin/log/exp of dimensional arguments or for sums of several terms.",
        "Errors: in a sum or difference, absolute errors add; in a product or quotient, relative errors add.",
        "Significant figures: leading zeros are not significant; trailing zeros after a decimal point are.",
    ],
    formulas=[
        "Force [MLT⁻²], Energy/Work [ML²T⁻²], Power [ML²T⁻³]",
        "Pressure [ML⁻¹T⁻²], Momentum [MLT⁻¹], Angular momentum [ML²T⁻¹]",
        "Planck's constant h [ML²T⁻¹], Gravitational constant G [M⁻¹L³T⁻²]",
        "For Z = Aᵃ Bᵇ : ΔZ/Z = a(ΔA/A) + b(ΔB/B)",
    ],
    example=(
        "**Example.** Find the dimensions of G from F = G m₁m₂ / r².\n\n"
        "G = F r² / (m₁m₂) = [MLT⁻²][L²] / [M²] = **[M⁻¹ L³ T⁻²]**."
    ),
    practice=[
        "Find the dimensions of pressure.",
        "If T ∝ lᵃ gᵇ for a simple pendulum, find a and b.",
        "Length 5.0 ± 0.1 cm and width 2.0 ± 0.1 cm. Find the percentage error in area.",
    ],
    answers="1) [ML⁻¹T⁻²]  2) a = 1/2, b = −1/2  3) 0.1/5 + 0.1/2 = 0.07, so 7%",
    focus=["Dimensional analysis to derive formulas", "Error propagation", "Least count of vernier and screw gauge"],
)

STUDY_CONTENT[("Physics", "Kinematics")] = _build(
    theory=[
        "Kinematics describes motion without considering its cause.",
        "Displacement is a vector; distance is a scalar. Velocity = d(displacement)/dt; acceleration = d(velocity)/dt.",
        "Slope of x-t graph gives velocity; slope of v-t graph gives acceleration; area under v-t graph gives displacement.",
        "In projectile motion, horizontal and vertical motions are independent: a_x = 0, a_y = −g.",
        "Relative velocity: v_AB = v_A − v_B (river-boat and rain-man problems).",
    ],
    formulas=[
        "v = u + at;  s = ut + ½at²;  v² = u² + 2as",
        "Distance in nth second: s_n = u + a(2n − 1)/2",
        "Projectile: T = 2u sinθ / g,  H = u² sin²θ / 2g,  R = u² sin2θ / g",
    ],
    example=(
        "**Example.** A car starts from rest and accelerates at 2 m/s² for 5 s. Find v and s.\n\n"
        "v = 0 + 2(5) = **10 m/s**;  s = ½(2)(5²) = **25 m**."
    ),
    practice=[
        "A body is thrown up at 20 m/s. Find the maximum height (g = 10).",
        "Range of a projectile at 30 m/s and 45° (g = 10).",
        "A train slows from 30 to 10 m/s in 10 s. Find a and the distance covered.",
    ],
    answers="1) 20 m  2) 90 m  3) a = −2 m/s², s = 200 m",
    focus=["Projectile motion", "Graph interpretation", "Relative motion and river-boat problems"],
)

STUDY_CONTENT[("Physics", "Laws of Motion")] = _build(
    theory=[
        "First law: a body stays at rest or in uniform motion unless a net force acts (inertia).",
        "Second law: F = dp/dt. Third law: action and reaction are equal and opposite and act on different bodies.",
        "Friction: static friction adjusts up to μₛN; kinetic friction is μₖN.",
        "Always draw a free-body diagram. In a non-inertial frame add a pseudo force −ma.",
        "Constraint relations (strings, pulleys) link accelerations of connected bodies.",
    ],
    formulas=[
        "F = ma;  p = mv",
        "fₛ ≤ μₛN;  fₖ = μₖN",
        "Smooth incline: a = g sinθ;  rough incline: a = g(sinθ − μ cosθ)",
        "Atwood machine: a = (m₁ − m₂)g / (m₁ + m₂)",
        "Angle of repose: tanθ = μₛ",
    ],
    example=(
        "**Example.** A 5 kg block is pulled by 20 N on a surface with kinetic friction 5 N. Find a.\n\n"
        "Net force = 20 − 5 = 15 N, so a = 15/5 = **3 m/s²**."
    ),
    practice=[
        "A 2 kg block rests on a surface with μₛ = 0.5. Minimum force to move it (g = 10)?",
        "Acceleration of a block down a smooth 30° incline?",
        "Masses 3 kg and 2 kg hang over a smooth pulley. Find the acceleration.",
    ],
    answers="1) 10 N  2) 5 m/s²  3) 2 m/s²",
    focus=["Pulley and block systems", "Friction on inclines", "Pseudo force in lifts and accelerating frames"],
)

STUDY_CONTENT[("Physics", "Work Energy Power")] = _build(
    theory=[
        "Work is the dot product of force and displacement; it can be negative.",
        "Work-energy theorem: net work equals change in kinetic energy.",
        "Conservative forces (gravity, spring) have potential energy; mechanical energy is conserved when only they act.",
        "Collisions: momentum is always conserved; kinetic energy is conserved only in elastic collisions.",
        "Power is the rate of doing work.",
    ],
    formulas=[
        "W = F d cosθ;  K = ½mv²;  U = mgh;  U_spring = ½kx²",
        "P = W/t = F·v",
        "Coefficient of restitution e = (v₂ − v₁)/(u₁ − u₂); e = 1 elastic, e = 0 perfectly inelastic",
        "Elastic 1D: v₁ = [(m₁ − m₂)u₁ + 2m₂u₂]/(m₁ + m₂)",
    ],
    example=(
        "**Example.** A 2 kg body at rest is pushed by a 10 N force over 5 m. Find the final speed.\n\n"
        "W = 10 × 5 = 50 J = ½(2)v², so v = √50 ≈ **7.07 m/s**."
    ),
    practice=[
        "A ball falls from 20 m (g = 10). Speed just before impact?",
        "Energy stored in a spring k = 200 N/m compressed by 0.1 m?",
        "Power of an engine exerting 2000 N at 10 m/s?",
    ],
    answers="1) 20 m/s  2) 1 J  3) 20 kW",
    focus=["Spring-block energy problems", "Collisions and restitution", "Variable force work by integration"],
)

STUDY_CONTENT[("Physics", "Rotational Motion")] = _build(
    theory=[
        "Torque τ = r × F causes angular acceleration.",
        "Moment of inertia depends on the mass distribution and the axis.",
        "Angular momentum is conserved when net external torque is zero.",
        "Rolling without slipping: v_cm = ωR; total kinetic energy = translational + rotational.",
        "Parallel axis theorem: I = I_cm + Md². Perpendicular axis theorem applies to planar bodies.",
    ],
    formulas=[
        "τ = Iα;  L = Iω;  K = ½Iω²",
        "Ring MR², disc ½MR², solid sphere (2/5)MR², hollow sphere (2/3)MR², rod about centre ML²/12, rod about end ML²/3",
        "Rolling on incline: a = g sinθ / (1 + I/MR²)",
    ],
    example=(
        "**Example.** Disc M = 2 kg, R = 0.5 m, torque 5 N·m. Find α.\n\n"
        "I = ½MR² = ½(2)(0.25) = 0.25 kg·m², α = τ/I = **20 rad/s²**."
    ),
    practice=[
        "A ring and a disc roll down the same incline from rest. Which reaches the bottom first?",
        "Write I of a solid sphere about its diameter.",
        "A skater pulls her arms in. What happens to ω?",
    ],
    answers="1) Disc (smaller I/MR²)  2) (2/5)MR²  3) ω increases because L is conserved",
    focus=["Rolling on inclines", "Angular momentum conservation", "Moment of inertia with axis shifts"],
)

STUDY_CONTENT[("Physics", "Gravitation")] = _build(
    theory=[
        "Newton's law: every mass attracts every other mass with a force along the line joining them.",
        "g varies with height and depth, and is lower at the equator because of Earth's rotation.",
        "Kepler: orbits are ellipses; equal areas in equal times; T² ∝ r³.",
        "Orbital and escape velocities are independent of the satellite's mass.",
        "Gravitational potential energy is negative and zero at infinity.",
    ],
    formulas=[
        "F = G m₁m₂ / r²;  g = GM/R²",
        "g at height h ≈ g(1 − 2h/R);  at depth d: g(1 − d/R)",
        "v_orbit = √(GM/r);  v_escape = √(2GM/R) = √(2gR) ≈ 11.2 km/s",
        "U = −GMm/r;  total energy in orbit = −GMm/2r",
    ],
    example=(
        "**Example.** Find g at a height equal to Earth's radius.\n\n"
        "g' = GM/(2R)² = g/4, so **g/4**."
    ),
    practice=[
        "Orbital velocity near Earth's surface (g = 10, R = 6.4 × 10⁶ m)?",
        "Ratio of escape velocity to orbital velocity near the surface?",
        "Weight of a body at height R compared with surface weight?",
    ],
    answers="1) 8 km/s  2) √2  3) 1/4",
    focus=["Satellite energy and velocity", "Variation of g", "Kepler's laws"],
)

STUDY_CONTENT[("Physics", "Thermodynamics")] = _build(
    theory=[
        "First law: heat supplied equals the change in internal energy plus work done by the gas.",
        "Isothermal: T constant. Adiabatic: no heat exchange. Isochoric: V constant. Isobaric: P constant.",
        "Internal energy of an ideal gas depends only on temperature.",
        "Carnot engine has the maximum efficiency between two temperatures.",
        "Degrees of freedom: monoatomic 3, diatomic 5 (at ordinary T).",
    ],
    formulas=[
        "ΔU = Q − W;  W_isothermal = nRT ln(V₂/V₁)",
        "Adiabatic: PVᵞ = constant;  W = (P₁V₁ − P₂V₂)/(γ − 1)",
        "Cp − Cv = R;  γ = Cp/Cv;  ΔU = nCvΔT",
        "Carnot efficiency η = 1 − T₂/T₁",
    ],
    example=(
        "**Example.** Carnot engine between 600 K and 300 K. Efficiency?\n\n"
        "η = 1 − 300/600 = **50%**."
    ),
    practice=[
        "Work done by 1 mol at 300 K in isothermal doubling of volume (R = 8.314)?",
        "Efficiency of a Carnot engine between 500 K and 300 K?",
        "ΔU for 2 mol of monoatomic gas heated by 50 K?",
    ],
    answers="1) RT ln2 ≈ 1.73 kJ  2) 40%  3) (3/2)(2)(8.314)(50) ≈ 1247 J",
    focus=["PV diagrams and cyclic processes", "Adiabatic vs isothermal", "Carnot efficiency"],
)

STUDY_CONTENT[("Physics", "Electrostatics")] = _build(
    theory=[
        "Like charges repel, unlike attract; charge is quantised and conserved.",
        "Electric field is force per unit charge; potential is work per unit charge.",
        "Gauss's law relates flux through a closed surface to enclosed charge.",
        "Field inside a conductor is zero; excess charge resides on the surface.",
        "Capacitors store energy in the electric field.",
    ],
    formulas=[
        "F = kq₁q₂/r², k = 9 × 10⁹ N·m²/C²;  E = kq/r²;  V = kq/r",
        "Gauss: ∮E·dA = q_enc/ε₀",
        "C = ε₀A/d;  U = ½CV²",
        "Series: 1/C = Σ1/Cᵢ;  parallel: C = ΣCᵢ",
        "Dipole: p = qd;  torque τ = pE sinθ",
    ],
    example=(
        "**Example.** Force between two 1 µC charges 1 m apart.\n\n"
        "F = 9×10⁹ × 10⁻¹² / 1 = **9 × 10⁻³ N**."
    ),
    practice=[
        "Electric field 1 m from a 1 µC point charge?",
        "Equivalent capacitance of 2 µF and 3 µF in parallel?",
        "Energy in a 10 µF capacitor at 100 V?",
    ],
    answers="1) 9000 N/C  2) 5 µF  3) 0.05 J",
    focus=["Gauss's law applications", "Capacitor networks", "Potential of charge distributions"],
)

STUDY_CONTENT[("Physics", "Current Electricity")] = _build(
    theory=[
        "Current is rate of flow of charge; drift velocity is the average velocity of electrons.",
        "Ohm's law holds for ohmic conductors; resistance depends on material and geometry.",
        "Kirchhoff's laws: junction rule (charge conservation) and loop rule (energy conservation).",
        "Wheatstone bridge is balanced when P/Q = R/S.",
        "A cell has internal resistance, so terminal voltage drops under load.",
    ],
    formulas=[
        "V = IR;  R = ρl/A;  I = neAvd",
        "Series: R = ΣRᵢ;  parallel: 1/R = Σ1/Rᵢ",
        "P = VI = I²R = V²/R;  H = I²Rt",
        "Terminal voltage V = E − Ir",
    ],
    example=(
        "**Example.** A 12 V battery with 1 Ω internal resistance drives a 5 Ω load. Find I and terminal voltage.\n\n"
        "I = 12/(5 + 1) = 2 A;  V = 12 − 2(1) = **10 V**."
    ),
    practice=[
        "Two 6 Ω resistors in parallel: equivalent?",
        "Power of a 220 V, 44 Ω heater?",
        "Equivalent of 2 Ω, 3 Ω, 6 Ω in parallel?",
    ],
    answers="1) 3 Ω  2) 1100 W  3) 1 Ω",
    focus=["Kirchhoff's law circuits", "Meter bridge and potentiometer", "Internal resistance problems"],
)

STUDY_CONTENT[("Physics", "Magnetism")] = _build(
    theory=[
        "Moving charges create magnetic fields (Biot-Savart law); Ampere's law handles symmetric cases.",
        "Magnetic force on a charge is perpendicular to velocity, so it does no work.",
        "A charge in a uniform field moves in a circle or helix.",
        "Faraday's law: induced EMF equals the rate of change of flux; Lenz's law gives its direction.",
        "A current loop in a field experiences torque (basis of the galvanometer).",
    ],
    formulas=[
        "F = qv × B;  F = BIl sinθ;  r = mv/(qB)",
        "Long wire: B = μ₀I/(2πr);  loop centre: B = μ₀I/(2R);  solenoid: B = μ₀nI",
        "τ = NIAB sinθ",
        "EMF = −dΦ/dt;  motional EMF = Blv",
    ],
    example=(
        "**Example.** Field 0.1 m from a long wire carrying 10 A.\n\n"
        "B = (4π×10⁻⁷ × 10)/(2π × 0.1) = **2 × 10⁻⁵ T**."
    ),
    practice=[
        "Field at the centre of a 10 cm radius loop carrying 5 A?",
        "Force on a 0.4 m wire carrying 2 A in a 0.5 T field (perpendicular)?",
        "Field in a solenoid with 1000 turns/m and 2 A?",
    ],
    answers="1) π × 10⁻⁵ T ≈ 3.14 × 10⁻⁵ T  2) 0.4 N  3) ≈ 2.5 × 10⁻³ T",
    focus=["Motion of charges in B fields", "Ampere's law", "Electromagnetic induction"],
)

STUDY_CONTENT[("Physics", "Optics")] = _build(
    theory=[
        "Reflection: angle of incidence equals angle of reflection. Refraction obeys Snell's law.",
        "Total internal reflection occurs from a denser to a rarer medium beyond the critical angle.",
        "Use the sign convention consistently (distances measured from the pole or optical centre).",
        "Young's double slit: bright fringes where path difference is nλ, dark where it is (n + ½)λ.",
        "Diffraction and polarisation show the wave nature of light.",
    ],
    formulas=[
        "Mirror: 1/v + 1/u = 1/f;  lens: 1/v − 1/u = 1/f",
        "n = sin i / sin r;  sin C = 1/n",
        "Lens maker: 1/f = (n − 1)(1/R₁ − 1/R₂)",
        "Fringe width β = λD/d;  Malus' law I = I₀cos²θ",
    ],
    example=(
        "**Example.** Object 30 cm from a concave mirror of f = 20 cm.\n\n"
        "u = −30, f = −20: 1/v = −1/20 + 1/30 = −1/60, so v = −60 cm (real image); "
        "m = −v/u = **−2** (inverted, twice the size)."
    ),
    practice=[
        "Critical angle for n = √2?",
        "Fringe width for d = 1 mm, D = 1 m, λ = 500 nm?",
        "Convex lens f = 20 cm, object at 40 cm: image distance and magnification?",
    ],
    answers="1) 45°  2) 0.5 mm  3) v = 40 cm, m = −1",
    focus=["Lens and mirror combinations", "YDSE and path difference", "Total internal reflection"],
)

STUDY_CONTENT[("Physics", "Modern Physics")] = _build(
    theory=[
        "Photoelectric effect: electrons are emitted only if photon energy exceeds the work function.",
        "de Broglie: matter has a wavelength λ = h/p.",
        "Bohr model: electrons occupy quantised orbits; spectral lines come from transitions.",
        "Radioactivity is random and follows exponential decay.",
        "Mass defect gives nuclear binding energy.",
    ],
    formulas=[
        "K_max = hν − φ;  eV₀ = K_max;  hc ≈ 1240 eV·nm",
        "λ = h/p;  for electrons, λ(nm) ≈ 1.227/√V(volts)",
        "Eₙ = −13.6 Z²/n² eV;  rₙ = 0.529 n²/Z Å",
        "N = N₀e^(−λt);  t½ = 0.693/λ",
        "E = Δm c²;  1 u = 931.5 MeV",
    ],
    example=(
        "**Example.** 5 eV photons strike a metal with φ = 2 eV.\n\n"
        "K_max = 5 − 2 = **3 eV**, so the stopping potential is **3 V**."
    ),
    practice=[
        "Energy of the n = 3 → 2 transition in hydrogen?",
        "de Broglie wavelength of an electron accelerated through 100 V?",
        "Fraction left after 30 days if t½ = 10 days?",
    ],
    answers="1) 13.6(1/4 − 1/9) ≈ 1.89 eV  2) ≈ 0.123 nm  3) 1/8",
    focus=["Photoelectric graphs", "Hydrogen spectrum", "Radioactive decay and half-life"],
)

# ======================== CHEMISTRY ========================

STUDY_CONTENT[("Chemistry", "Some Basic Concepts")] = _build(
    theory=[
        "A mole contains 6.022 × 10²³ entities (Avogadro's number).",
        "Laws: conservation of mass, definite proportions, multiple proportions.",
        "Limiting reagent decides the amount of product formed.",
        "Empirical formula is the simplest whole-number ratio; molecular formula = n × empirical formula.",
    ],
    formulas=[
        "moles = mass / molar mass = N / Nₐ = V(STP) / 22.4 L",
        "Molarity = moles of solute / litres of solution",
        "Molality = moles of solute / kg of solvent",
        "Mole fraction xₐ = nₐ / (nₐ + n_b)",
    ],
    example=(
        "**Example.** 4 g NaOH is dissolved to make 500 mL of solution. Molarity?\n\n"
        "Moles = 4/40 = 0.1; M = 0.1/0.5 = **0.2 M**."
    ),
    practice=[
        "How many moles are in 44 g of CO₂?",
        "How many molecules are in 36 g of water?",
        "Empirical formula for 40% C, 6.7% H, 53.3% O?",
    ],
    answers="1) 1 mol  2) 2 × 6.022 × 10²³ ≈ 1.2 × 10²⁴  3) CH₂O",
    focus=["Stoichiometry and limiting reagent", "Concentration conversions", "Empirical formula"],
)

STUDY_CONTENT[("Chemistry", "Atomic Structure")] = _build(
    theory=[
        "Bohr model explains the hydrogen spectrum; quantum mechanics describes orbitals.",
        "Quantum numbers: n (shell), l (subshell), mₗ (orbital orientation), mₛ (spin).",
        "Aufbau principle, Pauli exclusion and Hund's rule fix electron configurations.",
        "Exceptions: Cr is [Ar]3d⁵4s¹ and Cu is [Ar]3d¹⁰4s¹ (extra stability of half and full d-subshells).",
        "Heisenberg: position and momentum cannot both be known exactly.",
    ],
    formulas=[
        "Eₙ = −13.6 Z²/n² eV",
        "1/λ = R Z² (1/n₁² − 1/n₂²),  R = 1.097 × 10⁷ m⁻¹",
        "Orbitals in a shell = n²; electrons = 2n²",
        "Radial nodes = n − l − 1;  angular nodes = l",
        "λ = h/mv;  Δx·Δp ≥ h/4π",
    ],
    example=(
        "**Example.** Number of orbitals in n = 3?\n\n"
        "n² = **9** (one 3s, three 3p, five 3d)."
    ),
    practice=[
        "Maximum electrons in the n = 4 shell?",
        "Configuration of Fe²⁺?",
        "Radial nodes in a 3p orbital?",
    ],
    answers="1) 32  2) [Ar]3d⁶  3) 3 − 1 − 1 = 1",
    focus=["Quantum numbers", "Hydrogen spectrum lines", "Electronic configuration exceptions"],
)

STUDY_CONTENT[("Chemistry", "Chemical Bonding")] = _build(
    theory=[
        "Ionic bonds form by electron transfer; covalent bonds by sharing.",
        "VSEPR predicts shape from bond pairs and lone pairs.",
        "Hybridisation: sp (linear), sp² (trigonal planar), sp³ (tetrahedral), sp³d (trigonal bipyramidal), sp³d² (octahedral).",
        "Molecular orbital theory: bond order = (bonding − antibonding electrons)/2; O₂ is paramagnetic.",
        "Hydrogen bonding raises boiling points (H₂O, HF, NH₃).",
    ],
    formulas=[
        "Bond order = (Nb − Na)/2",
        "Dipole moment μ = q × d",
        "Shapes: CH₄ tetrahedral, NH₃ pyramidal, H₂O bent, BF₃ trigonal planar, SF₆ octahedral, XeF₄ square planar",
    ],
    example=(
        "**Example.** Bond order of N₂ and magnetism.\n\n"
        "Nb = 10, Na = 4, so bond order = (10 − 4)/2 = **3**; all electrons paired, so **diamagnetic**."
    ),
    practice=[
        "Shape and hybridisation of H₂O?",
        "Bond order of N₂⁺?",
        "Which has the largest bond angle: CH₄, NH₃ or H₂O?",
    ],
    answers="1) Bent, sp³  2) 2.5  3) CH₄ (109.5°)",
    focus=["MOT bond order and magnetism", "VSEPR shapes", "Hybridisation and dipole moment"],
)

STUDY_CONTENT[("Chemistry", "Thermodynamics")] = _build(
    theory=[
        "First law: ΔU = q + w (IUPAC sign convention: w is work done on the system).",
        "Enthalpy is heat at constant pressure; Hess's law: enthalpy change is path independent.",
        "Entropy measures disorder; a process is spontaneous if ΔG < 0.",
        "At equilibrium ΔG = 0; ΔG° is related to K.",
    ],
    formulas=[
        "ΔH = ΔU + Δn_g RT",
        "ΔG = ΔH − TΔS;  ΔG° = −RT ln K = −2.303 RT log K",
        "q = mcΔT;  w = −PΔV",
    ],
    example=(
        "**Example.** ΔH = −100 kJ, ΔS = −200 J/K at 300 K. Spontaneous?\n\n"
        "ΔG = −100000 − (300)(−200) = −100000 + 60000 = **−40 kJ**, so spontaneous."
    ),
    practice=[
        "For 2SO₂ + O₂ → 2SO₃, express ΔH − ΔU.",
        "ΔG at 300 K for ΔH = −50 kJ and ΔS = −100 J/K?",
        "Above what temperature is a reaction with ΔH = +40 kJ and ΔS = +100 J/K spontaneous?",
    ],
    answers="1) Δn_g = −1, so ΔH − ΔU = −RT  2) −20 kJ  3) T > 400 K",
    focus=["Gibbs energy and spontaneity", "Hess's law", "ΔH and ΔU relation"],
)

STUDY_CONTENT[("Chemistry", "Equilibrium")] = _build(
    theory=[
        "At equilibrium, forward and reverse rates are equal.",
        "Le Chatelier: a system shifts to oppose any change in concentration, pressure or temperature.",
        "Acids and bases: Arrhenius, Brønsted-Lowry, Lewis.",
        "A buffer resists pH change; it is a weak acid with its salt (or a weak base with its salt).",
        "Common ion effect lowers solubility.",
    ],
    formulas=[
        "Kp = Kc (RT)^Δn",
        "pH = −log[H⁺];  Kw = 10⁻¹⁴ at 25 °C;  pH + pOH = 14",
        "Henderson: pH = pKa + log([salt]/[acid])",
        "Ksp of AₓB_y = xˣ yʸ sˣ⁺ʸ",
    ],
    example=(
        "**Example.** pH of 0.01 M HCl.\n\n"
        "[H⁺] = 10⁻² M, so pH = **2**."
    ),
    practice=[
        "pH of 0.001 M HCl?",
        "Relation between Kp and Kc for N₂ + 3H₂ ⇌ 2NH₃?",
        "pH of a buffer with equal acid and salt (pKa = 4.76)?",
    ],
    answers="1) 3  2) Kp = Kc(RT)⁻²  3) 4.76",
    focus=["Buffer calculations", "Ksp and solubility", "Le Chatelier applications"],
)

STUDY_CONTENT[("Chemistry", "Electrochemistry")] = _build(
    theory=[
        "Galvanic cells convert chemical energy to electrical energy; electrolytic cells do the reverse.",
        "Oxidation occurs at the anode, reduction at the cathode.",
        "Higher reduction potential means a stronger oxidising agent.",
        "Conductance: molar conductivity increases on dilution.",
    ],
    formulas=[
        "E°cell = E°cathode − E°anode",
        "Nernst: E = E° − (0.0591/n) log Q at 298 K",
        "ΔG° = −nFE°;  F = 96500 C/mol",
        "Faraday: m = (M/nF) × I t",
        "Kohlrausch: Λm = Λ°m − A√c",
    ],
    example=(
        "**Example.** Daniell cell: E°(Cu²⁺/Cu) = +0.34 V, E°(Zn²⁺/Zn) = −0.76 V.\n\n"
        "E°cell = 0.34 − (−0.76) = **1.10 V**."
    ),
    practice=[
        "E°cell for Zn | Zn²⁺ || Ag⁺ | Ag (E°Ag = 0.80 V, E°Zn = −0.76 V)?",
        "Mass of Ag deposited by 1 A for 9650 s (Ag = 108)?",
        "ΔG° for the Daniell cell (n = 2, E° = 1.10 V)?",
    ],
    answers="1) 1.56 V  2) 0.1 mol e⁻ → 10.8 g  3) −212.3 kJ",
    focus=["Nernst equation", "Electrolysis and Faraday's laws", "Conductivity"],
)

STUDY_CONTENT[("Chemistry", "Chemical Kinetics")] = _build(
    theory=[
        "Rate law is found only by experiment; order need not equal stoichiometric coefficients.",
        "Molecularity applies to elementary steps and is a whole number.",
        "Temperature raises rate by increasing the fraction of molecules above the activation energy.",
        "Catalysts lower Ea without changing ΔH.",
    ],
    formulas=[
        "First order: k = (2.303/t) log(a/(a − x));  t½ = 0.693/k",
        "Zero order: t½ = a/2k",
        "Arrhenius: k = A e^(−Ea/RT)",
        "log(k₂/k₁) = (Ea/2.303R)(1/T₁ − 1/T₂)",
    ],
    example=(
        "**Example.** A first-order reaction has t½ = 20 min. What fraction remains after 60 min?\n\n"
        "60 min = 3 half-lives, so (1/2)³ = **12.5%** remains."
    ),
    practice=[
        "Unit of k for a first-order reaction?",
        "t½ if k = 0.0693 min⁻¹ (first order)?",
        "If rate = k[A]², what happens to the rate when [A] is doubled?",
    ],
    answers="1) s⁻¹  2) 10 min  3) Rate becomes 4 times",
    focus=["Integrated rate laws", "Half-life problems", "Arrhenius equation"],
)

STUDY_CONTENT[("Chemistry", "Organic Chemistry")] = _build(
    theory=[
        "IUPAC naming: find the longest chain with the principal functional group, number for the lowest locants.",
        "Electronic effects: inductive (−I/+I), resonance (±M), hyperconjugation.",
        "Carbocation stability: 3° > 2° > 1° > methyl; resonance-stabilised cations are the most stable.",
        "SN1 goes through a carbocation (racemisation, favoured by 3° halides); SN2 is one step with inversion (favoured by 1° halides).",
        "Isomerism: structural (chain, position, functional) and stereo (geometrical, optical).",
    ],
    formulas=[
        "Acid strength: −I groups and resonance stabilisation of the conjugate base increase acidity",
        "SN2 reactivity: CH₃X > 1° > 2° > 3°;  SN1 reactivity: 3° > 2° > 1°",
        "Chiral carbon: four different groups",
    ],
    example=(
        "**Example.** Which is more stable: (CH₃)₃C⁺ or CH₃CH₂⁺?\n\n"
        "(CH₃)₃C⁺ is a 3° cation stabilised by nine hyperconjugative C–H bonds and the +I effect of three methyls, so it is **more stable**."
    ),
    practice=[
        "Which is the more stable carbocation: tert-butyl or isopropyl?",
        "Which group shows a −I effect: –NO₂ or –CH₃?",
        "Order the SN2 reactivity of CH₃Br, (CH₃)₂CHBr, (CH₃)₃CBr.",
    ],
    answers="1) tert-butyl  2) –NO₂  3) CH₃Br > (CH₃)₂CHBr > (CH₃)₃CBr",
    focus=["Carbocation and acidity order", "SN1 vs SN2", "Optical and geometrical isomerism"],
)

STUDY_CONTENT[("Chemistry", "Hydrocarbons")] = _build(
    theory=[
        "Alkanes undergo free-radical substitution (halogenation).",
        "Alkenes undergo electrophilic addition; HX adds by Markovnikov's rule, but HBr with peroxide adds anti-Markovnikov.",
        "Terminal alkynes are weakly acidic and react with Na or ammoniacal AgNO₃.",
        "Aromatic compounds follow Hückel's rule (4n + 2 π electrons) and undergo electrophilic substitution.",
        "Ozonolysis cleaves C=C to give carbonyl compounds.",
    ],
    formulas=[
        "Alkene + H₂ (Ni) → alkane;  alkyne + 2H₂ (Ni) → alkane",
        "Benzene + Cl₂/FeCl₃ → chlorobenzene (substitution)",
        "Friedel-Crafts: benzene + RCl/AlCl₃ → alkylbenzene",
    ],
    example=(
        "**Example.** Propene + HBr.\n\n"
        "Without peroxide: **2-bromopropane** (Markovnikov). With peroxide: **1-bromopropane** (anti-Markovnikov)."
    ),
    practice=[
        "Product of propene + HBr in the presence of peroxide?",
        "Is cyclobutadiene aromatic?",
        "Product of ethyne + 2 mol H₂ with Ni?",
    ],
    answers="1) 1-bromopropane  2) No, it is anti-aromatic (4π electrons)  3) Ethane",
    focus=["Markovnikov and peroxide effect", "Aromaticity", "Ozonolysis products"],
)

STUDY_CONTENT[("Chemistry", "Aldehydes and Ketones")] = _build(
    theory=[
        "Characteristic reaction is nucleophilic addition; aldehydes are more reactive than ketones.",
        "Tollens' and Fehling's tests distinguish aldehydes from ketones.",
        "Aldol condensation needs α-hydrogens; Cannizzaro reaction occurs without α-hydrogens.",
        "Iodoform test is positive for CH₃CO– groups and CH₃CH(OH)– groups.",
    ],
    formulas=[
        "Clemmensen: C=O → CH₂ with Zn-Hg/HCl",
        "Wolff-Kishner: C=O → CH₂ with NH₂NH₂/KOH",
        "Cannizzaro: 2 HCHO + NaOH → CH₃OH + HCOONa",
    ],
    example=(
        "**Example.** Does acetone give a positive Tollens' test?\n\n"
        "**No.** Ketones are not oxidised by Tollens' reagent; acetone does give a positive iodoform test."
    ),
    practice=[
        "Which of acetaldehyde and acetone gives a silver mirror?",
        "Which of HCHO and CH₃CHO undergoes the Cannizzaro reaction?",
        "Aldol product of acetaldehyde?",
    ],
    answers="1) Acetaldehyde  2) HCHO  3) 3-hydroxybutanal",
    focus=["Name reactions", "Distinguishing tests", "Reactivity order"],
)

STUDY_CONTENT[("Chemistry", "Coordination Compounds")] = _build(
    theory=[
        "Werner's theory: primary valence (oxidation state) and secondary valence (coordination number).",
        "Ligands can be monodentate, bidentate (en, ox) or polydentate (EDTA); ambidentate ligands bind through two different atoms.",
        "Isomerism: structural (ionisation, linkage, coordination) and stereo (geometrical, optical).",
        "Crystal field theory: d-orbitals split into t₂g and e_g; strong-field ligands (CN⁻, CO) give low spin.",
        "Colour arises from d-d transitions.",
    ],
    formulas=[
        "Oxidation state: sum of charges of the metal and ligands = charge on the complex",
        "Magnetic moment μ = √(n(n + 2)) BM  (n = unpaired electrons)",
        "EAN = Z − oxidation state + 2 × (coordination number)",
    ],
    example=(
        "**Example.** Oxidation state of Cr in K₃[Cr(C₂O₄)₃].\n\n"
        "K contributes +3 and 3 oxalate ions contribute −6, so Cr = **+3**."
    ),
    practice=[
        "Oxidation state of Fe in K₄[Fe(CN)₆]?",
        "Coordination number of Co in [Co(en)₃]³⁺?",
        "Magnetic moment of [FeF₆]³⁻ (high spin)?",
    ],
    answers="1) +2  2) 6  3) Fe³⁺ is d⁵ with 5 unpaired electrons, so √35 ≈ 5.92 BM",
    focus=["Oxidation state and naming", "Isomerism", "Crystal field splitting and magnetic moment"],
)

# ======================== MATHEMATICS ========================

STUDY_CONTENT[("Mathematics", "Sets and Relations")] = _build(
    theory=[
        "A set is a well-defined collection; operations: union, intersection, difference, complement.",
        "A relation from A to B is a subset of A × B.",
        "Relation types: reflexive, symmetric, transitive; an equivalence relation has all three.",
        "A function is a relation with exactly one image for each element of the domain.",
    ],
    formulas=[
        "n(A ∪ B) = n(A) + n(B) − n(A ∩ B)",
        "Number of subsets of an n-element set = 2ⁿ",
        "Number of relations from A to B = 2^(mn)",
        "On an n-element set: reflexive 2^(n² − n), symmetric 2^(n(n + 1)/2)",
    ],
    example=(
        "**Example.** n(A) = 20, n(B) = 15, n(A ∩ B) = 5. Find n(A ∪ B).\n\n"
        "20 + 15 − 5 = **30**."
    ),
    practice=[
        "Number of subsets of a 4-element set?",
        "Is R = {(a, b): a − b divisible by 3} on ℤ an equivalence relation?",
        "Number of reflexive relations on a 3-element set?",
    ],
    answers="1) 16  2) Yes  3) 2⁶ = 64",
    focus=["Types of relations", "Counting relations and functions", "Venn diagram problems"],
)

STUDY_CONTENT[("Mathematics", "Complex Numbers")] = _build(
    theory=[
        "A complex number is z = a + ib with i² = −1.",
        "Modulus |z| = √(a² + b²); conjugate z̄ = a − ib; z·z̄ = |z|².",
        "Polar form: z = r(cosθ + i sinθ) = re^(iθ).",
        "The nth roots of unity lie on the unit circle, equally spaced.",
        "Geometry: |z − z₁| = r is a circle; |z − z₁| = |z − z₂| is the perpendicular bisector.",
    ],
    formulas=[
        "|z₁z₂| = |z₁||z₂|;  |z₁ + z₂| ≤ |z₁| + |z₂|",
        "De Moivre: (cosθ + i sinθ)ⁿ = cos nθ + i sin nθ",
        "Cube roots of unity: 1 + ω + ω² = 0, ω³ = 1",
        "i⁴ = 1, i² = −1",
    ],
    example=(
        "**Example.** Find |3 + 4i| and simplify (1 + i)².\n\n"
        "|3 + 4i| = √(9 + 16) = **5**;  (1 + i)² = 1 + 2i − 1 = **2i**."
    ),
    practice=[
        "Modulus and argument of 1 + i√3?",
        "Evaluate ((1 + i)/(1 − i))⁸.",
        "If ω is a cube root of unity, find (1 + ω)³.",
    ],
    answers="1) 2 and π/3  2) 1  3) −1",
    focus=["Roots of unity", "Locus problems", "Polar form and De Moivre"],
)

STUDY_CONTENT[("Mathematics", "Quadratic Equations")] = _build(
    theory=[
        "The roots of ax² + bx + c = 0 depend on the discriminant D = b² − 4ac.",
        "D > 0: two distinct real roots; D = 0: equal roots; D < 0: complex conjugate roots.",
        "If two quadratics share a common root, eliminate to find conditions.",
        "Location of roots uses sign of f(k) and the vertex position.",
    ],
    formulas=[
        "x = [−b ± √(b² − 4ac)]/2a",
        "Sum of roots = −b/a;  product = c/a",
        "x² − (α + β)x + αβ = 0",
        "Vertex at x = −b/2a",
    ],
    example=(
        "**Example.** For what k does x² + kx + 9 = 0 have equal roots?\n\n"
        "D = k² − 36 = 0, so **k = ±6**."
    ),
    practice=[
        "Sum and product of roots of 2x² − 5x + 3 = 0?",
        "Find k for equal roots in x² − 6x + k = 0.",
        "Nature of roots of x² + x + 1 = 0?",
    ],
    answers="1) 5/2 and 3/2  2) k = 9  3) Complex (D = −3)",
    focus=["Nature of roots", "Common roots", "Range of quadratic expressions"],
)

STUDY_CONTENT[("Mathematics", "Sequences and Series")] = _build(
    theory=[
        "AP: constant difference; GP: constant ratio; HP: reciprocals form an AP.",
        "AM ≥ GM ≥ HM for positive numbers, with equality when all numbers are equal.",
        "Infinite GP converges only if |r| < 1.",
        "Sums of special series: Σn, Σn², Σn³.",
    ],
    formulas=[
        "AP: aₙ = a + (n − 1)d;  Sₙ = (n/2)[2a + (n − 1)d]",
        "GP: aₙ = arⁿ⁻¹;  Sₙ = a(rⁿ − 1)/(r − 1);  S∞ = a/(1 − r)",
        "Σn = n(n + 1)/2;  Σn² = n(n + 1)(2n + 1)/6;  Σn³ = [n(n + 1)/2]²",
    ],
    example=(
        "**Example.** Sum of the first 5 terms of 2, 6, 18, ...\n\n"
        "a = 2, r = 3: S₅ = 2(3⁵ − 1)/2 = **242**."
    ),
    practice=[
        "Sum of the first 20 odd numbers?",
        "10th term of 3, 7, 11, ...?",
        "Sum to infinity of 3 + 1 + 1/3 + ...?",
    ],
    answers="1) 400  2) 39  3) 4.5",
    focus=["AM-GM inequality", "Mixed AP-GP problems", "Telescoping and special sums"],
)

STUDY_CONTENT[("Mathematics", "Straight Lines")] = _build(
    theory=[
        "A line is determined by a point and a slope, or by two points.",
        "Parallel lines have equal slopes; perpendicular lines have slopes whose product is −1.",
        "Family of lines through the intersection of two lines: L₁ + λL₂ = 0.",
        "Locus problems often reduce to a straight line.",
    ],
    formulas=[
        "y − y₁ = m(x − x₁);  slope m = (y₂ − y₁)/(x₂ − x₁)",
        "Distance from (x₁, y₁) to Ax + By + C = 0: |Ax₁ + By₁ + C|/√(A² + B²)",
        "Between parallel lines: |c₁ − c₂|/√(a² + b²)",
        "Angle: tanθ = |(m₁ − m₂)/(1 + m₁m₂)|",
    ],
    example=(
        "**Example.** Distance of (1, 2) from 3x + 4y − 5 = 0.\n\n"
        "|3 + 8 − 5|/5 = **6/5**."
    ),
    practice=[
        "Distance between 3x + 4y = 5 and 3x + 4y = 15?",
        "Angle between y = x and y = √3 x?",
        "Midpoint of (1, 2) and (5, 6)?",
    ],
    answers="1) 2  2) 15°  3) (3, 4)",
    focus=["Distance and angle formulas", "Family of lines", "Locus"],
)

STUDY_CONTENT[("Mathematics", "Circle")] = _build(
    theory=[
        "A circle is the locus of points at a fixed distance from a centre.",
        "A tangent is perpendicular to the radius at the point of contact.",
        "The radical axis of two circles is the locus of points with equal tangent lengths.",
        "A line is tangent when the perpendicular distance from the centre equals the radius.",
    ],
    formulas=[
        "(x − h)² + (y − k)² = r²",
        "x² + y² + 2gx + 2fy + c = 0: centre (−g, −f), r = √(g² + f² − c)",
        "Line y = mx + c is tangent to x² + y² = a² if c² = a²(1 + m²)",
        "Tangent at (x₁, y₁): xx₁ + yy₁ = a²",
    ],
    example=(
        "**Example.** Centre and radius of x² + y² − 4x + 6y − 12 = 0.\n\n"
        "g = −2, f = 3, c = −12: centre (2, −3), r = √(4 + 9 + 12) = **5**."
    ),
    practice=[
        "Centre and radius of x² + y² − 6x + 8y = 0?",
        "Values of c for which y = x + c touches x² + y² = 2?",
        "Equation of the circle centred at the origin with radius 3?",
    ],
    answers="1) (3, −4), r = 5  2) c = ±2  3) x² + y² = 9",
    focus=["Tangent conditions", "Radical axis", "Common tangents"],
)

STUDY_CONTENT[("Mathematics", "Conic Sections")] = _build(
    theory=[
        "A conic is the locus of a point whose distance from a focus is e times its distance from a directrix.",
        "e < 1 ellipse, e = 1 parabola, e > 1 hyperbola.",
        "Standard forms are centred at the origin with axes along the coordinate axes.",
        "Tangent and normal conditions are a frequent JEE theme.",
    ],
    formulas=[
        "Parabola y² = 4ax: focus (a, 0), directrix x = −a, latus rectum 4a",
        "Ellipse x²/a² + y²/b² = 1: e = √(1 − b²/a²), foci (±ae, 0)",
        "Hyperbola x²/a² − y²/b² = 1: e = √(1 + b²/a²)",
        "Tangent to y² = 4ax: y = mx + a/m",
    ],
    example=(
        "**Example.** Focus and directrix of y² = 8x.\n\n"
        "4a = 8, so a = 2: focus **(2, 0)**, directrix **x = −2**."
    ),
    practice=[
        "Focus of y² = 12x?",
        "Eccentricity of x²/9 + y²/4 = 1?",
        "Eccentricity of x²/9 − y²/16 = 1?",
    ],
    answers="1) (3, 0)  2) √5/3  3) 5/3",
    focus=["Tangents and normals", "Eccentricity and foci", "Chord properties"],
)

STUDY_CONTENT[("Mathematics", "Limits")] = _build(
    theory=[
        "A limit describes the value a function approaches, not necessarily its value at the point.",
        "Indeterminate forms (0/0, ∞/∞) are solved by factoring, rationalising, standard limits or L'Hôpital's rule.",
        "Left-hand and right-hand limits must be equal for the limit to exist.",
        "Sandwich theorem helps with bounded oscillating functions.",
    ],
    formulas=[
        "lim sin x / x = 1;  lim tan x / x = 1  (x → 0)",
        "lim (eˣ − 1)/x = 1;  lim ln(1 + x)/x = 1",
        "lim (1 + 1/x)ˣ = e  (x → ∞);  lim (1 + x)^(1/x) = e  (x → 0)",
        "lim (1 − cos x)/x² = 1/2",
    ],
    example=(
        "**Example.** lim (x → 1) (x² − 1)/(x − 1).\n\n"
        "(x − 1)(x + 1)/(x − 1) = x + 1 → **2**."
    ),
    practice=[
        "lim (x → 0) sin 5x / x?",
        "lim (x → 0) (1 − cos x)/x²?",
        "lim (x → ∞) (1 + 2/x)ˣ?",
    ],
    answers="1) 5  2) 1/2  3) e²",
    focus=["Standard limits", "L'Hôpital's rule", "Limits involving e and logs"],
)

STUDY_CONTENT[("Mathematics", "Continuity")] = _build(
    theory=[
        "f is continuous at a if lim f(x) as x → a exists and equals f(a).",
        "Types of discontinuity: removable, jump, infinite.",
        "Differentiable implies continuous, but not the other way round (e.g. |x| at 0).",
        "Intermediate value theorem: a continuous function takes every value between f(a) and f(b).",
    ],
    formulas=[
        "Continuity at a: LHL = RHL = f(a)",
        "Differentiability at a: left derivative = right derivative",
        "Rolle's theorem: f(a) = f(b) implies f′(c) = 0 for some c",
    ],
    example=(
        "**Example.** f(x) = (x² − 4)/(x − 2) for x ≠ 2, f(2) = k. Find k for continuity at 2.\n\n"
        "Limit = x + 2 → 4, so **k = 4**."
    ),
    practice=[
        "Value of k for f(x) = sin x / x (x ≠ 0), f(0) = k, to be continuous?",
        "Type of discontinuity of 1/x at 0?",
        "Is |x − 1| differentiable at x = 1?",
    ],
    answers="1) k = 1  2) Infinite discontinuity  3) No (sharp corner)",
    focus=["Piecewise function continuity", "Differentiability of modulus functions", "Greatest integer function"],
)

STUDY_CONTENT[("Mathematics", "Differentiation")] = _build(
    theory=[
        "The derivative gives the instantaneous rate of change and the slope of the tangent.",
        "Use product, quotient and chain rules; use logarithmic differentiation for powers like xˣ.",
        "Maxima and minima: f′(x) = 0 and check the sign of f″.",
        "Mean value theorem: some point has slope equal to the average slope.",
    ],
    formulas=[
        "d/dx(xⁿ) = nxⁿ⁻¹;  d/dx(sin x) = cos x;  d/dx(tan x) = sec²x",
        "d/dx(eˣ) = eˣ;  d/dx(ln x) = 1/x",
        "(uv)′ = u′v + uv′;  (u/v)′ = (u′v − uv′)/v²",
        "Chain rule: d/dx f(g(x)) = f′(g(x)) g′(x)",
    ],
    example=(
        "**Example.** Minimum value of x² − 4x + 5.\n\n"
        "f′ = 2x − 4 = 0 gives x = 2, f″ = 2 > 0, so minimum **f(2) = 1**."
    ),
    practice=[
        "Differentiate ln(sin x).",
        "Differentiate x² eˣ.",
        "Slope of the tangent to y = x³ at x = 2?",
    ],
    answers="1) cot x  2) eˣ(x² + 2x)  3) 12",
    focus=["Maxima and minima", "Chain and implicit differentiation", "Mean value theorems"],
)

STUDY_CONTENT[("Mathematics", "Integration")] = _build(
    theory=[
        "Integration reverses differentiation; definite integrals give the area under a curve.",
        "Methods: substitution, integration by parts (ILATE order), partial fractions.",
        "Properties of definite integrals can simplify symmetric or periodic integrands.",
        "Area between curves = ∫(upper − lower) dx.",
    ],
    formulas=[
        "∫xⁿ dx = xⁿ⁺¹/(n + 1) + C;  ∫(1/x) dx = ln|x| + C",
        "∫eˣ dx = eˣ + C;  ∫sin x dx = −cos x + C;  ∫cos x dx = sin x + C",
        "By parts: ∫u dv = uv − ∫v du",
        "∫₀ᵃ f(x) dx = ∫₀ᵃ f(a − x) dx",
    ],
    example=(
        "**Example.** ∫x eˣ dx.\n\n"
        "Take u = x, dv = eˣ dx: = x eˣ − ∫eˣ dx = **eˣ(x − 1) + C**."
    ),
    practice=[
        "∫₀^(π/2) cos x dx?",
        "∫x sin x dx?",
        "∫₀¹ x² dx?",
    ],
    answers="1) 1  2) −x cos x + sin x + C  3) 1/3",
    focus=["Definite integral properties", "Integration by parts", "Area under curves"],
)

STUDY_CONTENT[("Mathematics", "Matrices and Determinants")] = _build(
    theory=[
        "Matrix multiplication is not commutative in general.",
        "A matrix is invertible only if its determinant is non-zero.",
        "Systems of linear equations: unique, infinite or no solutions depending on rank.",
        "Symmetric: Aᵀ = A; skew-symmetric: Aᵀ = −A.",
    ],
    formulas=[
        "|AB| = |A||B|;  |kA| = kⁿ|A| (n × n matrix)",
        "A·adj(A) = |A|·I;  A⁻¹ = adj(A)/|A|",
        "|adj A| = |A|ⁿ⁻¹",
        "2×2: |[[a, b], [c, d]]| = ad − bc",
    ],
    example=(
        "**Example.** For A = [[1, 2], [3, 4]], find |A| and A⁻¹.\n\n"
        "|A| = 4 − 6 = −2;  A⁻¹ = (1/−2)[[4, −2], [−3, 1]] = **[[−2, 1], [1.5, −0.5]]**."
    ),
    practice=[
        "Determinant of [[2, 3], [1, 4]]?",
        "If A is 3 × 3 and |A| = 3, find |2A|.",
        "If A is 3 × 3 and |A| = 2, find |adj A|.",
    ],
    answers="1) 5  2) 8 × 3 = 24  3) 2² = 4",
    focus=["Properties of determinants", "Adjoint and inverse", "System of equations consistency"],
)

STUDY_CONTENT[("Mathematics", "Probability")] = _build(
    theory=[
        "Probability = favourable outcomes / total outcomes (for equally likely outcomes).",
        "Conditional probability and Bayes' theorem update probabilities given new information.",
        "Independent events satisfy P(A ∩ B) = P(A)P(B).",
        "Binomial distribution models repeated independent trials.",
    ],
    formulas=[
        "P(A ∪ B) = P(A) + P(B) − P(A ∩ B)",
        "P(A|B) = P(A ∩ B)/P(B)",
        "Bayes: P(Eᵢ|A) = P(Eᵢ)P(A|Eᵢ) / ΣP(Eⱼ)P(A|Eⱼ)",
        "Binomial: P(X = r) = ⁿCᵣ pʳ qⁿ⁻ʳ;  mean = np;  variance = npq",
    ],
    example=(
        "**Example.** Probability of exactly 2 heads in 3 coin tosses.\n\n"
        "³C₂ (1/2)³ = **3/8**."
    ),
    practice=[
        "Probability that two dice sum to 7?",
        "Probability of at least one head in 3 tosses?",
        "P(A) = 0.4, P(B) = 0.5, independent. Find P(A ∪ B).",
    ],
    answers="1) 1/6  2) 7/8  3) 0.7",
    focus=["Bayes' theorem", "Binomial distribution", "Conditional probability"],
)

# ------------------------------------------
# MOST IMPORTANT QUESTIONS (JEE pattern) with solutions
# ------------------------------------------
IMPORTANT = {
    ("Physics", "Units and Dimensions"): [
        ("Planck's constant h has the same dimensions as: (a) energy (b) angular momentum (c) power (d) momentum",
         "**(b).** h = E/ν = [ML²T⁻²]/[T⁻¹] = [ML²T⁻¹], the same as angular momentum mvr."),
        ("The time period T of oscillation of a liquid drop depends on density ρ, radius r and surface tension S. Find T ∝ ρᵃ rᵇ Sᶜ.",
         "S = [MT⁻²]. Matching M: a + c = 0; L: −3a + b = 0; T: −2c = 1. So c = −1/2, a = 1/2, b = 3/2, giving **T ∝ √(ρr³/S)**."),
        ("P = a³b² / (c√d). Percentage errors in a, b, c, d are 1%, 2%, 3%, 4%. Find the maximum percentage error in P.",
         "3(1) + 2(2) + 3 + ½(4) = **12%**."),
    ],
    ("Physics", "Kinematics"): [
        ("A particle moves as x = t³ − 6t² + 9t (SI). Find the distance travelled in the first 3 s.",
         "v = 3(t − 1)(t − 3), so it turns at t = 1. x(0) = 0, x(1) = 4, x(3) = 0. Distance = 4 + 4 = **8 m**."),
        ("Two projectiles are launched with the same speed at angles θ and (90° − θ). Find the ratio of their ranges.",
         "R ∝ sin 2θ and sin 2(90° − θ) = sin 2θ, so the ratio is **1 : 1**."),
        ("A boat moves at 5 m/s relative to water, heading straight across a 100 m wide river flowing at 3 m/s. Find the crossing time and the drift.",
         "t = 100/5 = **20 s**; drift = 3 × 20 = **60 m**."),
    ],
    ("Physics", "Laws of Motion"): [
        ("A 10 kg block on a rough surface (μ = 0.4) is pulled by a horizontal 50 N force. Find a (g = 10).",
         "Friction = 0.4 × 100 = 40 N, so a = (50 − 40)/10 = **1 m/s²**."),
        ("A 60 kg man stands in a lift accelerating upward at 2 m/s². Find his apparent weight (g = 10).",
         "N = m(g + a) = 60 × 12 = **720 N**."),
        ("Blocks of 4 kg and 6 kg touch on a smooth floor. A 20 N force pushes the 4 kg block. Find the contact force.",
         "a = 20/10 = 2 m/s². The contact force accelerates the 6 kg block: 6 × 2 = **12 N**."),
    ],
    ("Physics", "Work Energy Power"): [
        ("A 1 kg ball moving at 4 m/s collides head-on and elastically with a 1 kg ball at rest. Find their velocities after impact.",
         "Equal masses exchange velocities: the first stops and the second moves at **4 m/s**."),
        ("A ball dropped from 10 m rebounds to 2.5 m. Find the coefficient of restitution.",
         "e = √(h₂/h₁) = √0.25 = **0.5**."),
        ("A pump lifts 100 kg of water per minute from a 10 m deep well. Find the power (g = 10).",
         "P = mgh/t = (100 × 10 × 10)/60 ≈ **167 W**."),
    ],
    ("Physics", "Rotational Motion"): [
        ("A solid sphere rolls without slipping. What fraction of its total kinetic energy is rotational?",
         "I/MR² = 2/5. Rotational/Total = (2/5)/(1 + 2/5) = **2/7**."),
        ("A uniform rod of length L, hinged at one end, is released from the horizontal. Find the angular acceleration at release.",
         "τ = MgL/2, I = ML²/3, so α = τ/I = **3g/2L**."),
        ("A disc rotating at ω has a second identical disc, at rest, dropped coaxially onto it. Find the final angular speed.",
         "Angular momentum conserved: Iω = 2Iω′, so **ω′ = ω/2** (half the kinetic energy is lost)."),
    ],
    ("Physics", "Gravitation"): [
        ("Find the total energy of a satellite of mass m in a circular orbit of radius r around a planet of mass M.",
         "**−GMm/2r**: kinetic = +GMm/2r, potential = −GMm/r."),
        ("A planet has 4 times Earth's mass and the same radius. Compare its escape velocity with Earth's (11.2 km/s).",
         "v ∝ √M, so v = 2 × 11.2 = **22.4 km/s**."),
        ("At what fraction of the surface value is g at a depth d = R/2 inside the Earth?",
         "g′ = g(1 − d/R) = **g/2**."),
    ],
    ("Physics", "Thermodynamics"): [
        ("An ideal gas expands to twice its volume, once isothermally and once adiabatically, from the same initial state. Which final pressure is lower?",
         "**Adiabatic.** The gas cools while expanding, so its final pressure is lower than in the isothermal case."),
        ("What fraction of heat supplied at constant pressure to a monoatomic ideal gas is converted into work?",
         "W/Q = R/Cp = R/(5R/2) = **2/5**."),
        ("A Carnot engine has efficiency 40%. Lowering the sink temperature by 50 K raises it to 50%. Find the source temperature.",
         "T₂ = 0.6T₁ and T₂ − 50 = 0.5T₁, so 0.1T₁ = 50, giving **T₁ = 500 K** (T₂ = 300 K)."),
    ],
    ("Physics", "Electrostatics"): [
        ("What is the electric field and the potential inside a uniformly charged thin spherical shell?",
         "Field = **0**; potential is constant and equal to the surface value kQ/R."),
        ("A 5 µF capacitor is charged to 100 V and isolated. A dielectric of K = 2 fills the gap. Find the new energy.",
         "Initial U = ½(5×10⁻⁶)(100)² = 0.025 J. Q is constant and C doubles, so U halves: **0.0125 J**."),
        ("Charges +q and −q are 2a apart. Find the field at the midpoint.",
         "Both fields point toward −q: E = 2kq/a²."),
    ],
    ("Physics", "Current Electricity"): [
        ("A wire of resistance R is stretched to twice its length. Find the new resistance.",
         "Volume is fixed, so area halves: R′ = ρ(2l)/(A/2) = **4R**."),
        ("In a balanced Wheatstone bridge P = 10 Ω, Q = 20 Ω, R = 30 Ω. Find S.",
         "P/Q = R/S gives S = 30 × 20/10 = **60 Ω**."),
        ("A cell of EMF 2 V and internal resistance 0.5 Ω supplies a variable external resistance. Find the maximum power delivered.",
         "Maximum when R = r: P = E²/4r = 4/2 = **2 W**."),
    ],
    ("Physics", "Magnetism"): [
        ("A proton moves perpendicular to a uniform B field in a circle of radius r. If its speed doubles, what happens to the radius and the time period?",
         "r = mv/qB doubles; T = 2πm/qB is **unchanged**."),
        ("Two long parallel wires 1 m apart each carry 1 A in the same direction. Find the force per metre.",
         "F/l = μ₀I₁I₂/2πd = **2 × 10⁻⁷ N/m**, attractive."),
        ("A 0.5 m rod moves at 4 m/s perpendicular to a 0.2 T field, perpendicular to its length. Find the EMF induced.",
         "EMF = Blv = 0.2 × 0.5 × 4 = **0.4 V**."),
    ],
    ("Physics", "Optics"): [
        ("A glass slab of thickness 6 cm and refractive index 1.5 is placed over a printed page. By how much does the page appear to rise?",
         "Shift = t(1 − 1/n) = 6(1 − 2/3) = **2 cm**."),
        ("A prism with A = 60° and n = √2. Find the angle of minimum deviation.",
         "sin((A + δ)/2) = n sin(A/2) = √2 × 0.5, so (60° + δ)/2 = 45° and **δ = 30°**."),
        ("In Young's experiment with equal slit intensities, central maximum intensity is I₀. Find the intensity where the path difference is λ/3.",
         "φ = 2π/3, I = I₀cos²(φ/2) = I₀cos²60° = **I₀/4**."),
    ],
    ("Physics", "Modern Physics"): [
        ("Light of wavelength 400 nm falls on a metal with work function 2 eV. Find the stopping potential.",
         "E = 1240/400 = 3.1 eV, K_max = 3.1 − 2 = 1.1 eV, so **V₀ = 1.1 V**."),
        ("The activity of a sample falls to 1/16 of its initial value in 2 hours. Find the half-life.",
         "1/16 = (1/2)⁴, so 4 half-lives = 120 min and **t½ = 30 min**."),
        ("How much energy excites a hydrogen atom from the ground state to n = 2?",
         "13.6(1 − 1/4) = **10.2 eV**."),
    ],
    ("Chemistry", "Some Basic Concepts"): [
        ("What mass of CaCO₃ must be heated to get 11.2 L of CO₂ at STP?",
         "11.2 L = 0.5 mol CO₂, so 0.5 mol CaCO₃ = **50 g**."),
        ("Find the molality of an 18% (w/w) glucose solution (M = 180).",
         "18 g glucose = 0.1 mol in 82 g solvent: 0.1/0.082 ≈ **1.22 m**."),
        ("2 mol H₂ reacts with 1.5 mol O₂ to form water. Find the limiting reagent and the mass of water.",
         "2H₂ + O₂ → 2H₂O. 2 mol H₂ needs only 1 mol O₂, so **H₂ is limiting**; water = 2 mol = **36 g**."),
    ],
    ("Chemistry", "Atomic Structure"): [
        ("Find the de Broglie wavelength of an electron in the n = 2 orbit of hydrogen (r₁ = 0.529 Å).",
         "2πr = nλ gives λ = πr₂ = π(4 × 0.529) ≈ **6.65 Å**."),
        ("Which set is NOT allowed? (a) n=3, l=2, m=−2 (b) n=2, l=2, m=0 (c) n=3, l=0, m=0 (d) n=4, l=3, m=3",
         "**(b).** l must be less than n."),
        ("How many unpaired electrons does Mn²⁺ (Z = 25) have?",
         "Mn²⁺ is [Ar]3d⁵, so **5**."),
    ],
    ("Chemistry", "Chemical Bonding"): [
        ("Which species has bond order 2.5: O₂, O₂⁺, O₂⁻, N₂?",
         "**O₂⁺**: removing one π* electron from O₂ (bond order 2) gives 2.5."),
        ("Why is O₂ paramagnetic?",
         "In MO theory its two highest-energy electrons occupy separate π* orbitals with parallel spins, so it has **2 unpaired electrons**."),
        ("Give the hybridisation and shape of XeF₄.",
         "**sp³d², square planar** (4 bond pairs and 2 lone pairs)."),
    ],
    ("Chemistry", "Thermodynamics"): [
        ("1 mol of ice melts at 273 K with ΔH_fus = 6.0 kJ/mol. Find ΔS.",
         "ΔS = 6000/273 ≈ **22 J/K·mol**."),
        ("Find the reversible isothermal work for 1 mol of ideal gas expanding from 1 L to 10 L at 300 K.",
         "w = −2.303RT log(10) = −2.303 × 8.314 × 300 ≈ **−5744 J**."),
        ("A system absorbs 50 J of heat and does 20 J of work. Find ΔU.",
         "ΔU = q + w = 50 − 20 = **30 J**."),
    ],
    ("Chemistry", "Equilibrium"): [
        ("Find the pH of 0.1 M CH₃COOH (Ka = 1.8 × 10⁻⁵).",
         "[H⁺] = √(KaC) = √(1.8 × 10⁻⁶) ≈ 1.34 × 10⁻³, so **pH ≈ 2.87**."),
        ("Find the solubility of AgCl if Ksp = 1 × 10⁻¹⁰.",
         "s = √Ksp = **10⁻⁵ M**."),
        ("In N₂O₄ ⇌ 2NO₂, which way does equilibrium shift when pressure is increased?",
         "Toward fewer gas moles: **left** (towards N₂O₄)."),
    ],
    ("Chemistry", "Electrochemistry"): [
        ("How much charge is needed to deposit 1 mol of Al from Al³⁺?",
         "3F = 3 × 96500 = **289,500 C**."),
        ("Find E for Zn | Zn²⁺(0.01 M) || Cu²⁺(1 M) | Cu at 298 K (E° = 1.10 V).",
         "E = 1.10 − (0.0591/2) log(0.01/1) = 1.10 + 0.0591 ≈ **1.16 V**."),
        ("Why does the molar conductivity of a weak electrolyte rise sharply on dilution?",
         "The degree of dissociation increases, giving more ions."),
    ],
    ("Chemistry", "Chemical Kinetics"): [
        ("A first-order reaction is 75% complete in 32 min. Find t½.",
         "75% completion = 2 half-lives, so **t½ = 16 min**."),
        ("State the unit of k for a second-order reaction.",
         "**L mol⁻¹ s⁻¹**."),
        ("A first-order reaction has k = 0.0693 min⁻¹ and [A]₀ = 0.8 M. Find [A] after 30 min.",
         "t½ = 10 min, so 3 half-lives: 0.8/8 = **0.1 M**."),
    ],
    ("Chemistry", "Organic Chemistry"): [
        ("Which is more stable: CH₂=CH–CH₂⁺ or CH₃CH₂CH₂⁺?",
         "**Allyl cation**, because of resonance delocalisation."),
        ("Why is phenol more acidic than ethanol?",
         "The phenoxide ion is stabilised by resonance, while the ethoxide ion is not."),
        ("How many stereoisomers can a molecule with 2 different chiral centres have?",
         "2ⁿ = 2² = **4**."),
    ],
    ("Chemistry", "Hydrocarbons"): [
        ("Ozonolysis (followed by Zn/H₂O) of 2-methylpropene gives which products?",
         "**Acetone and formaldehyde.**"),
        ("How can 1-butyne be distinguished from 2-butyne?",
         "Ammoniacal AgNO₃: only the terminal alkyne (1-butyne) gives a **white precipitate**."),
        ("What are the main products of nitration of toluene?",
         "**Ortho and para nitrotoluene**: –CH₃ is an activating, ortho/para-directing group."),
    ],
    ("Chemistry", "Aldehydes and Ketones"): [
        ("Acetaldehyde is treated with dilute NaOH and then heated. Name the product.",
         "Aldol condensation gives **crotonaldehyde (but-2-enal)**."),
        ("Which does NOT give the iodoform test: ethanol, acetone, 2-propanol, 1-propanol?",
         "**1-Propanol**: it lacks CH₃CO– and CH₃CH(OH)– groups."),
        ("Name two reactions that reduce benzaldehyde to toluene.",
         "**Clemmensen** (Zn-Hg/HCl) and **Wolff-Kishner** (NH₂NH₂/KOH)."),
    ],
    ("Chemistry", "Coordination Compounds"): [
        ("How many geometrical isomers does [Co(NH₃)₄Cl₂]⁺ have?",
         "**2**: cis and trans."),
        ("Give the hybridisation, shape and magnetism of [Ni(CO)₄].",
         "Ni(0) with strong-field CO: **sp³, tetrahedral, diamagnetic**."),
        ("Give the IUPAC name of [Co(NH₃)₅Cl]Cl₂.",
         "**Pentaamminechloridocobalt(III) chloride.**"),
    ],
    ("Mathematics", "Sets and Relations"): [
        ("In a class of 100 students, 60 like tea, 50 like coffee and 20 like both. How many like neither?",
         "100 − (60 + 50 − 20) = **10**."),
        ("Is R = {(1,1), (2,2), (3,3), (1,2), (2,1)} on {1, 2, 3} an equivalence relation?",
         "It is reflexive, symmetric and transitive, so **yes**."),
        ("How many one-one functions are there from a 3-element set to a 5-element set?",
         "⁵P₃ = **60**."),
    ],
    ("Mathematics", "Complex Numbers"): [
        ("If |z − 1| = |z + 1|, find the locus of z.",
         "z is equidistant from 1 and −1, so it lies on the **imaginary axis** (Re z = 0)."),
        ("Evaluate (1 + i)¹⁰.",
         "(1 + i)² = 2i, so (2i)⁵ = 32i⁵ = **32i**."),
        ("If ω is a cube root of unity, find ω¹⁰⁰ + ω²⁰⁰ + ω³⁰⁰.",
         "ω¹⁰⁰ = ω, ω²⁰⁰ = ω², ω³⁰⁰ = 1, so the sum = 1 + ω + ω² = **0**."),
    ],
    ("Mathematics", "Quadratic Equations"): [
        ("If α and β are the roots of x² − 5x + 6 = 0, find α² + β².",
         "(α + β)² − 2αβ = 25 − 12 = **13**."),
        ("Find the number of real roots of x² − 3|x| + 2 = 0.",
         "|x| = 1 or 2, so x = ±1, ±2: **4 roots**."),
        ("Find m such that x² + mx + 4 > 0 for all real x.",
         "D < 0: m² − 16 < 0, so **−4 < m < 4**."),
    ],
    ("Mathematics", "Sequences and Series"): [
        ("Find the sum 1·2 + 2·3 + ... + n(n + 1).",
         "**n(n + 1)(n + 2)/3**."),
        ("Three numbers in AP have sum 15 and product 105. Find them.",
         "Let them be 5 − d, 5, 5 + d: 5(25 − d²) = 105, so d = ±2. The numbers are **3, 5, 7**."),
        ("The AM of two positive numbers is 5 and the GM is 4. Find them.",
         "a + b = 10 and ab = 16, so the numbers are **2 and 8**."),
    ],
    ("Mathematics", "Straight Lines"): [
        ("Find the line through (2, 3) perpendicular to 3x + 4y = 7.",
         "The slope is 4/3: y − 3 = (4/3)(x − 2), so **4x − 3y + 1 = 0**."),
        ("Find the area of the triangle with vertices (0, 0), (4, 0), (0, 3).",
         "½ × 4 × 3 = **6**."),
        ("Find the reflection of (1, 2) in the line y = x.",
         "**(2, 1)**."),
    ],
    ("Mathematics", "Circle"): [
        ("Find the length of the tangent from (5, 0) to x² + y² = 9.",
         "√(25 − 9) = **4**."),
        ("Find the circle through (0, 0), (4, 0), (0, 6).",
         "x² + y² + 2gx + 2fy = 0 with g = −2, f = −3: **x² + y² − 4x − 6y = 0**."),
        ("How do the circles x² + y² = 1 and (x − 3)² + y² = 4 touch?",
         "Distance between centres = 3 = 1 + 2, so they touch **externally**."),
    ],
    ("Mathematics", "Conic Sections"): [
        ("Find the length of the latus rectum of x²/25 + y²/16 = 1.",
         "2b²/a = 2(16)/5 = **32/5**."),
        ("For y² = 16x, find the focal distance of the point (4, 8).",
         "Focus (4, 0), a = 4, so the focal distance = x + a = **8**."),
        ("What is the eccentricity of a rectangular hyperbola?",
         "a = b gives e = √(1 + 1) = **√2**."),
    ],
    ("Mathematics", "Limits"): [
        ("Evaluate lim (x → 0) sin 3x / sin 5x.",
         "**3/5**."),
        ("Evaluate lim (x → 0) (1 + 3x)^(1/x).",
         "**e³**."),
        ("Evaluate lim (x → ∞) (x² + 1)/(2x² − 3).",
         "Divide by x²: **1/2**."),
    ],
    ("Mathematics", "Continuity"): [
        ("Where is f(x) = [x] (greatest integer function) discontinuous?",
         "At **every integer**."),
        ("Is f(x) = x sin(1/x) for x ≠ 0, f(0) = 0 continuous at 0?",
         "|x sin(1/x)| ≤ |x| → 0, so **yes** (sandwich theorem)."),
        ("How many points of non-differentiability does f(x) = |x| + |x − 1| have?",
         "**2** (at x = 0 and x = 1)."),
    ],
    ("Mathematics", "Differentiation"): [
        ("Differentiate xˣ.",
         "Take logs: **xˣ(1 + ln x)**."),
        ("Find dy/dx at (3, 4) for x² + y² = 25.",
         "dy/dx = −x/y = **−3/4**."),
        ("Find the maximum value of x e⁻ˣ.",
         "f′ = e⁻ˣ(1 − x) = 0 gives x = 1, so the maximum is **1/e**."),
    ],
    ("Mathematics", "Integration"): [
        ("Evaluate ∫₀^π x sin x dx.",
         "[−x cos x + sin x] from 0 to π = **π**."),
        ("Evaluate ∫₀¹ dx/(1 + x²).",
         "tan⁻¹(1) − tan⁻¹(0) = **π/4**."),
        ("Find the area bounded by y = x² and y = x.",
         "∫₀¹ (x − x²) dx = 1/2 − 1/3 = **1/6**."),
    ],
    ("Mathematics", "Matrices and Determinants"): [
        ("If A = [[1, 2], [0, 1]], find Aⁿ.",
         "**[[1, 2n], [0, 1]]**."),
        ("For a 3 × 3 matrix with |A| = 5, find |adj A|.",
         "|A|² = **25**."),
        ("Is the system x + y = 2, 2x + 2y = 5 consistent?",
         "No: the second equation contradicts twice the first, so it is **inconsistent** (no solution)."),
    ],
    ("Mathematics", "Probability"): [
        ("A bag has 3 red and 2 blue balls. Two are drawn without replacement. Find P(both red).",
         "(3/5)(2/4) = **3/10**."),
        ("Box A has 2 red and 3 blue balls; box B has 4 red and 1 blue. A box is chosen at random and a red ball is drawn. Find P(box B).",
         "P(R|A) = 2/5, P(R|B) = 4/5. P(B|R) = (0.5 × 0.8)/(0.5 × 0.4 + 0.5 × 0.8) = **2/3**."),
        ("A binomial variable has n = 10, p = 0.3. Find the mean and variance.",
         "Mean = np = **3**; variance = npq = **2.1**."),
    ],
}

for _key, _qs in IMPORTANT.items():
    _text = "\n\n".join(
        f"**Q{i}.** {q}\n\n{a}" for i, (q, a) in enumerate(_qs, 1)
    )
    _topics = STUDY_CONTENT[_key]["Most Important Questions"].split(
        "\n\nFor exact past-paper")[0]
    STUDY_CONTENT[_key]["Most Important Questions"] = (
        _text + "\n\n---\n\n" + _topics +
        "\n\n*These are JEE-pattern important questions written for practice. "
        "For official past papers visit jeemain.nta.nic.in and jeeadv.ac.in.*"
    )

# ------------------------------------------
# PRACTICE QUESTION BANK
# Key: (subject, chapter) -> list of {q, options, answer, explanation, difficulty}
# ------------------------------------------
QUESTION_BANK = {
    ("Physics", "Kinematics"): [
        {"difficulty": "Easy", "q": "A body starts from rest with acceleration 4 m/s². Its velocity after 3 s is?",
         "options": ["6 m/s", "12 m/s", "7 m/s", "24 m/s"], "answer": "12 m/s",
         "explanation": "v = u + at = 0 + 4×3 = 12 m/s."},
        {"difficulty": "Medium", "q": "A ball is thrown up at 20 m/s (g = 10 m/s²). Maximum height reached?",
         "options": ["10 m", "20 m", "40 m", "5 m"], "answer": "20 m",
         "explanation": "H = u²/2g = 400/20 = 20 m."},
        {"difficulty": "Hard", "q": "For the same speed, which launch angle gives the maximum projectile range on level ground?",
         "options": ["30°", "45°", "60°", "90°"], "answer": "45°",
         "explanation": "R ∝ sin 2θ, which is maximum when 2θ = 90°."},
    ],
    ("Physics", "Laws of Motion"): [
        {"difficulty": "Easy", "q": "A 2 kg mass is acted on by a net force of 10 N. Its acceleration is?",
         "options": ["5 m/s²", "20 m/s²", "0.2 m/s²", "12 m/s²"], "answer": "5 m/s²",
         "explanation": "a = F/m = 10/2 = 5 m/s²."},
        {"difficulty": "Medium", "q": "Acceleration of a block on a smooth 30° incline (g = 10 m/s²)?",
         "options": ["10 m/s²", "5 m/s²", "8.66 m/s²", "2.5 m/s²"], "answer": "5 m/s²",
         "explanation": "a = g sin 30° = 10 × 0.5 = 5 m/s²."},
    ],
    ("Mathematics", "Complex Numbers"): [
        {"difficulty": "Easy", "q": "The value of i⁴ is?",
         "options": ["-1", "1", "i", "-i"], "answer": "1",
         "explanation": "i² = -1, so i⁴ = (i²)² = 1."},
        {"difficulty": "Medium", "q": "The modulus of 3 + 4i is?",
         "options": ["7", "5", "25", "1"], "answer": "5",
         "explanation": "√(9 + 16) = 5."},
        {"difficulty": "Medium", "q": "If ω is a non-real cube root of unity, 1 + ω + ω² equals?",
         "options": ["1", "-1", "0", "ω"], "answer": "0",
         "explanation": "The sum of all cube roots of unity is zero."},
    ],
    ("Chemistry", "Atomic Structure"): [
        {"difficulty": "Easy", "q": "The number of electrons in a neutral carbon atom is?",
         "options": ["4", "6", "8", "12"], "answer": "6",
         "explanation": "Carbon has atomic number 6."},
        {"difficulty": "Medium", "q": "Maximum number of electrons in the n = 3 shell is?",
         "options": ["8", "18", "32", "2"], "answer": "18",
         "explanation": "Capacity = 2n² = 2×9 = 18."},
    ],
}

FORMULAS = {
    "Physics": ["v = u + at", "s = ut + 1/2 at²", "F = ma",
                "K.E. = 1/2 mv²", "P = W/t", "V = IR"],
    "Chemistry": ["PV = nRT", "pH = -log[H⁺]", "M = Moles / Volume", "ΔG = ΔH - TΔS"],
    "Mathematics": ["d/dx (xⁿ) = nxⁿ⁻¹", "sin²θ + cos²θ = 1",
                    "(a+b)² = a² + 2ab + b²", "∫xⁿ dx = xⁿ⁺¹/(n+1) + C"],
}

MOCK_QUESTIONS = [
    {"q": "What is the derivative of x²?", "options": ["x", "2x", "x²", "2"], "answer": "2x"},
    {"q": "SI unit of force?", "options": ["Joule", "Newton", "Watt", "Pascal"], "answer": "Newton"},
    {"q": "Atomic number of Carbon?", "options": ["4", "6", "8", "12"], "answer": "6"},
]

# ==========================================
# SIDEBAR
# ==========================================
st.sidebar.title("🎓 JEE AI PRO")
page = st.sidebar.radio(
    "MAIN MENU",
    ["Dashboard", "Study Material", "AI Teacher", "Practice Questions",
     "Mock Test", "Formula Revision", "Performance"],
)
exam = st.sidebar.selectbox("Exam Mode", ["JEE Mains", "JEE Advanced"])
st.sidebar.markdown("---")
st.sidebar.info("Physics | Chemistry | Mathematics")

# ==========================================
# HEADER
# ==========================================
st.title("🎓 JEE AI PRO")
st.caption("AI Powered JEE Mains & Advanced Preparation")

# ==========================================
# DASHBOARD
# ==========================================
if page == "Dashboard":
    st.subheader("Student Dashboard")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Attempts", st.session_state.attempts)
    c2.metric("Correct Answers", st.session_state.score)
    accuracy = (st.session_state.score / st.session_state.attempts * 100
                if st.session_state.attempts else 0)
    c3.metric("Accuracy", f"{accuracy:.1f}%")
    st.markdown("---")
    st.subheader("Select Your Subject")
    cols = st.columns(3)
    for i, subject_name in enumerate(SUBJECTS):
        with cols[i]:
            st.markdown(f"### 📘 {subject_name}")
            st.write(f"{len(SUBJECTS[subject_name])} Chapters")
            st.write("Theory | Questions | Revision")
    st.success("Welcome to your JEE preparation journey!")

# ==========================================
# STUDY MATERIAL
# ==========================================
elif page == "Study Material":
    st.subheader("📚 Chapter Wise Learning")

    ALL_CHAPTERS = [(s, c) for s, cs in SUBJECTS.items() for c in cs]

    # Initialise / repair navigation state (before widgets are created)
    if "sm_subject" not in st.session_state:
        st.session_state.sm_subject = list(SUBJECTS.keys())[0]
    if st.session_state.get("sm_chapter") not in SUBJECTS[st.session_state.sm_subject]:
        st.session_state.sm_chapter = SUBJECTS[st.session_state.sm_subject][0]
    if "sm_level" not in st.session_state:
        st.session_state.sm_level = "Basic"

    def go_chapter(step):
        idx = ALL_CHAPTERS.index(
            (st.session_state.sm_subject, st.session_state.sm_chapter)
        ) + step
        if 0 <= idx < len(ALL_CHAPTERS):
            s, c = ALL_CHAPTERS[idx]
            st.session_state.sm_subject = s
            st.session_state.sm_chapter = c
            st.session_state.study_selection = {
                "subject": s,
                "chapter": c,
                "level": st.session_state.sm_level,
                "sections": list(LEARNING_SECTIONS),
            }
            for sec in LEARNING_SECTIONS:
                st.session_state[f"study_{s}_{c}_{sec}"] = True

    def nav_bar(prefix):
        pos = ALL_CHAPTERS.index(
            (st.session_state.sm_subject, st.session_state.sm_chapter)
        )
        c1, c2, c3 = st.columns([1, 2, 1])
        c1.button("⬅ Previous Chapter", key=f"{prefix}_prev",
                  on_click=go_chapter, args=(-1,), disabled=(pos == 0))
        c2.markdown(
            f"<div style='text-align:center;padding-top:8px'>"
            f"Chapter {pos + 1} of {len(ALL_CHAPTERS)}</div>",
            unsafe_allow_html=True,
        )
        c3.button("Next Chapter ➡", key=f"{prefix}_next",
                  on_click=go_chapter, args=(1,),
                  disabled=(pos == len(ALL_CHAPTERS) - 1))

    subject = st.selectbox("Select Subject", list(SUBJECTS.keys()), key="sm_subject")
    chapter = st.selectbox("Select Chapter", SUBJECTS[subject], key="sm_chapter")
    level = st.radio("Learning Level", ["Basic", "JEE Mains", "JEE Advanced"],
                     horizontal=True, key="sm_level")

    nav_bar("top")

    st.markdown("---")
    st.subheader(chapter)
    st.write(f"Subject: {subject}  |  Level: {level}")

    st.write("### Learning Sections")
    selected_sections = []
    for section in LEARNING_SECTIONS:
        if st.checkbox(section, key=f"study_{subject}_{chapter}_{section}"):
            selected_sections.append(section)

    if st.button("SUBMIT / LOAD CHAPTER", type="primary",
                 use_container_width=True, key="submit_study_material"):
        if not selected_sections:
            st.warning("Please select at least one learning section.")
        else:
            st.session_state.study_selection = {
                "subject": subject,
                "chapter": chapter,
                "level": level,
                "sections": selected_sections,
            }

    # Render from session state so content stays visible across reruns
    sel = st.session_state.study_selection
    if sel and sel["subject"] == subject and sel["chapter"] == chapter:
        st.success(f"Loaded: {chapter} ({sel['level']})")
        content = STUDY_CONTENT.get((subject, chapter))
        if content is None:
            st.info(
                f"Content for **{chapter}** is not added yet. "
                "Add it to STUDY_CONTENT in app.py to display it here."
            )
        else:
            for s in sel["sections"]:
                with st.expander(f"📖 {s}", expanded=True):
                    st.markdown(content.get(s, "Content not available."))

    st.markdown("---")
    nav_bar("bottom")

# ==========================================
# AI TEACHER
# ==========================================
elif page == "AI Teacher":
    st.subheader("🤖 AI JEE Teacher")
    st.write("Ask your Physics, Chemistry or Mathematics doubts.")
    subject = st.selectbox("Subject", list(SUBJECTS.keys()))
    question = st.text_area("Enter Your Question", placeholder="Type your JEE question here...")
    uploaded = st.file_uploader("Upload Question Image", type=["png", "jpg", "jpeg"])
    method = st.selectbox(
        "Explanation Type",
        ["Detailed Explanation", "Shortcut Method", "JEE Mains Method", "JEE Advanced Method"],
    )
    if st.button("SOLVE QUESTION", type="primary"):
        if question.strip():
            st.info("Question received. Connect an AI API to generate a verified step-by-step solution.")
            st.write("Selected Subject:", subject)
            st.write("Explanation:", method)
            st.text_area("Your submitted question", value=question, disabled=True)
        elif uploaded is not None:
            st.image(uploaded, caption="Uploaded question", use_container_width=True)
            st.warning("Image received. Connect a vision-capable AI API to read and solve the image.")
        else:
            st.warning("Please enter a question or upload an image.")

# ==========================================
# PRACTICE QUESTIONS
# ==========================================
elif page == "Practice Questions":
    st.subheader("📝 Practice Questions")
    subject = st.selectbox("Subject", list(SUBJECTS.keys()))
    chapter = st.selectbox("Chapter", SUBJECTS[subject])
    difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

    bank = [q for q in QUESTION_BANK.get((subject, chapter), [])
            if q["difficulty"] == difficulty]

    if not bank:
        st.info(
            f"No {difficulty} questions for {chapter} yet. "
            "Add them to QUESTION_BANK in app.py."
        )
    else:
        base = f"practice_{subject}_{chapter}_{difficulty}"
        for i, q in enumerate(bank):
            st.markdown(f"### Q{i+1}. {q['q']}")
            st.radio("Choose answer", q["options"], index=None, key=f"{base}_{i}")

        if st.button("CHECK ANSWERS", type="primary", key=f"{base}_check"):
            st.session_state.practice_checked[base] = True
            for i, q in enumerate(bank):
                choice = st.session_state.get(f"{base}_{i}")
                if choice is not None:
                    st.session_state.attempts += 1
                    if choice == q["answer"]:
                        st.session_state.score += 1

        if st.session_state.practice_checked.get(base):
            st.markdown("---")
            for i, q in enumerate(bank):
                choice = st.session_state.get(f"{base}_{i}")
                if choice is None:
                    st.warning(f"Q{i+1}: not answered. Correct answer: {q['answer']}")
                elif choice == q["answer"]:
                    st.success(f"Q{i+1}: Correct ✅  {q['explanation']}")
                else:
                    st.error(f"Q{i+1}: Wrong ❌ Correct answer: {q['answer']}. {q['explanation']}")

# ==========================================
# MOCK TEST
# ==========================================
elif page == "Mock Test":
    st.subheader("⏱️ JEE Mock Test")
    st.write("Exam:", exam)

    if st.session_state.mock_questions is None:
        st.session_state.mock_questions = MOCK_QUESTIONS

    answers = {}
    for i, q in enumerate(st.session_state.mock_questions):
        st.markdown(f"### Q{i+1}. {q['q']}")
        answers[str(i)] = st.radio(f"Choose answer {i+1}", q["options"], key=f"mock_answer_{i}")

    if st.button("SUBMIT TEST", type="primary"):
        correct = sum(1 for i, q in enumerate(st.session_state.mock_questions)
                      if answers[str(i)] == q["answer"])
        total_questions = len(st.session_state.mock_questions)
        st.session_state.attempts += total_questions
        st.session_state.score += correct
        st.session_state.history.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "exam": exam,
            "score": correct,
            "total": total_questions,
        })
        st.session_state.mock_submitted = True
        st.session_state.mock_result = correct

    if st.session_state.mock_submitted:
        correct = st.session_state.mock_result
        total_questions = len(st.session_state.mock_questions)
        st.success(f"Your Score: {correct}/{total_questions}")
        for i, q in enumerate(st.session_state.mock_questions):
            st.write(f"Q{i+1}: Correct Answer: {q['answer']}")
        if st.button("RESTART TEST"):
            st.session_state.mock_submitted = False
            st.session_state.mock_result = 0
            st.rerun()

# ==========================================
# FORMULA REVISION
# ==========================================
elif page == "Formula Revision":
    st.subheader("📐 Formula Revision")
    subject = st.selectbox("Select Subject", list(SUBJECTS.keys()))
    for formula in FORMULAS[subject]:
        st.markdown(f"<div class='card'>{formula}</div>", unsafe_allow_html=True)

# ==========================================
# PERFORMANCE
# ==========================================
elif page == "Performance":
    st.subheader("📊 Performance Analysis")
    total = st.session_state.attempts
    correct = st.session_state.score
    accuracy = correct / total * 100 if total else 0
    st.metric("Questions Attempted", total)
    st.metric("Correct Questions", correct)
    st.metric("Accuracy", f"{accuracy:.2f}%")
    if st.session_state.history:
        st.subheader("Mock Test History")
        st.dataframe(st.session_state.history, use_container_width=True)
    else:
        st.info("Complete a mock test to see your performance.")

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.caption("JEE AI PRO | Physics • Chemistry • Mathematics | JEE Mains + Advanced")
