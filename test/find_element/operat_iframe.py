import time

from selenium import webdriver


# 获取当前窗口句柄
def test_iframe(driver):
    driver.get("http://mail.163.com")
    driver.implicitly_wait(30)
    # 切换iframe
    iframe = driver.find_element_by_tag_name("iframe")
    driver.switch_to_frame(iframe)
    driver.find_element_by_name("email").send_keys("123")
    driver.find_element_by_name("password").send_keys("456")


if __name__ == '__main__':
    driver = webdriver.Firefox()
    test_iframe(driver)
    time.sleep(2)
    driver.quit()
