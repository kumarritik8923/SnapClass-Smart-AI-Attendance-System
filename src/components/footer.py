import streamlit as st

def footer_home():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    st.markdown(f"""
    <div style ="display: flex; margin-top:2rem; justify-content: center; gap:6px; items-align:center">
    <p style="font-weight: bold; color:white;">Created with ❤️ by </p>
    <img src='{logo_url}' style="max-height: 25px;"/>
    </div>
    """,unsafe_allow_html=True)