from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://wqtest.xbwq.com.cn/wq/admin/core/login/index')
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element_by_name('company').send_keys('zdh2')
driver.find_element_by_name('account').send_keys('zdh2')
driver.find_element_by_name('pass').send_keys('zdh2')
driver.find_element_by_class_name('login_btn').click()
