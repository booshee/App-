#coding=utf-8

import HTMLTestRunner
from appium import webdriver

from time import sleep
import os
import unittest
import sys

'''
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

dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(2)
'''

class Android():
	#获取设备屏幕尺寸
	def getSize(self,dr):
		x = dr.get_window_size()['width']
		y = dr.get_window_size()['height']
		#print(x,y)
		return (x,y)

    # 向左滑动（t为持续时间）
	def swipeLeft(sefl,dr,t):
		I = Android().getSize(dr)
		x1 = int(I[0]*0.75)
		y1 = int(I[1]*0.5)
		x2 = int(I[0]*0.25)
		dr.swipe(x1,y1,x2,y1,t)



    # 向右滑动
	def swipeRight(self,dr,t):
		l = Android().getSize(dr)
		x1 = int(l[0]*0.25)
		y1 = int(l[1]*0.5)
		x2 = int(l[0]*0.75)
		dr.swipe(x1,y1,x2,y1,t)



    # 向上滑动
	def swipeUp(self,dr,t):
		l = Android().getSize(dr)
		x1 = int(l[0]*0.25)
		y1 = int(l[1]*0.95)
		y2 = int(l[1]*0.75)
		dr.swipe(x1,y1,x1,y2,t)



    # 向下滑动
	def swipeDown(self,dr,t):
		l = Android().getSize(dr)
		x1 = int(l[0]*0.25)
		y1 = int(l[1]*0.8)
		y2 = int(l[1]*0.9)
		dr.swipe(x1,y1,x1,y2,t)



