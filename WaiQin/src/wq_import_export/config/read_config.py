import configparser


class ReadConfigFile(object):
    # 登陆
    file_path = './' + 'src/wq_import_export/config/config.ini'
    config = configparser.ConfigParser()

    config.read(file_path, encoding='utf-8-sig')
    browser_Type = config.get('browserType', 'browserName')
    login_url = config.get('testUrl', 'login_url')
    f5_url = config.get('testUrl', 'f5_url')

    U_company = config.get('accountMessage', 'company')
    U_account = config.get('accountMessage', 'account')
    U_password = config.get('accountMessage', 'password')

    # 读取文件目录
    port_data_filepath = config.get('filePath', 'port_data_filepath')

    new_export_sheet = config.get('filePath', 'new_export_sheet')
    new_export_sheet1 = config.get('filePath', 'new_export_sheet1')

    old_export_sheet = config.get('filePath', 'old_export_sheet')
    old_export_sheet1 = config.get('filePath', 'old_export_sheet1')

    new_import_sheet = config.get('filePath', 'new_import_sheet')
    new_import_sheet1 = config.get('filePath', 'new_import_sheet1')

    old_import_sheet = config.get('filePath', 'old_import_sheet')
    old_import_sheet1 = config.get('filePath', 'old_import_sheet1')

    import_data_filepath = config.get('filePath', 'import_data_filepath')
    img_path = config.get('filePath', 'img_path')
    log_path = config.get('filePath', 'log_path')
    report_path = config.get('filePath', 'report_path')
    suites_path = config.get('filePath', 'suites_path')
    chromedriver_path = config.get('filePath', 'chromedriver_path')
    firefoxdriver_path = config.get('filePath', 'firefoxdriver_path')
    iedriver_path = config.get('filePath', 'iedriver_path')
