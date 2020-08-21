from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import xlrd
import urllib.request
import time
from selenium.webdriver.common.action_chains import ActionChains

#path to your chrome drivers
loc = 'chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(loc)
driver.get("http://web.thedirtylaundry.in/admin/db_manager/product/add/")
username = driver.find_element_by_id('id_username')
username.send_keys('admin')
password = driver.find_element_by_id('id_password')
password.send_keys('admin0912')
button = driver.find_element_by_xpath("//input[@type='submit']")
button.click()

file_location = "product_information.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols
#print(rows,cols)
data = [[sheet.cell_value(row,col) for col in range(cols-1)] for row in range(1,rows-1)]
output = []
#print(data)

sizes = []
colours = []

for item in data:
#looping through the data

    #getting the webelements by locator

    select = Select(driver.find_element_by_name('product_type'))
    select.select_by_value('3')
    name = driver.find_element_by_name('name')
    spec = driver.find_element_by_id('id_specification')
    short_desc = driver.find_element_by_id('id_short_desp')
    price = driver.find_element_by_id('id_price')
    discount = driver.find_element_by_id('id_discount')
    delivery = driver.find_element_by_id('id_del_price')
    status = driver.find_element_by_id('id_status')
    sizes = driver.find_elements_by_name('size')
    #print(sizes)
    #for size in sizes:
     #   print(size)

    img1 = driver.find_element_by_xpath("//select[@name='image']/option[@value='4']")
    img2 = driver.find_element_by_xpath("//select[@name='image']/option[@value='5']")

    excel_size = (item[10].split(','))
    print(excel_size[1])
    s = excel_size[0]
    print(s)
    print(excel_size)
    size_s = driver.find_element_by_xpath("//select[@name='size']/option[text()=" + " '" + excel_size[0] + "'" + "]")
    size_l = driver.find_element_by_xpath("//select[@name='size']/option[text()=" + " '" + excel_size[2] + "'" + "]")
    size_m = driver.find_element_by_xpath("//select[@name='size']/option[text()=" + " '" + excel_size[1] + "'" + "]")
    size_xl = driver.find_element_by_xpath("//select[@name='size']/option[text()=" + " '" + excel_size[3] + "'" + "]")


    color_black = driver.find_element_by_xpath("//select[@name='color']/option[@value='1']")
    color_blue = driver.find_element_by_xpath("//select[@name='color']/option[@value='3']")
    color_orange = driver.find_element_by_xpath("//select[@name='color']/option[@value='6']")
    color_red = driver.find_element_by_xpath("//select[@name='color']/option[@value='12']")
    color_white = driver.find_element_by_xpath("//select[@name='color']/option[@value='4']")




    name.send_keys(item[1] + ' Tshirt')
    spec.send_keys(item[6])
    short_desc.send_keys(item[5])
    price.send_keys(str(item[7])+ '0')
    delivery.send_keys(str(item[9])+ '0')
    discount.send_keys(str(item[8])+ '0')
    status.click()

    ActionChains(driver).key_down(Keys.CONTROL).click(img1).key_up(Keys.CONTROL).perform()
    ActionChains(driver).key_down(Keys.CONTROL).click(img2).key_up(Keys.CONTROL).perform()

    ActionChains(driver).key_down(Keys.CONTROL).click(size_s).key_up(Keys.CONTROL).perform()
    ActionChains(driver).key_down(Keys.CONTROL).click(size_l).key_up(Keys.CONTROL).perform()
    ActionChains(driver).key_down(Keys.CONTROL).click(size_m).key_up(Keys.CONTROL).perform()
    ActionChains(driver).key_down(Keys.CONTROL).click(size_xl).key_up(Keys.CONTROL).perform()

    ActionChains(driver).key_down(Keys.CONTROL).click(color_black).key_up(Keys.CONTROL).perform()
    ActionChains(driver).key_down(Keys.CONTROL).click(color_blue).key_up(Keys.CONTROL).perform()
    ActionChains(driver).key_down(Keys.CONTROL).click(color_orange).key_up(Keys.CONTROL).perform()
    ActionChains(driver).key_down(Keys.CONTROL).click(color_red).key_up(Keys.CONTROL).perform()
    ActionChains(driver).key_down(Keys.CONTROL).click(color_white).key_up(Keys.CONTROL).perform()

    button = driver.find_element_by_xpath("//input[@name='_addanother']")
    button.click()


    #select = Select(driver.find_element_by_name('size'))
    ##select.select_by_visible_text('M'and'XL')

    # sizes = driver.find_elements_by_xpath("//*[@class=excel_size[0] or @class=excel_size[1] or @class=excel_size[2] or @class=excel_size[3]]")
