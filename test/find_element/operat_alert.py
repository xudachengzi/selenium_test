from selenium import webdriver
import time


def test_alert(driver, url):
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_id("alert").click()
    time.sleep(2)
    t = driver.switch_to_alert()
    # 打印警告框文本内容
    print(t.text)
    # 点警告框确认按钮
    t.accept()
    time.sleep(2)
    driver.find_element_by_id("confirm").click()
    t1 = driver.switch_to_alert()
    print(t1.text)
    time.sleep(2)
    # 点关闭按钮
    t1.dismiss()


if __name__ == '__main__':
    url = "file://H:/my_selenium/test/html/alert.html"
    driver = webdriver.Chrome()
    test_alert(driver, url)
    time.sleep(2)
    driver.quit()
