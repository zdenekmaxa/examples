"""
Selenium based Django test experiments.

"""

import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestSeleniumCases(object):

    def setup_method(self, method):
        pass

    def test_selenium_basic(self):
        """
        Test external resource, run as:
        py.test -vv -rfsX -s cmsapp/tests/selenium_test.py

        """
        browser = webdriver.Firefox()
        print browser.get("https://docs.djangoproject.com/")
        browser.quit()

    def test_selenium_live_server(self, live_server):
        """
        Basic django-pytest-selenium test case.
        Run as: py.test --reuse-db -vv -rfsX -s --liveserver localhost:8080 tests/selenium_tests.py

        No other settings added to settings.py or pytest.ini

        """
        print live_server.url
        browser = webdriver.Firefox()
        url = "https://docs.djangoproject.com/"
        print browser.get(url)
        url = live_server.url + "/datetime/"
        print browser.get(url)
        #print dir(browser)
        browser.quit()

    def test_via_selenium_fixture(self, selenium, live_server):
        """
        Access via pytest selenium fixture:
        Must be run with --driver option:

        py.test --reuse-db -vv -rfsX -s --liveserver localhost:8080 --driver Firefox tests/selenium_tests.py

        """
        url = live_server.url + "/datetime/"
        print selenium.get(url)

    def test_serving_static_content(self, live_server):
        return
        print live_server.url
        browser = webdriver.Firefox()
        # url with static content
        # test actions ...
        browser.quit()