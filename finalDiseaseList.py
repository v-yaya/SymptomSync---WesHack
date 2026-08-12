from Disease import *
from Symptom import *
import datetime

# Defining symptoms for various diseases

# Heart Attack / Stroke
heart_attack_symptoms = [
    chest_pain := Symptom("Chest Pain / Chest Discomfort"),
    shortness_of_breath := Symptom("Shortness of Breath"),
    nausea := Symptom("Nausea"),
    vomiting := Symptom("Vomiting"),
    lightheadedness := Symptom("Lightheadedness"),
    dizziness := Symptom("Dizziness"),
    fatigue := Symptom("Fatigue"),
    weakness := Symptom("Weakness"),
    droopy_face := Symptom("Droopy Face"),
    inability_to_raise_arm := Symptom("Inability to Raise Arm"),
    slurred_speech := Symptom("Slurred Speech"),
    sudden_loss_of_balance := Symptom("Sudden Loss of Balance"),
    sudden_vision_changes := Symptom("Sudden Vision Changes in One or Both Eyes")
]

# Diabetes
diabetes_symptoms = [
    frequent_urination := Symptom("Frequent Urination"),
    excessive_thirst := Symptom("Excessive Thirst"),
    increased_hunger := Symptom("Increased Hunger"),
    fatigue,
    blurred_vision := Symptom("Blurred Vision"),
    fainting := Symptom("Fainting"),
    slow_healing_wound := Symptom("Slow-Healing Wound"),
    tingling_numbness := Symptom("Tingling / Numbness"),
    dry_skin := Symptom("Dry Skin"),
    yeast_infection := Symptom("Yeast Infection"),
    fruity_breath := Symptom("Fruity-Smelling Breath"),
    high_low_blood_sugar := Symptom("Persistent High/Low Blood Sugar")
]

# Asthma
asthma_symptoms = [
    shortness_of_breath,
    wheezing := Symptom("Wheezing"),
    persistent_coughing := Symptom("Persistent Coughing"),
    chest_pain,
    difficulty_breathing := Symptom("Difficulty Breathing"),
    fatigue,
    rapid_pulse := Symptom("Rapid Pulse / Heart Rate"),
    severe_wheezing := Symptom("Severe Wheezing & Difficulty Breathing"),
    cyanosis := Symptom("Cyanosis"),
    severe_anxiety := Symptom("Severe Anxiety Due to Breathlessness")
]

# Cancer
cancer_symptoms = [
    fatigue,
    fever := Symptom("Fever"),
    pain := Symptom("Pain (in any part of the body)"),
    change_in_skin := Symptom("Change in Skin (Darkening, Yellowing)"),
    lumps_swelling := Symptom("Lumps / Swelling"),
    blood_in_stool := Symptom("Blood in Stool"),
    blood_in_urine := Symptom("Blood in Urine"),
    constipation := Symptom("Constipation"),
    cough := Symptom("Cough"),
    difficulty_swallowing := Symptom("Difficulty Swallowing"),
    vaginal_bleeding := Symptom("Vaginal Bleeding"),
    blood_in_sputum := Symptom("Blood in Sputum")
]

# Common Cold
common_cold_symptoms = [
    runny_nose := Symptom("Runny Nose"),
    stuffy_nose := Symptom("Stuffy Nose"),
    sneezing := Symptom("Sneezing"),
    sore_throat := Symptom("Sore Throat"),
    cough,
    ache := Symptom("Ache"),
    fever,
    fatigue,
    watery_eyes := Symptom("Watery Eyes"),
    severe_fever := Symptom("SEVERE Fever Greater Than 101"),
    symptoms_lasting := Symptom("Symptoms Lasting > 10 Days")
]

# COVID
covid_symptoms = [
    fever,
    cough,
    loss_of_taste_smell := Symptom("Loss of Taste/Smell"),
    shortness_of_breath,
    difficulty_breathing,
    fatigue,
    ache,
    sore_throat,
    runny_nose,
    nausea,
    diarrhea := Symptom("Diarrhea")
]

# Pneumonia
pneumonia_symptoms = [
    high_fever := Symptom("High Fever"),
    productive_cough := Symptom("Productive Cough"),
    chest_pain,
    chills := Symptom("Chills"),
    fatigue,
    weakness,
    sweating := Symptom("Sweating"),
    loss_of_appetite := Symptom("Loss of Appetite")
]

# Anxiety
anxiety_symptoms = [
    nervousness := Symptom("Nervousness"),
    constant_worry := Symptom("Constant Worry"),
    increased_heart_rate := Symptom("Increased Heart Rate"),
    trouble_breathing := Symptom("Trouble Breathing"),
    difficulty_concentrating := Symptom("Difficulty Concentrating"),
    avoidance := Symptom("Avoidance of Feared Situations")
]

# Flu
flu_symptoms=[
    fever,chills,ache,fatigue,sore_throat,cough,stuffy_nose,runny_nose,nausea,vomiting
]

# STD
std_symptoms=[
    sores:=Symptom("Sores"),
    pain_during_urination:=Symptom("Pain During Urination"),
    discharge:=Symptom("Discharge"),
    pain_during_intercourse:=Symptom("Pain/Bleeding During Intercourse"),
    abdominal_pain:=Symptom("Abdominal Pain"),
    rash:=("Rash"),
    fever,
    fatigue,
    swollen_lymph_nodes:=Symptom("Swollen Lymph Nodes"),
    genital_warts:=Symptom("Genital Warts/Sores"),
    itchy:=Symptom("Itchy")
]

# Hepatitis
hepatitis_symptoms=[
    fatigue,
    jaundice:=Symptom("Jaundice"),
    dark_urine:=Symptom("Dark Urine"),
    fever,
    nausea,
    loss_of_appetite,
    abdominal_pain,
    jaundice,
    joint_pain:=Symptom("Joint Pain"),
    confusion:=Symptom("Confusion")
]

# Malaria
malaria_symptoms=[
fever,
chills,
sweating,
fatigue,
ache,
nausea,
anemia:=Symptom("Anemia"),
jaundice,
confusion,
seizures:=Symptom("Seizures"),
coma:=Symptom("Coma")
]

# Depression
depression_symptoms=[
    hopelessness:=Symptom("Hopelessness"),
    worthlessness:=Symptom("Worthlessness"),
    guilt:=Symptom("Guilt"),
    difficulty_concentrating,
    suicidal_thoughts:=Symptom("Suicidal Thoughts"),
    sleep_disturbance:=Symptom("Sleep Disturbance"),
    loss_of_interest:=Symptom("Loss of Interest")
]

# ADHD
adhd_symptoms=[
    difficulty_sustaining_attention:=Symptom("Difficulty Sustaining Attention"),
    frequently_losing_things:=Symptom("Frequently Losing Things"),
    poor_organization:=Symptom("Poor Organization"),
    fidgeting:=Symptom("Fidgeting"),
    excessive_talking:=Symptom("Excessive Talking"),
    procrastination:=Symptom("Procrastination"),
    difficulty_concentrating
]

# OCD
ocd_symptoms=[
    nervousness,
    difficulty_concentrating,
    persistent_doubts:=Symptom("Persistent Doubts"),
    intrusive_thoughts:=Symptom("Intrusive Thoughts"),
    repetitive_behavior:=Symptom("Repetitive Behavior")
]

# Marking fast-acting symptoms
fast_acting_symptoms = [
    droopy_face, inability_to_raise_arm, slurred_speech, sudden_loss_of_balance, sudden_vision_changes,
    fruity_breath, high_low_blood_sugar, rapid_pulse, severe_wheezing, cyanosis, severe_anxiety,
    severe_fever, symptoms_lasting,confusion,seizures,coma
]

for symptom in fast_acting_symptoms:
    symptom.set_fast_acting(True)

# Creating diseases
diseases=[
    heart_attack := Disease("Heart Attack / Stroke", heart_attack_symptoms),
    diabetes := Disease("Diabetes", diabetes_symptoms),
    asthma := Disease("Asthma", asthma_symptoms),
    cancer := Disease("Cancer", cancer_symptoms),
    common_cold := Disease("Common Cold", common_cold_symptoms),
    flu:=Disease("Flu",flu_symptoms),
    std:=Disease("STD",std_symptoms),
    covid := Disease("COVID", covid_symptoms),
    pneumonia := Disease("Pneumonia", pneumonia_symptoms),
    hepatitis:=Disease("Hepatitis",hepatitis_symptoms),
    malaria:=Disease("Malaria",malaria_symptoms),
    anxiety := Disease("Anxiety", anxiety_symptoms),
    depression:=Disease("Depression",depression_symptoms),
    adhd:=Disease("ADHD",adhd_symptoms),
    ocd:=Disease("OCD",ocd_symptoms)
]
