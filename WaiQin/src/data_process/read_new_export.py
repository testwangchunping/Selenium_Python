#coding=utf-8
import xlrd
from WaiQin.src.data_process.os_rows_process import OsRowsProcess
from WaiQin.Config.read_config_file import ReadConfigFile
from WaiQin.src.data_process.js_rows_process import JsRowsProcess
from WaiQin.src.service.export import Export

class ReadNewExport(object):
    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger
    readConfig=ReadConfigFile()
    def test_new_export(self):
        file_path = './' + 'src/data/read_file2.xlsx'
        sheet_name = 'new_export'
        # 打开excel
        workbook = xlrd.open_workbook(file_path)
        DataSheet = workbook.sheet_by_name(sheet_name)
        # sheet行数
        rowNum = DataSheet.nrows
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
                last_module_name = OsRowsProcess(module_list, self.driver, self.logger).os_rows_process_new()
            elif i % 2 == 1 and module_list:
                # 奇数行、非空数据处理
                for j in range(len(module_list)):
                    get_module_name = JsRowsProcess(module_list, j, self.driver).js_rows_process()
                    # 判断导出照片、导出
                    Export(self.driver,self.logger).new_Export(get_module_name)
            else:
                # 奇数行、空数据处理
                get_module_name = last_module_name
                # 判断导出照片、导出
                Export(self.driver, self.logger).new_Export(get_module_name)
            i = i + 1
            if i % 2 == 0 :
                # 页面刷新到首页
                self.driver.get(self.readConfig.f5_url)
        if i % 2 == 1 and i == count:
            # 处理最后一行为偶数的数据(即页面无table切换)
            Export(self.driver,self.logger).new_Export(last_module_name)
        if i == 0 and i==count:
            # 处理最后一行为偶数（0）的数据(即页面无table切换)
            Export(self.driver,self.logger).new_Export(last_module_name)
