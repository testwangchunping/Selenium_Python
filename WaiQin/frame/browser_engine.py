#coding=utf-8
import os
from selenium import webdriver
from WaiQin.src.wq_import_export.config.read_config import ReadConfigFile


class BrowserEngine(object):
    """
    定义一个浏览器引擎类，跟进browser_type的值，控制启动不同的浏览器，主要是IE,Firefox，Chrome
    """
    # 读取驱动路径
    readConfig= ReadConfigFile()
    chrome_path = os.path.abspath('.') + readConfig.chromedriver_path
    fire_path = os.path.abspath('.') + readConfig.firefoxdriver_path
    ie_path = os.path.abspath('.') + readConfig.iedriver_path

    driver = None
    #读取打开的浏览器
    browser_type = readConfig.browser_Type

    def set_driver(self, driver):
        BrowserEngine.driver = driver
        return BrowserEngine.driver

    def get_browser(self):
        """
        通过if语句来初始化不同浏览器的启动，默认启动Chrome
        """
        # 全局driver
        if self.browser_type == 'Firefox':
            driver = webdriver.Firefox(self.fire_path)
        elif self.browser_type == 'Chrome':
            driver = webdriver.Chrome(self.chrome_path)
        elif self.browser_type == 'IE':
            driver = webdriver.Ie(self.ie_path)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(self.readConfig.login_url)
        return BrowserEngine().set_driver(driver)

















