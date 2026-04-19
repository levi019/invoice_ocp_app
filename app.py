import streamlit as st
from PIL import Image
from pdf2image import convert_from_bytes
from parser import extract_invoice_data
from ai_parser import extract_with_gpt
from ocr_servicee import extract_text, image_to_bytes
#from ocr_local import extract_text


st.title("📄 Invoice OCR App")
st.write("Invoice faylini yuklang (PNG, JPG, PDF)")

uploaded_file = st.file_uploader(
    "Upload invoice",
    type=["png", "jpg", "pdf"]
)

if "uploaded" not in st.session_state:
    st.session_state.uploaded = False

if uploaded_file is not None:
    st.session_state.uploaded = True
    file_type = uploaded_file.type
    images = []
    all_text = ""

    # IMAGE FILE
    if file_type.startswith("image"):
        image = Image.open(uploaded_file)
        images.append(image)
        #st.image(image, caption="Uploaded Invoice", use_container_width=True)

    # PDF FILE
    elif file_type == "application/pdf":
        images = convert_from_bytes(uploaded_file.read())

    st.success("File uploaded ✅")

    with st.spinner("Processing..."):
        for img in images:
            st.image(img, caption="Uploaded Invoice", use_container_width=True)

            image_bytes = image_to_bytes(img)
            text = extract_text(image_bytes)
            all_text += text + "\n"
    
    #data = extract_with_gpt(all_text)
    try:
        data = extract_with_gpt(all_text)
    except:
        data = extract_invoice_data(all_text)

    # with st.spinner("Processing invoice..."):
    #     text = extract_text(image)
    #     #st.subheader("📊 Extracted Text")
    #     #st.text(text)

    #     data = extract_invoice_data(text)

    st.subheader("📦 Structured Data")
    st.json(data)

else:
    if not st.session_state.uploaded:
        st.info("Please upload an invoice file 📤")


# Agar fayl yuklansa
#if uploaded_file is not None:
#    st.success("File muvaffaqiyatli yuklandi ✅")

    # Fayl nomi
#    st.write("📌 File name:", uploaded_file.name)

    # Agar rasm bo‘lsa preview qilamiz
#    if uploaded_file.type.startswith("image"):
#        st.image(uploaded_file, caption="Uploaded Invoice", use_container_width=True)

# Natija uchun joy (hali OCR yo‘q)
#st.markdown("---")
#st.subheader("📊 Extracted Data (keyin chiqadi)")
#st.info("Hozircha bo‘sh - OCR keyingi bosqichda qo‘shiladi")
