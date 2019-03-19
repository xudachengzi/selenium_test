import time

from selenium import webdriver


def test_handle(driver):
    driver.get("http://bk.ganji.com")
    driver.implicitly_wait(10)

    # 获取句柄
    h = driver.current_window_handle  # 获取当前窗口句柄 h是一个集合
    print(h)  # 打印首页句柄
    driver.find_element_by_link_text("帮助中心").click()
    all_h = driver.window_handles  # 字典中 每个元素都是字符串包含的集合
    print(all_h)  # 打印全部句柄

    # 切换句柄
    driver.switch_to.window(all_h[1])  # 切换回到其中一页，其中0为首页
    print(driver.title)

    # 关闭新窗口，切回主页
    driver.close()
    driver.switch_to.window(h)
    print(driver.title)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    test_handle(driver)
    time.sleep(2)
    driver.quit()

