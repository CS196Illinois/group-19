from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    sentimentAnalyzer = SentimentIntensityAnalyzer()
    sentiment_dict = sentimentAnalyzer.polarity_scores(sentence) 
      
    print("Overall sentiment dictionary is : ", sentiment_dict) 
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
  
    print("Sentence Overall Rated As", end = " ") 
  
    # decide sentiment as positive, negative and neutral 
    if sentiment_dict['compound'] >= 0.05 : 
        print("Positive") 
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        print("Negative") 
  
    else : 
        print("Neutral") 


import sys, os
f = open(os.path.join(sys.path[0], "demofile.txt"), "r")
# paragraph = f.read()
# sentiment_scores(paragraph)
line = f.readline()
while line:
    print(line)
    print(sentiment_scores(line))
    line = f.readline()