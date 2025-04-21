import streamlit as st
import re
import pandas as pd

# Initialize a "users" DataFrame in session state (acts like a temporary DB)
if 'users' not in st.session_state:
    st.session_state.users = pd.DataFrame(columns=["Name", "Email", "Password"])

# Validation Functions
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_strong_password(password):
    return (
        len(password) >= 6
        and re.search(r"[A-Z]", password)
        and re.search(r"[a-z]", password)
        and re.search(r"[0-9]", password)
        and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    )

# Title
st.title("📝 User Registration Form")

# Registration Form
with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    submit = st.form_submit_button("Register")

    if submit:
        errors = []

        # Validation logic
        if not name.strip():
            errors.append("❗ Name is required.")
        if not is_valid_email(email):
            errors.append("❗ Invalid email format.")
        if not is_strong_password(password):
            errors.append("❗ Password must be at least 6 characters and include uppercase, lowercase, number, and special character.")
        if password != confirm_password:
            errors.append("❗ Passwords do not match.")
        if email in st.session_state.users["Email"].values:
            errors.append("❗ Email is already registered.")

        # Show results
        if errors:
            for error in errors:
                st.error(error)
        else:
            # Save user (simulate database)
            new_user = {"Name": name, "Email": email, "Password": password}
            st.session_state.users = pd.concat(
                [st.session_state.users, pd.DataFrame([new_user])],
                ignore_index=True
            )
            st.success("✅ Registration successful!")

            # Show user table
            st.subheader("👥 Registered Users")
            st.dataframe(st.session_state.users)
