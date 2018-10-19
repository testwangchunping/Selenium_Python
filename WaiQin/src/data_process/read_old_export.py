#coding=utf-8
import xlrd
from WaiQin.src.data_process.juge_old_export import JugeOldExport
from WaiQin.src.data_process.os_rows_process import OsRowsProcess
from WaiQin.Config.read_config_file import ReadConfigFile
from WaiQin.src.data_process.js_rows_process import JsRowsProcess


class ReadOldExport(object):
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
    readConfig = ReadConfigFile()
    def test_old_export(self):
        file_path = './' + 'src/data/read_file2.xlsx'
        sheet_name = 'old_export'
        # 打开excel
        workbook = xlrd.open_workbook(file_path)
        DataSheet = workbook.sheet_by_name(sheet_name)
        rowNum = DataSheet.nrows #sheet行数
        i = 0
        last_module_name = ''
        count = rowNum
        for i in range(rowNum):
            module = DataSheet.row_values(i)
            while '' in module:
                module.remove('')
            module_list = module
            # 偶数行（通过link_text获取的模块链接）数据处理
            if i % 2 == 0:
                # 偶数行数据处理
                last_module_name = OsRowsProcess(module_list, self.driver, self.logger).os_rows_process()
            elif i % 2 == 1 and module_list:
                # 奇数行、非空数据处理
                for j in range(len(module_list)):
                    get_module_name = JsRowsProcess(module_list, j, self.driver).js_rows_process()
                    # 判断导出照片、导出
                    JugeOldExport(self.driver, self.logger, get_module_name).juge_old_export()
            else:
                # 奇数行、空数据处理
                get_module_name = last_module_name
                # 判断导出照片、导出
                JugeOldExport(self.driver, self.logger, get_module_name).juge_old_export()
            i = i + 1
            if i % 2 == 0:
                    # 页面刷新到首页
                    self.driver.get(self.readConfig.f5_url)
        if i % 2 == 1 and i == count:
            # 处理最后一行为偶数的数据(即页面无table切换)
            JugeOldExport(self.driver, self.logger, last_module_name).juge_old_export()
            # 页面刷新到首页
            self.driver.get(self.readConfig.f5_url)
        if i == 0 and i == count:
            # 处理最后一行为偶数（0）的数据(即页面无table切换)
            JugeOldExport(self.driver, self.logger, last_module_name).juge_old_export()
            # 页面刷新到首页
            self.driver.get(self.readConfig.f5_url)