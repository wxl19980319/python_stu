#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

import requests

class Suopei_dingdan(object):

    def dingdan(self,c,d):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/queryApplication'
        head={
            'Content-Type': "application/json",
            'x-dealer-code': "2100150",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "QUERY_APPLICATION",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "djy0mx",
            'x-access-token': "0da5606a534fa727dfd7f502df38be65",
            'cache-control': "no-cache",
            'Postman-Token': "21b55e5a-3998-4cf3-96c3-d8bb3ad29906"
        }

        body='{"pageNum":%s,"pageSize":%s,"orderByField":"","orderByrule":"","status":"","applicationType":"","applicationMode":"","applicationNo":"","partCode":"","applicationStartDate":"","applicationEndDate":""}' % (c,d)
        body=body.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        return res.json()


if __name__ == '__main__':
    aaa=Suopei_dingdan()
    a=aaa.dingdan(1,10)
    print(a)