from selenium import webdriver
import requests
from bs4 import BeautifulSoup

url = 'http://instagram.com/umnpics/'
driver = webdriver.Firefox(executable_path=r'C:\Users\DELL\Downloads\geckodriver.exe')
driver.get(url)

soup = BeautifulSoup(driver.page_source,'html.parser')
# print(soup)

for x in soup.findAll('li', {'class':'photo'}):
    print(x)








