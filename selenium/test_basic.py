"""
Selenium tests example to test application running at
https://xmax-testapp.appspot.com

for py.test, discovery founds only test_*.py or *_test.py files

"""

import os

import pytest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


APP_URL = "https://xmax-testapp.appspot.com"


class TestBasic(object):
    pass


class TestApp(TestBasic):
    
    def setup_method(self, method):
        print "Current working directory: '%s'" % os.getcwd()
        # according to the name of the test (suffix) distinguish
        # which type of browser to instantiate
        if method.__name__.endswith("_chrome"):
            # for Chrome, when run without its driver:
            # WebDriverException: Message: 'ChromeDriver executable needs to be
            # available in the path.
            # Please download from
            # http://chromedriver.storage.googleapis.com/index.html
            # and read up at http://code.google.com/p/selenium/wiki/ChromeDrive

            # if some options, e.g. extensions paths are to be loaded
            op = webdriver.ChromeOptions()
            self.browser = webdriver.Chrome(executable_path="opt/chromedriver/chromedriver",
                                            chrome_options=op)
        else:
            self.browser = webdriver.Firefox()

    def teardown_method(self, _):
        self.browser.quit()

    def _test_sum(self, x_input, y_input, result):
        self.browser.get(APP_URL)
        print self.browser.title
        # find the element that's name attribute is x, y (input fields)
        x = self.browser.find_element_by_name("x")
        y = self.browser.find_element_by_name("y")
        # simulates typing into the element
        x.send_keys(x_input)
        y.send_keys(y_input)
        x.submit()
        try:
            # timeout - Number of seconds before timing out
            timeout = 5
            WebDriverWait(self.browser, timeout)
        except Exception as ex:
            print(str(ex))
            pytest.fail()
        r = self.browser.find_element_by_name("result")
        assert r.text == result

    def test_sum_correct_input_firefox(self):
        self._test_sum(30, 35, "result: 30 + 35 = 65")

    def test_sum_wrong_input_firefox(self):
        self._test_sum(30, "d", "result: 30 + d = error")

    def test_sum_correct_input_chrome(self):
        self._test_sum(30, 35, "result: 30 + 35 = 65")

    def test_sum_wrong_input_chrome(self):
        self._test_sum(30, "d", "result: 30 + d = error")