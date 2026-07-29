import streamlit as st
import sqlite3
import hashlib

st.set_page_config(page_title="Reset Password")

st.title("Reset Password")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


if "reset_email" not in st.session_state:
    st.error("Please verify OTP first.")
    st.stop()


new_password = st.text_input("New Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")


if st.button("Update Password"):

    if new_password == "" or confirm_password == "":
        st.error("Please fill all fields.")

    elif new_password != confirm_password:
        st.error("Passwords do not match.")

    else:

        conn = sqlite3.connect("database/users.db")
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE users SET password=? WHERE email=?",
            (
                hash_password(new_password),
                st.session_state.reset_email
            )
        )

        conn.commit()
        conn.close()

        st.success("Password Updated Successfully!")

        # Clear OTP session
        st.session_state.pop("otp", None)
        st.session_state.pop("reset_email", None)

        st.info("Go to Login page and login with your new password.")