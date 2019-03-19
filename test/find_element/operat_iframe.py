import time

from selenium import webdriver


# 获取当前窗口句柄
def test_handle(driver):
    driver.get("http://bk.ganji.com")
    driver.implicitly_wait(10)
    h = driver.current_window_handle  # 获取当前窗口句柄 h是一个集合

if __name__ == '__main__':
    driver = webdriver.Firefox()
    test_handle(driver)
    time.sleep(2)
    driver.quit()