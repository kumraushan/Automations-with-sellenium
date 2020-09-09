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
driver.get("http://img2url.thedirtylaundry.in/")

file = '/putatoe_images/putatoe.jpg'

file_upload = driver.find_element_by_name('mainimage')
file_upload.send_keys(file)

#submit = driver.find_element_by_xpath("//button[normalize-space()='Upload Image']")
button = driver.find_element_by_tag_name('button')
print(button)
#submit = button[0]
#print(submit)
button.click()

element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
print(element)
url = element.get_attribute('value')
print(url)

