import pandas as pd

def hospital_data_analyst():
    # Create sample hospital data
    hospital_data = {
        'patient_id': [f"P{100+i}" for i in range(10)],
        'name': ['John M', 'Sarah K', 'Mike L', 'Lisa R', 'Tom B', 
                'Anna S', 'Raj P', 'Maria G', 'Kenji T', 'Emma W'],
        'age': [25, 47, 62, 33, 58, 71, 29, 52, 44, 36],
        'blood_pressure': ['110/75', '140/92', '150/88', '118/76', '145/90', 
                         '160/95', '112/74', '138/85', '130/82', '120/78'],
        'heart_rate': [68, 85, 92, 72, 88, 96, 70, 82, 78, 74],
        'diagnosis': ['Healthy', 'Hypertension', 'Hypertension', 'Healthy', 'Diabetes',
                     'Hypertension', 'Healthy', 'Diabetes', 'Hypertension', 'Healthy']
    }
    
    df = pd.DataFrame(hospital_data)
    
    print("=== ORIGINAL PATIENT DATA ===")
    print(df)
    print("\n" + "="*50 + "\n")
    
    # 1. Add systolic_bp and diastolic_bp columns
    df['systolic_bp'] = df['blood_pressure'].str.split('/').str[0].astype(int)
    df['diastolic_bp'] = df['blood_pressure'].str.split('/').str[1].astype(int)
    
    print("1. ADDED BLOOD PRESSURE COLUMNS:")
    print(df[['name', 'blood_pressure', 'systolic_bp', 'diastolic_bp']])
    print("\n" + "-"*30 + "\n")
    
    # 2. Create risk_category column
    def get_risk_category(row):
        if row['systolic_bp'] > 140 or row['diastolic_bp'] > 90:
            return 'High Risk'
        elif row['systolic_bp'] > 130:
            return 'Moderate Risk'
        else:
            return 'Low Risk'
    
    df['risk_category'] = df.apply(get_risk_category, axis=1)
    
    print("2. ADDED RISK CATEGORIES:")
    print(df[['name', 'systolic_bp', 'diastolic_bp', 'risk_category']])
    print("\n" + "-"*30 + "\n")
    
    # 3. Find the 3 highest risk patients
    high_risk_patients = df[df['risk_category'] == 'High Risk'].sort_values('systolic_bp', ascending=False)
    
    print("3. TOP 3 HIGHEST RISK PATIENTS:")
    if len(high_risk_patients) >= 3:
        top_3 = high_risk_patients.head(3)
        for _, patient in top_3.iterrows():
            print(f"🚨 {patient['name']} (Age: {patient['age']}) - BP: {patient['blood_pressure']}, Risk: {patient['risk_category']}")
    else:
        print("Less than 3 high risk patients found")
    print("\n" + "-"*30 + "\n")
    
    # 4. Calculate average age for each diagnosis
    diagnosis_age_stats = df.groupby('diagnosis')['age'].agg(['mean', 'count']).round(1)
    
    print("4. AVERAGE AGE BY DIAGNOSIS:")
    for diagnosis, stats in diagnosis_age_stats.iterrows():
        print(f"{diagnosis}: Average age {stats['mean']} years ({stats['count']} patients)")
    print("\n" + "-"*30 + "\n")
    
    # 5. Create an alert for patients with both high BP and high heart rate (>85)
    critical_patients = df[(df['systolic_bp'] > 140) & (df['heart_rate'] > 85)]
    
    print("5. CRITICAL ALERTS - High BP + High Heart Rate:")
    if len(critical_patients) > 0:
        for _, patient in critical_patients.iterrows():
            print(f"🚨 CRITICAL: {patient['name']} - BP: {patient['blood_pressure']}, HR: {patient['heart_rate']}bpm")
    else:
        print("No critical patients meeting both criteria")
    
    print("\n" + "="*50)
    print("COMPREHENSIVE PATIENT SUMMARY:")
    print(f"Total patients: {len(df)}")
    print(f"High risk: {len(df[df['risk_category'] == 'High Risk'])} patients")
    print(f"Moderate risk: {len(df[df['risk_category'] == 'Moderate Risk'])} patients") 
    print(f"Low risk: {len(df[df['risk_category'] == 'Low Risk'])} patients")
    
    return df

# Run the analysis
print("🏥 HOSPITAL DATA ANALYST REPORT")
print("=" * 60)
result_df = hospital_data_analyst()

# Show final dataframe
print("\n" + "=" * 60)
print("FINAL ENHANCED DATAFRAME:")
print(result_df)
    