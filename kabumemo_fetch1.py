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
    driverpath= '/opt/google/chromedriver'
    browserpath  = '/opt/google/chrome/google-chrome'


#opt = webdriver.ChromeOptions()
opt = Options()

opt.binary_location=browserpath
opt.add_argument('--headless')
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-gpu')
opt.add_argument('--window-size=1280,1024')

print(opt.binary_location)
#driver = webdriver.Chrome(executable_path=driverpath,chrome_options=opt)
driver = webdriver.Chrome(driverpath,options=opt)

#driver.get('https://www.google.co.jp/')
#driver.save_screenshot('test.png')

code = 6502


def get_day_data(code,year):
	url = f"https://kabuoji3.com/stock/{code}/{year}/"

	driver.get(url)
	#print('[URL] {0}'.format(driver.current_url))
	#print('[Title] {0}'.format(driver.title))

	html = driver.page_source
	dfs = pd.read_html(html,encoding="utf-8")
	df = dfs[0]
	
	return df

years = [2000+i for i in range(20)]

data = pd.DataFrame()
for y in range(2000,2020):
	print(y)
	data_y = get_day_data(6502,y)
	data = pd.concat([data,data_y])



breakpoint()

