# coding=utf-8
import os
import time
from selenium.webdriver.common.by import By
from WaiQin.src.wq_import_export.config.read_config import ReadConfigFile
from WaiQin.frame.iframe_skip import iframe_skip
from WaiQin.frame.is_element_exist import IsElementExist
from WaiQin.frame.webElementWait import webElementWait
from WaiQin.frame.go_homepage import go_Homepage


class WqImport(object):
    def __init__(self, driver, logger, module_name):
        self.driver = driver
        self.logger = logger
        self.module_name = module_name

    # import_module_name,导入文件应该以模块名命名规则
    # 1、奇数列为空，即列表中无table切换，导入文件名为“最后一个link_text导航栏名”；
    # 2、奇数列不为空，即列表中有table切换，导入文件名为“切换的table的名字”）

    # 导入失败的提示
    error_message = '没有可导入的文件、导入文件名错误、导入失败或请求超时'
    readConfig = ReadConfigFile()
    file_path = os.path.abspath('.') + readConfig.import_data_filepath
    # 导入按钮
    import_text = '导入'

    # 文件上传按钮
    import_file_button1 = (By.ID, 'upload-file')  # xls格式文件
    import_file_button2 = (By.NAME, 'file')  # zip格式文件
    # 确认导入按钮
    confirm_button1 = (By.ID, 'OK-Button')  # xls格式文件
    confirm_button2 = (By.ID, 'save_button')  # zip格式文件
    # 导入成功的提示
    import_success_message = '//*[@id="task_body"]/div/div[1]/span[1]'
    # 导入成功后，返回上一级按钮
    import_success_button = (By.XPATH, '//*[@id="task_body"]/div/div[1]/a')
    # 返回上级按钮
    return_button = (By.CLASS_NAME, 'btn_back')

    def test_old_import(self):
        iee = IsElementExist(self.driver)
        if iee.is_element_exist(By.PARTIAL_LINK_TEXT, self.import_text):
            elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.import_text)
            number = len(elements)
            for self.id in range(number):
                time.sleep(2)
                elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.import_text)
                text = elements[self.id].text
                elements[self.id].click()
                time.sleep(2)

                # iframe跳转
                iframe_skip.iframe_enter(self.driver)

                try:
                    if number == 1:
                        import_file = self.file_path + self.module_name + '.xls'
                    else:
                        import_file = self.file_path + self.module_name + str(self.id + 1) + '.xls'
                    self.driver.find_element(*self.import_file_button1).send_keys(import_file)
                    time.sleep(2)
                    self.driver.find_element(*self.confirm_button1).click()
                except:
                    pass
                try:
                    if number == 1:
                        import_file = self.file_path + self.module_name + '.zip'
                    else:
                        import_file = self.file_path + self.module_name + str(self.id + 1) + '.zip'
                    self.driver.find_element(*self.import_file_button2).send_keys(import_file)
                    time.sleep(2)
                    self.driver.find_element(*self.confirm_button2).click()
                except:
                    pass
                try:
                    # webdriver显示等待：webElementWait
                    tips = webElementWait(self.driver, By.XPATH, self.import_success_message)

                    self.logger.info(self.module_name + '-->' + text + ':' + tips)
                    time.sleep(1)
                    self.driver.find_element(*self.import_success_button).click()
                    time.sleep(1)
                    self.driver.find_element(*self.return_button).click()
                except:
                    self.logger.warning(self.module_name + self.error_message)
                    # 页面刷新到首页
                    go_Homepage(self.driver)
        else:
            pass

    def test_new_import(self):
        iee = IsElementExist(self.driver)
        if iee.is_element_exist(By.PARTIAL_LINK_TEXT, self.import_text):
            elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.import_text)
            number = len(elements)
            for self.id in range(number):
                elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.import_text)
                text = elements[self.id].text
                elements[self.id].click()
                time.sleep(2)

                # iframe跳转
                iframe_skip.iframe_enter(self.driver)

                try:
                    if number == 1:
                        import_file = self.file_path + self.module_name + '.xls'
                    else:
                        import_file = self.file_path + self.module_name + str(self.id + 1) + '.xls'
                    self.driver.find_element(*self.import_file_button1).send_keys(import_file)
                    time.sleep(2)
                    self.driver.find_element(*self.confirm_button1).click()

                    # webdriver 显示等待：webElementWait
                    tips = webElementWait(self.driver, By.XPATH, self.import_success_message)

                    self.logger.info(self.module_name + '-->' + text + ':' + tips)
                    time.sleep(1)
                    self.driver.find_element(*self.import_success_button).click()
                    time.sleep(1)
                    self.driver.find_element(*self.return_button).click()
                except:
                    self.logger.warning(self.module_name + self.error_message)
            #页面刷新到首页
            go_Homepage(self.driver)
        else:
            pass
