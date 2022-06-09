from selenium import webdriver
import project.constants as const
from project.Booking_Filtration import BookingFiltration
import time
from project.bookingReport import BookingReport
import csv

class Booking(webdriver.Chrome):
    def __init__(self, teardown=True):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        
    def land_first_page(self):
        self.get(const.URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
        
    def change_currency(self, currency='USD'):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()
        
        
    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)
        
        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()
        
    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()
        
        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()
        
    def select_adults(self, count=1):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()
        
        while True:
            decrease_adult_element = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adult_element.click()
            
            adults_value_element = self.find_element_by_id('group_adults')
            if int(adults_value_element.get_attribute('value')) == 1:
                break
        
        increase_button_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )
        
        for _ in range(count-1):
            increase_button_element.click()
        
    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()
        
    def reserve(self, place, check_in, check_out, adults):
        self.select_place_to_go(place)
        self.select_dates(check_in, check_out)
        self.select_adults(adults)
        self.click_search()
        
    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.sort_price_lowest_first()
        filtration.apply_star_rating(3, 4)
        
    def report_results(self):
        hotel_boxes_list = self.find_elements_by_css_selector('[data-testid="property-card"]')
        
        report = BookingReport(hotel_boxes_list)
        data = report.pull_attributes()
        return data
        
    def export_to_excel(self):
        raw_dict = self.report_results()
        with open('output.csv','w') as output:
            writer = csv.write(output)
            for keys, values in raw_dict.items():
                writer.writerow([keys,values])
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        