import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")

# Example of input and output
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")
