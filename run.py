import requests
from bs4 import BeautifulSoup, SoupStrainer
import datetime

<<<<<<< HEAD
def newScrape():
    file = open("data.txt","r+")
    file.truncate(0)
    file.close()
=======
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
>>>>>>> 7da16a9ac0cc9f51a554b839d482dcf8c7ab6853
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

<<<<<<< HEAD
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
=======
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
    for i in cnnList:
        browser.get(i)
        articleText = browser.find_elements_by_tag_name('p')
        for n in articleText:
            try:
                if "© 2019 Cable News Network. Turner Broadcasting System, Inc. All Rights Reserved." not in n.text and "Listen to CNN (low-bandwidth usage)" not in n.text and "Go to the full CNN experience" not in n.text:
                    cnnText.append(n.text)
                    # print(n.text)
            except:
                pass

    print("Scraped CNN")
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
    for i in usaList:
        browser.get(i)
        articleText = browser.find_elements_by_class_name('gnt_ar_b_p')
        for n in articleText:
            usaText.append(n.text)
            # print(n.text)
    global usaSearched
    usaSearched = True

    print("Scraped USA")
    
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
    for i in upiList:
        browser.get(i)
        articleText = browser.find_elements_by_tag_name('p')
        for n in articleText:
            try:
                upiText.append(n.text)
                # print(n.text)
            except:
                pass
    global upiSearched
    upiSearched = True

    print("Scraped UPI")

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
    for i in politicoList:
        browser.get(i)
        articleText = browser.find_elements_by_class_name('story-text__paragraph')
        for n in articleText:
            try:
                politicoText.append(n.text)
                # print(n.text)
            except:
                pass
    global politicoSearched
    politicoSearched = True
    
    print("Scraped Politico")

# def foxScrape():
#     browser.get('https://www.foxnews.com')
#     foxHeadlines = browser.find_elements_by_tag_name('a')
#     for i in foxHeadlines:
#         try:
#             foxLink = i.get_attribute('href')
#             if '/' + currentYear + '/' + currentMonth + '/' + currentDay in foxLink:
#                 foxList.add(foxLink)
#         except:
#             pass

#     for i in foxList:
#         browser.get(i)
#         n = browser.find_elements_by_tag_name('p')
#         for paragraph in n:
#             try:
#                 foxText.append(n.text)
#                 print(n.text)
#             except:
#                 pass
    
#     global foxSearched
#     foxSearched = True

### Adding scraped data to data.txt ###
def storeData():
    
    #Delete data located in data.txt
    
    file = open("data.txt","r+")
    file.truncate(0)
>>>>>>> 7da16a9ac0cc9f51a554b839d482dcf8c7ab6853
    file.close()
            
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
<<<<<<< HEAD
    file.close()
=======
        file.close()

    # if foxSearched:
    #     file = open("data.text", "a+")
    #     for i in range(len(foxText)):
    #         try:
    #             file.write(foxText[i])
    #         except:
    #             pass
    #     file.close()
>>>>>>> 7da16a9ac0cc9f51a554b839d482dcf8c7ab6853

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
    

#Main

newScrape()
upiScrape()
usaScrape()
politicoScrape()
<<<<<<< HEAD
cnnScrape()
print('done')
=======
# foxScrape()
storeData()
print('\ndone')
>>>>>>> 7da16a9ac0cc9f51a554b839d482dcf8c7ab6853
