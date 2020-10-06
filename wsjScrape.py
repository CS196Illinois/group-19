# https://stackoverflow.com/questions/58733753 how-to-extract-daily-close-from-wsj-using-python

import os
from selenium import webdriver
import datetime

### Finding and setting up chromedriver for webscraping ###
driver_path = os.path.dirname(os.path.realpath(__file__)) + '/chromedriver'
browser = webdriver.Chrome(executable_path = driver_path)

wsjLinkList = []
wsjFilteredList = []
wsjText = []

wsjSearched = False


### Getting Current Date (Used in Webscraping) ###
def calibrateDate():
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


### Webscraping WSJ ###

def wsjScrape():
    browser.get('https://www.wsj.com/')
    wsjHeadlines = browser.find_elements_by_tag_name('a')

    # Puts all links from today into wsjLinkList
    target = '/' + currentYear + '/' + currentMonth + '/' + currentDay
    for i in wsjHeadlines:
        try:
            wsjLink = i.get_attribute('href')
            if target in wsjLink:
                wsjLinkList.append(wsjLink)
        except:
            pass

    for i in wsjLinkList:
        if i not in wsjFilteredList:
            wsjFilteredList.append(i)
    
    # print(wsjFilteredList)

    for i in wsjFilteredList:
        articleText = []
        browser.get(i)
        articleText = browser.find_elements_by_tag_name('p')
        for i in articleText:
            try:
                wsjText.append(i.text)
                print(i.text)
            except:
                pass

    global wsjSearched
    wsjSearched = True



### Adding scraped data to data.txt ###
def storeData():
    
    #Delete data located in data.txt
    file = open("data.txt","r+")
    file.truncate(0)
    file.close()
    
    if wsjSearched:
        file = open("data.txt", "a+")
        for i in range(len(wsjText)):
            try:
                file.write(wsjText[i])
            except:
                pass
        file.close()

calibrateDate()
wsjScrape()
storeData()
print('done')