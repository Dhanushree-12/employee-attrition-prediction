import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Employee Attrition Dashboard",
    page_icon="👨‍💼",
    layout="wide"
)

df = pd.read_csv("dataset/employee_attrition_cleaned.csv")

st.title("👨‍💼 Employee Attrition Prediction Dashboard")

st.markdown("""
### AI Powered HR Analytics System
Welcome to the HR Dashboard.
""")

st.divider()

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Employees",len(df))

with col2:
    st.metric("Accuracy","51.2%")

with col3:
    st.metric("Best Model","Random Forest")

with col4:
    st.metric("Features",30)

st.subheader("📈 HR Summary")

col1,col2 = st.columns(2)

with col1:

    st.info(f"Average Age : {round(df['Age'].mean(),1)} Years")

    st.info(f"Average Salary : ₹ {round(df['MonthlyIncome'].mean(),0)}")

with col2:

    st.info(f"Average Distance : {round(df['DistanceFromHome'].mean(),1)} km")

    st.info(f"Average Experience : {round(df['TotalWorkingYears'].mean(),1)} Years")

st.subheader("📊 Attrition Overview")
fig = px.pie(
    df,
    names="Attrition",
    hole=.6,
    color_discrete_sequence=[
        "#00C853",
        "#FF5252"
    ]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig = px.bar(
    df['Department'].value_counts().head(5),
    title="Top Departments"
)

st.plotly_chart(fig,use_container_width=True)

fig = px.pie(
    df,
    names="Attrition",
    hole=0.5,
    title="Employee Attrition Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)