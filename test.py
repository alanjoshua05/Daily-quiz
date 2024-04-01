import streamlit as st
import pandas as pd
from datetime import datetime, time

# Function to get user input and add it to the Excel sheet
def add_data_to_excel(data):
    df = pd.read_excel('cs.xlsx')  # Read the existing Excel file
    df = df.append(data, ignore_index=True)  # Append the new data to the DataFrame
    df.to_excel('cs.xlsx', index=False)  # Write the updated DataFrame back to Excel

# Function to check if the current time is within the blocked time range
def is_blocked_time():
    blocked_start_time = time(15, 0)  # e.g., 8:00 AM
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
            add_data_to_excel(data)
            st.success('Data added successfully!')

if __name__ == '__main__':
    main()
