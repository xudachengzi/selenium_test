import time


def login(driver, user, password):
    """登录测试服"""
    driver.get('http://112.13.89.101:9511/')
    driver.implicitly_wait(10)
    # 输入账号
    driver.find_element_by_xpath("//*[@id='account-input']").send_keys(user)
    time.sleep(1)
    # 输入密码
    driver.find_element_by_xpath("//*[@id='password-input']").send_keys(password)
    driver.find_element_by_xpath("//*[@id='login-btn']").click()


def logout(driver):
    """退出测试服"""
    # 点击右上角退出键
    driver.find_element_by_xpath("//span[contains(text(),'退出')]").click()
    time.sleep(1)
    # 点击确定键退出
    driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()


def my_resumption(driver):
    """我的履职"""
    driver.find_element_by_xpath("//ul[@class='menuNavigation el-menu--horizontal el-menu']/div[2]").click()


def npc_activity(driver):
    """我的履职-代表活动"""
    driver.find_element_by_xpath("//ul[@class='el-menu-vertical-demo parent-menu el-menu']/div[1]").click()


def report_on_work(driver):
    """我的履职-述职报告"""
    driver.find_element_by_xpath("//ul[@class='el-menu-vertical-demo parent-menu el-menu']/div[2]").click()


def policy_advisory(driver):
    """我的履职-政策咨询"""
    driver.find_element_by_xpath("//ul[@class='el-menu-vertical-demo parent-menu el-menu']/div[3]").click()


def test1(driver):
    """我的履职-代表活动页面检查"""
    time.sleep(1)
    my_resumption(driver)  # 点击我的履职
    time.sleep(1)
    npc_activity(driver)  # 点击代表活动
    try:
        t1 = driver.find_element_by_xpath("//div[@class='eachMeetingConfig']/p").text
        if t1 == "代表活动":
            print("代表活动页面检查通过")
        else:
            print("代表活动页面检查不通过")
    except:
        print("代表活动系统错误")


def test2(driver):
    """我的履职-代表活动-新增活动"""
    # 点击新增活动
    driver.find_element_by_xpath("//div[@class='topHeadRight']/button").click()
    time.sleep(5)

    # 届
    driver.find_element_by_xpath("//div[@class='el-select']/div[@class='el-input el-input--suffix']").click()
    time.sleep(3)
    driver.find_element_by_xpath(
        "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[@class='el-select-dropdown__item hover']").click()
    time.sleep(1)

    # 名称
    driver.find_element_by_xpath("//div[@class='el-form-item is-error is-required']/div[@class='el-form-item__content']/div[@class='el-input']/input[@class='el-input__inner']")
