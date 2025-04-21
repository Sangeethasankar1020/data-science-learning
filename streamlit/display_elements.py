
import streamlit as st

st.write("## h2 tag")

# super script - fast unicode math character 
st.metric(label="wind speed",value="120 ms-1",delta="1.4 ms-1")
st.metric(label="Wind Speed", value="120 ms⁻¹", delta="1.4 ms⁻¹")

st.markdown("This is $x^{a}$")     # x to the power of a
st.markdown("Speed: $120\\ ms^{-1}$")  # 120 m/s⁻¹

