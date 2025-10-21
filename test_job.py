from job_parser import extract_keywords

job_text = """
We are looking for a Python developer with experience in machine learning, data analysis, and web development.
Knowledge of Flask, pandas, and scikit-learn is required.
"""

keywords = extract_keywords(job_text)
print(keywords)
