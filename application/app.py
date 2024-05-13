import streamlit as st
from PIL import Image
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
hide_icons() # Function to hide Streamlit icons 
hide_sidebar() # Function to hide Streamlit sidebar 
remove_whitespaces() # Function to remove unnecessary whitespaces 


st.title("Certify")
st.write("")
st.subheader("Select Your Role")

col1, col2 = st.columns(2) # Create two columns for layout 

# Load the institute logo image
institite_logo = Image.open("../assets/institute_logo.png") 
with col1:
    # Display the institute logo
    st.image(institite_logo, output_format="jpg", width=230)
    # Create a button for the institute role
    clicked_institute = st.button("Institute")
    
# Load the company logo image
company_logo = Image.open("../assets/company_logo.png")
with col2:
    st.image(company_logo, output_format="jpg", width=230)
    # Create a button for the verifier role
    clicked_verifier = st.button("Verifier")

if clicked_institute:
    # Set the session state variable to "Institute"
    st.session_state.profile = "Institute"
    # Switch to the login page
    switch_page('login')
elif clicked_verifier:
    # Set the session state variable to "Verifier"
    st.session_state.profile = "Verifier"
    # Switch to the login page
    switch_page('login')
