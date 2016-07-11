"""
Basic selenium example starting Firefox browser.
With FF v47, selenium 2.53.6:
    WebDriverException: Message: The browser appears to have exited before we could
    connect. If you specified a log_file in the FirefoxBinary constructor, check it for details.

    Nothing useful in the logs.
    Stopping another instance of FF doesn't make any difference.
"""


from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class TestFirefox(object):

    def setup_method(self, method):
        """
        Called before every test case method is called.

        """
        self.current_method = method.__name__
        print "\nCurrent test: %s" % self.current_method
        print "Starting web browser ..."
        firefox_bin = FirefoxBinary(log_file=open("/tmp/firefoxselenium.log", 'w'))
        self.browser = webdriver.Firefox(firefox_binary=firefox_bin, timeout=60)
        # this is normally enough as well
        #self.browser = webdriver.Firefox()
        self.browser.delete_all_cookies()

    def teardown_method(self, method):
        self.browser.quit()
        self.browser = None
        print "\nBrowser instance destroyed.\n\n"

    def test_get_access(self):
        self.browser.get("http://www.zcu.cz")
        print "Page title is: '%s'" % self.browser.title
