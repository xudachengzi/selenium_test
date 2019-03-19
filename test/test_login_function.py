from selenium import webdriver
import time


def login(driver, user, password):
    """登录测试服"""
    driver.get('http://112.13.89.101:9011/')
    driver.implicitly_wait(10)
    # 输入账号
    driver.find_element_by_xpath("//*[@id='account-input']").send_keys(user)
    # 输入密码
    driver.find_element_by_xpath("//*[@id='password-input']").send_keys(password)
    driver.find_element_by_xpath("//*[@id='login-btn']").click()


def logout(driver):
    """退出测试服"""
    # 点击右上角退出键
    driver.find_element_by_xpath("//span[contains(text(),'退出')]").click()
    time.sleep(2)
    # 点击确定键退出
    driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    login(driver, "admin", "123456")

    # 判断是否登录成功
    t = driver.find_element_by_xpath("//div[@class='userinfo-box']/span[2]").text
    if t == '超级管理员，你好!':
        print('登录成功')
        time.sleep(3)
        logout(driver)
        print('登录失败')
    else:
        print('登录失败')
    # 关闭浏览器
    driver.quit()
