from dex_library.functions import Dex

sel = {
    "google search field": '',
    "selenium link": 'a[href="https://www.seleniumhq.org/"]',
    "selenium search field": '#q',
    "selenium search submit": '#submit'
}




class DemoPom(object):
    def __init__(self, driver):
        self.driver = driver
    
    def google_search_field(self):
        elem = Dex(self.driver).find_element(sel['google search field'])
        return elem
    
    def selenium_link(self):
        elem = Dex(self.driver).find_element(sel['selenium link'])
        return elem
    
    def selenium_search_field(self):
        elem = Dex(self.driver).find_element(sel['selenium search field'])
        return elem
    
    def selenium_search_submit(self):
        elem = Dex(self.driver).find_element(sel['selenium search submit'])
        return elem

