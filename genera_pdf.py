from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import colors

names_surnames = [
    "Mario Rossi",
    "Giovanni Cesario",
    "Axel Smith"
]

styles = getSampleStyleSheet()
styleN = styles['Normal']

for name_surname in names_surnames:
# Create a PDF document with the person's name as the filename
    doc = SimpleDocTemplate(f"{name_surname}.pdf", pagesize=letter)
    story = []

# Original text with a placeholder "XXXXX" to be replaced by the name
    Substituction_text = 'Ich, XXXXX, bestätige, dass ich online meiner Zustimmung zur Durchführung eines PoC-Antigen-Tests und zur Vorlage des entsprechenden Nachweises für die Berechtigung zur Testung gemäß der Coronavirus-Testverordnung zugestimmt habe.\n\nHeute wurde ein PoC-Antigen-Test zur direkten Erregererkennung des SARS-CoV-2-Virus bei mir durchgeführt. Ich bestätige dies hiermit.\n\nDiese Online-Zustimmung ist gültig und erfordert keine Unterschrift.'
# Replace "XXXXX" with the current name in the loop
    modified_text = Substituction_text.replace("XXXXX", name_surname)

# Split the text into paragraphs using '\n\n' as a separator
    paragraphs = modified_text.split('\n\n')

    for paragra in paragraphs:
# Create a Paragraph object for each paragraph in the text
        p = Paragraph(paragra, styleN)
        story.append(p)
# Add a space between paragraphs
        story.append(Spacer(1, 0.3 * inch))  
# Build the PDF document with the story content
    doc.build(story)