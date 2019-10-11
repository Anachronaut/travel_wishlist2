import selenium
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_title_shown_on_home_page(self):
        self.selenium.get(self.live_server_url)
        assert 'Travel Wishlist' in self.selenium.title

class AddEditPlacesTests(LiveServerTestCase):

    fixtures = ['test_places']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_add_new_place(self):
        self.selenium.get(self.live_server_url) #Load home page
        input_name = self.selenium.find_element_by_id('id_name') #find input text box. id was generated by Django forms
        input_name.send_keys('Denver') #Enter place name
        add_button = self.selenium.find_element_by_id('add-new-place') #find the add button
        add_button.click() #click add button

        #Wait for new element to appear on page
        wait_for_denver = self.selenium.find_element_by_id('place-name-5')

        #Assert places from test_places are on page
        assert 'Tokyo' in self.selenium.page_source
        assert 'New York' in self.selenium.page_source

        #And the new place
        assert 'Denver' in self.selenium.page_source
