import streamlit as st
from PIL import Image
from PIL.ImageFilter import*
from io import BytesIO

st.set_page_config(page_title="Image Editor ", page_icon="🖼️",layout="centered")
st.title("🖌️ Image Editor")
st.markdown("---")

image = st.file_uploader("📤 Upload your image", type=["jpg", "png", "jpeg"])

size = st.empty()
mode = st.empty()
format = st.empty()
info=st.empty()


if image:
    img = Image.open(image)
    info.title("information")
    # Display image
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Show image metadata
    size.markdown(f"**Size:** `{img.size}`")
    mode.markdown(f"**Mode:** `{img.mode}`")
    format.markdown(f"**Format:** `{img.format}`")
    st.title("Resizing")
    width=st.number_input("width",value=img.width)
    height=st.number_input("height",value=img.height)

    st.title("Rotation")
    degree=st.number_input("Degree")

    st.title("Filters")
    filters=st.selectbox("filters",options=("None","Blur","Detail","Emboss","smooth"))
    s_btn=st.button("Submit")

    if s_btn:
        edited=img.resize((width,height)).rotate(degree)
        filtered=edited
        # st.image(edited)
        if filters!=None:
            if filters=="Blur":
                filtered=edited.filter(BLUR)
            elif filters=="Detail":
                filtered=edited.filter(DETAIL)
            elif filters=="Emboss":
                filtered=edited.filter(EMBOSS)
            elif filters=="smooth":
                filtered=edited.filter(SMOOTH)
        st.image(filtered)
        img_byte_arr = BytesIO()
        filtered.save(img_byte_arr, format='PNG')
        st.download_button("📥 Download Edited Image", data=img_byte_arr.getvalue(), file_name="edited_image.png", mime="image/png")