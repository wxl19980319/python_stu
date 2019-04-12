#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL


import requests


class Zuoye_dingdan(object):

    def shouye_zhuangtai(self):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderHomePage'
        head={
            'Content-Type': "application/json",
            'x-dealer-code': "2100005",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderHomePage",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "0da5606a534fa727dfd7f502df38be65",
            'cache-control': "no-cache",
            'Postman-Token': "3708ccbb-25c7-44be-b74a-bb6aa05ec848"
        }
        res=requests.post(url=url,headers=head)
        return res.json()

    def chaxun_dingdan(self,a,b):
        url='https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderList'
        head={
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderList",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "0da5606a534fa727dfd7f502df38be65",
            'cache-control': "no-cache",
            'Postman-Token': "e99dd8d3-7074-4b85-9b92-fec6aaa154f8"
        }
        body='{"pageNum": %s,"pageSize": %s,"queryTerms": {"orderType": "","orderStatus": "","orderDelayFlag": "","orderNo": "","startReportDate": "","endReportDate": ""}}' %(a,b)
        body=body.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        return res.json()

    def peijian_mingxi(self,a):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail'
        head={
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderPartDetail",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "0da5606a534fa727dfd7f502df38be65",
            'cache-control': "no-cache",
            'Postman-Token': "00587d6d-f948-4bbf-a39e-892ca095a9a3"
        }
        body='{"partOrderItemId":%s}' % (a)
        body=body.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        return res.json()

    def dingdan_mingxi(self,a,b,c):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch'
        head={
            'Content-Type': "application/json",
            'x-dealer-code': "2100005",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "0da5606a534fa727dfd7f502df38be65",
            'cache-control': "no-cache",
            'Postman-Token': "ccd2b6f8-5d64-4cce-97e1-53e54498aa6d"
        }
        body='{"pageNum":%s,"pgeSize":%s,"queryTerms":{"orderNo":%s}}' %(a,b,c)
        body=body.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        return res.json()

    def suopei_dingdan(self,a,b):
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
            'Postman-Token': "bebd8b89-866a-4e32-ae1e-cb81f2af06f8"
        }
        body='{"pageNum":%s,"pageSize":%s,"orderByField":"","orderByrule":"","status":"","applicationType":"","applicationMode":"","applicationNo":"","partCode":"","applicationStartDate":"","applicationEndDate":""}'%(a,b)
        body=body.encode('utf-8')
        res=requests.post(url=url,headers=head,data=body)
        return res.json()


if __name__=='__main__':
    aa=Zuoye_dingdan()

    a=aa.shouye_zhuangtai()
    print(a)

    # b=aa.chaxun_dingdan(1,10)
    # print(b)

    # c=aa.peijian_mingxi(3108)
    # print(c)

    # d=aa.dingdan_mingxi(1,10,'"V2100880181219390"')
    # print(d)

    # e=aa.suopei_dingdan(1,10)
    # print(e)
