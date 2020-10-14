import os
from selenium import webdriver
import datetime

### Finding and setting up chromedriver for webscraping ###
driver_path = os.path.dirname(os.path.realpath(__file__)) + '/chromedriver'
browser = webdriver.Chrome(executable_path = driver_path)

foxList = set()
foxText = []

foxSearched = False


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


def foxScrape():
    browser.get('https://www.foxnews.com')
    foxHeadlines = browser.find_elements_by_tag_name('a')
    for i in foxHeadlines:
        try:
            foxLink = i.get_attribute('href')
            if '/' + currentYear + '/' + currentMonth + '/' + currentDay in foxLink:
                foxList.add(foxLink)
        except:
            pass

    for i in foxList:
        browser.get(i)
        n = browser.find_elements_by_tag_name('p')
        for paragraph in n:
            try:
                foxText.append(n.text)
                print(n.text)
            except:
                pass
    
    global foxSearched
    foxSearched = True


foxScrape()