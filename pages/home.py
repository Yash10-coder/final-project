import streamlit as st

def home_page():
    st.title("🎓 Welcome to College Review System")
    
    # Hero section
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <h2>Your Voice Matters!</h2>
        <p>Help us improve the quality of education by sharing your valuable feedback.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features section
    st.subheader("📌 Key Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📊 Course Ratings")
        st.write("Rate your courses and provide detailed feedback")
    
    with col2:
        st.markdown("### 🔒 Secure")
        st.write("Your feedback is confidential and secure")
    
    with col3:
        st.markdown("### 📈 Impact")
        st.write("Help improve the quality of education")
    
    # How it works section
    st.subheader("🔄 How It Works")
    st.markdown("""
    1. Sign up with your student credentials
    2. Login to access the dashboard
    3. Select subjects from the navigation panel
    4. Provide your valuable feedback
    5. Submit and help us improve!
    """)