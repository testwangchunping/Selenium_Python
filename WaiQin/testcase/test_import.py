# coding=utf-8
import unittest
import sys
from WaiQin.src.wq_import_export.data_process.read_new_import import ReadNewImport
from WaiQin.frame.logger import Logger
from WaiQin.frame.screenshoot import get_window_img
from WaiQin.src.wq_import_export.data_process.read_old_import import ReadOldImport
from WaiQin.frame.browser_engine import BrowserEngine
from WaiQin.src.wq_import_export.service.login import TestLogin


class TestImport(unittest.TestCase):
    """
    导入用例
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserEngine().get_browser()
        cls.logger = Logger(logger='Import').getlog()
        TestLogin(cls.driver, cls.logger).test_login()

    num = 0

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # cls.logger.realse()

    def test_old_import(self):
        """
        未重构模块导入
         """

        self.logger.info('开始导入--------------old_import')
        ReadOldImport(self.driver, self.logger).read_old_import()
        self.logger.info('结束导入--------------old_import')

        self.logger.info('开始导入--------------old_import1')
        ReadOldImport(self.driver, self.logger).read_old_import1()
        self.logger.info('结束导入--------------old_import1')

        # 截图
        name = sys._getframe().f_code.co_name
        TestImport.num = self.num + 1
        get_window_img(self, self.logger, name, str(TestImport.num))  # 最后一项为图片第几张

    def test_new_import(self):
        """
        重构模块导入
        """
        self.logger.info('开始导入--------------new_import')
        ReadNewImport(self.driver, self.logger).read_new_import()
        self.logger.info('结束导入--------------new_import')

        self.logger.info('开始导入--------------new_import1')
        ReadNewImport(self.driver, self.logger).read_new_import1()
        self.logger.info('结束导入--------------new_import1')

        # 截图
        name = sys._getframe().f_code.co_name
        TestImport.num = self.num + 1
        get_window_img(self, self.logger, name, str(TestImport.num))  # 最后一项为图片第几张

    if __name__ == '__main__':
        unittest.main
