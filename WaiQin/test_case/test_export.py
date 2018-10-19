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
        cls.num = 0

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # cls.logger.realse()

    # def test_old_export(self):
    #     """
    #     旧的模块导出
    #     """
    #     ReadOldExport(self.driver, self.logger).test_old_export()
    #     # 截图
    #     name = sys._getframe().f_code.co_name
    #     num = self.num + 1
    #     print('用例数量' + str(num))
    #     get_window_img(self, self.logger, name, str(num))  # 最后一项为图片第几张
    #
    # def test_new_export(self):
    #     """
    #     重构模块的导出
    #     """
    #     ReadNewExport(self.driver, self.logger).test_new_export()
    #     # 截图
    #     name = sys._getframe().f_code.co_name
    #     num = self.num + 1
    #     print('用例数量' + str(num))
    #     get_window_img(self, self.logger, name, str(num))  # 最后一项为图片第几张

    if __name__ == '__main__':
        unittest.main
