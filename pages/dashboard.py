import streamlit as st
from database.db_manager import save_review, get_user_reviewed_subjects

SUBJECTS = [
    "Physics",
    "Chemistry",
    "Mathematics",
    "Programming",
    "Web Technology",
    "Lab Practices",
    "Soft Skills"
]

def review_form(subject):
    with st.form(f"review_form_{subject}"):
        st.subheader(f"Review for {subject}")
        
        # Rating
        rating = st.radio(
            "How would you rate this subject? (1-5)",
            options=[1, 2, 3, 4, 5],
            horizontal=True
        )
        
        # Checkboxes
        attendance_regular = st.checkbox("Were you regular in attending classes?")
        understanding_level = st.checkbox("Did you understand the concepts clearly?")
        
        # Subjective feedback
        feedback = st.text_area("Please provide your detailed feedback about this subject")
        
        submit = st.form_submit_button("Submit Review")
        
        if submit:
            save_review(
                st.session_state.user_id,
                subject,
                rating,
                attendance_regular,
                understanding_level,
                feedback
            )
            st.success(f"Review for {subject} submitted successfully!")
            st.rerun()

def dashboard_page():
    st.title(f"Welcome, {st.session_state.username}!")
    
    # Get reviewed subjects
    reviewed_subjects = get_user_reviewed_subjects(st.session_state.user_id)
    remaining_subjects = [s for s in SUBJECTS if s not in reviewed_subjects]
    
    # Logout button
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.session_state.username = None
        st.rerun()
    
    if remaining_subjects:
        st.sidebar.title("Subjects to Review")
        selected_subject = st.sidebar.selectbox(
            "Select a subject to review",
            remaining_subjects
        )
        
        if selected_subject:
            review_form(selected_subject)
    else:
        st.sidebar.title("Reviews Complete")
        st.markdown("""
        ## 🎉 Thank You!
        
        We greatly appreciate your time and effort in providing feedback for all subjects.
        Your input will help us improve the quality of education for future students.
        
        ### 📈 Impact of Your Feedback
        - Helps identify areas for improvement
        - Contributes to curriculum enhancement
        - Supports better teaching methods
        
        *Thank you for being a part of this improvement process!*
        """)