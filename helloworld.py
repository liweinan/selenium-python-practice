from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
print("等待9秒，等待页面返回爬取结果")
time.sleep(9)
print(driver.find_element_by_id('content').text)

driver.close()
