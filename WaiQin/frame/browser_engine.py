#coding=utf-8
from selenium import webdriver
from WaiQin.Config.read_config_file import ReadConfigFile


class BrowserEngine(object):
    """
    定义一个浏览器引擎类，跟进browser_type的值，控制启动不同的浏览器，主要是IE,Firefox，Chrome
    """
    readConfig= ReadConfigFile()
    driver = None

    def set_driver(self, driver):
        BrowserEngine.driver = driver
        return BrowserEngine.driver
    browser_type = readConfig.browser_Type

    def get_browser(self):
        """
        通过if语句来初始化不同浏览器的启动，默认启动Chrome
        """
        # 全局driver
        if self.browser_type == 'Firefox':
            driver = webdriver.Firefox()
        elif self.browser_type == 'Chrome':
            driver = webdriver.Chrome()
        elif self.browser_type == 'IE':
            driver = webdriver.Ie()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(self.readConfig.login_url)
        return BrowserEngine().set_driver(driver)

















