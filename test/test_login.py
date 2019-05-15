import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://112.13.89.101:9511/')
driver.implicitly_wait(10)
# 输入账号
driver.find_element_by_xpath("//*[@id='account-input']").send_keys("13905740095")
# 输入密码
driver.find_element_by_xpath("//*[@id='password-input']").send_keys("740095")
driver.find_element_by_xpath("//*[@id='login-btn']").click()

# 判断登录是否成功

t = driver.find_element_by_xpath("//div[@class='userinfo-box']/span[2]")

if t == '超级管理员，你好!':
    print('登录成功')
else:
    print('登录失败')

time.sleep(2)
driver.find_element_by_xpath("//span[contains(text(),'退出')]").click()
driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
print('退出成功')
driver.quit()
