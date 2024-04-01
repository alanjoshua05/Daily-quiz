import streamlit as st
import pandas as pd
from datetime import datetime, time

# Initialize SessionState
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['Date', 'Name', 'Email', 'Question 1', 'Question 2'])

# Function to store data in a DataFrame
def store_data_in_dataframe(data):
    st.session_state.df = st.session_state.df.append(pd.Series(data), ignore_index=True)

# Function to check if the current time is within the blocked time range
def is_blocked_time():
    blocked_start_time = time(17, 0)  # e.g., 3:00 PM
    blocked_end_time = time(17, 0)    # e.g., 5:00 PM
    now = datetime.now().time()
    return blocked_start_time < now < blocked_end_time

# Streamlit web app
def main():
    st.title('Daily quiz')

    # Get input from the user
    name = st.text_input('Enter Name')
    email = st.text_input('Enter your college id')
    st.subheader("Questions")
    q2 = st.radio("1)hi", ["hello", "hey"], index=None)
    q1 = st.text_area("2)how are you?")
    current_date = datetime.now().date()

    if email[7:] != "@drngpit.ac.in" or len(email) > 21:
        st.error("Enter your college id or else the id shouldn't have empty space at the last")
    elif is_blocked_time():
        st.error("Sorry, the quiz is not available at the moment. Please try again later.")
    else:
        st.success("Hello ngpian")

        if st.button('Add Data'):
            # Create a dictionary with the user input
            data = {'Date': str(current_date), 'Name': name, 'Email': email, 'Question 1': q2, 'Question 2': q1}
            store_data_in_dataframe(data)
            st.success('Data added successfully!')
            st.write("Current DataFrame:")
            st.write(st.session_state.df)

if __name__ == '__main__':
    main()
