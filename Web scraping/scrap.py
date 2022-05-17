from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# chrome_options = Options()
# chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome()
sleep(1)
url = 'https://www.linkedin.com/login'

driver.get(url)
sleep(1)

email_field = driver.find_element_by_id('username')
email_field.send_keys('ducminhcsp@gmail.com')
sleep(1)

password_field = driver.find_element_by_name('session_password')
password_field.send_keys('ndm30122005')
sleep(1)

login_field = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
login_field.click()
sleep(1)

# skip_field = driver.find_element_by_xpath('//*[@id="ember455"]/button')
# if skip_field:
#     skip_field.click()

search_field = driver.find_element_by_xpath('//*[@class="search-global-typeahead__input always-show-placeholder"]')
# search_field.click()
search_field.send_keys('Computer science people')
search_field.send_keys(Keys.RETURN)

# driver.get("https://www.linkedin.com/jobs/")
# sleep(3)
# # find the keywords/location search bars:
# search_bars = driver.find_elements_by_class_name('jobs-search-box__text-input')
# print(search_bars[0])

def GetURL():
    page_source = BeautifulSoup(driver.page_source)
    profiles = page_source.find_all('a', class_ = 'app-aware-link') #('a', class_ = 'search-result__result-link ember-view')
    all_profile_URL = []
    for profile in profiles:
        profile_URL = profile.get('href')
        if profile_URL not in all_profile_URL:
            all_profile_URL.append(profile_URL)
    return all_profile_URL

print(GetURL())












