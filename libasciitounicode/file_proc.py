from docx import Document
from io import BytesIO


class Doc:
    def __init__(self, filepath):
        self.filepath = filepath
        self.content = []
        self.doc = None

    def __repr__(self):
        return "Documents reading, writing and converting support"

    def get_content(self):
        self.doc = Document(self.filepath)
        for docpara in self.doc.paragraphs:
            self.content.append(docpara.text)
        return self.content

    def save(self):
        self.doc.save(self.filepath)
