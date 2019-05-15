from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.12306.cn/')
driver.find_element_by_id('train_date')