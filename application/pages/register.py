import streamlit as st
from db.firebase_app import register
from streamlit_extras.switch_page_button import switch_page
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons()  # Function to hide Streamlit icons
hide_sidebar()  # Function to hide Streamlit sidebar
remove_whitespaces()  # Function to remove unnecessary whitespaces

form = st.form("login")
email = form.text_input("Enter your email")
password = form.text_input("Enter your password", type="password")
clicked_login = st.button("Already registered? Click here to login!")

if clicked_login:
    switch_page("login") # Switch to the login page
    
submit = form.form_submit_button("Register")
if submit:
    # Call the register function with the provided email and password
    result = register(email, password)
    if result == "success":
        # Display a success message for successful registration
        st.success("Registration successful!")
        if st.session_state.profile == "Institute":
            switch_page("institute") # Switch to the institute page
        else:
            switch_page("verifier") # Switch to the verifier page
    else:
        st.error("Registration unsuccessful!") # Display an error message for unsuccessful registration
