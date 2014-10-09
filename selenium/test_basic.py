"""
Selenium tests example to test application running at
https://xmax-testapp.appspot.com

for py.test, dicovery founds only test_*.py or *_test.py files

"""

import pytest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


APP_URL = "https://xmax-testapp.appspot.com"


class TestBasic(object):
    pass


class TestApp(TestBasic):
    
    def setup_method(self, _):
        # for Chrome ...
        # WebDriverException: Message: 'ChromeDriver executable needs to be
        # available in the path.
        # Please download from
        # http://chromedriver.storage.googleapis.com/index.html
        # and read up at http://code.google.com/p/selenium/wiki/ChromeDriver'
        # cls.browser = webdriver.Chrome()
        # hint:
        #return webdriver.Chrome(executable_path=driver,
        #chrome_options=options)
        self.browser = webdriver.Firefox()

    def teardown_method(self, _):
        self.browser.quit()

    def test_load(self):
        self.browser.get(APP_URL)
        print self.browser.title
        # find the element that's name attribute is x, y (input fields)
        x = self.browser.find_element_by_name("x")
        y = self.browser.find_element_by_name("y")
        # simulates typing into the element
        x.send_keys(30)
        y.send_keys(35)
        x.submit()
        try:
            WebDriverWait(self.browser, 1)
        except Exception as ex:
            print(str(ex))
            pytest.fail()
        r = self.browser.find_element_by_name("result")
        print dir(r)
        print r
        #result = "result: 30 + 35 = 65"
        # pytest.raises(Exception, call, args)

