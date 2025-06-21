import streamlit as st

agree = st.checkbox("I agree")

if agree:
    st.write("Great!" + " You agreed!" + " Thank you!")
else:
    st.write("You didn't agree")
    st.write("Please check the box if you agree.")