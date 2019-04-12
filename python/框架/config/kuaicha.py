#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL
import requests
class xuexiao(object):

    def kuaicha(self,diqu):
        url = 'http://testsupport-be.haofenshu.com/v1/schools/infos?filterInput={}'.format(diqu)
        head = {
            'Content-Type': "application/x-www-form-urlencoded",
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': "zh-CN,zh;q=0.9",
            'Cache-Control': "max-age=0",
            'Connection': "keep-alive",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
            'cache-control': "no-cache",
            'Postman-Token': "a0385919-40a2-46b9-95a8-dbf4505a02c5"
        }
        res=requests.get(url,headers=head)
        return res.json()

if __name__ == '__main__':
    aa = xuexiao()
    a = aa.kuaicha('123')
    print(a)