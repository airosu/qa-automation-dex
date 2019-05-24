import config
import platform
import random
import string
import time
import requests
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException, WebDriverException
from selenium.webdriver.common.keys import Keys


class Dex(object):
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def random_email():
        step = random.randint(9, 14)
        list1 = []
        for _ in range(0, step):
            x = random.choice(string.ascii_lowercase + string.digits)
            list1.append(x)
        list_string = ''.join(map(str, list1))
        d1 = random.choice(['@gmail', '@yahoo', '@outlook', '@aol', '@fakemail', '@mail', '@test2', '@test3', '@test'])
        d2 = random.choice(['.com', '.org', '.ro', '.es', '.it', '.ru', '.net', '.pt', '.uk', '.de', '.pl', '.gg'])
        return "QA_" + list_string + d1 + d2

    @staticmethod
    def random_name():
        list1 = []
        for _ in range(0, 7):
            x = random.choice(string.ascii_uppercase + string.digits)
            list1.append(x)
        list_string = ''.join(map(str, list1))
        return 'QA_' + list_string
    

    @staticmethod
    def url_split(url: str, steps: int):
        final_list = []
        try:
            for i in range(1, steps + 1):
                url_section0 = url.split('/')[-i]
                url_section = '/' + url_section0
                final_list.insert(0, url_section)
            final_string = ''.join(map(str, final_list))
            return final_string
        except IndexError:
            print('url_split -> IndexError: List index out of range')
            raise



    def driver_setup(self, screens=1):
        if screens == 2:
            self.driver.set_window_position(-1920, 80)
        #self.driver.set_window_size(1800, 500)
        self.driver.maximize_window()
        pass


    def response_json(self, url, write=False, filename="data_file"):
        # test_URL = "https://jsonplaceholder.typicode.com/photos/5000"
        response = requests.get(url)
        data = response.json()
        data_string = (json.dumps(data, indent=4))
        if write == True:
            with open(filename + ".json", "w") as write_file:
                json.dump(data, write_file, indent=4)
        return data_string


    def dataLayer(self):
        data_layer = self.driver.execute_script(''' return dataLayer; ''')
        return data_layer


    def click(self, elem):
        try:
            elem.click()
        except (WebDriverException, NoSuchElementException) as _:
            time.sleep(1)
            ActionChains(self.driver).move_to_element(elem).perform()
            try:
                elem.click()
            except (WebDriverException, NoSuchElementException) as _:
                time.sleep(1)
                self.driver.execute_script("arguments[0].scrollIntoView();", elem)
                self.driver.execute_script("scrollBy(0, -74);")
                try:
                    elem.click()
                except (WebDriverException, NoSuchElementException) as _:
                    time.sleep(1)
                    self.driver.execute_script('arguments[0].click();', elem)
                    # print('DEBUG: arguments[0].click() was executed.')




    def find_element(self, sel):
        a01 = (sel[0] + sel[1])
        if a01 in ('//', '(/', '(('):
            elem = self.driver.find_element(By.XPATH, sel)
        else:
            elem = self.driver.find_element(By.CSS_SELECTOR, sel)
        return elem
    
    def find_multiple_elements(self, sel):
        a01 = (sel[0] + sel[1])
        if a01 in ('//', '(/', '(('):
            elem = self.driver.find_elements(By.XPATH, sel)
        else:
            elem = self.driver.find_elements(By.CSS_SELECTOR, sel)
        return elem



    def wait_for_present(self, selector, time=30):
        a01 = (selector[0] + selector[1])
        if a01 in ('//', '(/', '(('):
            try:
                element_present = EC.presence_of_all_elements_located((By.XPATH, selector))
                WebDriverWait(self.driver, time).until(element_present)
            except TimeoutException:
                print('Timed out waiting for XPATH Selector: "' + selector + '" to become present.')
                print('')
                raise
        else:
            try:
                element_present = EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
                WebDriverWait(self.driver, time).until(element_present)
            except TimeoutException:
                print('Timed out waiting for CSS Selector: "' + selector + '" to become present.')
                print('')
                raise
    


    def wait_for_visible(self, selector, time=30):
        a01 = (selector[0] + selector[1])
        if a01 in ('//', '(/', '(('):
            try:
                element_visible = EC.visibility_of_all_elements_located((By.XPATH, selector))
                WebDriverWait(self.driver, time).until(element_visible)
            except TimeoutException:
                print('Timed out waiting for XPATH Selector: "' + selector + '" to become present.')
                print('')
                raise
        else:
            try:
                element_visible = EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector))
                WebDriverWait(self.driver, time).until(element_visible)
            except TimeoutException:
                print('Timed out waiting for CSS Selector: "' + selector + '" to become present.')
                print('')
                raise
    
    def wait_for_clickable(self, selector, time=30):
        a01 = (selector[0] + selector[1])
        if a01 in ('//', '(/', '(('):
            try:
                element_clickable = EC.element_to_be_clickable((By.XPATH, selector))
                EC.visibility_of_all_elements_located
                WebDriverWait(self.driver, time).until(element_clickable)
            except TimeoutException:
                print('Timed out waiting for XPATH Selector: "' + selector + '" to become present.')
                print('')
                raise
        else:
            try:
                element_clickable = EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                WebDriverWait(self.driver, time).until(element_clickable)
            except TimeoutException:
                print('Timed out waiting for CSS Selector: "' + selector + '" to become present.')
                print('')
                raise

    def switch_to_tab(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])
    
    def close_current_tab(self):
        self.driver.close()

    def open_in_new_tab(self, link):
        actions = ActionChains(self.driver)
        if platform.system() == 'Windows':
            actions.key_down(Keys.CONTROL)
        elif platform.system() == 'Darwin':
            actions.key_down(Keys.COMMAND)
        actions.move_to_element(link)
        actions.click()
        if platform.system() == 'Windows':
            actions.key_up(Keys.CONTROL)
        elif platform.system() == 'Darwin':
            actions.key_up(Keys.COMMAND)
        actions.perform()

        self.switch_to_tab(1)





""" JavaScript commands """
class JS(object):
    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        self.driver.execute_script('arguments[0].click();', element)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll(self):
        self.driver.execute_script("scrollBy(0, -74);")

    def scroll_by(self, x=0, y=-74):
        self.driver.execute_script("scrollBy(" + str(x) + "," + str(y) + ");")
    
    def scroll_to(self, x=0, y=0):
        self.driver.execute_script("window.scrollTo(" + x + ", " + y + ")")






""" Decorators used to repeat a function X times (use @repeat(X) just before declaring the function) """
def repeat(times):
    def repeatHelper(f):
        def callHelper(*args):
            for _ in range(0, times):
                f(*args)
        return callHelper
    return repeatHelper


""" Similar behavior to 'repeat' """
def retry(howmany):
    def tryIt(func):
        def f():
            attempts = 0
            while attempts < howmany:
                try:
                    return func()
                except:
                    attempts += 1
        return f
    return tryIt
