from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import xlrd
import urllib.request
import time

#path to your chrome drivers
loc = 'chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(loc)

#getting the webpage
driver.get("http://admin.thedirtylaundry.in/")

#login credentials
username = driver.find_element_by_id('id_username')
username.send_keys('admin')
password = driver.find_element_by_id('id_password')
password.send_keys('admin0912')
button = driver.find_element_by_tag_name('button')
button.click()

#Getting and working with excel sheet
file_location = "product_information.xlsx"     #replace the location of excel sheet
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols
data = [[sheet.cell_value(row,col) for col in range(cols-1)] for row in range(1,rows-1)]
output = []
#excel_size = []
sizes = []
colours = []

#getting the data
for item in data:
#looping through the data

    #getting the webelements by locator

    select = Select(driver.find_element_by_name('product_type'))
    select.select_by_value('1')
    name = driver.find_element_by_name('name')
    spec = driver.find_element_by_id('id_specification')
    short_desc = driver.find_element_by_id('id_short_desp')
    price = driver.find_element_by_id('id_price')
    discount = driver.find_element_by_id('id_discount')
    delivery = driver.find_element_by_id('id_del_price')
    status = driver.find_element_by_id('id_status')
    sizes = driver.find_elements_by_xpath("//*[@id='id_size_0' or @id='id_size_1' or @id='id_size_2' or @id='id_size_3']")
    colours = driver.find_elements_by_xpath("//*[@id='id_color_9' or @id='id_color_10' or @id='id_color_53' or @id='id_color_66' or @id='id_color_85']")
    #print(colours)
    file_upload = driver.find_element_by_name('myfile')
    submit = driver.find_element_by_name("Submit")

#sending the value to the input fields
    name.send_keys(item[1] + ' Tshirt')
    spec.send_keys(item[6])
    short_desc.send_keys(item[5])
    price.send_keys(str(item[7])+ '0')
    delivery.send_keys(str(item[9])+ '0')
    discount.send_keys(str(item[8])+ '0')
    status.click()
    for size in sizes:
        size.click()
    urllib.request.urlretrieve(item[2], "/home/raushan/Desktop/making_automations/putatoe_images/putatoe.jpg")
    file_upload.send_keys("/home/raushan/Desktop/making_automations/putatoe_images/putatoe.jpg")  #replace your image folder with atleast one image
    for colour in colours:
        colour.click()
    submit.click()
    time.sleep(2)
    driver.get("http://admin.thedirtylaundry.in/product/")

    excel_size = (item[10].split(','))
    #print(excel_size[1])
    # size_list = driver.find_element_by_id("id_size")
    # sizes = size_list.find_elements_by_tag_name("li")
    # for size in sizes:
    #     print(size.text)
    #     size.check()




# sizes = driver.find_elements_by_xpath("//*[@class=excel_size[0] or @class=excel_size[1] or @class=excel_size[2] or @class=excel_size[3]]")

