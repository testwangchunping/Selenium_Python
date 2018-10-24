1、目录结构
Selenium_Python
-->WaiQin
   -->frame(通用方法)
   -->Logs（日志）
   -->Report（测试报告）
   -->ScreenShots（测试截图）
   -->src（基本业务）
     -->wq_import_export(外勤导入导出业务)
        -->config(导入导出配置文件)
        -->data（测试服：导入数据+导入导出模块配置）
        -->data_cms（cms：导入数据+导入导出模块配置）
        -->data_process（导入导出模块配置文件的读取）
        -->page_object（页面对象）
        -->service（登陆、导入、导出基本方法）
   -->testcase（测试用例）
   -->Tools（相关工具）
   -->runtest（执行测试用例，生成测试报告）
   
 2、wq_import_export配置文件：
 Selenium_Python->WaiQin->src->wq_import_export->config.ini
 当需要修改需要测试的服务器时，需要在配置文件中修改对应登陆网址、账号信息、导入数据+导入导出模块配置的文件路径；
 当文件的目录结构调整后，也需要修改配置文件中的对应文件相对于当前执行文件的相对路径
 
 3、wq_import_export数据文件读取：
 -->data（测试服：导入数据+导入导出模块配置）
 -->data_cms（cms：导入数据+导入导出模块配置）
 -->data_demo（demo：导入数据+导入导出模块配置）
 -->data_cms3（cms3：导入数据+导入导出模块配置）
 -->data_cms5（cms5：导入数据+导入导出模块配置）
 -->data_cms7（cms7：导入数据+导入导出模块配置）
 -->data_cs（cs：导入数据+导入导出模块配置）
 
 4、导入数据规范+导入导出模块配置规范（data目录下）
 （1）、导入导出模块配置规范
    read_file.xlsx文件，用来配置需要导入和需要导出的模块（read_file2.xlsx用于测试基本流程）。
    文件包含8个sheet：
        new_export：重构后的导出功能+无table项
        new_export1：旧的导出功能+有table项
        old_export：未重构的导出功能+无table项
        old_export1：旧的导出功能+有table项
        new_import：重构后的导入功能+无table项
        new_import1：旧的导入功能+有table项
        old_import：重构的导入功能+无table项
        old_import1：旧的导入功能+有table项
    sheet内配置方法：
        a、无table项：每行按顺序将需要点击的导航栏名称依次填写出来（前两列为导航栏名称的填写，如果导航栏只有一项，第二列可以填写为空）；
        b、有table项：每行按顺序将需要点击的导航栏名称+需要点击的table栏名称依次填写出来。
 （2）、导入数据规范
       文件命名规范：
                  a、无table项+1个文件：最后一个导航栏名称.xls  (例如：员工管理.xls)
                  b、无table项+多个文件：最后一个导航栏名称+当前导入文件序号+.xls (例如：客户管理1.xls,客户管理2.xls)
                  c、有table项+1个文件：当前table项名称.xls  (例如：商品规格设置.xls)
                  d、有table项+多个文件：当前table项名称+当前导入文件序号+.xls (例如：xxxx1.xls,xxxx2.xls)
       文件内容：
                  当前系统导入模板
                  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 