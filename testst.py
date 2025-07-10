import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("My Simple Data App")

uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("ข้อมูลทั้งหมด:")
    st.dataframe(df)

    column = st.selectbox("เลือกคอลัมน์ที่ต้องการดู histogram", df.columns)
    fig, ax = plt.subplots()
    df[column].hist(ax=ax)
    st.pyplot(fig)
