from selenium import webdriver

driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")

# 通过百度定位百度搜索框，并输入“python”
driver.find_element_by_id('kw').send_keys("python")  # 通过id定位
driver.find_element_by_name('password-input').send_keys("123456")  # 通过name定位
driver.find_element_by_class_name('password-input').send_keys("123456")  # 通过class定位
driver.find_element_by_tag_name('password-input').send_keys("123456")  # 通过tag定位
driver.find_element_by_link_text('password-input').send_keys("123456")  # 通过link定位
driver.find_element_by_partial_link_text('password-input').send_keys("123456")  # 通过partial_link定位

# 若是没有元素的某个属性，比如id，name，class等属性，可以通过xpath或css来定位
driver.find_element_by_xpath('kw').send_keys("123456")  # 通过xpath定位
driver.find_element_by_css_selector('kw').send_keys("123456")  # 通过css定位
