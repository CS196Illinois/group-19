### WITH MAC CHROMEDRIVER CURRENTLY ###

### Imports ###
import os
from selenium import webdriver
import datetime

### Initializing Variables ###

cnnList = set()
cnnText = []
usaList = set()
usaText = []
upiList = set()
upiText = []
politicoList = set()
politicoText = []
cnnSearched = False
usaSearched = False
upiSearched = False
politicoSearched = False

### Finding and setting up chromedriver for webscraping ###

#driver_path = os.path.dirname(os.path.realpath(__file__)) + '\\chromedriver.exe'
     #PC Driver

driver_path = os.path.dirname(os.path.realpath(__file__)) + '/chromedriver'
browser = webdriver.Chrome(executable_path = driver_path)


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

#Webscraping CNN
def cnnScrape():
    browser.get('http://lite.cnn.com/en')
    cnnHeadlines = browser.find_elements_by_tag_name('a')
    for i in cnnHeadlines:
        try:
            if "http://lite.cnn.com/" in i.get_attribute('href'):
                cnnList.add(i.get_attribute('href'))
        except:
            pass
    print(cnnList)  
    for i in cnnList:
        browser.get(i)
        articleText = browser.find_elements_by_tag_name('p')
        for n in articleText:
            try:
                if "© 2019 Cable News Network. Turner Broadcasting System, Inc. All Rights Reserved." not in n.text and "Listen to CNN (low-bandwidth usage)" not in n.text and "Go to the full CNN experience" not in n.text:
                    cnnText.append(n.text)
                    print(n.text)
            except:
                pass

    global cnnSearched
    cnnSearched = True


### Webscraping USAtoday ###
def usaScrape():
    browser.get('https://www.usatoday.com/news/')
    usaHeadlines = browser.find_elements_by_tag_name('a')
    for i in usaHeadlines:
        try:
            usaLink = i.get_attribute('href')
            if '/' + currentYear + '/' + currentMonth + '/' + currentDay + '/' in usaLink:
                usaList.add(usaLink)
        except:
            pass
    print(usaList)  
    for i in usaList:
        browser.get(i)
        articleText = browser.find_elements_by_class_name('gnt_ar_b_p')
        for n in articleText:
            usaText.append(n.text)
            print(n.text)
    global usaSearched
    usaSearched = True

    
### Webscraping UPI ###
def upiScrape():
    browser.get('https://www.upi.com/Top_News/US/')
    upiHeadlines = browser.find_elements_by_tag_name('a')
    for i in upiHeadlines:
        try:
            upiLink = i.get_attribute('href')
            if '/' + currentYear + '/' + currentMonth + '/' + currentDay in upiLink:
                upiList.add(upiLink)
        except:
            pass
    print(upiList)  
    for i in upiList:
        browser.get(i)
        articleText = browser.find_elements_by_tag_name('p')
        for n in articleText:
            try:
                upiText.append(n.text)
                print(n.text)
            except:
                pass
    global upiSearched
    upiSearched = True

### Webscraping Politico ###
def politicoScrape():
    browser.get('https://www.politico.com/')
    politicoHeadlines = browser.find_elements_by_tag_name('a')
    for i in politicoHeadlines:
        try:
            politicoLink = i.get_attribute('href')
            if '/' + currentYear + '/' + currentMonth + '/' + currentDay + '/' in politicoLink:
                politicoList.add(politicoLink)
        except:
            pass
    print(politicoList)
    for i in politicoList:
        browser.get(i)
        articleText = browser.find_elements_by_class_name('story-text__paragraph')
        for n in articleText:
            try:
                politicoText.append(n.text)
                print(n.text)
            except:
                pass
    global politicoSearched
    politicoSearched = True

### Adding scraped data to data.txt ###
def storeData():
    
    #Delete data located in data.txt
    
    file = open("data.txt","r+")
    file.truncate(0)
    file.close()
    
    #Append CNN data

    if cnnSearched:
        file = open("data.txt","a+")
        for i in range(len(cnnText)):
            try:
                file.write(cnnText[i])
            except:
                pass
        file.close()
        
    #Append USAnews data

    if usaSearched:
        file = open("data.txt","a+")
        for i in range(len(usaText)):
            try:
                file.write(usaText[i])
            except:
                pass
        file.close()

    #Append UPI data

    if upiSearched:
        file = open("data.txt","a+")
        for i in range(len(upiText)):
            try:
                file.write(upiText[i])
            except:
                pass
        file.close()

    #Append Politico Data

    if politicoSearched:
        file = open("data.txt", "a+")
        for i in range(len(politicoText)):
            try:
                file.write(politicoText[i])
            except:
                pass
        file.close()



### Main ###

calibrateDate()
upiScrape()
usaScrape()
cnnScrape()
politicoScrape()
storeData()
print('done')

