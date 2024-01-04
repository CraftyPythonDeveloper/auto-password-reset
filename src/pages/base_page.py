import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class BasePage(object):
    def __init__(self):
        self.driver = uc.Chrome()
        self.timeout = 2
        self.sleep_time = 0.5

    def sleep(self, sec=None):
        sec = sec or self.timeout
        time.sleep(sec)
        return True

    def find_link(self, keywords: list, by=By.PARTIAL_LINK_TEXT, check_clickable=True):
        if isinstance(keywords, str):
            keywords = [keywords]

        for keyword in keywords:
            time.sleep(self.sleep_time)
            try:
                elements = self.driver.find_elements(by, keyword)
                for element in elements:
                    if not check_clickable:
                        return element
                    elif self.is_clickable(element):
                        return element
            except:
                pass
        return None

    def is_clickable(self, element):
        try:
            EC.element_to_be_clickable(element)
            return True
        except:
            return False

    def find_in_text(self, keywords: list):
        if isinstance(keywords, str):
            keywords = [keywords]

        xpath = "//*[contains(text(), '{keyword}')]"
        for keyword in keywords:
            time.sleep(self.sleep_time)
            try:
                element = self.driver.find_element(By.XPATH, xpath.format(keyword=keyword))
                if element:
                    return element
            except:
                pass
        return None

    def get_email_by_type(self, type_: str = "email"):
        input_elements = self.driver.find_elements(By.TAG_NAME, "input")
        for element in input_elements:
            try:
                if element.get_attribute("type") == type_:
                    return element
            except:
                pass
        return None
