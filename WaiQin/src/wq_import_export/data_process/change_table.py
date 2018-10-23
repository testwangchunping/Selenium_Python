import time
from selenium.webdriver.common.by import By
from WaiQin.frame.iframe_skip import iframe_skip


def change_table(mlist, i, driver):
    # 奇数行数据处理
    change_table_xpath1 = '//*[@id="content"]/ul/li[{}]/a'
    change_table_xpath2 = '//*[@id="myTab"]/li[{}]/a'
    change_table_xpath3 = '//*[@class="content"]/div[1]/a[{}]'

    module_name = mlist[i]
    try:
        driver.find_element(By.XPATH, change_table_xpath1.format(i + 1)).click()
    except:
        pass
    try:
        driver.find_element(By.XPATH, change_table_xpath2.format(i + 1)).click()
    except:
        pass
    try:
        driver.find_element(By.XPATH, change_table_xpath3.format(i + 1)).click()
    except:
        pass
    # 重构后模块奇数行后有iframe切换
    iframe_skip.iframe_enter(driver)
    time.sleep(1)
    return module_name
