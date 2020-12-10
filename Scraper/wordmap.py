from wordcloud import WordCloud, STOPWORDS
import sys, os



f = open(os.path.join(sys.path[0], "articletext.txt"), "r")
text = f.read()

stopwords = set(STOPWORDS)
cloud = WordCloud(stopwords=stopwords, background_color='white').generate(text)

#converts the wordcloud into an image and downloads it onto computer
cloud.to_file("wordcloud.png")


