# https://stackoverflow.com/questions/58733753 how-to-extract-daily-close-from-wsj-using-python

# https://crossbrowsertesting.com/blog/test-automation/automate-login-with-selenium/

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

def wsjLogin():
    browser.get('https://sso.accounts.dowjones.com/login?state=g6Fo2SAtaG9qTmN2djNoSzVlUzQtSlpkZUQ4LTZKTUFhM2FNT6N0aWTZIHVpOGtjdVUtVHpaMngxbVZsNnljcFV1WmdVRWxCc1VHo2NpZNkgNWhzc0VBZE15MG1KVElDbkpOdkM5VFhFdzNWYTdqZk8&client=5hssEAdMy0mJTICnJNvC9TXEw3Va7jfO&protocol=oauth2&scope=openid%20idp_id%20roles%20email%20given_name%20family_name%20djid%20djUsername%20djStatus%20trackid%20tags%20prts%20suuid&response_type=code&redirect_uri=https%3A%2F%2Faccounts.wsj.com%2Fauth%2Fsso%2Flogin&nonce=8ab5cc77-7bbe-4f9b-9d24-1e3dc33de2b1&ui_locales=en-us-x-wsj-83-2&ns=prod%2Faccounts-wsj&savelogin=on#!/signin')
    browser.find_element_by_class_name('username').send_keys('granthale10@gmail.com')
    browser.find_element_by_class_name('password').send_keys('Ferdamodel1')
    browser.find_element_by_class_name('solid-button basic-login-submit').click()



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
    for i in wsjFilteredList:
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

wsjLogin()
calibrateDate()
wsjScrape()
storeData()
print('done')