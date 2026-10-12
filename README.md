# 📄 Resume vs Job Description Matcher using TF-IDF and Cosine Similarity

A Python-based Natural Language Processing (NLP) project that compares a resume with a job description, calculates a text similarity score, identifies shared keywords, and highlights keywords from the job description that are missing from the resume.

The project uses **TF-IDF and Cosine Similarity** from Scikit-learn to demonstrate a practical text-analysis workflow.

## 📌 Project Overview

The goal of this project is to help users understand how closely their resume text matches a particular job description.

Users enter a resume summary and a job description. The program then converts both texts into numerical representations, calculates their similarity, and displays shared and missing keywords.

This is an educational text-matching tool. It is not a real Applicant Tracking System (ATS), a hiring prediction model, or a guarantee of recruitment success.

## ✨ Features

- Compare resume text with a job description
- Convert text into numerical features using TF-IDF
- Calculate text similarity using Cosine Similarity
- Display a similarity score as a percentage
- Identify keywords shared by both documents
- Find keywords in the job description that are absent from the resume
- Handle empty input with a validation message
- Organize the program into separate Python modules
- Run locally through a command-line interface

## 🛠️ Technologies Used

- Python
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Sets and list operations

## 📂 Project Structure

```text
python-resume-job-matcher/
├── main.py
├── resume_matcher.py
├── requirements.txt
└── README.md
```

### File Descriptions

- `main.py` — Collects user input, calls the matching function, and displays the results.
- `resume_matcher.py` — Contains the text vectorization, similarity calculation, and keyword comparison logic.
- `requirements.txt` — Lists the external Python dependency.
- `README.md` — Documents the project, setup instructions, and concepts.

## ⚙️ How It Works

1. The user enters a resume summary.
2. The user enters a job description.
3. The program checks that neither input is empty.
4. `TfidfVectorizer` converts both documents into numerical feature vectors.
5. `cosine_similarity()` compares the vectors.
6. The similarity value is converted into a percentage for display.
7. The program identifies shared keywords.
8. It identifies words present in the job description but absent from the resume.
9. The results are displayed in the terminal.

## 🧠 Core Concepts

### 1. TF-IDF

TF-IDF stands for **Term Frequency–Inverse Document Frequency**.

It assigns numerical weights to words based on their frequency and how informative they are across the documents being analyzed.

In this project, TF-IDF transforms the resume and job description into numerical vectors so that their text can be compared mathematically.

### 2. Cosine Similarity

Cosine Similarity measures the similarity between two numerical vectors by comparing the angle between them.

The result is multiplied by 100 to display a percentage-like similarity score.

A higher score generally means the two text representations are more similar. It does not necessarily mean that the resume is better qualified for the job.

### 3. Shared Keywords

Shared keywords are words recognized in both the resume and job description.

The program finds them using set intersection.

### 4. Missing Keywords

Missing keywords are words recognized in the job description that do not appear in the resume.

The program finds them using set difference.

These are simple word-level comparisons, not a complete assessment of required skills.

## 📊 Example

### Sample Resume

```text
Python developer with experience in SQL, Pandas, data analysis, and machine learning projects.
```

### Sample Job Description

```text
Looking for a Python developer with SQL knowledge, Pandas, data analysis, and machine learning skills.
```

### Example Output

```text
=== Resume vs Job Description Matcher ===

Text Similarity Score: 62.01%

Shared Keywords:
analysis, data, developer, learning, machine, pandas, python, sql

Keywords in job description not found in resume:
knowledge, looking, skills

Note: Similarity is not a hiring probability or an ATS score.
```

The exact score and keywords depend on the input text and implementation. The output above is an illustrative example.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ayushman-ece/python-resume-job-matcher.git
```

### 2. Open the project directory

```bash
cd python-resume-job-matcher
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

Enter your resume summary and job description when prompted.

## 📦 Requirements

The `requirements.txt` file contains:

```text
scikit-learn
```

Python and pip must be installed on your system.

## 📚 Concepts Learned

- Natural Language Processing fundamentals
- Text vectorization
- TF-IDF
- Cosine Similarity
- Feature extraction from text
- Set intersection and set difference
- Input validation
- Python functions and module imports
- Building a practical command-line application
- Understanding the limitations of similarity scores

## ⚠️ Limitations

- The project compares text rather than understanding the full meaning of a resume.
- It may miss synonyms and related skills, such as treating two differently worded skills as unrelated.
- Common words can affect the similarity score.
- Missing words are not necessarily missing qualifications.
- The score is not an ATS score or a probability of being hired.
- The tool does not assess experience quality, education, achievements, or interview performance.
- Users should avoid including sensitive personal information when testing sample resumes.

## 🔮 Future Improvements

- Support uploading resume files in PDF or DOCX format.
- Extract technical skills using a more targeted vocabulary.
- Recognize synonyms and related technical terms.
- Add configurable skill categories and keyword importance.
- Build a web interface using Streamlit or Flask.
- Add unit tests and more robust input handling.
- Compare traditional TF-IDF with semantic embeddings.

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub: [ayushman-ece](https://github.com/ayushman-ece)

---

*Built as a hands-on Python and NLP learning project.*