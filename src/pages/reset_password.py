from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from utils.logger import logger


class ResetPasswordPage(BasePage):
    def __init__(self, url, email):
        super(ResetPasswordPage, self).__init__()
        self.url = url
        self.email = email
        self.keywords = ['Forgot my password', 'Forgot password?', 'Reset your password',
                         'remember your password?', 'I forgot my password']

    def reset_password(self):
        self.driver.get(self.url)
        reset_password_element = self.find_link(keywords=self.keywords)
        reset_password_element = reset_password_element or self.find_in_text(keywords=self.keywords)

        if not reset_password_element:
            logger.info("Unable to find the reset password link or text")
            return

        reset_password_element.click()
        self.sleep(2)

        email_element = self.get_email_by_type()

        if not email_element:
            logger.info("Unable to find the email input box..")

        email_element.send_keys(self.email)
        self.sleep(1)
        email_element.send_keys(Keys.ENTER)

        logger.info("Sent password reset link..")

        self.driver.close()


if __name__ == "__main__":
    reset_page = ResetPasswordPage("https://account.leadiq.com/common/", "test@gmail.com")
    reset_page.reset_password()
