import random

from selenium import webdriver

from test.functions.my_resumption import *

import time

driver = webdriver.Chrome()
driver.get('http://112.13.89.101:9511')

login(driver, '18005740004', '740004')
time.sleep(5)
# 我的履职
driver.find_element_by_xpath("//ul[@class='menuNavigation el-menu--horizontal el-menu']/div[2]").click()
time.sleep(1)
# 代表活动
driver.find_element_by_xpath("//ul[@class='el-menu-vertical-demo parent-menu el-menu']/div[1]").click()
time.sleep(1)
# 新增活动
driver.find_element_by_xpath("//div[@class='topHeadRight']/button").click()
time.sleep(5)
# 届
driver.find_element_by_xpath("//div[@class='el-select']/div[@class='el-input el-input--suffix']").click()
time.sleep(3)

driver.find_element_by_xpath(
    ".//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[@class='el-select-dropdown__item']/span").click()
time.sleep(3)

# 名称
# name = '脚本测试会议' + str(random.randint(1, 10000))
# print(name)
# driver.find_element_by_xpath(
#     "//div[@class='el-form-item is-error is-required']/div[@class='el-form-item__content']/div[@class='el-input']").send_keys(
#     name)

# 履职记录类型


time.sleep(3)
driver.quit()
