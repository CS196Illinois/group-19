from wordcloud import WordCloud, STOPWORDS
import wikipedia 
import sys, os



f = open(os.path.join(sys.path[0], "testArticle.txt"), "r")
text = f.read()

stopwords = set(STOPWORDS)
stopwords.update(["stopword1", "stopword2"])
cloud = WordCloud(stopwords=stopwords, background_color='white').generate(text)

#converts the wordcloud into an image and downloads it onto computer
cloud.to_file("wordcloud.png")


