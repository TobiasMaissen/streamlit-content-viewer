import streamlit as st
import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO

@st.cache_data
def load_data():
    # Öffnet und lädt das JSON-Dokument
    with open("updated_content_flow.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    # Wir extrahieren die Liste der Blog-Posts
    return data.get("blog_posts", [])

def create_pdf(post):
    # Create a BytesIO buffer
    buffer = BytesIO()
    
    # Create the PDF object using ReportLab
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    
    # Create custom style for better formatting
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30
    )
    
    date_style = ParagraphStyle(
        'CustomDate',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=20,
        textColor=colors.gray
    )
    
    content_style = ParagraphStyle(
        'CustomContent',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        spaceAfter=12
    )
    
    # Create the elements that will make up our document
    elements = []
    
    # Add title
    elements.append(Paragraph(post["title"], title_style))
    elements.append(Paragraph(post["date"], date_style))
    
    # Add content sections with headers
    for section, content in [
        ("Blog Content", post.get("content", "Kein Content vorhanden.")),
        ("LinkedIn Content", post.get("linkedin_content", "Kein Content vorhanden.")),
        ("Whitepaper Content", post.get("whitepaper_content", "Kein Content vorhanden."))
    ]:
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(section, styles['Heading2']))
        elements.append(Spacer(1, 6))
        elements.append(Paragraph(content, content_style))
    
    # Build PDF
    doc.build(elements)
    
    # Get the value of the BytesIO buffer
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

# Daten laden
posts = load_data()

# Überschrift der App
st.title("Content-Vergleich")

# Sidebar: Auswahl eines Eintrags anhand des Titels
post_titles = [post["title"] for post in posts]
selected_title = st.sidebar.selectbox("Wähle einen Eintrag", post_titles)
selected_post = next(post for post in posts if post["title"] == selected_title)

# Anzeige des Titels und Datums
st.header(selected_post.get("title", "Kein Titel"))
st.subheader(selected_post.get("date", "Kein Datum"))

# PDF Export Button
if st.button("Als PDF exportieren"):
    pdf = create_pdf(selected_post)
    st.download_button(
        label="PDF herunterladen",
        data=pdf,
        file_name=f"{selected_title}.pdf",
        mime="application/pdf"
    )

# Nutzung von Tabs zur übersichtlichen Darstellung der drei Content-Bereiche
tabs = st.tabs(["Blog Content", "LinkedIn Content", "Whitepaper Content"])

with tabs[0]:
    st.markdown("### Blog Content")
    st.write(selected_post.get("content", "Kein Content vorhanden."))

with tabs[1]:
    st.markdown("### LinkedIn Content")
    st.write(selected_post.get("linkedin_content", "Kein Content vorhanden."))

with tabs[2]:
    st.markdown("### Whitepaper Content")
    st.write(selected_post.get("whitepaper_content", "Kein Content vorhanden."))
