
#Imports
import requests
from bs4 import BeautifulSoup, SoupStrainer
import datetime
from urllib.request import Request, urlopen
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from textblob import TextBlob
import json

jsonOutput = {}
averagePolarity = 0
polarityCount = 0
global liberalPolarity
global liberalCount
global neutralPolarity
global neutralCount
global conservativePolarity
global consevrativeCount


#To be called before every scrape attempt
def newScrape():
    jsonOutput = {}
    averagePolarity = 0
    polarityCount = 0
    file = open("articletext.txt","r+")
    file.truncate(0)
    file.close()
    try:
        global currentDay
        global currentMonth
        global currentYear
    except:
        pass
    dt = datetime.datetime.today()
    currentYear = str(dt.year)
    if dt.month < 10:
        currentMonth = '0' + str(dt.month)
    else:
        currentMonth = str(dt.month)
    if dt.day < 10:
        currentDay = '0' + str(dt.day)
    else:
        currentDay = str(dt.day)

#CNN Scrape
def cnnScrape():
    global averagePolarity
    global polarityCount
    cnnLinks = set()
    cnnText = ""
    cnn = requests.get("http://lite.cnn.com/en")
    cnn = BeautifulSoup(cnn.content, 'html.parser')
    cnn = cnn.find_all('a')
    for link in cnn:
        if "article" in link.get('href'):
            cnnLinks.add(link.get('href'))
    file = open("articletext.txt","a+")
    for link in cnnLinks:
        article = requests.get("http://lite.cnn.com" + link)
        article = BeautifulSoup(article.content, 'html.parser')
        text = article.find_all('p')
        for item in text:
            item = item.getText()
            if '© 2019 Cable News Network' not in item and "Listen to CNN (low-bandwidth usage)" not in item and "Go to the full CNN experience" not in item:
                try:
                    file.write(item)
                    cnnText = cnnText + item
                except:
                    pass
    file.close()
    if cnnText != "":
        cnnPolarity = polarityCheck(cnnText) 
        print("CNN Polarity: " + cnnPolarity)
        jsonOutput['cnn'] = cnnPolarity
        averagePolarity = averagePolarity + float(cnnPolarity)
        polarityCount = polarityCount + 1
    else:
        print("CNN Polarity: N/A")
        jsonOutput['cnn'] = "null"


#Webscraping Politico
def politicoScrape():
    global averagePolarity
    global polarityCount
    politicoLinks = set()
    politicoText = ""
    politico = requests.get("https://www.politico.com/politics")
    politico = BeautifulSoup(politico.content, 'html.parser')
    politico = politico.find_all('a')
    for link in politico:
        if currentYear + '/' + currentMonth + '/' + currentDay in link.get('href'):
            politicoLinks.add(link.get('href'))
    politico = requests.get("https://www.politico.com/politics/2")
    politico = BeautifulSoup(politico.content, 'html.parser')
    politico = politico.find_all('a')
    for link in politico:
        if currentYear + '/' + currentMonth + '/' + currentDay in link.get('href'):
            politicoLinks.add(link.get('href'))
    file = open("articletext.txt","a+")
    for link in politicoLinks:
        article = requests.get(link)
        article = BeautifulSoup(article.content, 'html.parser')
        text = article.find_all('p',{'class':'story-text__paragraph'})
        for item in text:
            item = item.getText()
            try:
                file.write(item)
                politicoText = politicoText + item
            except:
                pass
    file.close()
    if politicoText != "":
        politicoPolarity = polarityCheck(politicoText)
        print("Politico Polarity: " + politicoPolarity)
        jsonOutput['politico'] = politicoPolarity
        averagePolarity = averagePolarity + float(politicoPolarity)
        polarityCount = polarityCount + 1
    else:
        print("Politico Polarity: N/A")
        jsonOutput['politico'] = "null"

#USA Today Scrape    
def usaScrape():
    global averagePolarity
    global polarityCount
    usaLinks = set()
    usaText = ""
    usa = requests.get("https://www.usatoday.com/news/")
    usa = BeautifulSoup(usa.content, 'html.parser')
    usa = usa.find_all('a')
    for link in usa:
        if currentYear + '/' + currentMonth + '/' + currentDay in str(link.get('href')) and '/videos' != str(link.get('href'))[:7]:
            usaLinks.add(link.get('href'))
    file = open("articletext.txt","a+")
    for link in usaLinks:
        article = requests.get('https://www.usatoday.com' + link)
        article = BeautifulSoup(article.content, 'html.parser')
        text = article.find_all('p',{'class':'gnt_ar_b_p'})
        for item in text:
            item = item.getText()
            try:
                file.write(item)
                usaText = usaText + item
            except:
                pass
    file.close()
    if usaText != "":
        usaPolarity = polarityCheck(usaText)
        print("USA Today Polarity: " + usaPolarity)
        jsonOutput['usaToday'] = usaPolarity
        averagePolarity = averagePolarity + float(usaPolarity)
        polarityCount = polarityCount + 1
    else:
        print("USA Today Polarity: N/A")
        jsonOutput['usaToday'] = "null"

#UPI Scrape
def upiScrape():
    global averagePolarity
    global polarityCount
    upiLinks = set()
    upiText = ""
    upi = requests.get('https://www.upi.com/Top_News/US/')
    upi = BeautifulSoup(upi.content, 'html.parser')
    upi = upi.find_all('a')
    for link in upi:
        if currentYear + '/' + currentMonth + '/' + currentDay in str(link.get('href')):
            upiLinks.add(link.get('href'))
    file = open("articletext.txt","a+")
    for link in upiLinks:
        article = requests.get(link)
        article = BeautifulSoup(article.content, 'html.parser')
        text = article.find_all('p')
        for item in text:
            item = item.getText()
            if "});" not in item and "RELATED" not in item and "Advertisement" not in item:
                try:
                    file.write(item)
                    upiText = upiText + item
                except:
                    pass
    file.close()
    if upiText != "":
        upiPolarity = polarityCheck(upiText)
        print("UPI Polarity: " + upiPolarity)
        jsonOutput['upi'] = upiPolarity
        averagePolarity = averagePolarity + float(upiPolarity)
        polarityCount = polarityCount + 1
    else:
        print("UPI Polarity: N/A")
        jsonOutput['upi'] = "null"

#The Federalist Scrape

def fedScrape():
    global averagePolarity
    global polarityCount
    fedLinks = set()
    fedString = ""
    fedText = ""
    fed = Request("https://thefederalist.com/blog/", headers={'User-Agent': 'Mozilla/5.0'})
    fed = urlopen(fed).read()
    fed = BeautifulSoup(fed, 'html.parser')
    fed = fed.find_all('a')
    for match in fed:
        fedString = fedString + str(match)
    search = 'https://thefederalist.com/' + currentYear + '/' + currentMonth + '/' + currentDay + '/[^"]+'
    fedString = re.findall(search, fedString)
    for link in fedString:
        fedLinks.add(link)
    file = open("articletext.txt", "a+")
    for link in fedLinks:
        article = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        article = urlopen(article).read()
        article = BeautifulSoup(article, 'html.parser')
        text = article.find_all('p')
        for item in text:
            item = item.getText()
            if "Copyright © 2020 The Federalist" not in item:
                try:
                    file.write(item)
                    fedText = fedText + item
                except:
                    pass
    file.close()
    if fedText != "":
        fedPolarity = polarityCheck(fedText)
        print("The Federalist Polarity: " + fedPolarity)
        jsonOutput['federalist'] = fedPolarity
        averagePolarity = averagePolarity + float(fedPolarity)
        polarityCount = polarityCount + 1
    else:
        print("The Federalist Polarity: N/A")
        jsonOutput['federalist'] = "null"
        

#Polarity Check

def polarityCheck(articleText):
    tester = SentimentIntensityAnalyzer()
    dataBlob = TextBlob(articleText)
    dataBlob = dataBlob.sentences
    polarity = 0
    count = 0
    for sentence in dataBlob:
        sentimentScore = tester.polarity_scores(sentence)['compound']
        if abs(sentimentScore) >  0.3:
            polarity = polarity + sentimentScore
            count = count + 1
    polarity = polarity / count
    return(str(polarity))


#To be run at the end of scrape to store data to json

def endScrape():
    jsonOutput['average'] = averagePolarity / polarityCount
    jsonOutput['date'] = currentMonth + currentDay + currentYear
    jsonOutput['averageLiberal'] = (float(jsonOutput['cnn']) + float(jsonOutput['politico'])) / 2
    jsonOutput['averageNeutral'] = (float(jsonOutput['usaToday']) + float(jsonOutput['upi'])) / 2
    jsonOutput['averageConservative'] = jsonOutput['federalist']
    print("Average Polarity: " + str(averagePolarity / polarityCount))
    with open('polarity.txt', 'w') as file:
        json.dump(jsonOutput, file)


#Main

newScrape()
#Liberal
cnnScrape()
politicoScrape()
#Neutral
usaScrape()
upiScrape()
#Conservative
fedScrape()
endScrape()


