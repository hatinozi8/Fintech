import platform
pf = platform.system()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


if pf == 'Windows':
    driverpath = 'F:\\work\\chromedriver_win32\\chromedriver.exe'
    browserpath = 'F:\\work\\GoogleChromePortable\\App\\Chrome-bin\\chrome.exe'
elif pf == 'Linux':
    driverpath = '/opt/google/chrome/google-chrome'
    browserpath = '/opt/google/chromedriver'


opt = webdriver.ChromeOptions()

opt.binary_location=browserpath
opt.add_argument('--headless')
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-gpu')
opt.add_argument('--window-size=1280,1024')

print(opt.binary_location)
driver = webdriver.Chrome(executable_path=driverpath,chrome_options=opt)

driver.get('https://www.google.co.jp/')
driver.save_screenshot('test.png')

code = 6502

url = f"https://kabuoji3.com/stock/{code}/2019/"

driver.get(url)
print('[URL] {0}'.format(driver.current_url))
print('[Title] {0}'.format(driver.title))

html = driver.page_source

#download_button = driver.find_element_by_class_name("btn_form btn_download")
#download_button.click()
#time.sleep(1)

print(html)

#download_button = driver.find_element_by_class_name("btn_form btn_download")
#download_button.click()
