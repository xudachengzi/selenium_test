import time

from selenium import webdriver


def test_JS(driver, url):
    driver.get(url)
    # 滚动条回顶部
    # js1 = "var q=document.getElementById('id').scrollTop=0"
    # driver.execute_script(js1)
    # # 滚动条拉到底部
    # js2 = "var q=document.documentElement.scrollTop=10000"
    # driver.execute_script(js2)
    # 左右滚动
    js3 = "var q=document.body.scrollTop=0"
    driver.execute_script(js3)


if __name__ == '__main__':
    url = 'https://www.cnblogs.com/yoyoketang'
    driver = webdriver.Chrome()
    test_JS(driver, url)
    time.sleep(2)
    driver.quit()
