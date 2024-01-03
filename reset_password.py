import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys


def is_clickable(element):
    try:
        EC.element_to_be_clickable(element)
        return True
    except:
        return False


def find_reset_link(webdriver: uc.Chrome, keywords: list):
    for keyword in keywords:
        time.sleep(0.5)
        try:
            elements = webdriver.find_elements(By.PARTIAL_LINK_TEXT, keyword)
            for element in elements:
                if is_clickable(element):
                    return element
        except:
            pass

    return None


def find_in_text(webdriver: uc.Chrome, keywords: list):
    xpath = "//*[contains(text(), '{keyword}')]"
    for keyword in keywords:
        time.sleep(0.5)
        try:
            element = webdriver.find_element(By.XPATH, xpath.format(keyword=keyword))
            if element:
                return element
        except:
            pass

    return None


def get_email(webdriver: uc.Chrome, type_: str = "email"):
    input_elements = webdriver.find_elements(By.TAG_NAME, "input")
    for element in input_elements:
        try:
            if element.get_attribute("type") == type_:
                return element
        except:
            pass
    return None


if __name__ == "__main__":
    # getting reset link and email from user.
    url = input("Please enter your website url where reset password is present..\n")
    email = input("Please enter the email to submit for password reset..\n")

    print("Opening chrome..")
    driver = uc.Chrome()
    driver.get(url)

    reset_password_keywords = ['Forgot my password', 'Forgot password?', 'Reset your password',
                               'remember your password?', 'I forgot my password']

    reset_password_element = find_reset_link(webdriver=driver, keywords=reset_password_keywords)
    reset_password_element = reset_password_element or find_in_text(webdriver=driver, keywords=reset_password_keywords)
    import pdb; pdb.set_trace()

    if not reset_password_element:
        input("No password reset link found. press any key to exit..")
        driver.close()
        sys.exit()

    reset_password_element.click()
    time.sleep(2)
    email_element = get_email(driver)

    if not email_element:
        input("Unable to find the email input box.. Press any key to exit..")
        driver.close()
        sys.exit()

    email_element.send_keys(email)
    time.sleep(1)
    email_element.send_keys(Keys.ENTER)

    input("Sent password reset link.. press any key to exit..")
    driver.close()
    sys.exit()
