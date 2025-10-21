from pdfminer.high_level import extract_text

def extract_resume_text(file_path):
    """
    Extracts text from a PDF resume.
    :param file_path: Path to the PDF file
    :return: Extracted text as a string
    """
    try:
        text = extract_text(file_path)
        return text
    except Exception as e:
        return f"Error extracting text: {e}"
