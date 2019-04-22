

import collections
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import docx

class FileParser:
    def __init__(self,):
        input_file = None
        content = None# initial text of file
        content_split = None
        stop_words = set(stopwords.words('english'))#stop word filtering
        word_limiter = 10
        result_file = None
        filter_words = []
        keywords = {}
        wordcounter = None
        topkeywords = []

    def readtxt(self,txt = str("PracticeFile.txt")):
        self.input_file = open(str,'a')
        self.contents = self.input_file.read()
        self.content_split = self.content.split(' ')#splitstring
        for r in self.content_split:
            if not r in stop_words:
                self.filter_words.append(r)
        for word in self.filter_words:
            if word not in self.keywords:
                self.keywords[word] = 1
            else:
                self.keywords[word] += 1
        self.wordcounter = collections.Counter(self.keywords)
        for word, count in self.wordcounter.most_common(self.word_limiter):
            self.topkeywords.append(word)
        self.input_file.close()

    def readdocx(self,txt = str('/Users/idky/PycharmProjects/BasicProject/untitled/Corn, Cows, and Cash_word FINAL DRAFT.docx"')):
        self.input_file = docx.Document(txt)
        self.content = []
        for para in self.input_file.paragraphs:
            self.content.append(para.text)
        text = "".join(self.content)
        self.content_split = text.split(' ')
        for r in self.content_split:
            if not r in stop_words:
                self.filter_words.append(r)
        for word in self.filter_words:
            if word not in self.keywords:
                self.keywords[word] = 1
            else:
                self.keywords[word] += 1
        self.wordcounter = collections.Counter(self.keywords)
        for word, count in self.wordcounter.most_common(self.word_limiter):
            self.topkeywords.append(word)

    def gettopkeywords(self):
        return self.gettopkeywords()
    
