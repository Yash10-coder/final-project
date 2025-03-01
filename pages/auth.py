import streamlit as st
from database.db_manager import create_user, verify_user

def login_page():
    st.title("Login")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            if username and password:
                user = verify_user(username, password)
                if user:
                    st.session_state.logged_in = True
                    st.session_state.user_id = user['id']
                    st.session_state.username = user['username']
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid username or password")
            else:
                st.error("Please fill in all fields")

def signup_page():
    st.title("Sign Up")
    
    with st.form("signup_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        full_name = st.text_input("Full Name")
        email = st.text_input("Email")
        department = st.selectbox(
            "Department",
            ["Computer Science", "Electronics", "Mechanical", "Civil", "Other"]
        )
        
        submit = st.form_submit_button("Sign Up")
        
        if submit:
            if username and password and full_name and email and department:
                if create_user(username, password, full_name, email, department):
                    st.success("Account created successfully! Please login.")
                    st.rerun()
                else:
                    st.error("Username or email already exists")
            else:
                st.error("Please fill in all fields")