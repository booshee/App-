#coding=utf8
from selenium import webdriver
import time
dr=webdriver.Firefox()
dr.get("http://192.168.1.11:81")
dr.find_element_by_id("aw-login-user-name").send_keys("admin")
time.sleep(2)
dr.find_element_by_id("aw-login-user-password").send_keys("admin007")
time.sleep(2)
dr.find_element_by_xpath(".//*[@id='login_submit']/img").click()
time.sleep(3)
dr.find_element_by_xpath("html/body/div[1]/div/div[2]/nav/ul/li[2]/a").click()
time.sleep(3)







dr.close()