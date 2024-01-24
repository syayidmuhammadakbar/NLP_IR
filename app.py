import streamlit as st
from txtai.pipeline import Summary
from PyPDF2 import PdfFileReader

st.set_page_config(layout='wide')

@st.cache_resource
def summary_text(text):
    summary = Summary()
    text = (text)
    result = summary(text)
    return result

# Extract text from the PDF file using pyPDF2
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = PdfFileReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text

choice = st.sidebar.selectbox('select your choice', ['Summarize Text', 'Summarize Document'])

if choice == 'Summarize Text':
    st.title('_SummarizeME_ is :blue[cool] :sunglasses:')
    st.text('Ini adalah website _text summary_  yang dapat memudahkan dalam merangkum sebuah paragraph.')
    st.text('website ini disusun oleh: Syayid Muhammad Akbar dan Ayu Hapsary')
    input_text = st.text_area('Enter your text here !')
    if input_text is not None:
        if st.button('Summarize Text'):
            col1, col2 = st.columns([1,1])
            with col1:
                st.markdown("***your input text***")
                st.info(input_text)
            with col2:
                result = summary_text(input_text)
                st.markdown("***Summary***")
                st.success(result)

elif choice == 'Summarize Document':
    st.subheader('Summarize Document using textai')
    input_file = st.file_uploader('Input your file', type= ['pdf'])
    if input_file is not None:
        if st.button("Summarize Document"):
            with open(' PEMANFATAN TEOREMA BAYES DALAM PENENTUAN PENYAKIT THT.pdf', 'wb') as f:
                f.write(input_file.getbuffer())
            col1, col2 = st.columns([1,1])
            with col1:
                st.markdown("***Extracted file***")
                extracted_text = extract_text_from_pdf('PEMANFATAN TEOREMA BAYES DALAM PENENTUAN PENYAKIT THT.pdf')
            with col2:
                result = extract_text_from_pdf(input_file)
                st.markdown("***Summarize Document***")
                summary_result = summary_text(result)
                st.success(summary_result)