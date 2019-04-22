

import collections
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import docx
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

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
        wordfreq = {}
        wordcounter = None
        topkeywords = []

    def readtxt(self,txt = str('PracticeFile.txt'), txt2 = str('FinalFile.txt')):
        self.input_file = open(txt,'r')
        self.content = self.input_file.read()
        self.content_split = self.content.split(' ')#splitstring
        self.stop_words = set(stopwords.words('english'))#stop word filtering
        self.filter_words = []
        self.keywords = {}
        self.word_limiter = 10
        self.topkeywords = []
        self.wordfreq = {}
        for r in self.content_split:
            if not r in self.stop_words:
                self.filter_words.append(r)
        for word in self.filter_words:
            if word not in self.keywords:
                self.keywords[word] = 1
            else:
                self.keywords[word] += 1
        self.wordcounter = collections.Counter(self.keywords)
        for word, count in self.wordcounter.most_common(self.word_limiter):
            self.topkeywords.append(word)
            self.wordfreq[word] = count
        self.input_file.close()
        file = open(txt2,'a')
        file.truncate(0)
        for each in self.topkeywords:
            file.write(each + " " )
        file.close()

    def readdocx(self,txt = str('FileParser.docx'),txt2 = str('FinalFile.txt')):
        self.input_file = docx.Document(txt)
        self.content = []
        self.stop_words = set(stopwords.words('english'))  # stop word filtering
        self.filter_words = []
        self.keywords = {}
        self.word_limiter = 10
        self.topkeywords = []
        self.wordfreq = {}
        for para in self.input_file.paragraphs:
            self.content.append(para.text)
        text = "".join(self.content)
        self.content_split = text.split(' ')
        for r in self.content_split:
            if not r in self.stop_words:
                self.filter_words.append(r)
        for word in self.filter_words:
            if word not in self.keywords:
                self.keywords[word] = 1
            else:
                self.keywords[word] += 1
        self.wordcounter = collections.Counter(self.keywords)
        for word, count in self.wordcounter.most_common(self.word_limiter):
            self.topkeywords.append(word)
            self.wordfreq[word] = count
        file = open(txt2, 'a')
        file.truncate(0)
        for each in self.topkeywords:
            file.write(each + " ")
        file.close()

    def get_frequency(self):
        return self.wordfreq

    def gettopkeywords(self):
        return self.topkeywords

    def wordcloud(self):
        string = ""
        for each in self.topkeywords:
            string += each + " "

        wordcloud = WordCloud().generate(string)
        return wordcloud

    def showwordcloud(self):
        string = ""
        for each in self.topkeywords:
            string += each + " "

        wordcloud = WordCloud().generate(string)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

def __main__():
    Document = FileParser()
    Document.readtxt()
    words = Document.gettopkeywords()
    print("HELLO")
    print(type(words))
    for word in words:
        print(word)
    Document.showwordcloud()

if __name__ == '__main__':
    __main__()
