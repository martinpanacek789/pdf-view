import streamlit as st

import base64

st.title("PDF Viewer")

pdf_file = '/Users/martinpanacek/pdf-view/autentista_champagne_list_2023.pdf'  # Replace 'your-pdf-file.pdf' with your PDF file's filename

# Opening file from file path
with open(pdf_file, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

# Embedding PDF in HTML
pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

# Displaying File
st.markdown(pdf_display, unsafe_allow_html=True)