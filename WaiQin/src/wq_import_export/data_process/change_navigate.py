import time
from selenium.webdriver.common.by import By
from WaiQin.frame.iframe_skip import iframe_skip


# 偶数行数据处理
# 偶数行后切换iframe
def change_navigate(module_list, driver):
    module_name = ''
    if len(module_list) == 1:
        module_name = module_list[0]
        print(module_name)
        driver.find_element(By.LINK_TEXT, module_list[0]).click()
    elif module_list[0] == module_list[1]:
        module_name = module_list[0]
        print(module_name)
        driver.find_element(By.LINK_TEXT, module_list[0]).click()
        time.sleep(1)
        driver.find_elements(By.LINK_TEXT, module_list[0])[1].click()
        time.sleep(1)
    else:
        for name in module_list:
            module_name = name
            driver.find_element(By.LINK_TEXT, name).click()
            time.sleep(1)
    # iframe跳转，重构后的模块偶数行下不需要切换iframe
    iframe_skip.iframe_enter(driver)

    return module_name
