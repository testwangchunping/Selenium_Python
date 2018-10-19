# coding=utf-8
import os
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from WaiQin.frame.screenshoot import get_window_img
from WaiQin.Config.read_config_file import ReadConfigFile
from WaiQin.frame.is_element_exist import IsElementExist


class WqImport(object):
    def __init__(self, driver, logger, module_name):
        self.driver = driver
        self.logger = logger
        self.module_name = module_name

    readConfig = ReadConfigFile()

    # import_module_name,导入文件应该以模块名命名规则
    # 1、奇数列为空，即列表中无table切换，导入文件名为“最后一个link_text导航栏名”；
    # 2、奇数列不为空，即列表中有table切换，导入文件名为“切换的table的名字”）

    iframe_name = 'app_iframe'
    # 导入失败的提示
    error_message = '没有可导入的文件、导入文件名错误、导入失败或请求超时'
    file_path = os.path.abspath('.') + '\\src\\data\\'
    # 导入按钮
    import_text = '导入'

    # 文件上传按钮
    import_file_button1 = (By.ID, 'upload-file')   # xls格式文件
    import_file_button2 = (By.NAME, 'file')    # zip格式文件
    # 确认导入按钮
    confirm_button1 = (By.ID, 'OK-Button')    # xls格式文件
    confirm_button2 = (By.ID, 'save_button')   # zip格式文件
    # 导入成功的提示
    import_success_message = (By.XPATH, '//*[@id="task_body"]/div/div[1]/span[1]')
    # 导入成功后，返回上一级按钮
    import_success_button = (By.XPATH, '//*[@id="task_body"]/div/div[1]/a')
    # 返回上级按钮
    return_button = (By.CLASS_NAME, 'btn_back')

    def test_old_import(self):
        iee = IsElementExist(self.driver)
        if iee.is_element_exist(By.PARTIAL_LINK_TEXT,self.import_text):
            elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT,self.import_text)
            number = len(elements)
            for self.id in range(number):
                time.sleep(2)
                elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT,self.import_text)
                text = elements[self.id].text
                elements[self.id].click()
                time.sleep(2)
                try:
                    self.driver.switch_to.frame(self.iframe_name)
                except:
                    pass
                print(self.file_path)
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
                    # webdriver显示等待：WebDriverWait
                    message = WebDriverWait(self.driver, 60, 3, None).until(
                        EC.presence_of_element_located(self.import_success_message))
                    tips = message.text
                    self.logger.info(self.module_name + '-->' + text + ':' + tips)
                    time.sleep(1)
                    self.driver.find_element(*self.import_success_button).click()
                    time.sleep(1)
                    self.driver.find_element(*self.return_button).click()
                except:
                    # 错误截图
                    name = sys._getframe().f_code.co_name
                    get_window_img(self, self.logger, name, 1)  # 最后一项为图片第几张

                    self.logger.warning(self.module_name + self.error_message)
                    self.driver.get(self.readConfig.f5_url)
        else:
            pass

    def test_new_import(self):
        iee = IsElementExist(self.driver)
        if iee.is_element_exist(By.PARTIAL_LINK_TEXT, self.import_text):
            elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.import_text)
            number = len(elements)
            print(number)
            print(number)
            print(number)

            for self.id in range(number):
                elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.import_text)
                text = elements[self.id].text
                elements[self.id].click()
                time.sleep(2)
                try:
                    self.driver.switch_to.frame(self.iframe_name)
                except:
                    pass
                try:
                    if number == 1:
                        import_file = self.file_path + self.module_name + '.xls'
                    else:
                        import_file = self.file_path + self.module_name + str(self.id + 1) + '.xls'
                    self.driver.find_element(*self.import_file_button1).send_keys(import_file)
                    time.sleep(2)
                    self.driver.find_element(*self.confirm_button1).click()
                    # webdriver 显示等待：WebDriverWait
                    message = WebDriverWait(self.driver, 60, 3, None).until(
                        EC.presence_of_element_located(self.import_success_message))
                    tips = message.text
                    self.logger.info(self.module_name + '-->' + text + ':' + tips)
                    time.sleep(1)
                    self.driver.find_element(*self.import_success_button).click()
                    time.sleep(1)
                    self.driver.find_element(*self.return_button).click()
                except:
                    # 错误截图
                    name = sys._getframe().f_code.co_name
                    get_window_img(self, self.logger, name, 1)  # 最后一项为图片第几张

                    self.logger.warning(self.module_name + self.error_message)
                    self.driver.get(self.readConfig.f5_url)
        else:
            pass
