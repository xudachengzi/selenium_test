import time

from selenium import webdriver

# 二次定位 基本思路：先定位select框，再定位select内的选项
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


def test_select(driver, url):
    driver.get(url)
    driver.implicitly_wait(30)
    # 定位select
    mouse = driver.find_element_by_link_text("设置")
    ActionChains(driver).move_to_element(mouse).perform()
    driver.find_element_by_link_text("搜索设置").click()
    # 定位下拉框1
    s = driver.find_element_by_id("nr")
    s.find_element_by_xpath("//option[@value='50']").click()
    # 定位下拉框2 也可以用这种方法来
    driver.find_element_by_id("nr").find_element_by_xpath("//option[@value='50']").click()
    # 定位下拉框3 直接通过Xpath定位
    driver.find_element_by_xpath(".//*[@id='nr']/option[2]").click()
    # 定位下拉框4 Select模块
    y = driver.find_element_by_id('nr')
    Select(y).select_by_index(2)  # 根据index（索引）获取
    Select(y).select_by_value(20)  # 根据value获取
    Select(y).select_by_visible_text("每页显示50条")  # 根据文本获取
    # Select其他功能
    # select_by_index(): 通过索引定位
    # select_by_value(): 通过value值定位
    # select_by_visible_text(): 通过文本值定位
    # deselect_all()          ：取消所有选项
    # deselect_by_index()     ：取消对应index选项
    # deselect_by_value()      ：取消对应value选项
    # deselect_by_visible_text() ：取消对应文本选项
    # first_selected_option()  ：返回第一个选项
    # all_selected_options()   ：返回所有的选项


if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = 'http://www.baidu.com'
    test_select(driver, url)
    time.sleep(2)
    driver.quit()
