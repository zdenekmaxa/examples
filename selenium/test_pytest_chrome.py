"""
Basic selenium example starting Chrome browser.

"""

import os

from selenium import webdriver


class TestChrome(object):

    def setup_method(self, method):
        """
        Called before every test case method is called.

        """
        self.current_method = method.__name__
        print "\nCurrent test: %s" % self.current_method
        print "Starting web browser ..."
        op = webdriver.ChromeOptions()
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        # Set environment variable for Chrome.
        # Chrome driver needs to have an environment variable set,
        # this must be set to the path to the webdriver file.
        #os.environ["webdriver.chrome.driver"] = driver
        self.browser = webdriver.Chrome(executable_path="/opt/chromedriver/chromedriver",
                                        chrome_options=op,
                                        desired_capabilities=capabilities)
        self.browser.delete_all_cookies()

    def teardown_method(self, method):
        self.browser.quit()
        self.browser = None
        print "\nBrowser instance destroyed.\n\n"

    def test_get_access(self):
        self.browser.get("http://www.zcu.cz")
        print "Page title is: '%s'" % self.browser.title
