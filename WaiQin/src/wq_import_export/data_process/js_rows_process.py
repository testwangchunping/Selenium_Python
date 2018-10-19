import time
from selenium.webdriver.common.by import By


class JsRowsProcess(object):

    def __init__(self, module_list, j, driver):
        self.module_list = module_list
        self.j = j
        self.driver = driver

    # 奇数行数据处理
    change_table_xpath1 = (By.XPATH, '//*[@id="content"]/ul/li[{}]/a')
    change_table_xpath2 = (By.XPATH, '//*[@id="myTab"]/li[{}]/a')
    change_table_xpath3 = (By.XPATH, '//*[@class="content"]/div[1]/a[{}]')

    def js_rows_process(self):
        # 奇数行、非空数据处理
        module_name = self.module_list[self.j]
        try:
            self.driver.find_element(*self.change_table_xpath1.format(self.j + 1)).click()
        except:
            pass
        try:
            self.driver.find_element(*self.change_table_xpath2.format(self.j + 1)).click()
        except:
            pass
        try:
            self.driver.find_element(*self.change_table_xpath3.format(self.j + 1)).click()
        except:
            pass
        time.sleep(1)
        return module_name

    # 重构后模块奇数行后有iframe切换
    def js_rows_process_new(self):

        # 奇数行、非空数据处理
        module_name = self.module_list[self.j]
        try:
            self.driver.find_element(*self.change_table_xpath1.format(self.j + 1)).click()
        except:
            pass
        try:
            self.driver.find_element(*self.change_table_xpath2.format(self.j + 1)).click()
        except:
            pass
        try:
            self.driver.find_element(*self.change_table_xpath3.format(self.j + 1)).click()
        except:
            pass
        try:
            self.driver.switch_to.frame('app_iframe')
        except:
            pass
        time.sleep(1)
        return module_name
