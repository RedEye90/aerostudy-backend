# ═══════════════════════════════════════════════════════════
#  data.py  –  Yahan seedha content add/edit karo
#  Koi database nahi, koi admin panel nahi.
#  Bas Python dict mein content likho aur server restart karo.
# ═══════════════════════════════════════════════════════════


# ─────────────────────────────────────────────────────────
#  CPL SUBJECTS
# ─────────────────────────────────────────────────────────

CPL_SUBJECTS = [

    {
        "id": "navigation",
        "name": "Navigation",
        "icon": "🧭",
        "description": "Principles of aircraft navigation and procedures",

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
# ─────────────────────────────────────────────────────────

AME_MODULES = [

    {
        "id": 1,
        "number": 1,
        "title": "Mathematics",

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

        "diagrams": [
            {
                "title": "Trigonometry Circle",
                "description": "Unit circle showing sine, cosine values at key angles.",
                "image_url": ""
            },
        ],

        "questions": [
            {
                "year": "2022",
                "q": "Solve: 2x + 5 = 15",
                "a": "2x = 10, x = 5"
            },
        ],

        "practice_test": [
            {
                "question": "What is sin(90°)?",
                "options": ["0", "1", "-1", "0.5"],
                "answer": 1,
                "explanation": "sin(90°) = 1. At 90°, the sine function reaches its maximum value."
            },
        ],
    },

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

        # ── PRACTICE TEST – EASA M8 Question Bank (246 questions) ──
        "practice_test": [
            {
                "question": "On a swept wing aircraft if both wing tip sections",
                "options": ["roll", "pitch nose up", "pitch nose down"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Lift on a delta wing aircraft",
                "options": ["increases with an increased angle of incidence (angle of attack)", "decreases with an increase in angle of incidence (angle of attack)", "does not change with a change in angle of incidence (angle of attack)"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "On a straight wing aircraft, stall commences at the",
                "options": ["root on a high thickness ratio wing", "tip on a high thickness ratio wing", "tip on a low thickness ratio wing"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "On a high wing aircraft in a turn",
                "options": ["the up-going wing loses lift causing a de-stabilising effect", "the down-going wing gains lift causing a stabilising effect", "the down-going wing loses lift causing a de-stabilising effect"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "For the same angle of attack, the lift on a delta wing",
                "options": ["is greater than the lift on a high aspect ratio wing", "is lower than the lift on a high aspect ratio wing", "is the same as the lift on a high aspect ratio wing"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The ISA",
                "options": ["is taken from the equator", "is taken from 45 degrees latitude", "assumes a standard day"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "At higher altitudes as altitude increases, pressure",
                "options": ["decreases at constant rate", "increases exponentially", "decreases exponentially"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The thrust-drag couple overcomes the lift-weight",
                "options": ["upwards", "downwards", "sideways"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "When the pressure is half of that at sea level, what",
                "options": ["12,000 ft", "8,000 ft", "18,000 ft"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "During a turn, the stalling angle",
                "options": ["increases", "decreases", "remains the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The upper part of the wing in comparison to the lower",
                "options": ["develops more lift", "develops the same lift", "develops less lift"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What effect would a forward CG have on an aircraft on",
                "options": ["Increase stalling speed", "No effect on landing", "Reduce stalling speed"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "QNH refers to",
                "options": ["quite near horizon", "setting the altimeter to zero", "setting the mean sea level atmospheric pressure so an altimeter reads the aerodrome altitude above mean sea level"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "QNE refers to",
                "options": ["Setting an altimeter to read aerodrome altitude above sea level", "quite new equipment", "setting the mean sea level atmospheric pressure in accordance with ICAO standard atmosphere i.e. 1013 millibars"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "An aspect ratio of  8  would mean",
                "options": ["span 64, mean chord 8", "mean chord 64 , span 8", "span squared  64 ,chord 8"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If an aircraft in level flight loses engine power it",
                "options": ["pitch nose up", "pitch nose down", "not change pitch without drag increasing"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "QFE is",
                "options": ["sea level pressure", "airfield pressure", "difference between sea level and airfield"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The lift /drag ratio at stall",
                "options": ["increases", "decreases", "is unchanged"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "On a straight unswept wing, stall occurs at",
                "options": ["the thick portion, at the wing root", "the thick portion, at the wing tip", "the thin portion, at the wing tip"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "During a climb from a dive",
                "options": ["the thrust required is greater than required for level flight", "the thrust required is lower than for level flight", "the thrust required is the same as for level"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "An engine which produces an efflux of high speed will",
                "options": ["more efficient", "less efficient", "speed of efflux has no affect on the engine"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "When an aircraft with a C of G forward of the C of P",
                "options": ["stay level", "rise", "drop"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Directional stability may be increased with",
                "options": ["pitch dampers", "horn balance", "yaw dampers"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Lateral stability may be increased with",
                "options": ["increased lateral dihedral", "increased lateral anhedral", "increased longitudinal dihedral"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Longitudinal stability is increased if the",
                "options": ["CP moves forward of the CG", "Thrust acts on a line below the total drag", "CG is forward of the CP"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Wing loading is calculated by weight",
                "options": ["divided by gross wing area", "divided by lift", "multiplied by gross wing area"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Induced drag is",
                "options": ["inversely proportional to the square of speed", "proportional to speed", "nothing to do with speed"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "In a bank, the weight is",
                "options": ["increased", "decreased", "the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "L/D ratio is",
                "options": ["higher at supersonic cruise speed", "higher at sub sonic speed", "the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The power required at low altitude for a given IAS is",
                "options": ["the same as at high altitude", "higher", "lower"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If the stall speed is 75 knots. What is the same stall speed in mph?",
                "options": ["75 x 0.87", "75 / 0.87", "75 / 0.87 x relative density"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "As the angle of attack increases the stagnation point",
                "options": ["moves towards the upper surface", "moves towards the lower surface", "does not move"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The term pitch-up is due to",
                "options": ["compressibility effect", "ground effect", "longitudinal instability"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "In a steady climb at a steady IAS, the TAS is",
                "options": ["more than IAS", "less than IAS", "the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "An untapered straight wing will",
                "options": ["have no yaw effect in banking", "have no change in induced drag in the bank", "stall at the root first"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The lift/drag ratio is",
                "options": ["higher at mach numbers above supersonic", "higher at sub sonic mach numbers", "the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The force opposing thrust is",
                "options": ["drag", "lift", "Weight"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Directional stability is about the",
                "options": ["normal axis", "longitudinal axis", "lateral axis"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Lateral stability is about the",
                "options": ["longitudinal axis", "normal axis", "vertical axis"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which has the greater density?",
                "options": ["Air at low altitude", "Air at high altitude", "It remains constant"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "As air flows over the upper cambered surface of an aerofoil, what happens to velocity and pressure?",
                "options": ["Velocity decreases, pressure decreases", "Velocity increases, pressure increases", "Velocity increases, pressure decreases"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What is the force that tends to pull an aircraft down towards the earth?",
                "options": ["Drag", "Thrust", "Weight"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which of the following act in opposition to forward movement?",
                "options": ["Lift", "Gravity", "Drag"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The angle at which the chord line of the aerofoil is presented to the airflow is known as",
                "options": ["angle of attack", "angle of incidence", "resultant"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The imaginary straight line which passes through an aerofoil section from leading edge to trailing edge is called",
                "options": ["centre of pressure", "the direction of relative airflow", "the chord line"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What is the angle between the chord line of the wing, and the longitudinal axis of the aircraft, known as",
                "options": ["angle of attack", "angle of incidence", "angle of dihedral"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "An aircraft disturbed from its normal flight path, and automatically returns to that normal flight path, without any action on the part of the pilot is known as",
                "options": ["aircraft stability", "aircraft instability", "aircraft stall"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Directional control is provided by",
                "options": ["horizontal stabilizer", "rudder", "elevator"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "About which axis of the aircraft does a rolling motion take place?",
                "options": ["Normal axis", "Longitudinal axis", "Lateral axis"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which motion happens about the lateral axis?",
                "options": ["Pitching", "Yawing", "Rolling"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Wing tip vortices create a type of drag known as",
                "options": ["form drag", "induced drag", "profile drag"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which of the following describes the \u201cEmpennage\u201d?",
                "options": ["Nose section of an aircraft, including the cockpit", "Tail section of the aircraft, including fin, rudder, tail plane and elevators", "The wings, including the ailerons"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "At what altitude does stratosphere commence approximately?",
                "options": ["Sea level", "63,000 ft", "36,000 ft"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "When an aircraft is in straight and level unaccelerated flight, which of the following is correct?",
                "options": ["Lift and weight are equal, and thrust and drag are equal", "Lift greater than weight, and thrust greater than drag", "Lift greater than weight, and thrust is less"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "As the angle of attack is increased (up to the stall point), which of the following is correct?",
                "options": ["Pressure difference between top and bottom of the wing increases", "Lift increases", "Both a) and b) are correct"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The fin gives stability about which axis?",
                "options": ["Lateral axis", "Normal axis", "Longitudinal axis"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What is the horizontal movement of the nose of the aircraft called?",
                "options": ["Rolling movement", "Pitching movement", "Yawing movement"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What type of drag, depends on the smoothness of the body, and surface area over which the air flows?",
                "options": ["Parasite drag", "Form drag", "Skin friction drag"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If the nose of the aircraft is rotated about its lateral axis, what is its directional movement?",
                "options": ["Turning to the left or right", "Rolling or banking to the left or right", "Climbing or diving"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "When air flow velocity over an upper cambered surface of an aerofoil decreases, what takes place?",
                "options": ["Pressure increases, lift decreases", "Pressure increases, lift increases", "Pressure decreases, lift increases"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "When an aircraft stalls",
                "options": ["lift and drag increase", "lift increases and drag decreases", "lift decreases and drag increases"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Wing loading is",
                "options": ["the maximum all up weight multiplied by the total wing area", "the maximum all up weight divided by the total wing area", "the ratio of the all up weight of the aircraft to its basic weight"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "An aircraft wing with an aspect ration of 6:1 is proportional so that",
                "options": ["the mean chord is six times the thickness", "the wing span is six times the mean chord", "the wing area is six times the span"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Upward and outward inclination of a mainplane is termed",
                "options": ["sweep", "dihedral", "stagger"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The function of an aircraft fin",
                "options": ["is to provide stability about the normal axis", "is to provide directional control", "is to provide straight airflow across the"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Movement of an aircraft about its normal axis",
                "options": ["is pitching", "is rolling", "is yawing"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A pressure of one atmosphere is equal to",
                "options": ["14.7 psi", "100 millibar", "1 inch Hg."],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The millibar is a unit of",
                "options": ["atmospheric temperature", "pressure altitude", "barometric pressure"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "With an increase in altitude under I.S.A. conditions the temperature in the troposphere",
                "options": ["increases", "decreases", "remains constant"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The pendulum effect on a high wing aircraft",
                "options": ["increases lateral stability", "decreases lateral stability", "has no effect on lateral stability"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The amount of water vapor capacity in the air (humidity holding capacity of the air) is",
                "options": ["greater on a colder day, and lower on a hotter day", "greater on a hotter day and lower on a colder day", "doesn't have a significant difference"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Weight is equal to",
                "options": ["volume x gravity", "mass x acceleration", "mass x gravity"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Induced drag",
                "options": ["increases with an increase in speed", "reduces with an increase in angle of attack", "increases with increase in aircraft weight"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Airflow over the upper surface of the wing generally",
                "options": ["flows towards the root", "flows towards the tip", "flows straight from leading edge to trailing"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "With an increase in aspect ratio for a given IAS, induced drag will",
                "options": ["remain constant", "increase", "reduce"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "With increasing altitude the angle at which a wing will stall",
                "options": ["remains the same", "reduces", "increases"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If the density of the air is increased, the lift will",
                "options": ["increase", "decrease", "remain the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "All the factors that affect the lift produced by an aerofoil are",
                "options": ["angle of attack, air density, velocity, wing area", "angle of attack, air temperature, velocity, wing area", "angle of attack, velocity, wing area,"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A wing section suitable for high speed would be",
                "options": ["thick with high camber", "thin with high camber", "thin with little or no camber"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The induced drag of an aircraft",
                "options": ["increases with increasing speed", "increases if aspect ratio is increased", "decreases with increasing speed"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "As the speed of an aircraft increases the profile drag",
                "options": ["increases", "decreases", "decreases at first then increase"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The stagnation point on an aerofoil is the point where",
                "options": ["the suction pressure reaches a maximum", "the boundary layer changes from laminar to", "the airflow is brought completely to rest"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "After a disturbance in pitch, an aircraft continues to oscillate at constant amplitude. It is",
                "options": ["longitudinally unstable", "longitudinally neutrally stable", "laterally unstable"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "On an aircraft with an all-moving tailplane nose up pitch is caused by",
                "options": ["increasing tailplane incidence", "decreasing tailplane incidence", "up movement of the trim tab"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The stalling of an aerofoil is affected by the",
                "options": ["airspeed", "angle of attack", "transition speed"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What gives the aircraft directional stability?",
                "options": ["Vertical stabiliser", "Horizontal stabiliser", "Elevators"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The most fuel efficient of the following types of engine is the",
                "options": ["rocket", "turbo-jet engine", "turbo-fan engine"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The quietest of the following types of engine is the",
                "options": ["rocket", "turbo-jet engine", "turbo-fan engine"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Forward motion of a glider is provided by",
                "options": ["the engine", "the weight", "the drag"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Induced downwash",
                "options": ["reduces the effective angle of attack of the wing", "increases the effective angle of attack of the wing", "has no effect on the angle of attack of the"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which is the ratio of the water vapour actually present in the atmosphere to the amount that would be present if the air were saturated at the prevailing temperature and pressure?",
                "options": ["Absolute humidity", "Relative humidity", "Dew point"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Given 2 wings, the first with a span of 12m and a chord of 2 m. The second has a span of 6m and a chord of 1m. How do their Aspect Ratios compare?",
                "options": ["The first is higher", "The second is higher", "They are the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The C of G moves in flight.  The most likely cause of this is",
                "options": ["movement of passengers", "movement of cargo", "consumption of fuel and oils"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The speed of sound in the atmosphere",
                "options": ["varies according to the frequency of the sound", "changes with a change in temperature", "changes with a change in pressure"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A straight rectangular wing, without any twist, will",
                "options": ["stall first at the tip", "stall first at the root", "stall equally along the span of the wing"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What is sea level pressure?",
                "options": ["1013.2 mb", "1012.3 mb", "1032.2 mb"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which atmospheric conditions will cause the true landing speed of an aircraft to be the greatest?",
                "options": ["Low temperature with low humidity", "High temperature with low humidity", "High temperature with high humidity"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "In flight if your aircraft nose gets an upward gust of wind, what characteristic will have the greatest effect to counteract it?",
                "options": ["Horizontal stabiliser and fuselage length", "Wing Sweep", "Position of the centre of pressure relative"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "When the weight of an aircraft increases, the minimum drag speed",
                "options": ["decreases", "increases", "remains the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which statement concerning heat and/or temperature is true?",
                "options": ["There is an inverse relationship between temperature and heat.", "Temperature is a measure of the kinetic energy of the molecules of any substance", "Temperature is a measure of the potential energy of the molecules of any substance"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "To correct dutch roll you must damp oscillation around:",
                "options": ["The vertical axis", "The lateral axis", "The longitudinal axis"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "When an aircraft experiences induced drag",
                "options": ["air flows under the wing spanwise towards the tip and on top of the wing spanwise towards the root", "air flows under the wing spanwise towards the root and on top of the wing spanwise towards the tip", "Neither a) or b) since induced drag does not"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What is absolute humidity?",
                "options": ["The temperature to which humid air must be cooled at constant pressure to become saturated.", "The actual amount of the water vapour in a mixture of air and water", "The ratio of the water vapour actually present in the atmosphere to the amount that would be present if the air were saturated at the prevailing temperature and pressure"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If the load factor on an aircraft is 2, the stall speed is",
                "options": ["increased", "decreased", "stays the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "An elevator trim tab is used to",
                "options": ["prevent the control surface from stalling the airflow", "reduce control column forces on the pilot", "counteract propeller torque"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "On a power curve graph the intersection of available power and required power against speed gives the",
                "options": ["most efficient cruise speed", "minimum drag speed", "the aircraft's maximum speed"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "An aeroplane wing is designed to produce lift resulting from relatively",
                "options": ["positive air pressure below and above the wing's surface", "negative air pressure below the wing's surface and positive air pressure above the wing's surface", "positive air pressure below the wing's surface and negative air pressure above the wing's surface"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The Lift/Drag ratio of a wing at the stalling angle is",
                "options": ["of a negative value", "low", "high"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The speed of air over a swept wing which contributes to the lift is",
                "options": ["less than the aircraft speed", "more than the aircraft speed", "the same as the aircraft speed"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "For a given angle of attack induced drag is",
                "options": ["greater on a high aspect ratio wing", "greater towards the wing root", "greater on a low aspect ratio wing"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "In straight and level flight, the angle of attack of a swept wing is",
                "options": ["the same as the aircraft angle to the horizontal", "more than the aircraft angle to the horizontal", "less than the aircraft angle to the"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A delta wing aircraft flying at the same speed (subsonic) and angle of attack as a swept wing aircraft of similar wing area will produce",
                "options": ["the same lift", "more lift", "less lift"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The stagnation point is",
                "options": ["static pressure plus dynamic pressure", "static pressure minus dynamic pressure", "dynamic pressure only"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "On a swept wing aircraft, due to the adverse pressure gradient, the boundary layer on the upper surface of the wing tends to flow",
                "options": ["directly from leading edge to trailing edge", "towards the tip", "towards the root"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "With increased speed in level flight",
                "options": ["induced drag increases", "profile drag increases", "profile drag remains constant"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "At stall, the wingtip stagnation point",
                "options": ["moves toward the lower surface of the wing", "moves toward the upper surface of the wing", "doesn\u2019t move"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "How does IAS at the point of stall vary with height?",
                "options": ["It is practically constant", "It increases", "It decreases"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The rigging angle of incidence of an elevator is",
                "options": ["the angle between the mean chord line and the horizontal in the rigging position", "the angle between the bottom surface of the elevator and the horizontal in the rigging position", "the angle between the bottom surface of the"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What is the lapse rate with regard to temperature?",
                "options": ["1.98oC per 1000 ft", "1.98oF per 1000 ft", "4oC per 1000 ft"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What happens to load factor as you decrease turn radius?",
                "options": ["It increases", "It decreases", "It remains constant"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If you steepen the angle of a banked turn without increasing",
                "options": ["It will remain at the same height", "It will sideslip with attendant loss of height", "It will stall"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "An aircraft wing tends to stall first at",
                "options": ["the tip due to a higher ratio thickness/chord", "the tip due to a lower ratio thickness/chord", "the root due to a higher ratio thickness/chord"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Dihedral wings combat instability in",
                "options": ["pitch", "yaw", "sideslip"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "To stop aircraft decreasing in height during a sideslip, the",
                "options": ["advance the throttle", "pull back on the control column", "adjust the rudder position"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What control surface movements will make an aircraft fitted",
                "options": ["Left ruddervator lowered, right ruddervator raised", "Right ruddervator lowered, left ruddervator raised", "Both ruddervators raised"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If a swept wing stalls at the tips first, the aircraft will",
                "options": ["pitch nose up", "pitch nose down", "roll"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The thickness/chord ratio of the wing is also known as",
                "options": ["aspect ratio", "mean chord ratio", "fineness ratio"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Flexure of a rearward swept wing will",
                "options": ["increase the lift and hence increase the flexure", "decrease the lift and hence decrease the flexure", "increase the lift and hence decrease the flexure"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A High Aspect Ratio wing is a wing with",
                "options": ["long span, long chord", "long span, short chord", "short span, long chord"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "An aircraft flying in \u201cground effect\u201d will produce",
                "options": ["more lift than a similar aircraft outside of ground effect", "less lift than a similar aircraft outside of ground effect", "the same lift as a similar aircraft outside"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If the angle of attack of a wing is increased in flight, the",
                "options": ["C of P will move forward", "C of G will move aft", "C of P will move aft"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The Rams Horn Vortex on a forward swept wing will be",
                "options": ["the same as a rearward swept wing", "more than a rearward swept wing", "less than a rearward swept wing"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "When maintaining level flight an increase in speed will",
                "options": ["cause the C of P to move aft", "cause the C of P to move forward", "have no affect on the position of the C of P"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "For a cambered wing section the zero lift angle of attack will be",
                "options": ["zero", "4 degrees", "negative"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Density changes with altitude at a rate",
                "options": ["of 2kg/m3 per 1000ft", "which changes with altitude", "which is constant until 11km"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Airflow at subsonic speed is taken to be",
                "options": ["compressible", "incompressible", "either a or b depending on altitude"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Bernoulli's equation shows that",
                "options": ["at constant velocity the kinetic energy of the air changes with a change of height", "with a change in speed at constant height both kinetic and potential energies change", "with a change in velocity at constant height the static pressure will change"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If fluid flow through a venturi is said to be incompressible, the speed of the flow increases at the throat to",
                "options": ["maintain a constant volume flow rate", "allow for a reduction in static pressure", "allow for an increase in static pressure"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "To produce lift, an aerofoil must be",
                "options": ["asymmetrical", "symmetrical", "either a or b above"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Lift is dependent on",
                "options": ["the area of the wing, the density of the fluid medium, and the square of the velocity", "the net area of the wing ,the density of the fluid medium and the velocity", "the frontal area of the wing, the density of the fluid medium and the velocity"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The maximum lift/drag ratio of a wing occurs",
                "options": ["at the angle of attack where the wing develops its maximum lift", "during take off", "at an angle below which the wing develops"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A wing develops 10,000N of lift at 100knots. Assuming the wing remains at the same angle of attack and remains at the same altitude, how much lift will it develop at 300knots?",
                "options": ["900,000 N", "90,000 N", "30,000 N"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The angle of attack is",
                "options": ["related to angle of incidence", "always kept below 15 degrees", "not related to the angle of incidence"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The difference between the mean camber line and the chord line of an aerofoil is",
                "options": ["one is always straight and the other may be straight", "neither are straight", "they both may be curved"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "With all conditions remaining the same, if the aircraft speed is halved, by what factor is the lift reduced?",
                "options": ["Half", "By a factor of 4", "Remains the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The boundary layer over an aerofoil is",
                "options": ["a layer of air close to the aerofoil that is stationary", "a layer of air close to the aerofoil which is moving at a velocity less than free stream air", "a layer of turbulent air close to the aerofoil which is moving at a velocity less than free stream air"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "On a swept wing aircraft, the fineness ratio of an aerofoil is",
                "options": ["highest at the root", "highest at the tip", "equal throughout the span"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "IAS for a stall will",
                "options": ["increase with altitude", "decrease with altitude", "roughly remain the same for all altitude"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If the radius of a turn is reduced the load factor will",
                "options": ["increase", "decrease", "remain the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Streamlining will reduce",
                "options": ["form drag", "induced drag", "skin friction drag"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If an aircraft has a gross weight of 3000 kg and is then subjected to a total weight of 6000 kg",
                "options": ["2G", "3G", "9G"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A constant rate of climb is determined by",
                "options": ["weight", "wind speed", "excess engine power"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Ice formed on the leading edge will cause the aircraft to",
                "options": ["stall at the same stall speed and AoA", "stall at a lower speed", "stall at a higher speed"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "With an aircraft in bank, the upper wing produces more drag. To compensate",
                "options": ["the rudder is operated", "when bank angle is achieved then the ailerons are operated in the opposite direction to cause the opposite effect", "angle of attack is increased"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If both wings lose lift the aircraft",
                "options": ["pitches nose up", "pitches nose down", "glides on a horizontal plane"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Under what conditions will an aircraft create best lift?",
                "options": ["Cold dry day at 200 ft", "Hot damp day at 1200 ft", "Cold wet day at 1200 ft"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If there is an increase of density, what effect would there be in aerodynamic dampening?",
                "options": ["None", "Decreased", "Increased"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "As Mach number increases, what is the effect on boundary layer?",
                "options": ["Becomes more turbulent", "Becomes less turbulent", "Decreases in thickness"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "When a slat is retracted it moves",
                "options": ["towards the upper leading edge of the wing", "towards the lower leading edge of the wing", "towards the center of the leading edge of"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "In a turn the up-going wing causes a",
                "options": ["de-stabilising effect due to increased AoA", "de-stabilising effect due to decreased AoA", "stabilising effect due to decreased AoA"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The stagnation point consists of",
                "options": ["dynamic and static air pressure", "static air pressure", "dynamic air pressure"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "During a glide the following forces act on an aircraft",
                "options": ["lift, weight, thrust", "lift, drag, weight", "lift and weight only"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Yawing is a rotation around",
                "options": ["the normal axis obtained by the elevator", "the lateral axis obtained by the rudder", "the normal axis obtained by the rudder"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If an aileron is moved downward",
                "options": ["the stalling angle of that wing is increased", "the stalling angle of that wing is decreased", "the stalling angle is not affected but the"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Induced drag can be reduced by the use of",
                "options": ["streamlining", "high aspect ratio wings", "fairings at junctions between fuselage and"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Interference drag can be reduced by the use of",
                "options": ["streamlining", "high aspect ratio wings", "fairings at junctions between fuselage and"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A centre of gravity position close to its aft limit will cause the aircraft to",
                "options": ["pitch nose up and decrease it\u2019s longitudinal stability", "pitch nose down and increase it\u2019s longitudinal stability", "pitch nose up and increase it\u2019s longitudinal"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The result of an aircraft flying into a rainstorm of super cooled rain droplets would be an accretion of",
                "options": ["rime ice", "hoar ice", "glaze ice"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Ice accretion on an aircraft in flight that is opaque, rough, with low shear strength is",
                "options": ["rime ice", "hoar ice", "glaze ice"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "In a steady climb",
                "options": ["thrust is greater than drag", "thrust is equal to drag", "thrust is less than drag"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "On a slender delta wing at low speed the lift/drag ratio is",
                "options": ["reduced", "increased", "constant"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A high winged aircraft in a turn requires returning to level flight.",
                "options": ["Lift must decrease on the upper wing", "Lift must increase on the upper wing", "Lift must decrease on the lower wing"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What happens to the load factor as you decrease the turn radius?",
                "options": ["Load factor increases", "Load factor decreases", "Load factor remains constant"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A high wing aircraft in a banked turn increases it\u2019s angle of bank without increasing it\u2019s angle of attack. The aircraft will",
                "options": ["side slip", "side slip with a loss of altitude", "come out of the turn early"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If the ambient temperature at sea level decreases, the operational ceiling height of the aircraft",
                "options": ["increases", "decreases", "stays the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A sharply swept wing will promote",
                "options": ["excessive lateral instability", "excessive lateral stability", "excessive longitudinal stability"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which control surfaces provide directional and pitch control?",
                "options": ["Elevons", "Ruddervators", "Tailerons"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which control surfaces provide lateral control, also longitudinal control and stability?",
                "options": ["Flapperons", "Ruddervators", "Tailerons"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Under the category system the design load factor for an airplane in the normal category is",
                "options": ["4.4 g", "3.8 g", "5.7 g"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The degree of aeroplane wing loading during level coordinated turn in smooth air depends upon",
                "options": ["angle of bank", "rate of turn", "density altitude"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The primary purpose of wing spoilers is to",
                "options": ["decrease lift of the wing by disturbing the airflow", "decrease landing speed", "increase drag"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Wing flap is a",
                "options": ["primary control surface", "secondary control surface", "high lift device"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which of the following is true?",
                "options": ["Lift acts at right angles to the wing chord line and weight acts vertically down", "Lift acts at right angles to the relative airflow and weight acts vertically down", "Lift acts at right angles to the relative air  flow and weight acts at right angles to the aircraft centre line"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If the wing tips stall before the root on a swept wing",
                "options": ["roll", "pitch nose up", "pitch nose down"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Standard sea level temperature is",
                "options": ["0 degrees Celsius", "15 degrees Celsius", "20 degrees Celsius"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "As altitude increases, pressure",
                "options": ["decreases at constant rate", "increases exponentially", "decreases exponentially"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Deployment of a split flap will",
                "options": ["increase wing area and increase drag", "pitch the nose down and decrease drag", "increase camber and increase drag"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The total drag of an aircraft",
                "options": ["increases with the square of speed", "increases with speed", "changes with speed"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Put in sequence from the ground",
                "options": ["troposphere, tropopause, stratosphere", "tropopause, stratosphere, troposphere", "troposphere, tropopause, stratosphere"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If, after a disturbance, an aeroplane initially returns to its equilibrium state",
                "options": ["it has neutral stability", "it is neutrally unstable", "it has static stability and may be"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A stick shaker is intended to come into operation",
                "options": ["at the actual moment of aircraft stall", "prior to the actual moment of aircraft stall", "immediately after the aircraft is stalled"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "------ angle of attack is known as optimum angle of attack",
                "options": ["10 to 12 degrees", "3 to 4 degrees", "5 to 7 degrees"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "True stalling speed of an aircraft increases with altitude",
                "options": ["because reduced temperature causes compressibility effect", "because air density is reduced", "because humidity is increased and this"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Yaw dampers are designed to",
                "options": ["prevent dutch roll", "assist the pilot to move the rudder", "reduce the effect of crabbing due to cross"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Tuck under occurs when",
                "options": ["a shock stall occurs on the outboard portion of the swept wing", "a shock stall warning occurs on the inboard position of a straight wing", "the aircraft reaches Mcrit"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Induced drag is ------------ at root",
                "options": ["greatest", "lowest", "neutral"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Profile drag is --------- to speed",
                "options": ["neutral", "inversely proportional", "proportional"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The lateral axis is",
                "options": ["a straight line through the CG parallel to a line \t\t\t  joining the wingtips", "a straight line through the CG from nose to tail", "a straight line through the CG at right angles \t\t\t\t to the longitudinal and lateral axis"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The main factors which affect longitudinal \t\t\t\t  stability are",
                "options": ["design of the tailplane and position of the CG", "design of the mainplane and position of the CG", "design of the fuselage and position of the CG"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A yawing motion provides what kind of Stability?",
                "options": ["Lateral", "Longitudinal", "Directional"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "During inverted level flight an aircraft \t\t\t\t\t  accelerometer shows",
                "options": ["0g", "-2g", "-1g"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "During straight and level flight an aircraft \t\t\t\t  accelerometer shows",
                "options": ["2g", "1g", "4g"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "When is the L/D (Lift to Drag) ratio at its \t\t\t\t  highest. When the AoA is",
                "options": ["0 degrees", "4 degrees", "at stall"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which of the following is incorrect about induced \t\t\t  drag?",
                "options": ["It will increase inversely to the square of the \t\t\t  \t airspeed", "It will decrease in proportion to the square of \t\t\t\t the airspeed", "It will increase when the angle of attack is \t\t\t\t reduced"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which of the following is true about forces \t\t\t\t  acting on an aircraft during climb?",
                "options": ["Lift acts at right angles to the flight path and \t\t\t  the weight acts vertically downwards", "Lift acts at right angles to the longitudinal axis \t\t\t and weight act at right angles to the flight path", "Both lift and weight act at right angles to the \t\t\t\t flight path"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which of the following L/D ratio will enable one \t\t\t  to achieve maximum distance in a glide?",
                "options": ["Maximum L/D", "Minimum L/D", "Zero L/D"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "If an aircraft is turned/controlled to the left, \t\t\t   what happens to the speed of the airflow over \t\t\t\t   the left wing?",
                "options": ["Increases", "Decreases", "Stays the same"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Vortex generators on the wing are most effective at",
                "options": ["high speed", "low speed", "high angles of attack"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The chord line of a wing is a line that runs from",
                "options": ["the centre of the leading edge of the wing to the trailing edge", "half way between the upper and lower surface of the wing", "one wing tip to the other wing tip"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The angle of incidence of a wing is an angle formed by lines",
                "options": ["parallel to the chord line and longitudinal axis", "parallel to the chord line and the lateral axis", "parallel to the chord line and the vertical axis"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The centre of pressure of an aerofoil is located",
                "options": ["30 - 40% of the chord line back from the leading edge", "30 - 40% of the chord line forward of the leading edge", "50% of the chord line back from the leading edge"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Lateral control of an aircraft at high angle of attack can be",
                "options": ["fences", "vortex generators", "wing slots"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Stall strips are always",
                "options": ["made of metal", "on the leading edge of a wing", "fitted forward of the ailerons"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Stall strips",
                "options": ["cause the wing root to stall", "cause the wing tip to stall", "cause the wings to stall symmetrically"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Due to the interference of the airflow on a high wing aircraft",
                "options": ["the upper wing to increase its lift", "the upper wing to decrease its lift", "the lower wing to decrease its lift"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Slats",
                "options": ["reduce the stall speed", "reduce the tendency of the aircraft to Yaw", "decrease the aerofoil drag at high speeds"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A high aspect ratio wing will give",
                "options": ["high profile and low induced drag", "low profile and high induced drag", "low profile and low induced drag"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Aerofoil efficiency is defined by",
                "options": ["lift over drag", "drag over lift", "lift over weight"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "An aircraft banks into a turn. No change is made to the",
                "options": ["The aircraft enters a side slip and begins to lose altitude", "The aircraft turns with no loss of height", "The aircraft yaws and slows down"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The relationship between induced drag and airspeed is, induced",
                "options": ["directly proportional to the square of the speed", "inversely proportional to the square of the speed", "directly proportional to speed"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What is the definition of Angle of Incidence?",
                "options": ["The angle the underside of the mainplane or tailplane makes with the horizontal", "The angle the underside of the mainplane or tailplane makes with the longitudinal datum line", "The angle the chord of the mainplane or tailplane makes with the horizontal"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What is Boundary Layer?",
                "options": ["Separated layer of air forming a boundary at the leading edge", "Turbulent air moving from the leading edge to trailing edge", "Sluggish low energy air that sticks to the wing surface and gradually gets faster until it joins the free stream flow of air"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The normal axis of an aircraft passes through",
                "options": ["the centre of gravity", "a point at the centre of the wings", "at the centre of pressure"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "On a high winged aircraft, what effect will the fuselage have",
                "options": ["The up-going wing will have a decrease in angle of attack and therefore a decrease in lift", "The down-going will have a decrease in angle of attack and therefore a decrease in lift", "The up-going wing will have an increase in angle of \t\t\tattack and therefore a decrease in lift"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What is the collective term for the fin and rudder and other",
                "options": ["Effective keel surface", "Empennage", "Fuselage surfaces"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Temperature above 36,000 feet will",
                "options": ["decrease exponentially", "remain constant", "increase exponentially"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A decrease in incidence toward the wing tip may be",
                "options": ["prevent adverse yaw in a turn", "prevent spanwise flow in maneuvers", "retain lateral control effectiveness at high"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The angle of attack which gives the best L/D ratio",
                "options": ["decreases with a decrease in density", "in unaffected by density changes", "increases with a decrease in density"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "For a given aerofoil production lift, where",
                "options": ["P1 is greater than P2, and V1 is greater than V2", "P1 is less than P2 and V1 is greater than V2", "P1 is greater than P2, and V1 is less than"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Low wing loading",
                "options": ["increases stalling speed, landing speed and landing run", "increases lift, stalling speed and maneuverability", "decreases stalling speed, landing speed and"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Due to the change in downwash on an untapered wing",
                "options": ["not provide any damping effect when rolling", "tend to stall first at the root", "not suffer adverse yaw effects when turning"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "True stalling speed of an aircraft increases with",
                "options": ["because reduced temperature causes compressibility effect", "because air density is reduced", "because humidity is increased and this"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "As a general rule, if the aerodynamic angle of incidence",
                "options": ["never move", "move forward towards the leading edge", "move towards the tip"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The \"wing setting angle\" is commonly known as",
                "options": ["angle of incidence", "angle of attack", "angle of dihedral"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "On a very  humid day, an aircraft taking off would",
                "options": ["a shorter take off run", "a longer take off run", "humidity does not affect the take off run"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "An aircraft is flying at 350 MPH, into a head wind of",
                "options": ["175 mph", "275 mph", "200 mph"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "When does the angle of incidence change?",
                "options": ["When the aircraft attitude changes", "When the aircraft is ascending or descending", "It never changes"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "As the angle of attack decreases, what happens to the",
                "options": ["It moves forward", "It moves rearwards", "Centre of pressure is not affected by angle"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "A decrease in pressure over the upper surface of a wing",
                "options": ["approximately 2/3 (two thirds) of the lift obtained", "approximately 1/3 (one third) of the lift obtained", "approximately 1/2 (one half) of the"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which of the four forces act on an aircraft?",
                "options": ["Lift, gravity, thrust and drag", "Weight, gravity, thrust and drag", "Lift, weight, gravity and drag"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Which of the following types of drag increases as the",
                "options": ["Parasite drag", "Induced drag", "Interference drag"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Correcting for a disturbance which has caused a rolling",
                "options": ["Lateral stability", "Directional stability", "Longitudinal stability"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The layer of air over the surface of an aerofoil which is slower moving, in relation to the rest of",
                "options": ["camber layer", "boundary layer", "none of the above"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "What is a controlling factor of turbulence and skin friction?",
                "options": ["Aspect ratio", "Fineness ratio", "Counter sunk rivets  used on skin exterior"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "Changes in aircraft weight",
                "options": ["will not affect total drag since it is dependant only upon speed", "cause corresponding changes in total drag due to the associated lift change", "will only affect total drag if the lift is kept constant"],
                "answer": 0,
                "explanation": ""
            },
            {
                "question": "The aircraft stalling speed will",
                "options": ["increase with an increase in weight", "be unaffected by aircraft weight changes since it is dependant upon the angle of attack", "only change if the MTMA were changed"],
                "answer": 0,
                "explanation": ""
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
