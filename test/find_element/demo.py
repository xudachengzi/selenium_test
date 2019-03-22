import time

from selenium import webdriver


def test_iframe(driver, url):
    driver.get(url)
    driver.find_element_by_tag_name("iframe")


if __name__ == '__main__':
    url = ''
    driver = webdriver.Chrome()
    test_iframe(driver)
    time.sleep(2)
    driver.quit()
