from webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from twilio.rest import Client
from getLoginCode import getCode
import util


import time
import random
import time


class Bot:

    def __init__(self, start_page_url):
        self.webdriver = WebDriver()
        self.start_page_url = start_page_url

    def go_to_start_page(self):
        self.webdriver.open_url(self.start_page_url)

    def login(self):
        settings = util.get_settings()
        emailCreds = settings['emailCredentials']
        email = str(emailCreds["email"].strip())
        print(email)

        print('clicking login')

        item = self.webdriver.find_element_by_visible_text('Inloggen')
        self.webdriver.click_on_element(item)
        self.select_item_by_x_path("//input[@id='email']")
        emailField = self.webdriver.find_element_by_x_path(
            "//input[@id='email']")
        self.webdriver.click_on_element(emailField)
        self.webdriver.fill_in_input_field(
            "//input[@id='email']", email)
        self.select_item_by_x_path("//button[@type='submit']")
        time.sleep(5)
        print(getCode())
        self.webdriver.fill_in_input_field(
            "//input[@id='one-time-code-input-1']", getCode())
        self.select_item_by_x_path("//button[@class='css-117ynj1 e1dvqv261']")
        time.sleep(2)

    def refresh(self):
        self.webdriver.refresh()

    def go_to_festival_page(self, festival_name):

        self.webdriver.fill_in_input_field("/html/body/div[1]/div[1]/section/div[2]/div/div/div[1]/label/div[2]/input",
                                           festival_name)
        time.sleep(1)

    def quit(self):
        self.webdriver.quit()

    def is_on_start_page(self):
        return self.webdriver.get_current_url() == self.start_page_url

    def select_item(self, item_name):
        item = self.webdriver.find_element_by_x_path(
            f'//*[text()="{item_name}"]')
        return self.webdriver.click_on_element(item)

    def select_item_by_x_path(self, item_x_path):
        item = self.webdriver.find_element_by_x_path(item_x_path)
        return self.webdriver.click_on_element(item)

    def go_to_ticket_page(self, otherCategory, ticketName):
        if otherCategory == "":
            self.select_item_by_x_path(f'//*[text()="{ticketName}"]')
        else:
            self.select_item(otherCategory)
            time.sleep(1)
            self.select_item_by_x_path(f'//*[text()="{ticketName}"]')

    def find_available(self):
        try:
            self.webdriver.driver.find_element(
                By.XPATH, '//*[text()="Er worden op dit moment geen tickets aangeboden."]')

        except NoSuchElementException:
            return True
        return False

    def refresher(self):
        random_decimal = random.randint(40000, 80000) / 10000
        time.sleep(random_decimal)
        self.refresh()

    def reserve_ticket(self):
        self.select_item_by_x_path("/html/body/div[1]/div[2]/div[3]/a[1]")
        time.sleep(0.355)
        self.select_item_by_x_path('//*[text()="Koop ticket"]')

    def dial_number(self, twilioNumber, number, sid, token):
        TWIML_INSTRUCTIONS_URL = \
            "https://static.fullstackpython.com/phone-calls-python.xml"
        client = Client(sid, token)

        client.calls.create(to=number, from_=twilioNumber,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")
