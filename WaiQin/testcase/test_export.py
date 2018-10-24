# coding=utf-8
import unittest
import sys
from WaiQin.frame.screenshoot import get_window_img
from WaiQin.src.wq_import_export.data_process.read_new_export import ReadNewExport
from WaiQin.frame.logger import Logger
from WaiQin.src.wq_import_export.data_process.read_old_export import ReadOldExport
from WaiQin.frame.browser_engine import BrowserEngine
from WaiQin.src.wq_import_export.service.login import TestLogin


class TestExport(unittest.TestCase):
    """
    导出用例
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserEngine().get_browser()
        cls.logger = Logger(logger='Export').getlog()
        TestLogin(cls.driver, cls.logger).test_login()
    num = 0

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # cls.logger.realse()

    def test_old_export(self):
        """
        旧的模块导出
        """
        self.logger.info('开始导出--------------old_export')
        ReadOldExport(self.driver, self.logger).test_old_export()
        self.logger.info('结束导出--------------old_export')

        self.logger.info('开始导出--------------old_export1')
        ReadOldExport(self.driver, self.logger).test_old_export1()
        self.logger.info('结束导出--------------old_export1')
        # 截图
        name = sys._getframe().f_code.co_name
        TestExport.num = self.num + 1
        get_window_img(self, self.logger, name, str(TestExport.num))  # 最后一项为图片第几张

    def test_new_export(self):
        """
        重构模块的导出
        """
        self.logger.info('开始导出--------------new_export')
        ReadNewExport(self.driver, self.logger).test_new_export()
        self.logger.info('结束导出--------------new_export')

        self.logger.info('开始导出--------------new_export1')
        ReadNewExport(self.driver, self.logger).test_new_export1()
        self.logger.info('结束导出--------------new_export1')
        # 截图
        name = sys._getframe().f_code.co_name
        TestExport.num = self.num + 1
        get_window_img(self, self.logger, name, str(TestExport.num))  # 最后一项为图片第几张

    if __name__ == '__main__':
        unittest.main
