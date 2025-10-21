from matcher import match_resume_to_job

resume_text = """
Experienced Python developer skilled in machine learning, data analysis, and web development.
Proficient in Flask, pandas, and scikit-learn.
"""

job_text = """
We are looking for a Python developer with experience in machine learning, data analysis, and web development.
Knowledge of Flask, pandas, and scikit-learn is required.
"""

score = match_resume_to_job(resume_text, job_text)
print(f"Match Score: {score}%")
