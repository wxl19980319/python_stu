#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL


import unittest
import requests
from 框架.config import suopei
from 框架.data import suopei_duqu

class Suopei_test(unittest.TestCase):
    shuju = suopei_duqu.suopei_shuju()
    shuju=shuju.duqu_shuju()
    def test_suopei_1(self):
        suo= suopei.Suopei()
        asd=suo.jichu_shuju(int(self.shuju[0][0]),int(self.shuju[0][1]))
        self.assertEqual(asd['data']['applicationType'][0]['name'], '多装')

    def test_suopei_2(self):
        suo = suopei.Suopei()
        asd = suo.jichu_shuju((self.shuju[1][0]), int(self.shuju[1][1]))
        self.assertEqual(asd['message'],'get error')

    def test_suopei_3(self):
        suo = suopei.Suopei()
        asd = suo.jichu_shuju(int(self.shuju[2][0]), (self.shuju[2][1]))
        self.assertEqual(asd['message'], 'get error')

if __name__ == '__main__':
    unittest.main()

