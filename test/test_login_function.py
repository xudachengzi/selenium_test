import xlrd
from selenium import webdriver
import selenium
import time
import xlwt
from xlutils.copy import copy


def login(driver, user, password):
    """登录测试服"""
    driver.get('http://112.13.89.101:9511/')
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


def write_excel_xls(path, sheet_name, value):
    """xls格式表格写入数据成功"""
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿


def write_excel_xls_append(path, value):
    """xls格式表格【追加】写入数据成功"""
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")


def read_excel_xls(path):
    """读取数据"""
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据
        print()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    login(driver, "13905740095", "740095")

    try:
        # 判断是否登录成功
        t = driver.find_element_by_xpath("//div[@class='userinfo-box']/span[2]").text
        if t == '姚志坚，你好!':

            print('登录成功')
            time.sleep(1)
            logout(driver)
            print('登出成功')

        else:
            print('登录失败')
    except Exception as fp:
        time.sleep(1)
        alert = driver.switch_to_alert()  # 获取弹窗内容
        print(alert.text)
        print('登录失败')

    # 关闭浏览器
    driver.quit()
