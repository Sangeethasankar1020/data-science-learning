import streamlit as st

# for title 

st.title("Hi  I am sangeetha !!!")
st.title("Sangeetha")

# subheading

st.subheader("hi!!! , Iam your sub header")
st.header("Hi , Iam your Header")
st.text("hi iam your text function, use as paragragh")

st.markdown("**jsido** *world*")

# - heading 

st.markdown("# hello")

# > -|

st.markdown("> helllo sa")

# horizoantal row

st.markdown("---")

# link

st.markdown("https://oceanacademy.co.in/")

st.caption("hi iam caption")

# latex functions - allow mathematical formula

st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

json={"a":1,"b":5}

st.json(json)

code="""
print("hello world")
def funct():
    return 0;
"""

st.code(code,language="python")


st.write()