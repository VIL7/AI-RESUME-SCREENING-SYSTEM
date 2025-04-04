# AI-RESUME-SCREENING-TOOL
AI-powered web tool for resume screening and ranking, built with HTML, CSS, and JavaScript AND Python. Extracts text from PDFs, ranks resumes using TF-IDF and cosine similarity, and features a modern UI

## Overview
The AI Resume Screening Tool is a web-based application designed to automate the process of screening and ranking resumes against a job description. It extracts text from PDF resumes, computes relevance scores using AI techniques, and presents the results in a modern, user-friendly interface. The system employs TF-IDF vectorization and cosine similarity to rank resumes, enabling recruiters to identify top candidates efficiently.

## Features
- **PDF Text Extraction**: Utilizes pdf.js to extract text from text-based PDF resumes.
- **AI-Driven Ranking**: Ranks resumes based on relevance to a job description using TF-IDF and cosine similarity.
- **Modern Interface**: Features a responsive UI with HTML, CSS, and JavaScript, including animations and a professional design.
- **Client-Side Processing**: Operates entirely in the browser, ensuring accessibility without server requirements.

## Tech Stack
- **Frontend**: HTML5, CSS3, JavaScript
- **Libraries**: pdf.js (v2.11.338) for PDF text extraction
- **Algorithms**: TF-IDF vectorization, Cosine Similarity

## Project Setup
### Prerequisites
- A modern web browser (e.g., Google Chrome, Firefox).
- No additional software or server setup required.

### Installation
#1. Clone the repository:
https://github.com/VIL7/AI-RESUME-SCREENING-SYSTEM.git

#2. Navigate to the project directory:
   cd AI-Resume-Screening-Tool

#3.STEPS

   Open `index.html` in your browser:
- Double-click `index.html`, or
- Use a local server (e.g., VS Code Live Server) for optimal performance.

## Usage
1. Open the application in your browser.
2. Enter a job description in the text area (e.g., "Executive Secretary").
3. Upload one or more PDF resumes using the file input.
4. Click "Rank Resumes" to process and view the results.
5. Review the ranked list of resumes with scores and the top match’s extracted text.

## Screenshots
### Initial Interface
![Initial Interface](screenshots/initial.png)  
*The initial interface with input fields for job description and resume upload.*

### Results Interface
![Results Interface](screenshots/results.png)  
*The results interface showing ranked resumes and the top match’s extracted text.*

## Limitations
- Supports only text-based PDFs (scanned PDFs are not supported).
- Relies on keyword-based matching, lacking semantic understanding.
- Client-side processing may be slow for large datasets.

## Future Improvements
- Integrate NLP for semantic analysis.
- Add OCR support for scanned PDFs.
- Implement result export functionality (e.g., CSV download).
