from dex_library.functions import Dex

sel = {
    "google search field": 'input[name="q"]',
    "selenium link": 'a[href="https://www.seleniumhq.org/"]',
    "selenium search field": '#q',
    "selenium search submit": '#submit'
}




class DemoPom(object):
    def __init__(self, driver):
        self.driver = driver
    
    def google_search_field(self, keyword):
        elem = Dex(self.driver).find_element(sel['google search field'])
        elem.send_keys(keyword)
    
    def selenium_link(self, click=True):
        elem = Dex(self.driver).find_element(sel['selenium link'])
        if click == True:
            Dex(self.driver).click(elem)
        else:
            return elem
    
    def selenium_search_field(self, keyword='python'):
        elem = Dex(self.driver).find_element(sel['selenium search field'])
        elem.send_keys(keyword)

    
    def selenium_search_submit(self, click=True):
        elem = Dex(self.driver).find_element(sel['selenium search submit'])
        if click == True:
            Dex(self.driver).click(elem)
        else:
            return elem

