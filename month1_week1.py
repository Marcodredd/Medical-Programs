# print("Hello, Doctor!")

# # Create variables
# patient_name = "John Smith"
# patient_age = 45
# body_temperature = 98.6
# is_diabetic = True

# # Use variables
# print(patient_name)
# print(patient_age)

# Create variables for your own patient
# patient_name = "John Doe"
# patient_age = 67
# patient_weight = 105
# has_insurance = True

# print("Patient Name: ", patient_name)
# print("Patient Age: ", patient_age)
# print(f"Patient Weight: {patient_weight}kg")
# print("Has Insurance? ", has_insurance)


# Medical Record Example
# patient_data = {
#     "name": "Maria Garcia",
#     "age": 28,
#     "temperature": 99.2,
#     "is_critical": False
# }

# print("Patient: ", patient_data["name"])
# print("Temperature: ", patient_data["temperature"])


# Format Patient Information
# first_name = "sarah"
# last_name = "chen"
# condition = "stable"

# # Create Formatted medical ID
# medical_id = f"Dr{last_name.upper()}_{first_name.capitalize()}"
# status_report = f"Patient {first_name.title()} is {condition.upper()}"

# print(medical_id)
# print(status_report)

# BMI Calculation
# weight_kg = 70
# height_m = 1.75
# bmi = weight_kg / (height_m ** 2)  # ** means power
# print(f"BMI: {bmi}")  # BMI: 22.857

# # Medicine dosage
# adult_dose = 500
# child_weight = 35  # kg
# adult_weight = 70  # kg
# child_dose = (child_weight / adult_weight) * adult_dose
# print(f"Child dose: {child_dose}mg")  # Child dose: 250.0mg


# Patient queue in emergency room
# er_queue = ["Patient A - Critical", "Patient B - Stable", "Patient C - Urgent"]
# print("Next patient: ", er_queue[0])

# # New patient arrives
# er_queue.append("Patient D - Stable")
# print("Queue now: ", er_queue)

# # Treat first patient
# treated_patient = er_queue.pop(0)
# print(f"Treated: {treated_patient}")
# print("Remaining queue: ", er_queue)

# Triage system
# patient_condition = "critical "
# oxygen_level = 85

# if patient_condition == "critical" or oxygen_level < 90:
#     print("IMMEDIATE ATTENTION REQUIRED")
#     print("Move to resuscitation room")
#     priority_level = 1
# elif patient_condition == "serious":
#     print("Urgent care needed")
#     priority_level = 2
# else:
#     print("Routine care")
#     priority_level = 3

# print(f"priority level: {priority_level}")

# Monitor patient until stable
patient_stable = False
check_count = 0

while not patient_stable and check_count < 5:
    check_count += 1
    print(f"Vital check #{check_count}...")
    
    # Simulate getting vitals (in real app, this would be real data)
    blood_pressure = "110/70"  # This would come from monitoring equipment
    heart_rate = 80
    
    if blood_pressure == "110/70" and 60 <= heart_rate <= 100:
        patient_stable = True
        print("✅ Patient stable - monitoring complete")
    else:
        print("Patient unstable - continue monitoring")