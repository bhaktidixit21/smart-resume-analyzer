from auth import register_user
import streamlit as st

st.title("Create Account")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")


if st.button("Register"):

    if name == "" or email == "" or password == "":
        st.error("Please fill all fields.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:

        success, message = register_user(
            name,
            email,
            password
        )

        if success:
            st.success("✅ " + message)
        else:
            st.error("❌ " + message)