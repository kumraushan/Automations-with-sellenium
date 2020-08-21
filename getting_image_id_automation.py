from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import xlrd
from xlutils.copy import copy
import xlwt
import urllib.request
import time
from selenium.webdriver.common.action_chains import ActionChains

#path to your chrome drivers
loc = 'chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(loc)

#getting the webpage
driver.get("http://web.thedirtylaundry.in/admin/db_manager/image/add/")

#login credentials
username = driver.find_element_by_id('id_username')
username.send_keys('admin')
password = driver.find_element_by_id('id_password')
password.send_keys('admin0912')
button = driver.find_element_by_xpath("//input[@type='submit']")
button.click()

#Getting and working with excel sheet
file_location = "product_information.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols
data = [[sheet.cell_value(row,col) for col in range(cols-1)] for row in range(1,rows-1)]

wb = copy(workbook)
wb_sheet = wb.get_sheet(0)
output = []
#img_id = []

color = ["1","3","4","6","12"]

#getting the data
i = 1
for ele in data:
    if ele not in output:
        output.append(ele)

#submitting the input field value
for item in output:
    url = driver.find_element_by_id('id_url')
    status = driver.find_element_by_id('id_status')

    color_black = driver.find_element_by_xpath("//select[@name='color']/option[@value='1']")
    color_blue = driver.find_element_by_xpath("//select[@name='color']/option[@value='3']")
    color_orange = driver.find_element_by_xpath("//select[@name='color']/option[@value='6']")
    color_red = driver.find_element_by_xpath("//select[@name='color']/option[@value='12']")
    color_white = driver.find_element_by_xpath("//select[@name='color']/option[@value='4']")

    url.send_keys(item[2])
    status.click()
    select = Select(driver.find_element_by_name('color'))
    select.select_by_value('3')


    # driver.find_element_by_class_name("related-widget-wrapper").click()
    # ActionChains(driver).key_down(Keys.CONTROL).click(color_black).key_up(Keys.CONTROL).perform()
    # ActionChains(driver).key_down(Keys.CONTROL).click(color_blue).key_up(Keys.CONTROL).perform()
    # ActionChains(driver).key_down(Keys.CONTROL).click(color_orange).key_up(Keys.CONTROL).perform()
    # ActionChains(driver).key_down(Keys.CONTROL).click(color_red).key_up(Keys.CONTROL).perform()
    # ActionChains(driver).key_down(Keys.CONTROL).click(color_white).key_up(Keys.CONTROL).perform()

    button = driver.find_element_by_xpath("//input[@name='_save']")
    button.click()

    #getting the img_id value
    img_id = driver.find_element_by_name("_selected_action")
    #print(img_id.text)
    image_id = img_id.get_attribute("value")
    print(image_id)

    #getting the admin page
    driver.get("http://web.thedirtylaundry.in/admin/db_manager/image/add/")

    #writing img_id to the same excel sheet
    wb_sheet.write(i, 12, image_id)
    wb.save(file_location)
    i+=1






