#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL


import unittest
from 框架.config import suopeidingdan
from 框架.data import dingdan_duqu

class dingdan_test(unittest.TestCase):
    shuju=dingdan_duqu.dingdan_shuju()
    shuju=shuju.dingdan_duqu()

    def test_dingdan_1(self):
        ding=suopeidingdan.Suopei_dingdan()
        asd=ding.dingdan(int(self.shuju[0][0]),int(self.shuju[0][1]))
        self.assertEqual(asd['totalSize'],1)

    def test_dingdan_2(self):
        ding=suopeidingdan.Suopei_dingdan()
        asd=ding.dingdan((self.shuju[1][0]),int(self.shuju[1][1]))
        self.assertEqual(asd['message'],"get error")

    def test_dingdan_3(self):
        ding=suopeidingdan.Suopei_dingdan()
        asd=ding.dingdan(int(self.shuju[2][0]),(self.shuju[2][1]))
        self.assertEqual(asd['message'],"get error")


if __name__ == '__main__':
    unittest.main()