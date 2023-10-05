import streamlit as st

import base64

st.title("PDF Viewer")

pdf_url = 'https://storage.googleapis.com/test-public-1234567/autentista_champagne_list_2023.pdf'

# Opening file from file path
#with open(pdf_file, "rb") as f:
#    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

# Embedding PDF in HTML
pdf_display = F'<iframe class="content_viewport" src="{pdf_url}" width="100%" height="600"></iframe>'

# Displaying File
st.markdown(pdf_display, unsafe_allow_html=True)