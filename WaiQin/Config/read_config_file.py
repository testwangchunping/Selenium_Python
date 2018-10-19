import configparser


class ReadConfigFile(object):
    file_path = './' + 'Config/config.ini'
    config = configparser.ConfigParser()

    config.read(file_path, encoding='utf-8-sig')
    browser_Type = config.get('browserType', 'browserName')
    login_url = config.get('testUrl', 'login_url')
    f5_url = config.get('testUrl', 'f5_url')

    U_company = config.get('accountMessage', 'company')
    U_account = config.get('accountMessage', 'account')
    U_password = config.get('accountMessage', 'password')
