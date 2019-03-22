import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys


# 点击（鼠标左键）页面按钮   clink()
# 清空输入框     clear()
# 输入字符串     send_keys()


def test_mouse(driver):
    driver.get("http://www.hordehome.com")
    driver.implicitly_wait(10)
    driver.find_element_by_id("search-button").click()
    driver.find_element_by_id("search-term").clear()
    driver.find_element_by_id("search-term").send_keys("selenium")


# submit提交表单
def test_submit(driver):
    driver.get("http://www.baidu.com")
    driver.implicitly_wait(10)
    driver.find_element_by_id("kw").send_keys(u'测试部落')
    driver.find_element_by_id("kw").submit()  # submit()模拟enter键提交表单


#  键盘操作       需要导入Keys
def test_keyboard(driver):
    driver.get("http://www.hordehome.com")
    driver.implicitly_wait(10)
    driver.find_element_by_id("search-button").click()
    driver.find_element_by_id("search-term").clear()
    driver.find_element_by_id("search-term").send_keys("selenium")
    # 模拟键盘enter键做回车操作
    driver.find_element_by_id("search-term").send_keys(Keys.ENTER)
    # 常见的键盘操作：
    # F1-F12 send_keys(Keys.F1)
    # 复制Ctrl+C  send_keys(Keys.CONTROL,'c')
    # 粘贴Ctrl+V  send_keys(Keys.CONTROL,'v')
    # 全选Ctrl+A  send_keys(Keys.CONTROL,'a')
    # 剪切Ctrl+X  send_keys(Keys.CONTROL,'x')
    # 制表键Tab   send_keys(Keys.TAB)


# 鼠标悬停事件    需要导入ActionChains
def test_actionchains(driver):
    driver.get("http://www.baidu.com")
    driver.implicitly_wait(10)
    mouse = driver.find_element_by_link_text("设置")
    # ActionChains(driver).move_to_element(mouse).perform()  # 鼠标悬停
    ActionChains(driver).move_to_element(mouse).context_click()  # 右击鼠标
    ActionChains(driver).move_to_element(mouse).double_click()  # 双击鼠标


if __name__ == '__main__':
    driver = webdriver.Chrome()
    test_mouse(driver)
    test_submit(driver)
    test_keyboard(driver)
    test_actionchains(driver)
    time.sleep(2)
    driver.quit()
