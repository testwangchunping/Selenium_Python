import time
from selenium.webdriver.common.by import By
from WaiQin.frame.iframe_skip import iframe_skip
from WaiQin.frame.is_element_exist import IsElementExist


# 偶数行数据处理
# 偶数行后切换iframe
def change_navigate(module_list, driver):
    module_name = ''
    iee = IsElementExist(driver)
    if len(module_list) == 1:
        module_name = module_list[0]
        if iee.is_element_exist(By.LINK_TEXT, module_list[0]):
            driver.find_element(By.LINK_TEXT, module_list[0]).click()
        else:
            print('导航栏'+module_list[0]+'不存在')
    elif module_list[0] == module_list[1]:
        module_name = module_list[0]
        if iee.is_element_exist(By.LINK_TEXT, module_list[0]):
            driver.find_element(By.LINK_TEXT, module_list[0]).click()
            time.sleep(1)
            driver.find_elements(By.LINK_TEXT, module_list[0])[1].click()
            time.sleep(1)
        else:
            print('导航栏' + module_list[0] + '不存在')
    else:
        for name in module_list:
            module_name = name
            if iee.is_element_exist(By.LINK_TEXT, module_name):
                driver.find_element(By.LINK_TEXT, name).click()
                time.sleep(1)
            else:
                print('导航栏' + module_name + '不存在')
    # iframe跳转，重构后的模块偶数行下不需要切换iframe
    iframe_skip.iframe_enter(driver)

    return module_name
