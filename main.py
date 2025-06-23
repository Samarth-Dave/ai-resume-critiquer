import streamlit as st
import PyPDF2
import io
import os

import requests
from dotenv import load_dotenv


load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer",page_icon="📃",layout="centered")


st.title("AI Resume Critiquer")

st.markdown("Upload your resume to get it critiqued by AI")

uploaded_file=st.file_uploader("upload your resume (PDF or TXT)",type=["pdf","txt"])
job_role=st.text_input("entere the job role you are targeting ")

grok_API_KEY=os.getenv("API_KEY")

analyze=st.button("analyze resume")

def extract_text_pdf(pdf_file):
    pdf_reader=PyPDF2.PdfReader(pdf_file)
    text=""
    for page in pdf_reader.pages:
        text+=page.extract_text()+"\n"
    return text

def extract_text_file(upladed_file):
    if(upladed_file.type =="application/pdf"):
        text=extract_text_pdf(io.BytesIO(upladed_file.read()))
        return text
    return upladed_file.read().decode("utf-8")
        

if analyze and uploaded_file:
    try:
        file_content=extract_text_file(uploaded_file)
        if not file_content.strip():
            st.error("file has no content....")
            st.stop()
        prompt=f"""
                please anlyze this resume and provide constructive feedback
                focus on the following aspects :
                content clarity and impact,
                skill presentation,
                experince disctription
                specific imporvements for  {job_role if job_role else 'genratal application jobs'}
        resume content={file_content}          
        please provide you content in clear,structured format with specific recommendations"""

        headers = {
            "Authorization": f"Bearer {grok_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama3-70b-8192",
            "messages": [
                {"role": "system", "content": "You are a professional resume reviewer."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 1024
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            feedback = result['choices'][0]['message']['content']
            st.subheader("AI Feedback:")
            st.markdown(feedback)
        else:
            st.error(f"Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
        