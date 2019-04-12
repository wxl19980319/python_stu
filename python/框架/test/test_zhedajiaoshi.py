#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

import unittest
from 框架.config import zheda_jiaoshi
from appium import webdriver
import warnings
from time import sleep
from ddt import ddt, file_data


@ddt
class Denglu_test(unittest.TestCase):


    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        desired_caps = {'platformName': 'Android',
                        # 'platfromVersion':'6.0',
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'net.crigh.cgapp_schedule',
                        'appActivity': '.activity.login.LoginActivity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)

    @file_data(r'C:\Users\WXL\Desktop\python_学习\框架\data\canshu.json')
    def test_1(self,values):
        b=values[0]
        a=zheda_jiaoshi.denglu(self.driver,b['username'],b['password'])
        self.assertEqual(a,'浙大教室')

    @file_data(r'C:\Users\WXL\Desktop\python_学习\框架\data\canshu.json')
    def test_2(self,values):
        b = values[1]
        a = zheda_jiaoshi.denglu1(self.driver, b['username'], b['password'])
        self.assertEqual(a,'登 录')

    @file_data(r'C:\Users\WXL\Desktop\python_学习\框架\data\canshu.json')
    def test_3(self, values):
        b = values[2]
        a = zheda_jiaoshi.denglu1(self.driver, b['username'], b['password'])
        self.assertEqual(a, '登 录')




    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()