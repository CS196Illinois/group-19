
#Imports
import requests
from bs4 import BeautifulSoup, SoupStrainer
import datetime
from urllib.request import Request, urlopen
import re

#To be called before every scrape attempt
def newScrape():
    file = open("data.txt","r+")
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
    cnnLinks = set()
    cnn = requests.get("http://lite.cnn.com/en")
    cnn = BeautifulSoup(cnn.content, 'html.parser')
    cnn = cnn.find_all('a')
    for link in cnn:
        if "article" in link.get('href'):
            cnnLinks.add(link.get('href'))
    file = open("data.txt","a+")
    for link in cnnLinks:
        article = requests.get("http://lite.cnn.com" + link)
        article = BeautifulSoup(article.content, 'html.parser')
        text = article.find_all('p')
        for item in text:
            item = item.getText()
            if '© 2019 Cable News Network' not in item and "Listen to CNN (low-bandwidth usage)" not in item and "Go to the full CNN experience" not in item:
                try:
                    file.write(item)
                except:
                    pass
    file.close()


#Webscraping Politico
def politicoScrape():
    politicoLinks = set()
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
    file = open("data.txt","a+")
    for link in politicoLinks:
        article = requests.get(link)
        article = BeautifulSoup(article.content, 'html.parser')
        text = article.find_all('p',{'class':'story-text__paragraph'})
        for item in text:
            item = item.getText()
            try:
                file.write(item)
            except:
                pass
    file.close()

#USA Today Scrape    
def usaScrape():
    usaLinks = set()
    usa = requests.get("https://www.usatoday.com/news/")
    usa = BeautifulSoup(usa.content, 'html.parser')
    usa = usa.find_all('a')
    for link in usa:
        if currentYear + '/' + currentMonth + '/' + currentDay in str(link.get('href')) and '/videos' != str(link.get('href'))[:7]:
            usaLinks.add(link.get('href'))
    file = open("data.txt","a+")
    for link in usaLinks:
        article = requests.get('https://www.usatoday.com' + link)
        article = BeautifulSoup(article.content, 'html.parser')
        text = article.find_all('p',{'class':'gnt_ar_b_p'})
        for item in text:
            item = item.getText()
            try:
                file.write(item)
            except:
                pass
    file.close()

#UPI Scrape
def upiScrape():
    upiLinks = set()
    upi = requests.get('https://www.upi.com/Top_News/US/')
    upi = BeautifulSoup(upi.content, 'html.parser')
    upi = upi.find_all('a')
    for link in upi:
        if currentYear + '/' + currentMonth + '/' + currentDay in str(link.get('href')):
            upiLinks.add(link.get('href'))
    file = open("data.txt","a+")
    for link in upiLinks:
        article = requests.get(link)
        article = BeautifulSoup(article.content, 'html.parser')
        text = article.find_all('p')
        for item in text:
            item = item.getText()
            if "});" not in item and "RELATED" not in item and "Advertisement" not in item:
                try:
                    file.write(item)
                except:
                    pass
    file.close()

#The Federalist Scrape

def fedScrape():
    fedLinks = set()
    fedString = ""
    fed = Request("https://thefederalist.com/blog/", headers={'User-Agent': 'Mozilla/5.0'})
    fed = urlopen(fed).read()
    fed = BeautifulSoup(fed, 'html.parser')
    fed = fed.find_all('a')
    for match in fed:
        fedString = fedString + str(match)
    fedString = re.findall(r'https://thefederalist.com/2020/10/23/[^"]+', fedString)
    for link in fedString:
        fedLinks.add(link)
    file = open("data.txt", "a+")
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
                except:
                    pass
    file.close()
        


#Main

newScrape()
fedScrape()
upiScrape()
usaScrape()
politicoScrape()
cnnScrape()
print('done')
