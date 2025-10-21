import spacy
import subprocess
import sys
from PyPDF2 import PdfReader

# ----------------------------
# Load spaCy model safely
# ----------------------------
def load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
        return spacy.load("en_core_web_sm")

# ----------------------------
# Extract raw text from a job description PDF
# ----------------------------
def extract_job_text(file_path: str) -> str:
    """
    Extracts raw text from a job description PDF.
    :param file_path: Path to the job description PDF
    :return: Extracted text as a string
    """
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        text = f"Error reading job description: {e}"
    return text

# ----------------------------
# Extract keywords from job description text
# ----------------------------
def extract_keywords(text: str) -> list[str]:
    """
    Extracts keywords from job description text using spaCy.
    :param text: Job description as a string
    :return: List of unique keywords
    """
    nlp = load_spacy_model()
    doc = nlp(text)
    keywords = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
    return list(set(keywords))  # remove duplicates
