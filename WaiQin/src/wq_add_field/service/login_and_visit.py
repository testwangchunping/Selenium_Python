from WaiQin.src.wq_add_field.config.read_config import ReadConfig
from selenium.webdriver.common.by import By
from WaiQin.frame.switch_handle import SwitchHandle


class LoginAndVisit(object):
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    config = ReadConfig()
    account = (By.ID, 'LoginForm_account')
    password = (By.ID, 'LoginForm_pwd')
    ok = (By.CLASS_NAME, 'btn')
    company_list = (By.LINK_TEXT, '企业列表')
    change_to_url = (By.XPATH, '//*[@id="nestable"]/div/ol/li[1]/div/div')

    def login_and_visit(self):
        # 登陆
        self.driver.get(self.config.login_ur1)
        self.driver.find_element(*self.account).send_keys(self.config.Login_Account)
        self.driver.find_element(*self.password).send_keys(self.config.Login_Password)
        self.driver.find_element(*self.ok).click()

        # 进入企业列表
        self.driver.find_element(*self.company_list).click()
        self.logger.debug('进入企业列表')

        # 进入对应公司的模块/文案设置页面
        self.driver.get(self.config.company_url1 + self.config.Company_Message + '&is_exp=0')
        self.logger.debug('进入公司模块设置页面')

        # 点击第一个模块字段设置页面(列表第一个模块，必须要有模块设置按钮)
        self.driver.find_element(*self.change_to_url).click()
        self.logger.debug('先进入一个模块的字段设置页面')

        # 页面句柄切换
        SwitchHandle(self.driver, self.logger).switch_handle()
