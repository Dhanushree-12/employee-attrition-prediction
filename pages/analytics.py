import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Analytics Dashboard")

df = pd.read_csv("dataset/employee_attrition_cleaned.csv")

st.write("Explore employee insights through interactive visualizations.")

col1,col2 = st.columns(2)

with col1:

    fig = px.pie(
        df,
        names="Attrition",
        hole=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig = px.histogram(
        df,
        x="Gender",
        color="Attrition",
        barmode="group"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )