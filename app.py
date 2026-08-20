import streamlit as st

st.set_page_config(page_title='Enterprise RAG Assistant')
st.title('Enterprise RAG Knowledge Assistant')

st.write('Upload documents and chat with your knowledge base.')

uploaded_file = st.file_uploader('Upload PDF', type=['pdf'])

if uploaded_file:
    st.success('Document uploaded successfully.')

query = st.text_input('Ask a question')

if query:
    st.info('RAG pipeline will process this query.')
