### WITH MAC CHROMEDRIVER CURRENTLY ###

### Imports ###
import os
from selenium import webdriver
import datetime

### Initializing Variables ###

cnnFilteredList = []
cnnLinkList = []
cnnText = []
usaFilteredList = []
usaLinkList = []
usaText = []
upiFilteredList = []
upiLinkList = []
upiText = []
politicoLinkList = []
politicoFilteredList = []
politicoText = []
cnnSearched = False
usaSearched = False
upiSearched = False
politicoSearched = False

### Finding and setting up chromedriver for webscraping ###
# driver_path = os.path.dirname(os.path.realpath(__file__)) + '\\chromedriver.exe'
    # PC Driver
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
    
def cnnScrape():
    #Goes to CNN US page and gets links from all headlines
    browser.get('https://www.cnn.com/us')
    cnnHeadlines = browser.find_elements_by_tag_name('a')


    #Checks all links for current date and filters for today
    targetStart = 'https://www.cnn.com/' + currentYear + '/' + currentMonth + '/' + currentDay
    for i in range(len(cnnHeadlines)):
        try:
            cnnLink = cnnHeadlines[i].get_attribute('href')
            if cnnLink[:len(targetStart)] == targetStart:
                cnnLinkList.append(cnnLink)
        except:
            pass

    #Remove repeat links
    for i in range(len(cnnLinkList)):
        if cnnLinkList[i] not in cnnFilteredList:
            cnnFilteredList.append(cnnLinkList[i])

    #Print list of links
    print(cnnFilteredList)  

    #Get body paragraph text and add text to cnnText
    for i in range(len(cnnFilteredList)):
        articleText = []
        browser.get(cnnFilteredList[i])
        articleText = browser.find_elements_by_class_name('zn-body__paragraph')
        for i in range(len(articleText)):
            try:
                cnnText.append(articleText[i].text)
                print(articleText[i].text)
            except:
                pass

    #Make it so storeData() stores CNN data
    global cnnSearched
    cnnSearched = True


### Webscraping USAtoday ###

def usaScrape():
    browser.get('https://www.usatoday.com/news/')
    usaHeadlines = browser.find_elements_by_tag_name('a')

    #Puts all links from today into usaLinkList
    target = '/' + currentYear + '/' + currentMonth + '/' + currentDay
    for i in range(len(usaHeadlines)):
        try:
            usaLink = usaHeadlines[i].get_attribute('href')
            if target in usaLink:
                usaLinkList.append(usaLink)
        except:
            pass

    for i in range(len(usaLinkList)):
        if usaLinkList[i] not in usaFilteredList:
            usaFilteredList.append(usaLinkList[i])
    
    print(usaFilteredList)  

    for i in range(len(usaFilteredList)):
        articleText = []
        browser.get(usaFilteredList[i])
        articleText = browser.find_elements_by_class_name('gnt_ar_b_p')
        for i in range(len(articleText)):
            usaText.append(articleText[i].text)
            print(articleText[i].text)
    global usaSearched
    usaSearched = True

    
### Webscraping UPI ###
def upiScrape():
    browser.get('https://www.upi.com/Top_News/US/')
    upiHeadlines = browser.find_elements_by_tag_name('a')

    #Puts all links from today into upiLinkList
    target = '/' + currentYear + '/' + currentMonth + '/' + currentDay
    for i in range(len(upiHeadlines)):
        try:
            upiLink = upiHeadlines[i].get_attribute('href')
            if target in upiLink:
                upiLinkList.append(upiLink)
        except:
            pass

    for i in range(len(upiLinkList)):
        if upiLinkList[i] not in upiFilteredList:
            upiFilteredList.append(upiLinkList[i])
    
    print(upiFilteredList)  

    for i in range(len(upiFilteredList)):
        articleText = []
        browser.get(upiFilteredList[i])
        articleText = browser.find_elements_by_tag_name('p')
        for i in range(len(articleText)):
            try:
                upiText.append(articleText[i].text)
                print(articleText[i].text)
            except:
                pass
    global upiSearched
    upiSearched = True

### Webscraping Politico ###
def politicoScrape():
    browser.get('https://www.politico.com/')
    
    politicoHeadlines = browser.find_elements_by_tag_name('a')

    target = '/' + currentYear + '/' + currentMonth + '/' + currentDay
    
    for i in politicoHeadlines:
        try:
            politicoLink = i.get_attribute('href')
            if target in politicoLink:
                politicoLinkList.append(politicoLink)
        except:
            pass

    for i in politicoLinkList:
        if i not in politicoFilteredList:
            politicoFilteredList.append(i)

    print(politicoFilteredList)

    for i in politicoFilteredList:
        articleText = []
        browser.get(i)
        articleText = browser.find_elements_by_tag_name('p')
        for i in articleText:
            try:
                politicoText.append(i.text)
                print(i.text)
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