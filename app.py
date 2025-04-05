import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Apply Streamlit theme colors
st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for colorful styling
st.markdown(
    """
    <style>
    /* Background color for the entire app */
    .stApp {
        background-color: #e6e6fa; /* Light blue */
    }

    /* Header Colors */
    h1 {
        color: #000000; /* Dark Blue */
    }
    h2 {
        color: #000000; /* Dark Blue */
    }

    /* Job Description Section Styling */
    .stTextArea > label {
        color: #000000; /* Indigo */
        font-weight: bold;
        font-size: 16px;
    }

    /* Upload PDF Section Styling */
    .stFileUploader > label {
        color: #000000; /* Chocolate */
        font-weight: bold;
        font-size: 16px;
    }

    /* Box styling for content */
    .reportview-container .main .block-container {
        background-color: #ffffff; /* White background */
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()
    return cosine_similarities
# Streamlit app
st.title("AI Resume Screening & Candidate Ranking System")

# Job description input
st.header("Job Description")
job_description = st.text_area("Enter the job description")

# File uploader
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("Ranking Resumes")
    resumes = [extract_text_from_pdf(file) for file in uploaded_files]
    scores = rank_resumes(job_description, resumes)
    results = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": scores})
    results = results.sort_values(by="Score", ascending=False)
    st.write("### Results")
    st.dataframe(results)
