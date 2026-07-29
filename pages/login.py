import streamlit as st
import sqlite3
import hashlib

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ---------------- LOGIN ---------------- #

if st.button("Login"):

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, hash_password(password))
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        st.session_state["logged_in"] = True
        st.session_state["user"] = user[1]

        st.success(f"Welcome {user[1]}!")

        st.switch_page("app.py")

    else:

        st.error("Invalid Email or Password")


st.divider()


# ---------------- FORGOT PASSWORD ---------------- #

if st.button("Forgot Password"):
    st.switch_page("pages/forgot_password.py")