import time
from selenium.webdriver.common.by import By


class OsRowsProcess(object):

    def __init__(self, module_list, driver, logger):
        self.module_list = module_list
        self.driver = driver
        self.logger = logger

    # 偶数行数据处理
    # 偶数行后切换iframe
    def os_rows_process(self):
        get_module_name = ''
        try:
            if self.module_list[0] == self.module_list[1]:
                self.driver.find_element(By.LINK_TEXT, self.module_list[0]).click()
                time.sleep(1)
                self.driver.find_elements(By.LINK_TEXT, self.module_list[0])[1].click()
                time.sleep(1)
        except:
            pass
        for name in self.module_list:
            get_module_name = name
            # try:
            self.driver.find_element(By.LINK_TEXT, name).click()
            time.sleep(1)
            # except:
            #     self.logger.warning(get_module_name+'导航栏名称配置错误')
        try:
            self.driver.switch_to.frame('app_iframe')
        except:
            pass
        return get_module_name

    # 重构后的模块偶数行下不需要切换iframe
    def os_rows_process_new(self):
        get_module_name = ''
        try:
            if self.module_list[0] == self.module_list[1]:
                self.driver.find_element(By.LINK_TEXT, self.module_list[0]).click()
                time.sleep(1)
                self.driver.find_elements(By.LINK_TEXT, self.module_list[0])[1].click()
                time.sleep(1)
        except:
            pass
        for name in self.module_list:
            get_module_name = name
            # try:
            self.driver.find_element(By.LINK_TEXT, name).click()
            time.sleep(1)
            # except:
            #     self.logger.warning(get_module_name+'导航栏名称配置错误')
        return get_module_name
