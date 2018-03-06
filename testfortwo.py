#coding=utf-8

import HTMLTestRunner
from appium import webdriver
from time import sleep
import os
import unittest
import sys
from swipe import Android
from menutab import MenuTab

desired_caps = {}

desired_caps['deviceName'] = '85GABMMHXSD3'  #adb devices查到的设备名

desired_caps['platformName'] = 'Android'  #设备平台

desired_caps['platformVersion'] = '5.1'   #设备系统版本   

desired_caps['appPackage'] = 'com.sunbird.zimaoqu'  #被测App的包名

desired_caps['appActivity'] = 'com.sunbird.zimaoqu.activity.WelcomeActivity' #启动时的Activity

desired_caps['appWaitActivity'] ='com.sunbird.zimaoqu.activity.MainActivity'

desired_caps['appWaitActivity'] ='com.sunbird.zimaoqu.activity.LoginActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(2)
#登录
#driver.find_element_by_id('com.sunbird.zimaoqu:id/button1').click()
#sleep(2)
driver.find_element_by_id('com.sunbird.zimaoqu:id/edit_username').click()
driver.find_element_by_id('com.sunbird.zimaoqu:id/ib_username_delete').click()
#dr.hide_keyboard()
driver.find_element_by_id('com.sunbird.zimaoqu:id/edit_username').send_keys('admin')
sleep(1)
driver.find_element_by_id('com.sunbird.zimaoqu:id/edit_pwd').click()
driver.find_element_by_id('com.sunbird.zimaoqu:id/ib_pwd_delete').click()
#dr.hide_keyboard()
driver.find_element_by_id('com.sunbird.zimaoqu:id/edit_pwd').send_keys('admin')
sleep(1)
driver.find_element_by_id('com.sunbird.zimaoqu:id/tv_register').click()
sleep(2)
#登录成功

driver.find_element_by_id('com.sunbird.zimaoqu:id/bar_right_button').click()#查看推广二维码
sleep(1)
driver.find_element_by_id('com.sunbird.zimaoqu:id/ib_back').click()#返回主菜单
sleep(1)
driver.find_element_by_id('com.sunbird.zimaoqu:id/tv_country').click()#进入统计页面
sleep(1)
driver.find_element_by_class_name('android.view.View').click()
driver.find_element_by_class_name('android.view.View').click()
sleep(1)
driver.find_element_by_id('com.sunbird.zimaoqu:id/start_time_tv').click()
sleep(1)
driver.find_element_by_id('com.sunbird.zimaoqu:id/year').click()
sleep(3)
Android().swipeUp(driver,1000)#这里调用的wipe文件内的swipeUp方法
sleep(2)
driver.find_element_by_id('com.sunbird.zimaoqu:id/btn_sure').click()
sleep(5)
driver.find_element_by_id('com.sunbird.zimaoqu:id/ib_back').click()
sleep(1)
#切换到点位查询页签
driver.find_element_by_id('com.sunbird.zimaoqu:id/main_tab2').click()
sleep(1)
#切换到信息展示页签
driver.find_element_by_id('com.sunbird.zimaoqu:id/main_tab3').click()
sleep(1)
#切换到报表查看页签
driver.find_element_by_id('com.sunbird.zimaoqu:id/main_tab4').click()
sleep(2)

#MenuTab().TjfxtoDwcx()#调用主菜单切换文件内的TjfxtoDwcx方法
#MenuTab().DwcxtoXxzs()#调用主菜单切换文件内的DwcxtoXxzs方法
#MenuTab().XxzstoBbck()#调用主菜单切换文件内的XxzstoBbck方法

		
driver.close_app()
driver.quit()


