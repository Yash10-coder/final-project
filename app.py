import streamlit as st
from pages.auth import login_page, signup_page
from pages.dashboard import dashboard_page
from pages.home import home_page
from database.db_manager import init_db

def main():
    # Initialize the database
    init_db()
    
    # Initialize session state variables if they don't exist
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
    if 'username' not in st.session_state:
        st.session_state.username = None

    # Page routing
    if not st.session_state.logged_in:
        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Go to", ["Home", "Login", "Sign Up"])
        
        if page == "Home":
            home_page()
        elif page == "Login":
            login_page()
        elif page == "Sign Up":
            signup_page()
    else:
        dashboard_page()

if __name__ == "__main__":
    st.set_page_config(
        page_title="College Review System",
        page_icon="🎓",
        layout="wide"
    )
    main()