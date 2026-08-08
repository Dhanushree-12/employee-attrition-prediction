import streamlit as st
import pandas as pd

st.title("📈 Model Performance")

comparison = pd.DataFrame({
    "Model":[
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "XGBoost"
    ],
    "Accuracy":[
        49.3,
        50.6,
        51.2,
        48.6
    ]
})

st.dataframe(comparison)

st.line_chart(
    comparison.set_index("Model")
)