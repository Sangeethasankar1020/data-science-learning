import streamlit as st
import time

# CALL BACK


# def printer(name):
#     print(name)

# input=st.text_input("Enter your Name:")
# s_btn=st.button("Submit")
# if s_btn:
#     opt=st.checkbox("want to display your name?",on_change=printer,args=(input,))
#     # if opt:
#     #     print(input)

# SESSION STATES 

# text ="Dog"
# if "click" not in st.session_state:
#     st.session_state.click=False

# else:
#     if st.session_state.click==False:
#         text="Cat"
#         st.session_state.click=True
#     else:
#         text ="Dog"
#         st.session_state.click=False
# st.button(text)

# CACHE
@st.cache_data
def printer():
    time.sleep(10)
    return "Message"

st.write(printer())
