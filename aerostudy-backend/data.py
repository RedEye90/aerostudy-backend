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
        "study_material": [],
        "diagrams": [],
        "questions": [],
        "practice_test": [],
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
