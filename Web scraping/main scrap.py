from selenium import webdriver
# have to set up the environment for selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

# Open a chrome tab
driver = webdriver.Chrome()

# put the link into the tab
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

# for any elements want to find, wait
driver.implicitly_wait(3)

# find the element
btn = driver.find_element_by_id('downloadButton')

# interact with the element
btn.click()

# wait until some condition is completed
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        # element filltration
        (By.CLASS_NAME, 'progress-label') ,
        'Complete!'
    )
)




