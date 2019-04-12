#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

import unittest
from selenium import webdriver
from time import sleep


class QQ_kongjian(object):

    def kongjian_denglu(self,u,p):
        global dr
        dr= webdriver.Chrome()
        dr.get('https://www.qzone.qq.com')
        sleep(2)

        dr.switch_to.frame('login_frame')
        sleep(2)

        dr.find_element_by_css_selector('#switcher_plogin').click()
        sleep(2)

        dr.find_element_by_id('u').send_keys('{}'.format(u))
        sleep(2)
        dr.find_element_by_id('p').send_keys('{}'.format(p))
        sleep(2)
        dr.find_element_by_id('login_button').click()
        sleep(5)

        return dr.title


import xlrd

class QQkongjian_canshu(object):

    def zhanghao_mima(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\WXL\Desktop\python_学习\框架\data\qq空间.xlsx')
        sheet=f.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju


# import unittest

class QQkongjian_test(unittest.TestCase):
    shuju=QQkongjian_canshu()
    shuju=shuju.zhanghao_mima()

    def setUp(self):
        print('this is the setUp')

    def test_1(self):
        suo=QQ_kongjian()
        asd=suo.kongjian_denglu(int(self.shuju[0][0]),(self.shuju[0][1]))
        self.assertEqual(asd,'你就是光阿^ [http://1147695719.qzone.qq.com]')

    def test_2(self):
        suo=QQ_kongjian()
        asd=suo.kongjian_denglu(int(self.shuju[1][0]),int(self.shuju[1][1]))
        self.assertNotEqual(asd,'你就是光阿^ [http://1147695719.qzone.qq.com]')

    def test_3(self):
        suo=QQ_kongjian()
        asd=suo.kongjian_denglu((self.shuju[2][0]),(self.shuju[2][1]))
        self.assertNotEqual(asd,'你就是光阿^ [http://1147695719.qzone.qq.com]')


    def tearDown(self):
        dr.quit()
        print('this is tearDown')


if __name__ =='__main__':
    unittest.main()