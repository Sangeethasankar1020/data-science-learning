import streamlit as st
import streamlit.components.v1 as com
with open("style.css") as source:
    design=source.read()


com.html(f"""

<div>
         <style>
        
         {design}
         </style>
      <h1 class="head">This is my heading</h1>   
         <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
</div>



""" ,height=800,scrolling=True)

# height-800
# scrolling=True
