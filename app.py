import streamlit as st
import fitz
import plotly.express as px
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io


def generate_pdf(score, skills, role):

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Smart Resume Analyzer Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Resume Score: {score}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Recommended Role: {role}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "Detected Skills:",
            styles["Heading2"]
        )
    )

    for skill in skills:
        content.append(
            Paragraph(
                "• " + skill,
                styles["Normal"]
            )
        )

    doc.build(content)

    buffer.seek(0)

    return buffer



st.set_page_config(
    page_title="Smart Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# Sidebar

st.sidebar.title("🤖 Smart Resume Analyzer")

st.sidebar.info(
    """
AI-powered Resume Screening System

Features:
✅ Skill Detection
✅ Resume Score
✅ Job Matching
✅ AI Suggestions
✅ PDF Report

Technologies:
• Python
• Streamlit
• NLP
• PyMuPDF
• Plotly
"""
)


st.title("🚀 Smart Resume Analyzer")

st.subheader(
    "AI-Powered Resume Screening & Career Assistant"
)



skills = [
    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "Machine Learning",
    "AI",
    "IoT",
    "ESP32",
    "Arduino",
    "Embedded Systems",
    "GitHub"
]


suggestion_rules = {

    "Projects": "Add more practical projects with GitHub links",
    "GitHub": "Create a GitHub profile and upload your projects",
    "Machine Learning": "Learn Machine Learning and AI concepts",
    "SQL": "Improve database and SQL skills",
    "Cloud": "Learn AWS / Google Cloud basics",
    "Communication": "Improve communication and presentation skills"

}



uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)


job_description = st.text_area(
    "Paste Job Description Here"
)



if uploaded_file:

    pdf = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )


    text = ""

    for page in pdf:
        text += page.get_text()


    text_lower = text.lower()



    # Skill Detection

    detected = []

    for skill in skills:

        if skill.lower() in text_lower:
            detected.append(skill)



    # Resume Score

    score = min(
        len(detected) * 5,
        100
    )


    # Resume Strength

    st.subheader("📊 Resume Strength")

    st.progress(score / 100)

    st.write(
        f"Resume Strength: {score}%"
    )



    # Metrics

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "📊 Resume Score",
            f"{score}%"
        )


    with col2:

        st.metric(
            "🛠 Skills Found",
            len(detected)
        )


    with col3:

        st.metric(
            "📄 Pages",
            len(pdf)
        )



    st.divider()



    # Skill Chart

    st.subheader("📊 Skill Analysis")


    if detected:

        chart_data = {
            "Skill": detected,
            "Count": [1] * len(detected)
        }


        fig = px.bar(
            chart_data,
            x="Skill",
            y="Count",
            title="Detected Skills"
        )


        st.plotly_chart(fig)


    else:

        st.warning(
            "No skills found"
        )



    # Detected Skills

    st.subheader("🤖 AI Detected Skills")


    for skill in detected:

        st.success(
            "✅ " + skill
        )



    # AI Suggestions

    st.subheader("💡 AI Resume Improvement Suggestions")


    suggestions = []


    for item, message in suggestion_rules.items():

        if item.lower() not in text_lower:

            suggestions.append(message)



    for suggestion in suggestions:

        st.warning(
            "📌 " + suggestion
        )



    # Resume Text

    st.subheader("📄 Resume Text")


    st.text_area(
        "Extracted Text",
        text,
        height=250
    )



    # Job Matching

    st.subheader("🎯 Job Description Matching")


    if job_description:


        jd_lower = job_description.lower()


        matched = []

        missing = []


        for skill in skills:

            if skill.lower() in jd_lower:

                if skill.lower() in text_lower:

                    matched.append(skill)

                else:

                    missing.append(skill)



        total = len(matched) + len(missing)


        if total > 0:

            match_score = int(
                (len(matched) / total) * 100
            )


            st.metric(
                "Job Match Score",
                f"{match_score}%"
            )


            st.write("✅ Matched Skills")

            for skill in matched:

                st.success(skill)



            st.write("❌ Missing Skills")

            for skill in missing:

                st.warning(skill)



    # PDF Download

    st.subheader("📄 Download Report")


    pdf_file = generate_pdf(
        score,
        detected,
        "Recommended Role"
    )


    st.download_button(
        label="Download Resume Report PDF",
        data=pdf_file,
        file_name="Resume_Analysis_Report.pdf",
        mime="application/pdf"
    )