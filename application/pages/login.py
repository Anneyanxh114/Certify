import streamlit as st
from db.firebase_app import login
from dotenv import load_dotenv
import os
from streamlit_extras.switch_page_button import switch_page
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()  # Function to hide Streamlit icons
hide_sidebar()  # Function to hide Streamlit sidebar
remove_whitespaces()  # Function to remove unnecessary whitespace

load_dotenv()

form = st.form("login")
email = form.text_input("Enter your email")
password = form.text_input("Enter your password", type="password")

if st.session_state.profile != "Institute":
    clicked_register = st.button("New user? Click here to register!")

    if clicked_register:
        switch_page("register") # Switch to the register page


submit = form.form_submit_button("Login")
if submit:
    if st.session_state.profile == "Institute":
        valid_email = os.getenv("institute_email")
        valid_pass = os.getenv("institute_password")
        if email == valid_email and password == valid_pass:
            switch_page("institute") # Switch to the institute page
        else:
            st.error("Invalid credentials!") # Display an error message for invalid credentials
    else:
        result = login(email, password) # Call the login function with the provided email and password
        if result == "success":
            st.success("Login successful!")  # Display a success message for successful login
            switch_page("verifier")  # Switch to the verifier page
        else:
            st.error("Invalid credentials!") # Display an error message for invalid credentials
        
