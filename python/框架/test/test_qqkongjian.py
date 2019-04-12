#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL



import unittest
from 框架.config import qq_kongjian
from 框架.data import qqkongjian_canshu



class QQkongjian_test(unittest.TestCase):
    shuju=qqkongjian_canshu.QQkongjian_canshu()
    shuju=shuju.zhanghao_mima()

    def setUp(self):
        print('------this is the setUp-------')

    def test_1(self):
        suo=qq_kongjian.QQ_kongjian()
        asd=suo.kongjian_denglu(int(self.shuju[0][0]),(self.shuju[0][1]))
        self.assertIn('你就是光阿^ ',asd)


    def test_2(self):
        suo=qq_kongjian.QQ_kongjian()
        asd=suo.kongjian_denglu(int(self.shuju[1][0]),int(self.shuju[1][1]))
        self.assertEqual(asd,'QQ空间-分享生活，留住感动')

    def test_3(self):
        suo=qq_kongjian.QQ_kongjian()
        asd=suo.kongjian_denglu((self.shuju[2][0]),int(self.shuju[2][1]))
        self.assertNotEqual(asd,'你就是光阿^ [http://1147695719.qzone.qq.com]')

    def tearDown(self):
        # dr.quit()
        print('------this is tearDown--------')


if __name__ == '__main__':
    unittest.main()