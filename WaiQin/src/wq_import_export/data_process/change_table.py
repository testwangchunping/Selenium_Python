import time
from selenium.webdriver.common.by import By
from WaiQin.frame.iframe_skip import iframe_skip


def change_table(mlist, i, driver):

    module_name = mlist[i]
    driver.find_element(By.LINK_TEXT, module_name).click()

    # 重构后模块tab后有iframe切换
    iframe_skip.iframe_enter(driver)
    time.sleep(1)
    return module_name
