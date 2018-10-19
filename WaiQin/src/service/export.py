# coding=utf-8
import datetime
import time
import sys
from selenium.webdriver.common.by import By
from WaiQin.frame.screenshoot import get_window_img
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from WaiQin.frame.is_element_exist import IsElementExist


class Export(object):
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    # 旧导出
    old_export_id = (By.ID, 'Export')
    old_export_photo_id = (By.ID, 'Export_photo')
    old_export_success_message = '//*[@id="task_body"]/a'
    old_close_export_window = (By.CLASS_NAME, 'btn_ok')
    old_mult_photo_export = (By.CLASS_NAME, 'photo')
    # 新导出
    new_export_id1 = 'async_export'
    # 导出考勤报表弹窗元素
    window_include_message = 'explain'  # 考勤报表导出选择
    # 订单导出
    new_export_id2 = 'btn_order_export'  # 订单导出按钮
    order_radio_choose1 = 'form-radio'
    order_radio_choose2 = (By.XPATH, '//*[@type="radio"]')
    order_click_export = (By.CLASS_NAME, 'btn_ok')  # 导出订单弹窗-确定
    close_order_window = (By.CLASS_NAME, 'btn_cancel')  # 导出订单弹窗-取消
    # 定位轨迹导出
    new_export_id3 = 'btn_expor_track'  # 轨迹导出按钮
    new_export_id31 = (By.ID, 'btn_add_export_task')  # 轨迹导出按钮
    tree_checkbox = 'x-tree-item-checkbox'
    new_export_success_message = '//*[@class="ow_open_cont"]/div/span'  # 导出成功提示
    new_close_export_window = (By.CLASS_NAME, 'confirm')  # 导出成功后，关闭弹窗
    tree_select = (
        By.XPATH, '//*[@id="export_user_dept"]/div/div/div[2]/div/div[2]/div[3]/div/i[2]')  # 轨迹导出，树结构选择，选择第一个部门
    export_error_message = '导出失败或请求超时'
    close_select_window = (By.CLASS_NAME, 'ow_open_close')

    def old_export(self, module_name):
        time.sleep(1)
        elements = self.driver.find_elements(*self.old_export_id)
        number = len(elements)
        for id in range(number):
            text = elements[id].text
            elements[id].click()
            iee = IsElementExist(self.driver)
            if iee.is_element_exist(By.CLASS_NAME, self.window_include_message):
                self.driver.find_element(*self.old_close_export_window).click()
            else:
                pass
            try:
                # webdriver显示等待：WebDriverWait
                message = WebDriverWait(self.driver, 60, 3, None).until(
                    EC.presence_of_element_located((By.XPATH, self.old_export_success_message)))
                tips = message.text
                self.logger.info(module_name + '-->' + text + ':' + tips)
                self.driver.find_element(*self.old_close_export_window).click()
            except:
                self.logger.warning(module_name + '-->' + text + ':' + self.export_error_message)
            time.sleep(1)

    def old_export_photo(self, module_name):
        element = self.driver.find_elements(*self.old_export_photo_id)
        print(element)
        text = element.text
        element.click()
        time.sleep(1)
        try:
            self.driver.find_element(*self.old_mult_photo_export).click()
            self.driver.find_element(*self.old_close_export_window).click()
        except:
            pass
        try:
            # webdriver显示等待：WebDriverWait
            message = WebDriverWait(self.driver, 60, 3, None).until(
                EC.presence_of_element_located((By.XPATH, self.old_export_success_message)))
            tips = message.text
            self.logger.info(module_name + '-->' + text + ':' + tips)
            self.driver.find_element(*self.old_close_export_window).click()
        except:
            self.logger.warning(module_name + '-->' + text + ':' + self.export_error_message)
        time.sleep(1)

    def new_Export(self, module_name):
        iee = IsElementExist(self.driver)
        # 获取模块名
        elements = ''
        if iee.is_element_exist(By.CLASS_NAME, self.new_export_id1):
            elements = self.driver.find_elements(By.CLASS_NAME, self.new_export_id1)
        elif iee.is_element_exist(By.ID, self.new_export_id2):
            elements = self.driver.find_elements(By.ID, self.new_export_id2)
        elif iee.is_element_exist(By.ID, self.new_export_id3):
            elements = self.driver.find_elements(By.ID, self.new_export_id3)
        else:
            pass
        number = len(elements)
        print(number)

        for id in range(number):
            text = elements[id].text
            elements[id].click()
            # 订单导出
            if iee.is_element_exist(By.CLASS_NAME, self.order_radio_choose1):
                for i in self.driver.find_elements(*self.order_radio_choose2):
                    i.click()
                    self.driver.find_element(*self.order_click_export).click()
                    try:
                        # webdriver显示等待：WebDriverWait
                        message = WebDriverWait(self.driver, 60, 3, None).until(
                            EC.presence_of_element_located((By.XPATH, self.new_export_success_message)))
                        tips = message.text
                        self.logger.info(module_name + '-->' + text + ':' + tips)
                        self.driver.find_element(*self.new_close_export_window).click()
                    except:
                        self.logger.warning(module_name + '-->' + text + self.export_error_message)
                self.driver.find_element(*self.close_order_window).click()
            # 定位轨迹导出
            elif iee.is_element_exist(By.CLASS_NAME, self.tree_checkbox):
                time.sleep(2)
                self.driver.find_element(*self.tree_select).click()
                t_max = datetime.datetime.now()
                t_min = t_max - datetime.timedelta(days=2)
                max_time = datetime.datetime.strftime(t_max, '%Y-%m-%d')
                min_time = datetime.datetime.strftime(t_min, '%Y-%m-%d')
                self.driver.find_element(By.ID, 'min_time').send_keys(min_time)
                self.driver.find_element(By.ID, 'max_time').send_keys(max_time)
                self.driver.find_element(*self.new_export_id31).click()
                try:
                    # webdriver显示等待：WebDriverWait
                    message = WebDriverWait(self.driver, 60, 3, None).until(
                        EC.presence_of_element_located((By.XPATH, self.new_export_success_message)))
                    tips = message.text
                    self.logger.info(module_name + '-->' + text + ':' + tips)
                    self.driver.find_element(*self.new_close_export_window).click()
                    self.driver.find_element(*self.close_select_window).click()
                except:
                    self.logger.warning(module_name + '-->' + text + self.export_error_message)

            # 其他普通导出
            else:
                try:
                    # webdriver显示等待：WebDriverWait
                    message = WebDriverWait(self.driver, 60, 3, None).until(
                        EC.presence_of_element_located((By.XPATH, self.new_export_success_message)))
                    tips = message.text
                    self.logger.info(module_name + '-->' + text + ':' + tips)
                    self.driver.find_element(*self.new_close_export_window).click()
                except:
                    self.logger.warning(module_name + '-->' + text + self.export_error_message)
