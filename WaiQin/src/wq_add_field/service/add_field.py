import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class AddField(object):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    btn_sm = (By.CLASS_NAME, 'btn-sm')  # 添加字段按钮
    type = (By.NAME, 'type')  # 字段类型
    field_alias = (By.XPATH, '//*[@id="field_alias"]')  # 字段名
    btn_ok = (By.CLASS_NAME, 'btn_ok')  # 确定按钮
    box_btn_close = (By.CLASS_NAME, 'box_btn_close')  # 关闭

    # 单选、多选
    add_choose_list = (By.ID, 'add_choose_list')  # 新增字段按钮
    input1 = (By.XPATH, '//*[@id="choose_list"]/li[1]/input')  # 选项1
    input2 = (By.XPATH, '//*[@id="choose_list"]/li[2]/input')  # 选项2

    # 多级单选、多级多选
    is_level = (By.NAME, 'is_level')  # 同级选项、多级选项
    add_id = (By.CLASS_NAME, 'add_id')  # 新增字段按钮
    diy_name = (By.ID, 'diy_name')  # 字段名
    layui_layer_btn0 = (By.CLASS_NAME, 'layui-layer-btn0')  # 确定按钮

    def add_common_field(self, field_type, field_name):
        self.driver.find_element(*self.btn_sm).click()
        sel = self.driver.find_element(*self.type)
        Select(sel).select_by_value(field_type)
        self.driver.find_element(*self.field_alias).send_keys(field_name)
        self.driver.find_element(*self.btn_ok).click()
        self.driver.find_element(*self.box_btn_close).click()
        time.sleep(3)

    # 单选、多选
    def add_select_field(self, field_type, field_name1, field_name2, field_name3):
        self.driver.find_element(*self.btn_sm).click()
        sel = self.driver.find_element(*self.type)
        Select(sel).select_by_value(field_type)
        self.driver.find_element(*self.field_alias).send_keys(field_name1)
        self.driver.find_element(*self.add_choose_list).click()
        self.driver.find_element(*self.input1).send_keys(field_name2)
        self.driver.find_element(*self.input2).send_keys(field_name3)
        self.driver.find_element(*self.btn_ok).click()
        self.driver.find_element(*self.box_btn_close).click()
        time.sleep(3)

    # 多级单选、多级多选
    def add_special_select_field(self, field_type, field_name4):
        self.driver.find_element(*self.btn_sm).click()
        sel = self.driver.find_element(*self.type)
        Select(sel).select_by_value(field_type)
        self.driver.find_element(*self.field_alias).send_keys(field_name4)
        self.driver.find_elements(*self.is_level)[1].click()
        lenth = (len(self.config.keys) - 1) // 2
        dkeys = self.config.keys.split('-', lenth)
        dvalues = self.config.Values.split('-', lenth)
        for i in range(len(dkeys)):
            dkey = (int)(dkeys[i])
            dvalue = dvalues[i]
            self.driver.find_elements(*self.add_id)[dkey].click()
            self.driver.find_element(*self.diy_name).send_keys(dvalue)
            self.driver.find_element(*self.layui_layer_btn0).click()
            time.sleep(3)
        self.driver.find_element(*self.btn_ok).click()
        self.driver.find_element(*self.box_btn_close).click()
        time.sleep(3)
