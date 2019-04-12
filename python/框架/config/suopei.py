#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

import requests

class Suopei(object):

    def jichu_shuju(self,a,b):
        url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
        head = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100150",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "BASIC_DATA",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "djy0mx",
            'x-access-token': "0da5606a534fa727dfd7f502df38be65",
            # 'cache-control': "no-cache",
            # 'Postman-Token': "da05ee37e5676e7b27972b2892e0fdeb"
        }
        body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": %s,"curPage": %s}' % (a,b)
        body=body.encode('utf-8')
        res = requests.post(url=url, headers=head, data=body)
        return res.json()


# class xuexiao(object):
#
#     def kuaicha(self,diqu):
#         url = 'http://testsupport-be.haofenshu.com/v1/schools/infos?filterInput={}'.format(diqu)
#         head = {
#             'Content-Type': "application/x-www-form-urlencoded",
#             'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#             'Accept-Encoding': "gzip, deflate",
#             'Accept-Language': "zh-CN,zh;q=0.9",
#             'Cache-Control': "max-age=0",
#             'Connection': "keep-alive",
#             'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
#             'Cookie': "yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA",
#             'cache-control': "no-cache",
#             'Postman-Token': "a0385919-40a2-46b9-95a8-dbf4505a02c5"
#         }
#         res=requests.get(url,headers=head)
#         return res.json()


if __name__ == '__main__':
    ss=Suopei()
    a=ss.jichu_shuju(10,1)
    print(a)

    # aa=xuexiao()
    # a=aa.kuaicha('郑州')
    # print(a)




