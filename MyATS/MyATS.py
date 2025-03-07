import re
from docx import Document
import pdfplumber

class ATSSimulator:
    def __init__(self, file):
        self.file = file
    def simulate(self):
        if self.file.endswith(".docx"):
            get_text = self.get_text_doc()
        elif self.file.endswith(".pdf"):
                get_text=self.get_text_pdf()
        else:
            return "Invalid File"
        x=len(re.findall(r"\b(python|sql|tablaeu|power bi)\b", get_text, re.IGNORECASE))
        return x


    def get_text_doc(self):
        doc=Document(self.file)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        fullText = ' '.join(fullText)
        return fullText
    def get_text_pdf(self):
        with pdfplumber.open(self.file) as pdf:
            fullText = []
            for page in pdf.pages:
                fullText.append(page.extract_text())
            fullText = ' '.join(fullText)
            return fullText


