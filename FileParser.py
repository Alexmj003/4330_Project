from typing import Any, Union
###import pandas
#import nltk
#import re
#from pandas import DataFrame
#from pandas.io.parsers import TextFileReader

#file = str(pandas.read_csv('PracticeFile.txt'))
#print(file)
#words = {}
#words = nltk.word_tokenize(file)
#print(words)
import io

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

fo = open("PracticeFile.txt", "r") #open file
content = fo.read() #readfile
contentSplit = content.split(' ') #splitString
stop_words = set(stopwords.words('english'))#stop word filtering
for r in contentSplit:#loop
    if not r in stop_words:#filter stop words
        appendFile = open('filteredtext.txt','a') #new file of filtered words
        appendFile.write(" "+r) # append to file
        appendFile.close() # close file

FilterFile = open("filteredtext.txt","r") #split
FilteredContent = FilterFile.read() #filteredcontent
FilteredContentSplit = FilteredContent.split(' ') #split content
