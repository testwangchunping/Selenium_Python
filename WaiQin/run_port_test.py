# coding=utf-8
import sys

# sys.path.append('H:\\Selenium_Python\\WaiQin')
# sys.path.append('H:\\Selenium_Python\\WaiQin\\Tools\\HTMLTestRunner_PY3')
# sys.path.append('H:\\Selenium_Python\\WaiQin\\src\\wq_import_export\\config')
# sys.path.append('C:\\Windows\\SYSTEM32\\python34.zip')
# sys.path.append('G:\\Python\\DLLs')
# sys.path.append('G:\\Python\\lib')
# sys.path.append('G:\\Python')
# sys.path.append('G:\\Python\\lib\\site-packages')

from WaiQin.src.wq_import_export.config.read_config import ReadConfigFile
import time
import unittest
from WaiQin.Tools.HTMLTestRunner_PY3 import HTMLTestRunner


# print(sys.path)

readConfig = ReadConfigFile()
# 设置报告文件保存路径
report_path = './Report/'
# 设置执行用例路径
suites_path = './testcase'
# 设置报告名
report_name = 'Report.html'
# 设置报告标题
report_title = '项目导入导出测试报告'
# 设置报告副标题
report_descibe = '用例测试情况'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d %H-%m", time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + now + report_name
# 通过open()方法以二进制写模式打开当前目录下的Report.html，如果没有，则自动创建该文件
fp = open(HtmlFile, "wb")

# discover找到指定目录下所有测试模块，并可递归查到子目录下的测试模块，只有匹配到的文件才能被加载
# 跑testsuite包下所有测试用例,在实际脚本开发过程中，最后都采用这个方法来批量管理和执行几百上千的测试用例
suite = unittest.TestLoader().discover(suites_path, pattern='test*.py')

if __name__ == '__main__':
    # 执行用例
    # 初始化一个HTMLTestRunner实例对象，用来生成报告（stream用来指定测试报告文件，title定义测试报告标题，description定义测试报告副标题）
    runner = HTMLTestRunner(stream=fp, title=report_title, description=report_descibe)
    # 开始执行测试套件中所组装的测试用例
    runner.run(suite)
    # 关闭报告文件
    fp.close()
