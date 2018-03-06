#coding=utf-8
import os
import time
import unittest
from selenium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'　　#u设备系统
desired_caps['platformVersion'] = '5.1'　　#u设备系统版本
desired_caps['deviceName'] = 'MX5'　　#u设备名称

#desired_caps['app'] = PATH('C:\\Users\\LENOVO\\Desktop\\StarZone_V2.0.0.apk')　
desired_caps['appPackage'] = 'com.sunbird.zimaoqu'　　
desired_caps['appActivity'] = 'com.sunbird.zimaoqu/.activity.WelcomeActivity'

#如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)　　#启动app

time.sleep(5)　　#启动app时，需要一定时间进入引导页，所以必须设置等待时间，不然下面会一直报错定位不到元素
driver.find_element_by_name(u'登录').click()
time.sleep(2)
driver.quit()