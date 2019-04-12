#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

# import requests
# import time
# import unittest
# import HTMLTestRunner
#
# def jiekou():
#     url='http://testsupport-be.haofenshu.com/v1/schools/infos?filterInput=郑州'
#     head = {
#         'Content-Type': "application/x-www-form-urlencoded",
#         'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         'Accept-Encoding': "gzip, deflate",
#         'Accept-Language': "zh-CN,zh;q=0.9",
#         'Cache-Control': "max-age=0",
#         'Connection': "keep-alive",
#         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
#         'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
#         'cache-control': "no-cache",
#         'Postman-Token': "a0385919-40a2-46b9-95a8-dbf4505a02c5"
#     }
#     res=requests.get(url,headers=head)
#     mes=res.json()
#     return mes
#
# # print(jiekou())
# mes=jiekou()
# print(mes)
#
# class Kuaicha(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(mes['code'],0)
#
#     def test_2(self):
#         self.assertEqual(mes['msg'],'学校快查成功')
#
#     def setUp(self):
#         print('hello')
#
#     def tearDown(self):
#         print('OK')
#
#
# if __name__ == '__main__':
#     suit=unittest.TestSuite()
#     for i in range(1,3):
#         suit.addTest(Kuaicha('test_{}'.format(i)))
#     f = open('asd.html','wb')
#     runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='学校快查测试报告',tester='位晓磊',description='结果如下')
#     runner.run(suit)
#     f.close()









