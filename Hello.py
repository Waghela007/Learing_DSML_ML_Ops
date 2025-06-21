import streamlit as st

st.title("Click the button to see the magic!")

st.checkbox("Click me to see the magic!", key="magic_checkbox")
if st.session_state.get("magic_checkbox", False):
    st.write("✨ The magic is here! ✨")    
          
