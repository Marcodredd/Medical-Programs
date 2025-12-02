# PATIENT MANAGEMENT SYSTEM


# 1. Create patient information
patient_name = "Robert Johnson"
age = 52
conditions = ["hypertension", "diabetes"]
medications = ["Lisinopril", "Metformin"]
vital_signs = [98.6, 85, "140/90", 96]  # temp, hr, bp, oxygen

# 2. Display patient summary
print("=== PATIENT SUMMARY ===")
print(f"Name: {patient_name}")
print(f"Age: {age}")
print(f"Conditions: {conditions}")
print(f"Medications: {medications}")

# 3. Check each vital sign and alert if abnormal
print("\n=== VITAL SIGNS ANALYSIS ===")
temperature = vital_signs[0]
heart_rate = vital_signs[1]
blood_pressure = vital_signs[2]
oxygen = vital_signs[3]

# Add your monitoring logic here...
if temperature > 100.4:
    print("ALERT: Fever detected!")
if heart_rate > 100:
    print("ALERT: High heart rate!")
if oxygen < 92:
    print("ALERT: Low oxygen levels!")

# 4. Medication reminder system
print("\n=== MEDICATION SCHEDULE ===")
for medicine in medications:
    print(f"💊 Administer {medicine}")