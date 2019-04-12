#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL


import unittest
from 框架.config import kuaicha
from 框架.data import kuaicha_duqu

class Kuaicha_test(unittest.TestCase):

    shuju = kuaicha_duqu.kuaicha_shuju()
    shuju = shuju.didian_mingcheng()
    # print(shuju)

    def test_kuaicha_1(self):
        cha=kuaicha.xuexiao()
        abc=cha.kuaicha(self.shuju[0][0])
        self.assertEqual(abc['code'],0)

    def test_kuaicha_2(self):
        cha = kuaicha.xuexiao()
        abc = cha.kuaicha(self.shuju[1][0])
        self.assertEqual(abc['msg'], '学校快查成功')

    def test_kuaicha_3(self):
        cha = kuaicha.xuexiao()
        abc = cha.kuaicha(self.shuju[2][0])
        self.assertEqual(abc['code'], 1)

    def  test_kuaicha_4(self):
        cha = kuaicha.xuexiao()
        abc = cha.kuaicha(self.shuju[3][0])
        self.assertNotEqual(abc['code'], 0)

    def test_kuaicha_5(self):
        cha = kuaicha.xuexiao()
        abc = cha.kuaicha(int(self.shuju[4][0]))
        self.assertNotEqual(abc['code'], 0)

if __name__ == '__main__':
    unittest.main()


