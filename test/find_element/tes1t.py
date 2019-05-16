import time

from selenium import webdriver  # 导入webdriver模块

# 打开网站
driver = webdriver.Firefox()  # 打开浏览器
driver.get('https://www.baidu.com/')  # 打开百度

# 设置休眠
time.sleep(1)  # 休眠1s

# 页面刷新
driver.refresh()  # 页面刷新

# 前进与后退
driver.back()  # 返回上一页
driver.forward()  # 切换到下一页
time.sleep(1)

# 设置窗口大小
driver.set_window_size(540, 960)  # 设置窗口大小为540*960
driver.maximize_window()  # 最大化窗口

# 截屏
driver.get_screenshot_as_file("H:\\selenium\\screen\\1.jpg")

# 退出
driver.close()  # 关闭当前窗口
driver.quit()  # 退出浏览器进程
