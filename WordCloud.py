from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#Wordcloud rapper class
class WordClout():
    def __init__(self, text = str("")):# passes a string to be converted to wordcloud text
        self.text = text
        self.wordclout = WordCloud().generate(self.text)

    def getclout(self):# returns a wordcloud
        return self.wordclout

    def saveclout(self, pathname = str('demo')): # saves a worcloud to a pathname provide, include the pathname but not the file extension
        pathname = pathname + '.png'
        self.wordclout.to_file(pathname)

    def showclout(self):# displays a wordcloud
        plt.imshow(self.wordclout, interpolation='bilinear')
        plt.axis("off")
        plt.show()

def __main__():
    Clout = WordClout("sample text to be fitted in a wordcloud")
    cloutt = Clout.getclout()
    Clout.saveclout("/Users/idky/PycharmProjects/BasicProject/untitled/CloutDemo")
    Clout.showclout()

if __name__ == '__main__':
    __main__()