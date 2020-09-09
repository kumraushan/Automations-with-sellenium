from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd
from xlwt import Workbook
import urllib.request
import time
import os

#path to your chrome drivers
loc = 'chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(loc)
driver.get("http://127.0.0.1:5000/")

wb = Workbook()
ws = wb.add_sheet('writing_in_excel')
ws.write(0,0,'id')
ws.write(0,1,'url')

path = '/home/raushan/Downloads/putatoe_images/'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.png' in file:
            files.append(os.path.join(r, file))

#print(files)
#print(len(files))
i = 1
for file in files:
    file_upload = driver.find_element_by_name('files[]')
    file_upload.send_keys(file)

    submit = driver.find_element_by_name("submit")
    submit.click()

    element = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.NAME,"imgUrl")))
    #print(element)
    url = element.get_attribute('value')
    print(url)

    ws.write(i,0,file)
    ws.write(i,1,url)
    i= i+1
wb.save('1st.xls')