
import streamlit as st 

st.title("Uploading files")
st.markdown("___")

images=st.file_uploader("Please upload an image",type=["png","jpg"],accept_multiple_files=True)

if images is not None:
    for image in images:
        st.image(image)