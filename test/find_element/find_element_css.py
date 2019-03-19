from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

# CSS属性定位
# id以“#”表示，class以“.”表示，其他直接用标签名表示
driver.find_element_by_css_selector("#kw").send_keys("python")
driver.find_element_by_css_selector(".s_ipt").send_keys("python")
driver.find_element_by_css_selector("input").send_keys("python")

# 其他属性
# name、autocomplete、type等属性
driver.find_element_by_css_selector("[name='wd']").send_keys('python')
driver.find_element_by_css_selector("[autocomplete='of']").send_keys('python')
driver.find_element_by_css_selector("[type='text']").send_keys('python')

# 标签
driver.find_element_by_css_selector("input：contains('kw')").send_keys('python')
# 标签与class属性、id属性、其他属性组合定位
driver.find_element_by_css_selector("input.s_upt").send_keys('python')
driver.find_element_by_css_selector("input#kw").send_keys('python')
driver.find_element_by_css_selector("input[id='kw']").send_keys('python')

# 层级关系
driver.find_element_by_css_selector("form#from>span>input").send_keys('python')
driver.find_element_by_css_selector("form.fm>span>input").send_keys('python')

# 索引
driver.find_element_by_css_selector("select#nr>option:nth-child(1)").click()
driver.find_element_by_css_selector("select#nr>option:nth-child(2)").click()

# 逻辑运算
driver.find_element_by_css_selector("input[id='kw'][name='wd]]").send_keys('python')


