import random
import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys(u'测试部落')
time.sleep(2)
driver.find_element_by_id("kw").submit()  # submit() 表示点击回车键
s = driver.find_elements_by_css_selector("h3.t>a")  # s是一个列表

# 获取包含该测试内容中所有条数的的href
for i in s:
    print(i.get_attribute("href"))

# 随机获取一个结果url
t = random.randint(0, 9)
a = s[t].get_attribute("href")

# 跳转该url
driver.get(a)

# 跳转随机url
s[t].click()

driver.quit()
