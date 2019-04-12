#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

import unittest
from 框架.config import zuoye_dingdan

suo=zuoye_dingdan.Zuoye_dingdan()
asd=suo.shouye_zhuangtai()

class zuoye_test(unittest.TestCase):

    def test_shouyezhuagtai_1(self):
        self.assertEqual(asd['totalSize'],0)

    def test_shouyezhuagtai_2(self):
        self.assertEqual(asd['status'],1)

    def test_shouyezhuagtai_3(self):
        self.assertEqual(asd['errMsg'],'处理成功')

    def test_shouyezhuagtai_4(self):
        self.assertEqual(asd['data'][0]['orderStatusCode'],'0')

    def test_shouyezhuagtai_5(self):
        self.assertEqual(asd['data'][0]['orderStatusDesc'],'草稿')


if __name__ == '__main__':
    unittest.main()