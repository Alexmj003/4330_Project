
import collections
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

fo = open("PracticeFile.txt", "r") #open file
content = fo.read() #readfile
contentSplit = content.split(' ') #splitString
stop_words = set(stopwords.words('english'))#stop word filtering
appendFile = open('filteredtext.txt', 'a')  # new file of filtered words
appendFile.truncate(0)#Clears Temp file of txt
appendFile.close() #closes The File
for r in contentSplit:#loop
    if not r in stop_words:#filter stop words
        appendFile = open('filteredtext.txt', 'a') # opens the file again
        appendFile.write(" "+r) # append to file
        appendFile.close() # close file

FilterFile = open("filteredtext.txt","r") #split
FilteredContent = FilterFile.read() #filteredcontent
FilteredContentSplit = FilteredContent.split(' ') #split content

wordcount = {} # list of key words
for word in FilteredContentSplit: #loop for gathering key words
    if word not in wordcount: #nested loop
        wordcount[word] = 1 #algoritm
    else:
        wordcount[word] += 1 #algorithm


WordLimiter = 10 #limit for keywords
word_counter = collections.Counter(wordcount) #collections class for counting words
FinalFile = open("FinalFile.txt","w") #Opens file to be passed to the wordcloud

for word, count in word_counter.most_common(WordLimiter): # writes words to file
    FinalFile.write(word + " ")

FilterFile.close()#cleanup
fo.close()#cleanup
FinalFile.close()#cleanup
