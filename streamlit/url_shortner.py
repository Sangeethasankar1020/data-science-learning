import streamlit as st
import pyshorteners

# Title
st.title("🔗 URL Shortener")

# Input
url = st.text_input("Enter the URL to shorten")

# Button
if st.button("Shorten URL"):
    if url:
        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(url)
            st.success(f"Shortened URL: {short_url}")
            st.markdown(f"[Click here to visit]({short_url})")
        except Exception as e:
            st.error("Something went wrong. Please check the URL.")
    else:
        st.warning("Please enter a valid URL.")
