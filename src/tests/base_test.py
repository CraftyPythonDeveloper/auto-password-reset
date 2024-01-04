import unittest
import undetected_chromedriver as uc


class BaseTest(unittest.TestCase):
    driver = uc.Chrome()

    def setUp(self):
        self.driver.get("https://google.com")

    def tearDown(self):
        self.driver.close()

