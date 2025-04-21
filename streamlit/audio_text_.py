import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import os

st.title('Audio to Text Converter')

uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    audio_path = "uploaded_audio.mp3"
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.read())

    # Convert MP3 to WAV using pydub
    wav_path = "converted_audio.wav"
    try:
        sound = AudioSegment.from_file(audio_path)
        sound.export(wav_path, format="wav")
    except Exception as e:
        st.error(f"Error converting audio: {e}")
        st.stop()

    st.audio(wav_path, format="audio/wav")

    # Recognize speech
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(wav_path)

    with audio_file as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        st.write("Text from audio:")
        st.write(text)
    except sr.UnknownValueError:
        st.write("Could not understand the audio.")
    except sr.RequestError:
        st.write("Could not request results from Google Speech Recognition service.")

    # Clean up temporary files
    os.remove(audio_path)
    os.remove(wav_path)
