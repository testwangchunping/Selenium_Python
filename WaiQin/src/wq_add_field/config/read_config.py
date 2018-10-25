# coding=utf-8
import os
import configparser


# 读取配置文件
class ReadConfig(object):
    # 获取项目根目录的相对路径
    file_path = '.\\src\\wq_add_field\\config\\config.ini'

    # Python中有一个类ConfigParser支持读ini文件
    config = configparser.ConfigParser()
    config.read(file_path, encoding='utf-8-sig')  # encoding='utf-8-sig'  配置文件中包含中文

    login_ur1 = config.get('testUrl', 'login_ur1')
    company_url1 = config.get('testUrl', 'company_url1')

    Login_Account = config.get('accountMessage', 'account')
    Login_Password = config.get('accountMessage', 'password')

    Company_Message = config.get('companyMessage', 'com_id')
    Fun_Id = config.get('companyMessage', 'fun_id')

    Input_Message = config.get('fieldMessage', 'inputMessage')
    TextareaMessage = config.get('fieldMessage', 'textareaMessage')
    NumberMessage = config.get('fieldMessage', 'numberMessage')
    TelMessage = config.get('fieldMessage', 'telMessage')
    PriceMessage = config.get('fieldMessage', 'priceMessage')
    SelectMessage = config.get('fieldMessage', 'selectMessage')
    Select1Message = config.get('fieldMessage', 'select1Message')
    Select2Message = config.get('fieldMessage', 'select2Message')
    MultiselectMessage = config.get('fieldMessage', 'multiselectMessage')
    MultiselectMessage1 = config.get('fieldMessage', 'multiselectMessage1')
    MultiselectMessage2 = config.get('fieldMessage', 'multiselectMessage2')
    DateMessage = config.get('fieldMessage', 'dateMessage')
    DatetimeMessage = config.get('fieldMessage', 'datetimeMessage')
    Time_rangeMessage = config.get('fieldMessage', 'time_rangeMessage')
    PicMessage = config.get('fieldMessage', 'picMessage')
    Pic_and_textareaMessage = config.get('fieldMessage', 'pic_and_textareaMessage')
    LineMessage = config.get('fieldMessage', 'lineMessage')
    LocationMessage = config.get('fieldMessage', 'locationMessage')
    SpecialselectMessage = config.get('fieldMessage', 'specialselectMessage')
    SpecialmultselectMessage = config.get('fieldMessage', 'specialmultselectMessage')
    keys = config.get('dictType', 'keys')
    Values = config.get('dictType', 'values')
    keys2 = config.get('dictType2', 'keys2')
    Values2 = config.get('dictType2', 'values2')
