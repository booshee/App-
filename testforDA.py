#coding:utf-8

import os

import HTMLTestRunner

import unittest

import time

from appium import webdriver

 

# Returns abs path relative to this file and not cwd

PATH = lambda p: os.path.abspath(

    os.path.join(os.path.dirname(__file__), p)

)

 

class elementA(unittest.TestCase):

    def test_(self):  

        desired_caps = {}

        desired_caps['deviceName'] = '85GABMMHXSD3'  #adb devices查到的设备名

        desired_caps['platformName'] = 'Android'

        desired_caps['platformVersion'] = '5.1'      

        desired_caps['appPackage'] = 'com.sunbird.moveandoperate'  #被测App的包名

        desired_caps['appActivity'] = 'com.sunbird.moveandoperate.activity.base.Splash' #启动时的Activity

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

 

        login = driver.find_element_by_name(u"登录")

        self.assertIsNotNone(login)

        login.click()     

        time.sleep(2)

        cancel = driver.find_element_by_name(u"取消")

        self.assertIsNotNone(cancel)

        cancel.click() 

        time.sleep(2)   

        PLupdate = driver.find_element_by_name(u"问题上传") 
        time.sleep(1)
        self.assertIsNotNone(PLupdate)

        PLupdate.click()

        photos =driver.find_element_by_name(u"拍照")
        driver.quit()

     

if __name__ == '__main__':

    testunit=unittest.TestSuite()        #定义一个单元测试容器

    testunit.addTest(elementA("test_"))  #将测试用例加入到测试容器中    

    filename="./myAppiumLog.html"        #定义个报告存放路径，支持相对路径。

    fp=file(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述

    runner.run(testunit) 