#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

import unittest
from 框架.config import wangyiyun
from 框架.data import wangyiyun_canshu
from  appium import webdriver
from  time import sleep
import warnings
# warnings.simplefilter("ignore", ResourceWarning)



class Denglu_test(unittest.TestCase):
    shuju=wangyiyun_canshu.Canshu()
    shuju=shuju.zhaohao_mima()

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        desired_caps = {'platformName': 'Android',
                        # 'platfromVersion':'6.0',
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'com.netease.cloudmusic',
                        'appActivity': '.activity.LoadingActivity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(20)

    def test_1(self):
        a=wangyiyun.denglu(self.driver,int(self.shuju[0][0]),self.shuju[0][1])
        self.assertEqual(a,'wxl0801')

    def test_2(self):
        a = wangyiyun.denglu1(self.driver, int(self.shuju[1][0]), int(self.shuju[1][1]))
        self.assertEqual(a, '登录')

    def test_3(self):
        a=wangyiyun.denglu1(self.driver,int(self.shuju[2][0]),self.shuju[2][1])
        self.assertEqual(a,'登录')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()