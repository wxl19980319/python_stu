#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

import unittest
from 框架.config import zuoye_dingdan
from  框架.data import zuoye_canshu

class zuoye_test(unittest.TestCase):

    shuju=zuoye_canshu.Zuoye_canshu()
    shuju=shuju.peijian_2canshu()

    def test_peijianmingxi_1(self):
        suo=zuoye_dingdan.Zuoye_dingdan()
        asd=suo.peijian_mingxi(int(self.shuju[0][0]))
        self.assertEqual(asd['status'],1)

    def test_peijianmingxi_2(self):
        suo=zuoye_dingdan.Zuoye_dingdan()
        asd=suo.peijian_mingxi((self.shuju[1][0]))
        self.assertEqual(asd['message'],'get error')

    def test_peijianmingxi_3(self):
        suo=zuoye_dingdan.Zuoye_dingdan()
        asd=suo.peijian_mingxi((self.shuju[2][0]))
        self.assertEqual(asd['message'],'get error')

    def test_peijianmingxi_4(self):
        suo=zuoye_dingdan.Zuoye_dingdan()
        asd=suo.peijian_mingxi((self.shuju[3][0]))
        self.assertEqual(asd['message'],'get error')

    def test_peijianmingxi_5(self):
        suo=zuoye_dingdan.Zuoye_dingdan()
        asd=suo.peijian_mingxi((self.shuju[4][0]))
        self.assertEqual(asd['message'],'get error')


if __name__ =='__main__':
    unittest.main()