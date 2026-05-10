# ═══════════════════════════════════════════════════════════
#  data.py  –  Yahan seedha content add/edit karo
#  Koi database nahi, koi admin panel nahi.
#  Bas Python dict mein content likho aur server restart karo.
# ═══════════════════════════════════════════════════════════


# ─────────────────────────────────────────────────────────
#  CPL SUBJECTS
#  Ek subject add karna ho to neeche ka format copy karo
# ─────────────────────────────────────────────────────────

CPL_SUBJECTS = [

    # ══════════════════════════════════════════════════════
    {
        "id": "navigation",
        "name": "Navigation",
        "icon": "🧭",
        "description": "Principles of aircraft navigation and procedures",

        # ── NOTES ──────────────────────────────────────────
        # Naya note add karna ho to ek dict copy karo
        "notes": [
            {
                "title": "Introduction to Navigation",
                "content": "Navigation is the process of planning, recording, and controlling the movement of a craft from one place to another. In aviation, it involves determining position, direction, and distance.\n\nKey types:\n• Dead Reckoning (DR)\n• Pilotage\n• Radio Navigation\n• GPS / GNSS"
            },
            {
                "title": "Magnetic Variation & Deviation",
                "content": "Magnetic Variation: The angle between True North and Magnetic North at any given location.\n\nDeviation: Error caused by the aircraft's own magnetic field affecting the compass.\n\nFormula:\nTrue Heading = Magnetic Heading ± Variation\nMagnetic Heading = Compass Heading ± Deviation"
            },
        ],

        # ── QUESTION BANK ──────────────────────────────────
        "questions": [
            {
                "q": "What is Dead Reckoning?",
                "a": "Dead Reckoning is the process of calculating one's current position by using a known past position, advancing it using known speed, elapsed time, and course."
            },
            {
                "q": "Define Magnetic Variation.",
                "a": "Magnetic Variation is the angular difference between True North and Magnetic North at a specific location."
            },
        ],

        # ── MCQ ────────────────────────────────────────────
        # options: list of 4 choices, answer: index (0-based)
        "mcq": [
            {
                "question": "What does VOR stand for?",
                "options": [
                    "Very High Frequency Omni-directional Range",
                    "Visual Omni Range",
                    "VHF Omni Receiver",
                    "Variable Omni Range"
                ],
                "answer": 0,
                "explanation": "VOR = Very High Frequency Omni-directional Range. It is a radio navigation system used by aircraft."
            },
            {
                "question": "Which instrument gives the aircraft's magnetic heading?",
                "options": ["Altimeter", "Magnetic Compass", "VSI", "ASI"],
                "answer": 1,
                "explanation": "The Magnetic Compass directly measures the magnetic heading of the aircraft."
            },
        ],

        # ── MOCK TESTS ─────────────────────────────────────
        # Ek mock test = ek full test paper
        "mock_tests": [
            {
                "test_name": "Navigation Mock Test 1",
                "duration_minutes": 30,
                "questions": [
                    {
                        "question": "What is the purpose of a Course Deviation Indicator (CDI)?",
                        "options": [
                            "To show deviation from a selected VOR radial",
                            "To measure altitude deviation",
                            "To show compass deviation",
                            "To display fuel deviation"
                        ],
                        "answer": 0
                    },
                    {
                        "question": "Wind correction angle is used to correct for?",
                        "options": ["Magnetic variation", "Wind drift", "Engine torque", "Fuel imbalance"],
                        "answer": 1
                    },
                ]
            }
        ],
    },

    # ══════════════════════════════════════════════════════
    {
        "id": "meteorology",
        "name": "Meteorology",
        "icon": "⛅",
        "description": "Weather principles and its impact on aviation",

        "notes": [
            {
                "title": "Atmosphere Layers",
                "content": "The atmosphere is divided into layers:\n\n1. Troposphere (0–12 km): Most weather occurs here. Temperature decreases with altitude.\n2. Stratosphere (12–50 km): Contains the ozone layer.\n3. Mesosphere (50–80 km)\n4. Thermosphere (80–700 km)\n\nThe Tropopause is the boundary between Troposphere and Stratosphere."
            },
            {
                "title": "Types of Clouds",
                "content": "Clouds are classified by altitude:\n\n• High clouds (above 20,000 ft): Cirrus, Cirrostratus, Cirrocumulus\n• Middle clouds (6,500–20,000 ft): Altostratus, Altocumulus\n• Low clouds (below 6,500 ft): Stratus, Stratocumulus, Nimbostratus\n• Vertical clouds: Cumulus, Cumulonimbus (most dangerous for aviation)"
            },
        ],

        "questions": [
            {
                "q": "What is the standard lapse rate?",
                "a": "The standard lapse rate is 2°C (or 1.98°C) per 1000 feet increase in altitude in the Troposphere."
            },
            {
                "q": "Why is Cumulonimbus dangerous for aviation?",
                "a": "Cumulonimbus contains severe turbulence, icing, lightning, heavy precipitation, and windshear — all of which are extremely hazardous to aircraft."
            },
        ],

        "mcq": [
            {
                "question": "Standard Sea Level pressure is?",
                "options": ["1013.25 hPa", "1030 hPa", "1000 hPa", "990 hPa"],
                "answer": 0,
                "explanation": "ICAO standard atmosphere defines sea level pressure as 1013.25 hPa (29.92 inHg)."
            },
        ],

        "mock_tests": [],
    },

    # ══════════════════════════════════════════════════════
    {
        "id": "regulation",
        "name": "Regulation",
        "icon": "📋",
        "description": "Aviation rules, standards and procedures",
        "notes": [],
        "questions": [],
        "mcq": [],
        "mock_tests": [],
    },

    # ══════════════════════════════════════════════════════
    {
        "id": "metrology",
        "name": "Metrology",
        "icon": "🔩",
        "description": "Measurement systems and instruments",
        "notes": [],
        "questions": [],
        "mcq": [],
        "mock_tests": [],
    },

    # ══════════════════════════════════════════════════════
    {
        "id": "aircraft-general-knowledge",
        "name": "Aircraft General Knowledge",
        "icon": "✈️",
        "description": "General knowledge about aircraft and systems",
        "notes": [],
        "questions": [],
        "mcq": [],
        "mock_tests": [],
    },
]


# ─────────────────────────────────────────────────────────
#  AME MODULES
#  Naya module add karna ho to neeche ka format copy karo
# ─────────────────────────────────────────────────────────

AME_MODULES = [

    # ══════════════════════════════════════════════════════
    {
        "id": 1,
        "number": 1,
        "title": "Mathematics",

        # ── STUDY MATERIAL ──────────────────────────────────
        "study_material": [
            {
                "topic": "Arithmetic",
                "content": "Arithmetic operations: Addition, Subtraction, Multiplication, Division.\n\nFractions, decimals, percentages.\n\nRatios and proportions.\n\nAverages and means."
            },
            {
                "topic": "Algebra",
                "content": "Linear equations.\nSimultaneous equations.\nPolynomials.\nFactorisation.\nQuadratic equations."
            },
        ],

        # ── DIAGRAMS ────────────────────────────────────────
        "diagrams": [
            {
                "title": "Trigonometry Circle",
                "description": "Unit circle showing sine, cosine values at key angles.",
                "image_url": ""  # URL add karo agar image host ki ho
            },
        ],

        # ── PREVIOUS YEAR QUESTIONS ──────────────────────────
        "questions": [
            {
                "year": "2022",
                "q": "Solve: 2x + 5 = 15",
                "a": "2x = 10, x = 5"
            },
        ],

        # ── PRACTICE TEST ────────────────────────────────────
        "practice_test": [
            {
                "question": "What is sin(90°)?",
                "options": ["0", "1", "-1", "0.5"],
                "answer": 1,
                "explanation": "sin(90°) = 1. At 90°, the sine function reaches its maximum value."
            },
        ],
    },

    # ══════════════════════════════════════════════════════
    {
        "id": 2,
        "number": 2,
        "title": "Aerodynamics",

        "study_material": [
            {
                "topic": "Bernoulli's Principle",
                "content": "Bernoulli's principle states that an increase in the speed of a fluid occurs simultaneously with a decrease in pressure.\n\nIn aviation: The curved upper surface of a wing makes air travel faster over it, creating lower pressure above and higher pressure below — generating LIFT."
            },
            {
                "topic": "Four Forces of Flight",
                "content": "1. Lift – upward force generated by wings\n2. Weight – gravitational force pulling down\n3. Thrust – forward force from engine\n4. Drag – resistance force opposing motion\n\nFor level flight: Lift = Weight, Thrust = Drag"
            },
        ],

        "diagrams": [],
        "questions": [
            {
                "year": "2023",
                "q": "What are the four forces acting on an aircraft in flight?",
                "a": "Lift, Weight (Gravity), Thrust, and Drag."
            },
        ],
        "practice_test": [
            {
                "question": "Lift is primarily generated by which component?",
                "options": ["Fuselage", "Wings", "Engine", "Tail"],
                "answer": 1,
                "explanation": "Wings are shaped (aerofoil) to generate lift using Bernoulli's principle."
            },
        ],
    },

    # ══════════════════════════════════════════════════════
    {
        "id": 3,
        "number": 3,
        "title": "Electrical Fundamentals",
        "study_material": [],
        "diagrams": [],
        "questions": [],
        "practice_test": [],
    },

    {
        "id": 4,
        "number": 4,
        "title": "Electronic Fundamentals",
        "study_material": [],
        "diagrams": [],
        "questions": [],
        "practice_test": [],
    },

    {
        "id": 5,
        "number": 5,
        "title": "Digital Techniques",
        "study_material": [],
        "diagrams": [],
        "questions": [],
        "practice_test": [],
    },

    {
        "id": 6,
        "number": 6,
        "title": "Materials & Hardware",
        "study_material": [],
        "diagrams": [],
        "questions": [],
        "practice_test": [],
    },

    {
        "id": 7,
        "number": 7,
        "title": "Maintenance Practices",
        "study_material": [],
        "diagrams": [],
        "questions": [],
        "practice_test": [],
    },

    {
        "id": 8,
        "number": 8,
        "title": "Basic Aerodynamics",

        "study_material": [
            {
                "topic": "Bernoulli's Principle & Lift",
                "content": "Bernoulli's Principle: Where velocity of a fluid increases, pressure decreases.\n\nWing (Aerofoil) shape:\n• Upper camber is curved → air moves FASTER → LOW pressure\n• Lower surface is flatter → air moves SLOWER → HIGH pressure\n• This pressure difference = LIFT\n\nLift formula: L = ½ρV²SCL\n  ρ = air density, V = velocity, S = wing area, CL = lift coefficient"
            },
            {
                "topic": "Four Forces of Flight",
                "content": "1. LIFT – Upward force. Generated by wings. Opposes Weight.\n2. WEIGHT (Gravity) – Downward force. Acts through Centre of Gravity.\n3. THRUST – Forward force. Generated by engine/propeller.\n4. DRAG – Rearward force. Opposes Thrust.\n\nLevel flight equilibrium:\n  Lift = Weight\n  Thrust = Drag\n\nTypes of Drag:\n• Parasite Drag – form drag + skin friction + interference drag\n• Induced Drag – byproduct of lift (decreases as speed increases)\n• Total Drag = Parasite + Induced"
            },
            {
                "topic": "Aerofoil Terminology",
                "content": "• Chord Line: Straight line from leading edge to trailing edge\n• Camber: Curvature of the aerofoil (upper > lower for lift)\n• Angle of Attack (AoA): Angle between chord line and relative airflow\n• Centre of Pressure: Point where lift acts on the wing\n• Aspect Ratio: Wing span² / Wing area (high AR = less induced drag)"
            },
            {
                "topic": "Stall",
                "content": "Stall occurs when Angle of Attack exceeds Critical AoA (~15–16°).\n\nAt stall:\n• Airflow separates from upper wing surface\n• Lift drops sharply\n• Drag increases sharply\n\nStall speed increases with:\n• Weight increase\n• Bank angle increase\n• Load factor increase\n\nStall recovery: Lower AoA (push forward), add power, level wings."
            },
            {
                "topic": "Stability",
                "content": "STATIC STABILITY: Initial tendency to return to original position after disturbance.\n• Positive: Returns to original (good)\n• Neutral: Stays displaced\n• Negative: Diverges further (dangerous)\n\nDYNAMIC STABILITY: Long-term behavior after disturbance.\n• Positive dynamic: Oscillations decrease over time\n\nAxes of aircraft:\n• Longitudinal axis (roll) – controlled by ailerons\n• Lateral axis (pitch) – controlled by elevator\n• Normal/Vertical axis (yaw) – controlled by rudder"
            },
            {
                "topic": "Atmosphere & Airspeed",
                "content": "ISA (International Standard Atmosphere):\n• Sea Level Temp: 15°C\n• Sea Level Pressure: 1013.25 hPa\n• Lapse Rate: 2°C per 1000 ft (up to 36,000 ft tropopause)\n\nAirspeed types:\n• IAS – Indicated Airspeed (from ASI, not corrected)\n• CAS – Calibrated Airspeed (IAS corrected for instrument error)\n• TAS – True Airspeed (CAS corrected for altitude & temp)\n• GS – Ground Speed = TAS ± wind\n\nDensity Altitude = Pressure Altitude corrected for temp deviation from ISA"
            },
        ],

        "diagrams": [
            {
                "title": "Aerofoil Cross-Section",
                "description": "Shows chord line, camber, leading/trailing edge, upper and lower surface pressure distribution.",
                "image_url": ""
            },
            {
                "title": "Four Forces of Flight",
                "description": "Diagram showing Lift (up), Weight (down), Thrust (forward), Drag (backward) on an aircraft.",
                "image_url": ""
            },
        ],

        "questions": [
            {
                "year": "2022",
                "q": "What is angle of attack?",
                "a": "Angle of Attack is the angle between the chord line of the aerofoil and the direction of the relative airflow (relative wind)."
            },
            {
                "year": "2022",
                "q": "What happens to induced drag as airspeed increases?",
                "a": "Induced drag decreases as airspeed increases. It is inversely proportional to the square of the airspeed."
            },
            {
                "year": "2023",
                "q": "Define critical angle of attack.",
                "a": "The critical angle of attack is the angle at which the aerofoil produces maximum lift (CLmax). Beyond this angle, airflow separates and the wing stalls. Typically around 15–16° for most aerofoils."
            },
            {
                "year": "2023",
                "q": "What are the three axes of an aircraft and which control surface controls each?",
                "a": "1. Longitudinal axis (roll) – Ailerons\n2. Lateral axis (pitch) – Elevator\n3. Normal/Vertical axis (yaw) – Rudder"
            },
            {
                "year": "2024",
                "q": "State Bernoulli's theorem and its application to lift generation.",
                "a": "Bernoulli's theorem states that in a streamlined flow, an increase in fluid velocity causes a decrease in pressure. In a wing, the curved upper surface accelerates airflow, reducing pressure above the wing. Higher pressure below the wing pushes upward, creating LIFT."
            },
        ],

        "practice_test": [
            {
                "question": "What is the primary cause of lift on an aerofoil?",
                "options": [
                    "Engine thrust pushing the aircraft upward",
                    "Pressure difference between upper and lower wing surfaces",
                    "Weight acting downward",
                    "Rudder deflection"
                ],
                "answer": 1,
                "explanation": "Lift is generated by the pressure difference — lower pressure on the curved upper surface (faster airflow) and higher pressure on the lower surface (slower airflow), per Bernoulli's principle."
            },
            {
                "question": "Which axis does the elevator control?",
                "options": [
                    "Longitudinal axis (roll)",
                    "Normal axis (yaw)",
                    "Lateral axis (pitch)",
                    "Vertical axis (bank)"
                ],
                "answer": 2,
                "explanation": "The elevator controls pitch movement about the lateral axis. Pulling back raises the nose; pushing forward lowers it."
            },
            {
                "question": "What happens when an aircraft exceeds the critical angle of attack?",
                "options": [
                    "Lift increases sharply",
                    "Drag decreases",
                    "The wing stalls — lift drops suddenly",
                    "Thrust increases automatically"
                ],
                "answer": 2,
                "explanation": "Beyond the critical AoA (~15-16°), airflow separates from the upper wing surface, causing a sudden loss of lift — this is called a stall."
            },
            {
                "question": "In level unaccelerated flight, which forces are in equilibrium?",
                "options": [
                    "Lift = Drag and Thrust = Weight",
                    "Lift = Weight and Thrust = Drag",
                    "Lift = Thrust and Weight = Drag",
                    "All four forces are zero"
                ],
                "answer": 1,
                "explanation": "For steady level flight: Lift equals Weight (vertical equilibrium) and Thrust equals Drag (horizontal equilibrium)."
            },
            {
                "question": "Induced drag is produced as a result of?",
                "options": [
                    "Skin friction on the fuselage",
                    "Frontal area of the aircraft",
                    "Lift generation by the wings",
                    "Propeller slipstream"
                ],
                "answer": 2,
                "explanation": "Induced drag is a byproduct of lift production. It is caused by wingtip vortices that create a downwash, tilting the lift vector rearward. Higher angle of attack = more lift = more induced drag."
            },
            {
                "question": "ISA sea-level temperature and pressure are:",
                "options": [
                    "0°C and 1013.25 hPa",
                    "15°C and 1013.25 hPa",
                    "15°C and 1030 hPa",
                    "20°C and 1000 hPa"
                ],
                "answer": 1,
                "explanation": "ICAO ISA defines standard sea-level conditions as 15°C temperature and 1013.25 hPa pressure (29.92 inHg)."
            },
            {
                "question": "Which of the following increases stall speed?",
                "options": [
                    "Reducing aircraft weight",
                    "Extending flaps",
                    "Increasing bank angle",
                    "Reducing altitude"
                ],
                "answer": 2,
                "explanation": "Increasing bank angle increases the load factor (g-force), which raises the stall speed. VS_banked = VS_level × √(load factor)."
            },
            {
                "question": "Aspect Ratio of a wing is defined as:",
                "options": [
                    "Chord / Wingspan",
                    "Wingspan / Chord (= Span² / Area)",
                    "Wing Area / Chord",
                    "Lift / Drag ratio"
                ],
                "answer": 1,
                "explanation": "Aspect Ratio = Wingspan / Mean Chord = Span² / Wing Area. High aspect ratio wings (long, narrow) produce less induced drag — used in gliders and long-range aircraft."
            },
            {
                "question": "Angle of Attack is measured between:",
                "options": [
                    "The wing and the horizon",
                    "The chord line and the relative airflow",
                    "The fuselage and the ground",
                    "The camber line and the chord line"
                ],
                "answer": 1,
                "explanation": "Angle of Attack (AoA) is the angle between the chord line of the aerofoil and the relative airflow (relative wind) direction."
            },
            {
                "question": "A wing with positive static stability will:",
                "options": [
                    "Continue to diverge after a disturbance",
                    "Stay in the displaced position",
                    "Return to its original position after a disturbance",
                    "Oscillate with increasing amplitude"
                ],
                "answer": 2,
                "explanation": "Positive static stability means the aircraft has an initial tendency to return to its trimmed equilibrium position after being disturbed."
            },
            {
                "question": "True Airspeed (TAS) compared to Indicated Airspeed (IAS) at high altitude is:",
                "options": [
                    "Less than IAS",
                    "Equal to IAS",
                    "Greater than IAS",
                    "Depends only on temperature"
                ],
                "answer": 2,
                "explanation": "At higher altitudes, air density is lower. TAS = IAS corrected for density. Lower density means the aircraft moves through less dense air, so TAS > IAS. As a rule of thumb: TAS increases by ~2% per 1000 ft of altitude."
            },
            {
                "question": "Which type of drag decreases as airspeed increases?",
                "options": [
                    "Form drag",
                    "Skin friction drag",
                    "Induced drag",
                    "Interference drag"
                ],
                "answer": 2,
                "explanation": "Induced drag is inversely proportional to velocity squared (∝ 1/V²), so it decreases as airspeed increases. All parasite drag components (form, friction, interference) increase with speed."
            },
            {
                "question": "The standard lapse rate in the troposphere is:",
                "options": [
                    "1°C per 1000 ft",
                    "3°C per 1000 ft",
                    "2°C per 1000 ft",
                    "0.5°C per 1000 ft"
                ],
                "answer": 2,
                "explanation": "ISA standard lapse rate is 2°C (1.98°C) per 1000 ft altitude gain in the troposphere, up to the tropopause at approximately 36,000 ft."
            },
            {
                "question": "The point through which the resultant aerodynamic force acts on a wing is called:",
                "options": [
                    "Centre of Gravity",
                    "Neutral Point",
                    "Centre of Pressure",
                    "Aerodynamic Centre"
                ],
                "answer": 2,
                "explanation": "Centre of Pressure (CP) is the point on the aerofoil chord line through which the resultant aerodynamic lift force acts. It moves forward as AoA increases (in most aerofoils)."
            },
            {
                "question": "Wingtip vortices are formed due to:",
                "options": [
                    "Skin friction at the wing surface",
                    "High pressure air from below spilling to low pressure area above at the wingtip",
                    "Engine exhaust flowing over the wing",
                    "High speed airflow at leading edge"
                ],
                "answer": 1,
                "explanation": "Wingtip vortices form when high-pressure air beneath the wing flows around the wingtip toward the low-pressure area above, creating rotating vortices. These are responsible for induced drag and wake turbulence."
            },
        ],
    },

    {
        "id": 9,
        "number": 9,
        "title": "Human Factors",
        "study_material": [],
        "diagrams": [],
        "questions": [],
        "practice_test": [],
    },

    {
        "id": 10,
        "number": 10,
        "title": "Aviation Legislation",
        "study_material": [],
        "diagrams": [],
        "questions": [],
        "practice_test": [],
    },

    {
        "id": 11,
        "number": 11,
        "title": "Aeroplane Aerodynamics",
        "study_material": [],
        "diagrams": [],
        "questions": [],
        "practice_test": [],
    },
]
