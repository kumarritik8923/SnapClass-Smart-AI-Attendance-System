import streamlit as st

def footer_home():
    st.markdown(f"""
    <div style ="display: flex; margin-top:2rem; justify-content: center; gap:6px; items-align:center">
    <p style="font-weight: bold; color:white;">Designed & developed with ⚡ by Ritik </p>
    </div>
    """,unsafe_allow_html=True)

def footer_dashboard():
    st.markdown(f"""
    <div style ="display: flex; margin-top:2rem; justify-content: center; gap:6px; items-align:center">
    <p style="font-weight: bold; color:black;">Designed & developed with ⚡ by Ritik </p>
    </div>
    """,unsafe_allow_html=True)