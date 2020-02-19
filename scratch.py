from selenium import webdriver
from bs4 import BeautifulSoup
import request
import pandas as pd

driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe")

url=[]
title=[]
desc=[]
driver.get("https://www.udemy.com/courses/search/?q=free&p=1&courseLabel=7380")
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
result = soup.find(id='search-result-page-v3')
urlr = result.find_all('div',class_='curriculum-course-card--container--1ZgwU')
descr = result.find_all('div',class_='curriculum-course-card--container--1ZgwU')
titler = result.find_all('div',class_='list-view-course-card--title--2pfA0')
for titler in titler :
    title1 = titler.find('h4')
    title.append(title1.text)
    print('{}\n'.format(title1))
for descr in descr :
    desc1 = descr.find('a')
    desc.append(desc1.text)
    print('{}\n'.format(desc))
for urlr in urlr :
    url1 = urlr.find('a').get('href')
    url2 = 'udemy.com{}'.format(url1)
    url.append(url2)
    print('{}\n'.format(url1))



df = pd.DataFrame({'Title':title,'Uniform Resource Locator':url,'Descriptio':desc})
df.to_csv('udemy.csv', index=False, encoding='utf-8')