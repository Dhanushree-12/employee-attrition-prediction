import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediction", layout="wide")

model = joblib.load("models/employee_attrition_model_v2.pkl")

st.title("🤖 Employee Attrition Prediction")

st.markdown("### Enter Employee Details")
age = st.number_input("Age",18,60,30)

income = st.number_input("Monthly Income",5000,300000,50000)

daily = st.number_input("Daily Rate",100,3000,1000)

hourly = st.number_input("Hourly Rate",10,300,80)

monthly = st.number_input("Monthly Rate",1000,60000,25000)

salary = st.number_input("Percent Salary Hike",0,100,15)

distance = st.number_input("Distance From Home",0,50,5)

years = st.number_input("Total Working Years",0,40,8)

promotion = st.number_input("Years Since Last Promotion",0,20,2)

role = st.number_input("Years In Current Role",0,20,3)
if st.button("Predict Attrition"):

    data = pd.DataFrame([[
        age,
        income,
        daily,
        hourly,
        monthly,
        salary,
        distance,
        years,
        promotion,
        role
    ]],
    columns=[
        'Age',
        'MonthlyIncome',
        'DailyRate',
        'HourlyRate',
        'MonthlyRate',
        'PercentSalaryHike',
        'DistanceFromHome',
        'TotalWorkingYears',
        'YearsSinceLastPromotion',
        'YearsInCurrentRole'
    ])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0]

    if prediction == 1:
        st.error("🔴 High Attrition Risk")
        st.progress(int(probability[1]*100))
        st.write(f"Risk Score: **{probability[1]*100:.1f}%**")

        st.warning("""
### Recommendations

- Improve salary package
- Reduce overtime
- Career growth opportunities
- Employee engagement programs
""")

    else:
        st.success("🟢 Low Attrition Risk")
        st.progress(int(probability[0]*100))
        st.write(f"Confidence: **{probability[0]*100:.1f}%**")

        st.info("""
### Recommendations

- Continue employee engagement
- Maintain work-life balance
- Reward good performance
""")