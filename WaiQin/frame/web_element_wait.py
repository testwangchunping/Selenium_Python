from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebElementWait(object):

    def __init__(self, driver):
        self.driver = driver

    def web_element_wait(self, time_out, rate, element, error_tips):
        # webdriver显示等待：WebDriverWait
        message = WebDriverWait(self.driver, time_out, rate, None).until(EC.presence_of_element_located((element, self.error_tips)))
        tips = message.text
        return tips