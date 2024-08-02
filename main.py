from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader
from langchain import OpenAI
import streamlit as st
import tempfile
import os
from dotenv import load_dotenv
from langchain.globals import set_verbose
set_verbose(True)


load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0)

def summarize_pdfs_from_folder(pdfs_folder):
    summaries = []
    for pdf_file in pdfs_folder:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(pdf_file.read())
        
        loader = PyPDFLoader(temp_path)
        docs = loader.load_and_split()
        chain = load_summarize_chain(llm, chain_type="map_reduce")
        summary = chain.run(docs)
        summaries.append(summary)

        
        os.remove(temp_path)
    
    return summaries

st.title("Multiple PDF Summarizer")


pdf_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if pdf_files:
   
    if st.button("Generate Summary"):
        st.write("Summaries:")
        summaries = summarize_pdfs_from_folder(pdf_files)
        for i, summary in enumerate(summaries):
            st.write(f"Summary for PDF {i+1}:")
            st.write(summary)