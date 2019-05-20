import config

class DEMO(object):
    def __init__(self, driver):
        self.driver = driver
    
    def homepage(self, sub_url=''):
        self.driver.get(config.URL[config.ENVIRONMENT] + sub_url)

    