import streamlit as st
from matplotlib import pyplot as plt
import numpy as np

# Create x values
x = np.linspace(0, 10, 100)

# Sidebar selection
opt = st.sidebar.radio("**Select any Graph**", options=("Line", "Bar", "H-Bar"))

# Apply custom style
plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
# plt.style.use('seaborn-dark')
# Line Chart
if opt == "Line":
    st.markdown("<h1 style='text-align:center'>Line Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.plot(x, np.sin(x), label="sin(x)")
    plt.plot(x, np.cos(x), "--", label="cos(x)")
    plt.legend()
    st.pyplot(fig)

# Vertical Bar Chart
elif opt == 'Bar':
    st.markdown("<h1 style='text-align:center'>Bar Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    categories = ['A', 'B', 'C', 'D']
    values = [10, 24, 36, 15]
    plt.bar(categories, values, color='skyblue')
    # plt.title("Bar Chart Example")
    st.pyplot(fig)

# Horizontal Bar Chart
elif opt == 'H-Bar':
    st.markdown("<h1 style='text-align:center'>Horizontal Bar Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    categories = ['A', 'B', 'C', 'D']
    values = [10, 24, 36, 15]
    plt.barh(categories, values, color='lightgreen')
    # plt.title("Horizontal Bar Chart Example")
    st.pyplot(fig)
