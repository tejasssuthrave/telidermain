"""
Database of skin disease information including causes, symptoms, and treatments.
This module provides structured data about common skin conditions for the prediction module.
"""

def get_disease_info():
    """
    Returns a dictionary with detailed information about skin diseases.
    
    Each disease entry contains:
    - name: Full name of the condition
    - description: Brief description
    - causes: Common causes
    - symptoms: Key symptoms
    - treatments: Treatment options
    - severity: Condition severity level (Mild, Moderate, Severe)
    - contagious: Whether the condition is contagious
    - when_to_see_doctor: When medical attention should be sought
    - prevention: Prevention strategies and tips
    - additional_resources: Links to trusted resources for more information
    """
    return {
        "Acne": {
            "name": "Acne (Acne Vulgaris)",
            "description": "A common skin condition where hair follicles become clogged with oil and dead skin cells.\nCauses pimples, blackheads, and whiteheads typically on the face, chest, and back.",
            "causes": "Excess oil production, bacteria, inflammation, clogged pores, hormonal changes, and genetics.",
            "symptoms": "Whiteheads, blackheads, pimples, and in severe cases, painful nodules and cysts.",
            "treatments": "Topical treatments (benzoyl peroxide, retinoids), oral antibiotics, hormonal therapy, and isotretinoin for severe cases.",
            "severity": "Mild to Moderate",
            "contagious": "No, acne is not contagious and cannot spread from person to person.",
            "when_to_see_doctor": "Consult a dermatologist if over-the-counter treatments aren't effective after 2-3 months, if your acne is severe (many painful cysts and nodules), or if it's causing significant scarring or emotional distress.",
            "prevention": "• Wash face twice daily with a gentle cleanser\n• Use non-comedogenic (won't clog pores) moisturizers and makeup\n• Avoid touching your face\n• Clean items that touch your face regularly (phones, pillowcases)\n• Maintain a healthy diet and stay hydrated",
            "additional_resources": {
                "American Academy of Dermatology": "https://www.aad.org/public/diseases/acne",
                "Mayo Clinic": "https://www.mayoclinic.org/diseases-conditions/acne/symptoms-causes/syc-20368047"
            }
        },
        "Atopic Dermatitis": {
            "name": "Atopic Dermatitis (Eczema)",
            "description": "A chronic inflammatory skin condition characterized by dry, itchy skin.\nCauses red, inflamed patches that may become cracked, scaly, and sometimes ooze fluid when scratched.",
            "causes": "Immune system dysfunction, genetics, environmental triggers, and skin barrier defects.",
            "symptoms": "Dry, itchy, red, and inflamed skin that may develop small, fluid-filled bumps that weep when scratched.",
            "treatments": "Moisturizers, topical corticosteroids, calcineurin inhibitors, antihistamines, and avoiding triggers.",
            "severity": "Mild to Severe",
            "contagious": "No, eczema is not contagious and cannot be spread from person to person.",
            "when_to_see_doctor": "Consult a healthcare provider if:\n• Your skin becomes painful, extremely red, or weeps yellow fluid\n• Home treatments aren't working after 1 week\n• The condition interferes with sleep or daily activities\n• You suspect your skin is infected (increased pain, redness, swelling, warmth, or pus)\n• You develop eye complications (redness, itching, or discharge)",
            "prevention": "• Moisturize your skin at least twice daily with fragrance-free products\n• Identify and avoid triggers (certain foods, allergens, stress)\n• Take shorter, lukewarm (not hot) baths or showers\n• Use gentle, fragrance-free soaps and detergents\n• Wear soft, breathable fabrics like cotton\n• Manage stress through meditation or other relaxation techniques\n• Use a humidifier in dry or cold weather",
            "additional_resources": {
                "National Eczema Association": "https://nationaleczema.org/",
                "American Academy of Dermatology": "https://www.aad.org/public/diseases/eczema/atopic-dermatitis"
            }
        },
        "Psoriasis": {
            "name": "Psoriasis",
            "description": "A chronic autoimmune condition causing rapid skin cell growth leading to thick, scaly patches.\nCauses distinctive red patches with silvery scales, commonly on elbows, knees, scalp, and lower back.",
            "causes": "Immune system dysfunction, genetics, and environmental triggers such as stress, injuries, or infections.",
            "symptoms": "Red patches of skin covered with thick, silvery scales, dry and cracked skin that may bleed, itching, and soreness.",
            "treatments": "Topical treatments, phototherapy, oral or injected medications, and biologics targeting specific immune system pathways."
        },
        "Seborrheic Keratosis": {
            "name": "Seborrheic Keratosis",
            "description": "Common benign skin growths that appear as waxy, stuck-on lesions.\nThese harmless growths often appear in middle-aged and older adults as light brown to black raised spots.",
            "causes": "Aging, genetic factors, and sun exposure, though exact causes remain unclear.",
            "symptoms": "Light brown to black, waxy or scaly, slightly raised growths with a 'stuck-on' appearance.",
            "treatments": "Usually no treatment is needed as they are benign. If desired for cosmetic reasons, they can be removed via cryotherapy, curettage, or electrosurgery."
        },
        "Melanoma": {
            "name": "Melanoma",
            "description": "The most serious type of skin cancer that develops from the pigment-producing cells.\nOften appears as a new or changing mole with irregular borders, multiple colors, and asymmetry.",
            "causes": "UV radiation exposure, genetic factors, and having many moles or atypical moles.",
            "symptoms": "Asymmetrical moles, borders that are irregular, color that varies, diameter larger than 6mm, and evolving size/shape/color.",
            "treatments": "Surgery to remove the melanoma and surrounding tissue, and potentially lymph nodes. Advanced cases may require immunotherapy, targeted therapy, radiation, or chemotherapy.",
            "severity": "Severe",
            "contagious": "No, melanoma is not contagious and cannot spread from person to person.",
            "when_to_see_doctor": "See a dermatologist IMMEDIATELY if you notice:\n• A new mole that looks different from your other moles\n• A mole that changes in size, shape, or color\n• Any mole with the ABCDE warning signs (Asymmetry, Border irregularity, Color variation, Diameter >6mm, Evolving)\n• Early detection is critical for successful treatment of melanoma.",
            "prevention": "• Apply broad-spectrum sunscreen (SPF 30+) year-round\n• Wear protective clothing, wide-brimmed hats, and sunglasses\n• Seek shade between 10 AM and 4 PM\n• Avoid tanning beds and sunlamps\n• Perform regular skin self-examinations\n• Get annual skin checks from a dermatologist",
            "additional_resources": {
                "Skin Cancer Foundation": "https://www.skincancer.org/skin-cancer-information/melanoma/",
                "American Academy of Dermatology": "https://www.aad.org/public/diseases/skin-cancer/types/common/melanoma"
            }
        },
        "Basal Cell Carcinoma": {
            "name": "Basal Cell Carcinoma",
            "description": "The most common type of skin cancer, developing in the basal cells of the skin.\nOften appears as a shiny bump, pink growth, or open sore that doesn't heal properly.",
            "causes": "Long-term sun exposure, radiation therapy, fair skin, personal or family history of skin cancer.",
            "symptoms": "Pearly or waxy bumps, flat lesions that are flesh-colored or brown, or a sore that doesn't heal or recurs.",
            "treatments": "Surgical excision, Mohs surgery, radiation therapy, cryotherapy, or topical treatments."
        },
        "Rosacea": {
            "name": "Rosacea",
            "description": "A chronic inflammatory skin condition primarily affecting the face.\nCauses facial redness, visible blood vessels, and sometimes small bumps that may resemble acne.",
            "causes": "Genetic factors, abnormal facial blood vessels, microscopic skin mites, and environmental triggers.",
            "symptoms": "Facial redness, visible blood vessels, swollen red bumps, eye problems, enlarged nose.",
            "treatments": "Topical medications, oral antibiotics, laser therapy, and avoiding triggers such as sun exposure, spicy foods, and alcohol."
        },
        "Tinea": {
            "name": "Tinea (Ringworm)",
            "description": "A fungal infection affecting the skin, hair, or nails.\nCauses ring-shaped rashes with red, scaly borders and clearer centers, despite its name has nothing to do with worms.",
            "causes": "Dermatophyte fungi spreading through direct contact with infected people, animals, or surfaces.",
            "symptoms": "Ring-shaped, red, itchy, scaly patches with raised edges and clearer centers.",
            "treatments": "Antifungal creams, powders, or oral medications depending on the infection's severity and location.",
            "severity": "Mild to Moderate",
            "contagious": "Yes, ringworm is contagious and can spread through direct contact with infected people, animals, or contaminated objects.",
            "when_to_see_doctor": "See a doctor if:\n• Over-the-counter treatments don't clear the infection within 2 weeks\n• The rash is on the scalp or beard area (may require prescription treatment)\n• The rash is spreading rapidly or is widespread\n• You have diabetes or a weakened immune system\n• You develop a fever or the affected skin becomes painful, swollen, oozing, or has red streaks",
            "prevention": "• Avoid sharing personal items such as clothing, towels, or hairbrushes\n• Keep skin clean and dry\n• Change socks and underwear at least once a day\n• Shower after contact sports or gym activities\n• Wear flip-flops or sandals in public showers and pool areas\n• Avoid touching pets with patches of missing fur",
            "additional_resources": {
                "Mayo Clinic": "https://www.mayoclinic.org/diseases-conditions/ringworm-body/symptoms-causes/syc-20353780",
                "CDC": "https://www.cdc.gov/fungal/diseases/ringworm/index.html"
            }
        },
        "Vitiligo": {
            "name": "Vitiligo",
            "description": "A condition where the skin loses pigment cells, resulting in white patches.\nCauses smooth, white patches on various parts of the body, most noticeable on darker skin tones.",
            "causes": "Autoimmune disorder where the immune system attacks pigment-producing cells (melanocytes).",
            "symptoms": "White patches on the skin, premature whitening of hair, loss of color in the mouth and nose tissues.",
            "treatments": "Topical corticosteroids, calcineurin inhibitors, phototherapy, skin grafting, and depigmentation for extensive cases."
        },
        "Herpes": {
            "name": "Herpes (Herpes Simplex)",
            "description": "A viral infection causing painful blisters or sores, most commonly around the mouth or genitals.\nCauses recurring outbreaks of small, painful fluid-filled blisters that break and form open sores.",
            "causes": "Herpes simplex virus (HSV) spread through direct contact with infected sores or bodily fluids.",
            "symptoms": "Painful blisters or ulcers, tingling or itching before outbreaks, flu-like symptoms during the first outbreak.",
            "treatments": "Antiviral medications to reduce severity and frequency of outbreaks, pain relievers, and cold compresses."
        },
        "Scabies": {
            "name": "Scabies",
            "description": "A contagious skin infestation caused by a tiny burrowing mite.\nCauses intense itching, especially at night, and a pimple-like rash commonly between fingers, wrists, and other skin folds.",
            "causes": "Sarcoptes scabiei mite, spread through prolonged skin-to-skin contact with an infected person.",
            "symptoms": "Intense itching, especially at night, a pimple-like rash, tiny blisters and scales, and burrows in the skin.",
            "treatments": "Prescription scabicide lotions or creams, antihistamines for itching, and washing all clothes and bedding."
        },
        "Warts": {
            "name": "Warts",
            "description": "Small, rough growths on the skin caused by a viral infection.\nThese generally harmless growths can appear anywhere on the body and may have tiny black dots (clotted blood vessels).",
            "causes": "Human papillomavirus (HPV) entering the skin through cuts or breaks.",
            "symptoms": "Small, rough, grainy growths that are flesh-colored, white, pink, or tan. They may have black dots (clotted blood vessels).",
            "treatments": "Over-the-counter salicylic acid, cryotherapy (freezing), laser therapy, or surgical removal."
        },
        "Example Condition": {
            "name": "Example Condition",
            "description": "This is an example placeholder used when actual predictions cannot be made.\nIt appears when the model or required dependencies are not available.",
            "causes": "This is not a real skin condition. It appears when the model or required dependencies are not available.",
            "symptoms": "Not applicable as this is just a placeholder for demonstration purposes.",
            "treatments": "Please ensure the application has all required dependencies installed to see actual predictions."
        }
    }