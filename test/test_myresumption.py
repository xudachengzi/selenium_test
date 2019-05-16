from selenium import webdriver

from test.functions.my_resumption import *

import time

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://112.13.89.101:9511')

    login(driver, '18005740004', '740004')
    time.sleep(5)

    test1(driver)  # 页面检查
    test2(driver)


    time.sleep(1)
    # logout(driver)

    # driver.quit()
