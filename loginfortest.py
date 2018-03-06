#coding=utf-8

import HTMLTestRunner
from appium import webdriver
from time import sleep
import os
import unittest
import time


class LoginTest(unittest.TestCase):

	def setUpClass(cls):
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
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		sleep(5)
	
	
	def tearDownClass(cls):
		cls.driver.quit()
		print('用例执行结束！')

	def test_login(self):
		u'''正确用户名密码可以登录成功'''

		self.driver.find_element_by_id('com.sunbird.zimaoqu:id/button1').click()
		sleep(2)
		self.driver.find_element_by_id('com.sunbird.zimaoqu:id/edit_username').click()
		self.driver.find_element_by_id('com.sunbird.zimaoqu:id/ib_username_delete').click()
		#self.driver.hide_keyboard()
		self.driver.find_element_by_id('com.sunbird.zimaoqu:id/edit_username').send_keys('admin')
		sleep(1)
		self.driver.find_element_by_id('com.sunbird.zimaoqu:id/edit_pwd').click()
		self.driver.find_element_by_id('com.sunbird.zimaoqu:id/ib_pwd_delete').click()
		#self.driver.hide_keyboard()
		self.driver.find_element_by_id('com.sunbird.zimaoqu:id/edit_pwd').send_keys('admin')
		sleep(1)
		self.driver.find_element_by_id('com.sunbird.zimaoqu:id/tv_register').click()
		sleep(2)
		try:
			self.assertIsNotNone(self.driver.find_element_by_id('com.sunbird.zimaoqu:id/bar_title'),'无统计分析按钮，登录失败')
		except:
			self.driver.get_screenshot_as_file("C:\Python27\登录失败.png")


	def test_toDwcx(self):
		u'''成功切换到点位查询页签'''
		el=self.driver.find_elements_by_id("com.sunbird.zimaoqu:id/main_tab2")
		el[2].click()
		sleep(2)
		try:
			self.assertIsNotNone(self.find_element_by_id('com.sunbird.zimaoqu:id/btn_message_shousuo'),'无信息检索字段，页面切换错误')
		except:
			self.driver.get_screenshot_as_file("E:\bugpicture\页面切换错误1.png")
	
	def test_toXxzs(self):
		u'''成功切换到信息展示页签'''
		el=self.driver.find_elements_by_id("com.sunbird.zimaoqu:id/main_tab3")
		el[3].click()
		sleep(2)
		try:
			self.assertIsNotNone(self.find_element_by_id('com.sunbird.zimaoqu:id/about_us_tv'),'无关于我们字段，页面切换错误')
		except:
			self.driver.get_screenshot_as_file("E:\bugpicture\页面切换错误2.png")

	def test_toBbck(self):
		u'''成功切换到报表查看页签'''
		el=self.driver.find_elements_by_id("com.sunbird.zimaoqu:id/main_tab4")
		el[4].click()
		sleep(3)
		try:
			self.assertIsNotNone(self.find_element_by_class_name('android.widget.TextView'),'无名称字段，页面切换错误')
		except:
			self.driver.get_screenshot_as_file("E:\bugpicture\页面切换错误3.png")

if __name__ == '__main__':
	suite = unittest.TestSuite()   
	suite.addTest(LoginTest('test_login'))#需要测试的用例就addTest，不加的就不会运行
	suite.addTest(LoginTest('test_toDwcx'))
	suite.addTest(LoginTest('test_toXxzs'))
	suite.addTest(LoginTest('test_toBbck'))
	#unittest.TextTestRunner(verbosity=1).run(suite)
	#timestr = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))#本地日期时间作为测试报告的名字
	filename = 'E:\\report.html'#这个路径改成自己的目录路径
	fp = open(filename,'w+')
	runner = HTMLTestRunner.HTMLTestRunner(
		stream=fp,
		title=u'自贸区app测试结果',
		description=u'自贸区app自动化测试报告简述'
	)
	runner.run(suite)
	fp.close()
