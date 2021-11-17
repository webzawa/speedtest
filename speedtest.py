# pip install requests
# pip install selenium
# pip install beautifulsoup4
# pip install pyinstaller # 2021/11/02時点でPython3.9以上だとエラーになるので注意
# chrome webdriver
# pyinstaller ./speedtest.py --onefile --noconsole --add-binary "./driver/chromedriver.exe;./driver"
# ↑実行時"./driver"ディレクトリに"chromedriver.exe"が必要

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
from bs4 import BeautifulSoup
import time
import datetime
import requests
import sys
import socket
import os

# Python & Selenium のプログラムを実行形式(.exe)化する（webdriverも.exeに含める方法）
# https://www.zacoding.com/post/python-selenium-to-exe/
def resource_path(relative_path):
  try:
    base_path = sys._MEIPASS
  except Exception:
    base_path = os.path.dirname(__file__)
  return os.path.join(base_path, relative_path)

HOSTNAME = socket.gethostname()
USERNAME = os.getlogin()
SPEEDTEST_URL = 'https://www.musen-lan.com/speed/'
SAVE_RESULT_DIR = 'C:\speedtest'
SAVE_RESULT_FILENAME = '\speedtest_result' + '_' + HOSTNAME + '_' + USERNAME + '.csv'
SLEEP_SECOND = 45

# SeleniumのChromeをバックグラウンドで起動する方法
# https://watlab-blog.com/2019/08/18/selenium-chrome-background/
option = Options()
option.add_argument('--headless')

# Python Selenium でコンソールを非表示にする
# https://www.zacoding.com/post/python-selenium-hide-console/
service = Service('./driver/chromedriver.exe')
service.creationflags = CREATE_NO_WINDOW

driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), options=option, service=service)

driver.get(SPEEDTEST_URL)

down_start_btn = driver.find_element_by_xpath('//*[@id="down-start"]')
down_start_btn.click()

time.sleep(SLEEP_SECOND)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

speed_result = soup.find('span', attrs={ 'class': 'answer' }).text

f = open(SAVE_RESULT_DIR + SAVE_RESULT_FILENAME, 'a')

f.write(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') + ',' + HOSTNAME + ',' + USERNAME + ',' + speed_result + '\n')

f.close()

driver.quit()
sys.exit()
