#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

from 框架.report import HTMLTestRunner
import unittest



def baogao(aa):
    suit = unittest.TestSuite()
    #两个参数，1、路径 2、匹配条件
    #到这个路径下匹配所有以test开头的文件，test开头文件中找到以test开头的函数
    for o in aa:
        dis=unittest.defaultTestLoader.discover(r'C:\Users\WXL\Desktop\python_学习\框架\test',pattern='test_{}.py'.format(o.strip()))
        for i in dis:
            suit.addTest(i)
    # suit.addTest(unittest.makeSuite(Suopei_test))

    f = open(r'C:\Users\WXL\Desktop\python_学习\框架\report\zuoye.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='索赔测试报告', tester='位晓磊', description='结果如下')
    runner.run(suit)
    f.close()

if __name__ == '__main__':
    baogao('*')