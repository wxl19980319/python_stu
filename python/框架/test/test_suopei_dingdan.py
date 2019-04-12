#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

import unittest
from 框架.config import zuoye_dingdan
from 框架.data import zuoye_canshu

class zuoye_test(unittest.TestCase):

    shuju=zuoye_canshu.Zuoye_canshu()
    shuju=shuju.suopei_4canshu()

    def test_suopeidingdan_1(self):
        suo=zuoye_dingdan.Zuoye_dingdan()
        asd=suo.suopei_dingdan(int(self.shuju[0][0]),int(self.shuju[0][1]))
        self.assertEqual(asd['totalSize'], 1)

    def test_suopeidingdan_2(self):
        suo=zuoye_dingdan.Zuoye_dingdan()
        asd=suo.suopei_dingdan((self.shuju[1][0]),int(self.shuju[1][1]))
        self.assertEqual(asd['message'],'get error')

    def test_suopeidingdan_3(self):
        suo=zuoye_dingdan.Zuoye_dingdan()
        asd=suo.suopei_dingdan((self.shuju[2][0]),int(self.shuju[2][1]))
        self.assertEqual(asd['message'],'get error')

    def test_suopeidingdan_4(self):
        suo=zuoye_dingdan.Zuoye_dingdan()
        asd=suo.suopei_dingdan(int(self.shuju[3][0]),(self.shuju[3][1]))
        self.assertEqual(asd['message'],'get error')

    def test_suopeidingdan_5(self):
        suo=zuoye_dingdan.Zuoye_dingdan()
        asd=suo.suopei_dingdan(int(self.shuju[3][0]),(self.shuju[3][1]))
        self.assertEqual(asd['message'],'get error')

if __name__ =='__main__':
    unittest.main()