from docx import Document
from docx.enum.text import WD_COLOR_INDEX

class DocxHighlighter():
    def __init__(self,doc = str('FileParser.docx'),keywords = []):
        self.doc = Document(doc)
        self.keywords = keywords
        self.highlight()


    def highlight(self):
        for para in self.doc.paragraphs:
            for word in self.keywords:
                if word in para.text:
                    for run in para.runs:
                        if word in run.text:
                            x = run.text.split(word)
                            run.clear()
                            for i in range(len(x) - 1):
                                run.add_text(x[i])
                                run.add_text(word)
                                run.font.highlight_color = WD_COLOR_INDEX.YELLOW

    def getDoc(self):
        return self.doc


class TxtHighliter():
    def __init__(self,file = str("PracticeFile.txt"), keywords = []):
        self.ref = file
        self.doc = open(str,'r')
        self.contents = self.doc.read()
        self.splitter = self.contents.split('')

    def highlight(self):
        for word in self.splitter:
            for key in self.keywords:
                if word == key:
                    self.splitter[word] = "\033[1;32;40m{key}"
        self.doc.truncate(0)
        for word in self.splitter:
            self.doc.write(word + " ")

    def closeTxt(self):
        self.doc.close()
