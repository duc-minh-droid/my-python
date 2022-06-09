
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
    def __init__(self, box_section_selection:WebElement):
        self.box_section_selection = box_section_selection  
        
    def pull_attributes(self):
        titles = []
        price = []
        
        for box in self.box_section_selection:
            for i in box.find_elements_by_css_selector('[data-testid="title"]'):
                titles.append(i.get_attribute('innerHTML').strip())
            for j in box.find_elements_by_class_name('bd73d13072'):
                price.append(j.get_attribute('innerHTML').strip())
                
        collection = []
        for i in titles:
            for j in price:
                collection.append({
                    "place": i,
                    "price": " ".join(j.split("&nbsp;"))
                })
            
        return collection