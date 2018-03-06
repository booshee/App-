#coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '85GABMMHXSD3'
desired_caps['appPackage'] = 'com.sunbird.moveandoperate'
desired_caps['appActivity'] = 'com.sunbird.moveandoperate.activity.base.Splash'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)
driver.find_element_by_name("登录").click()
time.sleep(2)
driver.find_element_by_name("取消").click()
time.sleep(1)
driver.find_element_by_name("问题上传").click()
time.sleep(2)
driver.find_element_by_name("拍照").click()


driver.quit()
