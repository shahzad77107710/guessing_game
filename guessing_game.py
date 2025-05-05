import streamlit as st
import random

# Set page title
st.title("🎯 Number Guessing Game")

# Initialize the secret number in session state (to persist between reruns)
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)

# User input
guess = st.number_input("Guess a number between 1 and 10:", min_value=1, max_value=10, step=1)

# Check the guess
if st.button("Submit Guess"):
    if guess == st.session_state.secret_number:
        st.success(f"🎉 Correct! The number was {st.session_state.secret_number}.")
        # Generate a new number for the next round
        st.session_state.secret_number = random.randint(1, 10)
    elif guess > st.session_state.secret_number:
        st.warning("Too high! Try a smaller number.")
    else:
        st.warning("Too low! Try a bigger number.")