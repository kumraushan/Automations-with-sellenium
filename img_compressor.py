from PIL import Image
import PIL
import os
import glob

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlrd
from xlutils.copy import copy
from xlwt import Workbook
import urllib.request
import os
import time
from io import BytesIO

#path to your chrome drivers
loc = 'chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(loc)
driver.get("http://img2url.thedirtylaundry.in/")

#Getting and working with excel sheet
file_location = "product_information.xlsx"     #replace the location of excel sheet
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols
data = [[sheet.cell_value(row,col) for col in range(cols-1)] for row in range(1,rows-1)]

wb = copy(workbook)
wb_sheet = wb.get_sheet(0)
wb_sheet.write(0, 13, "compressed_url")

i=1
#getting the data
for item in data:
#looping through the data
    file_upload = driver.find_element_by_name('mainimage')
    urllib.request.urlretrieve(item[2], "/home/raushan/Desktop/making_automations/putatoe_images/putatoe.jpg")
    file_name =("/home/raushan/Desktop/making_automations/putatoe_images/putatoe.jpg")
    im =Image.open(file_name)
    #print(im)
    #path = BytesIO(urllib.request.urlopen(item[2]).read())
    #print(im.tell())
    print(f"The image size dimensions are: {im.size}")
    rgb_im = im.convert('RGB')
    rgb_im.save(file_name,optimize=True,quality=50)
    print(rgb_im.size)
    #print(rgb_im.tell())
    file_upload.send_keys(
    "/home/raushan/Desktop/making_automations/putatoe_images/putatoe.jpg")  # replace your image folder with atleast one image

    button = driver.find_element_by_tag_name('button')
    #print(button)
    button.click()
    time.sleep(30)
    element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
    #print(element)
    url = element.get_attribute('value')
    print(url)

    wb_sheet.write(i, 13, url)
    wb.save(file_location)
    i+=1












#file_name = "army2.png"
# im = Image.open(file_name)
# print(f"The image size dimensions are: {im.size}")
# # The image size dimensions are: (1920, 1280)
# rgb_im = im.convert('RGB')
# rgb_im.save("Compressed_"+file_name,optimize=True,quality=50)
# print(rgb_im.size)

#file_upload.send_keys("/home/raushan/Desktop/Compressed_"+file_name)



