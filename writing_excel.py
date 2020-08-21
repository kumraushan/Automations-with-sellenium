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
loc = '/home/raushan/Downloads/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(loc)
driver.get("http://img2url.thedirtylaundry.in/")
folder_name = driver.find_element_by_id('UserInput')
folder_name.send_keys('Raushan')
file_upload = driver.find_element_by_name('mainimage')
file_upload.send_keys("/home/raushan/Desktop/putatoe_images/bal.png")
submit = driver.find_elements_by_tag_name("button")
#print(submit)
submit[0].click()
time.sleep(20)
input = driver.find_element_by_id('Textarea1&quot;')
print(input)
# wait = WebDriverWait(driver, 15)
# element = wait.until(EC.presence_of_element_located((By.ID, "Textarea1")))
# print(element)
# print(element.getText())
url = input.get_attribute('value')
print(url)

path = '/home/raushan/Desktop/putatoe_images/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.png' in file:
            files.append(os.path.join(r, file))

print(files[1])

#xpath("//div[@id='profile']/textarea")

wb = Workbook()
ws = wb.add_sheet('writing_in_excel')
ws.write(0,0,'id')
ws.write(0,1,'url')
wb.save('1st.xls')