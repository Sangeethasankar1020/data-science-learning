import streamlit as st
import time as ts
from datetime import time

def convertor(value):
    m,s,ms=value.split(":")
    t_s=int(m)*60+int(s)+int(ms)/1000
    return t_s

val=st.time_input("Set Timer",value=time(0,0,0))
print(type(val))

if str(val)=="00:00:00":
    st.write("Please sent Timer")
else:
    # print("performing other functions")
    sec=convertor(str(val))
    Bar=st.progress(0)
    per=sec/100
    progress_status=st.empty()
    for i in range(100):
        Bar.progress(i+1)
        progress_status.write(f"{i + 1}%")
        ts.sleep(per)