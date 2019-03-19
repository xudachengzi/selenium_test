from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

# xptah可以通过元素的id、name、class这些属性定位
# 用xpath通过id属性定位
driver.find_element_by_xpath("//*[@id='kw']").send_keys("python")
# 用xpath通过name属性定位
driver.find_element_by_xpath("//*[@name='wd']").send_keys("python1")
# 用xpath通过class属性定位
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("python2")

# 用xpath通过其他属性定位
# 如果一个元素id、name、class属性都没有，这时候也可以通过其它属性定位
driver.find_element_by_xpath("//*[@autocomplete='off']").send_keys("python3")

# 用xpath来指定标签定位
# 用xpath指定input标签autocomplete属性为off定位
# 有时候同一个属性，同名的比较多，这时候可以通过标签筛选下，定位更准一点
driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys("python4")

# 用xpath来指定层级（也就是定位它的父元素）
# 如果一个元素，它的属性不是很明显
driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("python5")

# 用xpath来索引定位
# 如果一个元素它的兄弟元素跟它的标签一样，这时候无法通过层级定位
driver.find_element_by_xpath("//select[@id='nr']/option[1]").click()

# 用xpath来逻辑运算定位
# xpath可以多个属性逻辑运算的，可以支持与（and）、或（or）、非（not）
driver.find_element_by_xpath("//*[@id='kw' and @autocomplete='off']").click()

# 用xpath来模糊匹配定位
# 掌握了模糊匹配功能，基本上没有定位不到的
driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()
# xpath模糊匹配某个属性
driver.find_element_by_xpath("//*[contains(@id,'kw')]").click()
# xpath模糊匹配以什么开头
driver.find_element_by_xpath("//*[starts-with(@id,'s_kw_')]").click()
# xpath模糊匹配以什么结尾
driver.find_element_by_xpath("//*[ends-with(@id,'kw_wrap')]").click()
# xpath支持最强的正则表达式
driver.find_element_by_xpath("//*[match(text(),'hao12')]").click()
