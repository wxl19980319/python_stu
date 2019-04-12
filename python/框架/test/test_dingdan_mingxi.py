#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL


import unittest
from 框架.config import zuoye_dingdan
from 框架.data import zuoye_canshu

class zuoye_test(unittest.TestCase):

    shuju=zuoye_canshu.Zuoye_canshu()
    shuju=shuju.dingdan_3canshu()

    def test_dingdanmingxi_1(self):
        suo=zuoye_dingdan.Zuoye_dingdan()
        asd=suo.dingdan_mingxi(int(self.shuju[0][0]),int(self.shuju[0][1]),(self.shuju[0][2]))
        self.assertEqual(asd['status'], 1)

    def test_dingdanmingxi_2(self):
        suo=zuoye_dingdan.Zuoye_dingdan()
        asd=suo.dingdan_mingxi((self.shuju[1][0]),int(self.shuju[1][1]),(self.shuju[1][2]))
        self.assertEqual(asd['message'],'get error')

    def test_dingdanmingxi_3(self):
        suo = zuoye_dingdan.Zuoye_dingdan()
        asd = suo.dingdan_mingxi(int(self.shuju[2][0]), (self.shuju[2][1]), (self.shuju[2][2]))
        self.assertEqual(asd['message'], 'get error')

    def test_dingdanmingxi_4(self):
        suo = zuoye_dingdan.Zuoye_dingdan()
        asd = suo.dingdan_mingxi(int(self.shuju[3][0]), int(self.shuju[3][1]), (self.shuju[3][2]))
        self.assertEqual(asd['errMsg'], '该订单号对应的订单不存在！')

    def test_dingdanmingxi_5(self):
        suo = zuoye_dingdan.Zuoye_dingdan()
        asd = suo.dingdan_mingxi((self.shuju[4][0]), int(self.shuju[4][1]), (self.shuju[4][2]))
        self.assertEqual(asd['message'], 'get error')


if __name__ == '__main__':
    unittest.main()