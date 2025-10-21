from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_to_job(resume_text, job_text):
    """
    Compares resume and job description using cosine similarity.
    :param resume_text: Text from resume
    :param job_text: Text from job description
    :return: Match score as a percentage
    """
    try:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, job_text])
        score = cosine_similarity(vectors[0:1], vectors[1:2])
        return round(score[0][0] * 100, 2)
    except Exception as e:
        return f"Error matching texts: {e}"
