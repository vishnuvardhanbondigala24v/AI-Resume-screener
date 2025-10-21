 - AI Resume Screener

A Streamlit web app that compares resumes with job descriptions using NLP. It calculates match scores, visualizes keyword overlap, and suggests improvements.

  Features
- Upload resume and job description (PDF)
- Match score calculation
- Keyword match visualization
- Smart suggestions for missing skills

  Tech Stack
- Python
- Streamlit
- spaCy
- Matplotlib
- PyPDF2

  Installation
  bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py


AI-Resume-Screener/
├── app.py
├── resume_parser.py
├── job_parser.py
├── matcher.py
├── requirements.txt
├── uploads/
└── .streamlit/
    └── config.toml
