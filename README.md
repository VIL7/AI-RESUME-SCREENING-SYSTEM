# AI-Powered Resume Screening and Ranking System

An intuitive tool that leverages machine learning to rank resumes based on their similarity to a job description. This system automates the tedious process of resume screening, ensuring efficiency and accuracy.

---

## 🚀 Features
- **Input Job Description**: Paste or write the desired job description into the text area.
- **Upload Resumes**: Upload multiple resumes in PDF format.
- **Automated Ranking**: Uses TF-IDF and cosine similarity to rank resumes based on relevance.
- **Results Display**: Outputs a ranked list of resumes along with similarity scores.

---

## 🛠️ Technologies Used
- **Streamlit**: For the user interface.
- **PyPDF2**: To parse and extract text from PDFs.
- **Scikit-learn**: For TF-IDF vectorization and cosine similarity calculations.
- **Pandas**: For structured data manipulation and display.

---

## 📋 Workflow Overview
### 1. **User Input and Frontend**
   - Enter job description in a text area.
   - Upload one or more resumes as PDF files.

### 2. **Backend Processing**
   - Parse and extract text from uploaded resumes.
   - Process the input job description.

### 3. **Feature Engineering**
   - Convert text data into numerical representations using TF-IDF.

### 4. **Similarity Computation**
   - Calculate similarity scores using cosine similarity.

### 5. **Output**
   - Display ranked resumes in a sortable table.



---



