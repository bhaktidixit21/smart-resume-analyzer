import streamlit as st
import sqlite3
from modules.email_utils import generate_otp, send_otp

st.set_page_config(page_title="Forgot Password")

st.title("Forgot Password")

email = st.text_input("Enter your Registered Email")

if "otp" not in st.session_state:
    st.session_state.otp = None

if st.button("Send OTP"):

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()
    conn.close()

    if user:

        otp = generate_otp()

        st.session_state.otp = otp
        st.session_state.reset_email = email

        send_otp(email, otp)

        st.success("OTP sent successfully.")

    else:
        st.error("Email not registered.")

if st.session_state.otp:

    user_otp = st.text_input("Enter OTP")

    if st.button("Verify OTP"):

        if user_otp == st.session_state.otp:

            st.success("OTP Verified")

            st.switch_page("pages/reset_password.py")

        else:

            st.error("Invalid OTP")