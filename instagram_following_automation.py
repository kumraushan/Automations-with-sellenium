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
driver.get("https://www.instagram.com/")
time.sleep(2)

#login credentials
username = driver.find_element_by_name('username')
username.send_keys('putatoe_graphics')
password = driver.find_element_by_name('password')
password.send_keys('putatoegraphics0123')
login = driver.find_element_by_xpath('//button[normalize-space()="Log In"]')
login.click()
time.sleep(7)

#clicking not now
not_now = driver.find_elements_by_tag_name('button')
print(not_now)
not_now[1].click()
time.sleep(5)

#turning on notifications
turn_on = driver.find_element_by_xpath('//button[normalize-space()="Turn On"]')
#print(turn_on)
turn_on.click()

#getting profile page
driver.get("https://www.instagram.com/putatoe_graphics/")
time.sleep(2)

#getting following page
following_link = driver.find_elements_by_xpath('//ul[@class="k9GMp "]/li[@class="Y8-fY "]/a[@class="-nal3 "]')
#print(following_link)
following_link[1].click()
time.sleep(3)

#unfollowing the following ones
for item in range(150):
    following = driver.find_elements_by_xpath('//button[@class="sqdOP  L3NKy    _8A5w5    "]')
    #print(following)
    following[0].click()
    time.sleep(3)
    unfollow = driver.find_element_by_xpath('//button[@class="aOOlW -Cab_   "]')
    #print(unfollow)
    unfollow.click()
    time.sleep(12)




# <li class="wo9IH">
#     <div class="uu6c_">
#         <div class="t2ksc">
#             <div class="Jv7Aj    pZp3x">
#             <div class="RR-M- h5uC0 SAvC5" aria-disabled="false" role="button" tabindex="0"><canvas class="CfWVH" height="40" width="40" style="position: absolute; top: -5px; left: -5px; width: 40px; height: 40px;"></canvas><span class="_2dbep " role="link" tabindex="-1" style="width: 30px; height: 30px;"><img alt="miss_cutie_pie__07's profile picture" class="_6q-tv" data-testid="user-avatar" draggable="false" src="https://scontent-del1-1.cdninstagram.com/v/t51.2885-19/s150x150/109234451_384717555836578_4223997294731585524_n.jpg?_nc_ht=scontent-del1-1.cdninstagram.com&amp;_nc_ohc=U9axqZt0w3sAX8kb35t&amp;oh=f38bd2f57adf9475aa2f30a99d8592c8&amp;oe=5F686E7E"></span></div></div>
#             <div class="enpQJ"><div class="d7ByH"><span class="Jv7Aj  MqpiF  "><a class="FPmhX notranslate  _0imsa " title="miss_cutie_pie__07" href="/miss_cutie_pie__07/" tabindex="0">miss_cutie_pie__07</a></span></div>
# <div class="wFPL8 ">👑 queen</div></div></div><div class="Pkbci">
# <button class="sqdOP  L3NKy    _8A5w5    " type="button">Following</button></div></div></li>