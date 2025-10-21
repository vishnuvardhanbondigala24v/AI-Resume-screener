import streamlit as st
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader

from resume_parser import extract_resume_text
from job_parser import extract_keywords
from matcher import match_resume_to_job

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="AI Resume Screener", layout="wide")

st.title("📄 AI Resume Screener")
st.markdown(
    "Upload your resume and a job description to see how well they match. "
    "You'll get a match score, keyword analysis, and smart suggestions to improve your resume."
)

# ----------------------------
# Sidebar Uploads
# ----------------------------
st.sidebar.header("📂 Upload Your Files")
resume_file = st.sidebar.file_uploader("Resume (PDF)", type=["pdf"])
job_file = st.sidebar.file_uploader("Job Description (PDF)", type=["pdf"])

# ----------------------------
# Helper: Extract text directly from uploaded PDF
# ----------------------------
def extract_text_from_upload(uploaded_file):
    text = ""
    try:
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        text = f"Error reading PDF: {e}"
    return text

# ----------------------------
# Main Logic
# ----------------------------
if resume_file and job_file:
    with st.spinner("🔎 Analyzing your resume and job description..."):
        try:
            # Extract text directly from uploaded files
            resume_text = extract_text_from_upload(resume_file)
            job_text = extract_text_from_upload(job_file)

            # Match score
            score = match_resume_to_job(resume_text, job_text)
            st.header("📊 Match Score")
            st.success(f"Your resume matches the job description by **{score}%**")

            # Keyword analysis
            job_keywords = extract_keywords(job_text)
            matched_keywords = [kw for kw in job_keywords if kw in resume_text.lower()]
            unmatched_keywords = [kw for kw in job_keywords if kw not in resume_text.lower()]

            st.header("🔍 Keyword Match Summary")
            col1, col2 = st.columns(2)
            col1.metric("Matched Keywords", len(matched_keywords))
            col2.metric("Unmatched Keywords", len(unmatched_keywords))

            # Bar chart
            fig, ax = plt.subplots()
            ax.bar(["Matched", "Unmatched"],
                   [len(matched_keywords), len(unmatched_keywords)],
                   color=["green", "red"])
            ax.set_ylabel("Number of Keywords")
            ax.set_title("Resume vs Job Keyword Match")
            st.pyplot(fig)

            # Expanders
            with st.expander("✅ Matched Keywords"):
                st.write(", ".join(matched_keywords) if matched_keywords else "None")
            with st.expander("❌ Unmatched Keywords"):
                st.write(", ".join(unmatched_keywords) if unmatched_keywords else "None")

            # Suggestions
            st.header("💡 Smart Suggestions to Improve Your Resume")
            if unmatched_keywords:
                st.write("Consider adding these keywords or skills to better match the job description:")
                for kw in unmatched_keywords[:10]:
                    st.markdown(f"- **{kw}**")
                st.write("You can include these in sections like:")
                st.markdown("- **Skills**")
                st.markdown("- **Summary**")
                st.markdown("- **Experience bullet points**")
            else:
                st.success("Your resume already covers all the key terms from the job description. Great job!")

            # Raw text views
            with st.expander("📄 See Resume Text"):
                st.write(resume_text)
            with st.expander("📄 See Job Description Text"):
                st.write(job_text)

        except Exception as e:
            st.error(f"⚠️ An error occurred while processing: {e}")

st.markdown("---")
st.caption("Built using Streamlit and spaCy")
