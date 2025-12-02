import pandas as pd

# # Create a simple patient DataFrame
# patient_data = {
#     'patient_id': ['P001', 'P002', 'P003', 'P004'],
#     'name': ['Alice Smith', 'Bob Johnson', 'Carol Davis', 'David Wilson'],
#     'age': [34, 45, 29, 51],
#     'temperature': [98.6, 99.1, 100.4, 97.9],
#     'condition': ['Stable', 'Stable', 'Fever', 'Stable']
# }

# df = pd.DataFrame(patient_data)
# print(df)
# print(df.info())

# Load medical data from file
# First, let's create a sample CSV file to practice with
sample_data = """patient_id,name,age,blood_pressure,heart_rate,diagnosis
P001,Alice Smith,34,120/80,72,Healthy
P002,Bob Johnson,45,140/90,85,Hypertension
P003,Carol davis,29,110/70,68,Healthy
P004,David Wilson,51,150/95,92,Hypertension
P005,Eva Brown,62,130/85,78,Diabetes"""

# Save to file
with open('patients.csv', 'w') as f:
    f.write(sample_data)


# Now read it with pandas
patients_df = pd.read_csv('patients.csv')
print('Loaded patient data:')
print(patients_df)

# Get basic statistics
# print('Statistical Summary:')
# print(patients_df.describe())

# # Check dtata types
# print("\nData types:")
# print(patients_df.dtypes)

# # Chcek for missing values
# print('\nMissing Values:')
# print(patients_df.isnull().sum())

# print('\nNumber of patients: ', len(patients_df))
# print('Columns available: ', list(patients_df.columns))
# print('Average age: ', patients_df['age'].mean())

# # Select a single column
# names = patients_df['name']
# print('Patient names')
# print(names)

# # Print multiple coulmns
# patient_info = patients_df[['name', 'age', 'diagnosis']]
# print('\nKey patient info: ')
# print(patient_info)

# Find patients with hypertension
# hypertension_patients = patients_df[patients_df['diagnosis'] == 'Hypertension']
# print("Hypertension patients:")
# print(hypertension_patients)

# Patients over 40 years old
# over_40 = patients_df[patients_df['age'] > 40]
# print('\nPatients over 40:')
# print(over_40)

# Multiple conditions
critical_patients = patients_df[(patients_df['age'] > 50) & (patients_df['diagnosis'] == 'Diabetes')]
print('Critical Patients:')
print(critical_patients)

# Create sample data with missing values
messy_data = {
    'patient_id': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'name': ['Alice Smith', 'Bob Johnson', None, 'David Wilson', 'Eva Brown'],
    'age': [34, 45, 29, None, 62],
    'temperature': [98.6, None, 100.4, 97.9, 98.2],
    'condition': ['Stable', 'Stable', 'Fever', None, 'Stable']
}

messy_df = pd.DataFrame(messy_data)
print('Messy data with missing values')
print(messy_df)

# Find missing values
print("\nMissing values in each column:")
print(messy_df.isnull().sum())

# Option 1: reove rows with missing values
clean_df = messy_df.dropna()
print("\nAfter removing missing values:")
print(clean_df)

# Option 2: Fill missing values
filled_df = messy_df.fillna({
    'name': 'Unknown Patient',
    'age': messy_df['age'].mean(),
    'temperature': 98.6,   # Normal body temperature
    'condition': 'Unknown'
})
print('\nAfter filling missing values:')
print(filled_df)

# Putting all into a function
def clean_medical_data(df):
    # Fill missing ages with average
    df['age'] = df['age'].fillna(df['age'].mean())
    # Fill missing temperature with normal
    df['temperature'] = df['temperature'].fillna(98.6)
    # Fill missing names
    df['name'] = df['name'].fillna('Unknown Patient')
    # Remove rows where critical info is missing
    df = df.dropna(subset=['patient_id', 'condition'])

    return df

cleaned_patients = clean_medical_data(messy_df)
print('\nCleaned medical data:')
print(cleaned_patients)

# Create new columns
# Add calculated columns
patients_df['age_group'] = patients_df['age'].apply(lambda x: 'Young' if x < 40 else 'Middle' if x < 60 else 'Senior')

# Extract systolic blood pressure (first number in 120/80)
patients_df['systolic_bp'] = patients_df['blood_pressure'].str.split('/').str[0].astype(int)
patients_df['diastolic_bp'] = patients_df['blood_pressure'].str.split('/').str[1].astype(int)

print("Enhanced patient data:")
print(patients_df)

# Categorizing Patients
# Create risk categories based on blood pressure
def categorize_risk(row):
    systolic = int(row['blood_pressure'].split('/')[0])
    diastolic = int(row['blood_pressure'].split('/')[1])

    if systolic >= 140 or diastolic >= 90:
        return 'High Risk'
    elif systolic >= 130 or diastolic >= 85:
        return 'Moderate Risk'
    else:
        return 'Low Risk'

patients_df['risk_category'] = patients_df.apply(categorize_risk, axis=1)
print("\nPatients with risk categories:")
print(patients_df[['name', 'blood_pressure', 'risk_category']])

# Medical Application: Patient Triage System
# Create traige priority system
def assign_priority(row):
    priority = 3  # Default: routine

    # High priority conditions
    if row['risk_category'] == 'High Risk':
        priority = 1
    elif row['heart_rate'] > 90:
        priority = 2
    elif row['age'] > 60:
        priority = 2
    
    return priority

patients_df['priority'] = patients_df.apply(assign_priority, axis=1)
print("Patients triage priorities:")
print(patients_df[['name', 'age', 'risk_category', 'heart_rate', 'priority']].sort_values('priority'))

# Group patients by diagnosis
diagnosis_groups = patients_df.groupby('diagnosis')
print("Patients by diagnosis:")
for diagnosis, group in diagnosis_groups:
    print(f"\n{diagnosis}:")
    print(group[['name', 'age']])


# Get statistics for each diagnosis group
diagnosis_stats = patients_df.groupby('diagnosis').agg({
    'age': ['mean', 'min', 'max'],
    'heart_rate': 'mean',
    'patient_id': 'count'   # Number of patients
})

print("Medical statistics by diagnosis:")
print(diagnosis_stats)

# Multiple grouping criteria
age_diagnosis_stats = patients_df.groupby(['age_group', 'diagnosis']).agg({
    'heart_rate': ['mean', 'std'],
    'systolic_bp': 'mean',
    'patient_id': 'count'
})

print("Detailed medical analysys")
print(age_diagnosis_stats)


# Complete Patient Analysis System
def comprehensive_patient_analysis(file_path):
    # Load data
    df = file_path

    print("=== COMPREHENSIVE PATIENT ANALYSIS ===")
    print(f"Total patients: {len(df)}")

    # Basic statistics
    print(f"\nAverage age: {df['age'].mean():.1f} years")
    print(f"Average hear rate: {df['heart_rate'].mean():.1f} bpm")

    # Diagnosis distribution
    print("\n=== DIAGNOSIS DISTRIBUTION ===")
    diagnosis_counts = df['diagnosis'].value_counts()
    for diagnosis, count in diagnosis_counts.items():
        percentage = (count / len(df)) * 100
        print(f"{diagnosis}: {count} patients ({percentage:.1f}%)")
    
    # Risk analysis
    print("\n=== RISK ANALYSYS ===")
    risk_counts = df['risk_category'].value_counts()
    print("Patients by risk category:")
    for risk, count in risk_counts.items():
        print(f"{risk}: {count} patients")
    
    # Emergency Alerts
    print("\n=== EMERGENCY ALERTS ===")
    critical_cases = df[(df['heart_rate'] > 100) | (df['systolic_bp'] > 160) |
                        (df['age'] > 70)
    ]

    if len(critical_cases) > 0:
        print("CRITICAL CASES NEEDING IMMEDIATE ATTENTION:")
        for _, patient in critical_cases.iterrows():
            alerts = []
            if patient['heart_rate'] > 100:
                alerts.append(f"High HR ({patient['heart_rate']})")
            if patient['systolic_bp'] > 160:
                alerts.append(f"High bp ({patient['systolic_bp']})")
            if patient['age'] > 70:
                alerts.append(f"Senior ({patient['age']} years)")
            
            print(f" {patient['name']}: {' '.join(alerts)}")
    else:
        print("No critical cases detected")
    
    return df

# Run the analysis
analysis_result = comprehensive_patient_analysis(patients_df)

# Add these features to your analysis:

# 1. Find patients who need follow-up
follow_up_needed = patients_df[
    (patients_df['priority'] == 1) | 
    (patients_df['age'] > 65)
]

print("\nPatients needing follow-up:")
print(follow_up_needed[['name', 'age', 'diagnosis', 'priority']])

# 2. Calculate average values by age group
age_group_stats = patients_df.groupby('age_group').agg({
    'systolic_bp': 'mean',
    'heart_rate': 'mean',
    'age': 'count'
}).round(1)

print("\nHealth metrics by age group:")
print(age_group_stats)