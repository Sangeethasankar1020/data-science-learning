import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to extract YouTube video details
def extract_youtube_details(video_url):
    # Set up Chrome WebDriver (Make sure ChromeDriver is installed)
    options = Options()
    options.headless = True  # Run browser in the background
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the YouTube video URL
    driver.get(video_url)

    # Wait for the page to load fully (adjust time if necessary)
    time.sleep(5)

    # Extract title, description, and keywords (if available)
    title = driver.title
    try:
        description = driver.find_element(By.XPATH, '//*[@id="description"]/yt-formatted-string').text
    except:
        description = "Description not found"

    try:
        keywords = driver.find_element(By.XPATH, '//*[@name="keywords"]').get_attribute('content')
    except:
        keywords = "Keywords not found"

    # Close the browser
    driver.quit()

    return title, description, keywords

# Streamlit UI
def main():
    st.title('YouTube Video Details Extractor')

    # User input for YouTube video URL
    video_url = st.text_input('Enter YouTube Video URL:', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    # Button to trigger extraction
    if st.button('Extract Details'):
        if video_url:
            with st.spinner('Extracting details...'):
                title, description, keywords = extract_youtube_details(video_url)
                
            # Display the results
            st.subheader('Extracted Details:')
            st.text(f"Title: {title}")
            st.text(f"Description: {description}")
            st.text(f"Keywords: {keywords}")
        else:
            st.error('Please enter a valid YouTube URL.')

# Run the Streamlit app
if __name__ == '__main__':
    main()
