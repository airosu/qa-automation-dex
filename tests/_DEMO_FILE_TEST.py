from selenium import webdriver
from unittest import TestCase
from dex_library.functions import Dex, repeat
from common.functions import DEMO
from POM._DEMO_FILE_POM import DemoPom
import config
import pyautogui
import time


class Test1(TestCase):
    """ DEMO SCENARIO - Search for keyword """
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        Dex(cls.driver).driver_setup(config.SCREEN)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_01_access_main_page(self):
        """ Access main page """

        DEMO(self.driver).homepage()
    

    def test_02_search_for_keyword(self):
        """ Search for 'selenium' keyword """

        DemoPom(self.driver).google_search_field('selenium')
        pyautogui.press('enter')
        


    def test_03_open_link(self):
        """ Open 'selenium' webpage from search results """

        DemoPom(self.driver).selenium_link()

    
    def test_04_search_for_python_keyword(self):
        """ Search for 'python' keyword """

        DemoPom(self.driver).selenium_search_field('python')
        DemoPom(self.driver).selenium_search_submit()
        time.sleep(3)










class Test2(TestCase):
    """ DEMO SCENARIO 2 - No webdriver used """

    def test_01(self):
        """ Step 1 of set """
        pass

    def test_02(self):
        """ Step 2 of set """
        print('Outputted text')
    
    def test_03(self):
        """ Step 3 of set """
        pass
    
    def test_04(self):
        """ Step 4 of set """
        self.fail('This is the reason for failing.')







class TestUsingRepeat(TestCase):
    """ DEMO 3 - Using Repeat Decorator """

    @repeat(5)
    def test_01_the_code_in_this_method_will_be_repeated_5_times(self):
        print('This code was repeated.')

        

