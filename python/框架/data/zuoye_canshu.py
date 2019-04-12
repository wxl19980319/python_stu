#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

import xlrd

class Zuoye_canshu(object):

    def chaxun_1canshu(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\WXL\Desktop\python_学习\框架\data\查询订单.xlsx')
        sheet=f.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju

    def peijian_2canshu(self):
        shuju=[]
        f = xlrd.open_workbook(r'C:\Users\WXL\Desktop\python_学习\框架\data\配件明细.xlsx')
        sheet = f.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju

    def dingdan_3canshu(self):
        shuju = []
        f = xlrd.open_workbook(r'C:\Users\WXL\Desktop\python_学习\框架\data\订单明细.xlsx')
        sheet = f.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju

    def suopei_4canshu(self):
        shuju = []
        f = xlrd.open_workbook(r'C:\Users\WXL\Desktop\python_学习\框架\data\索赔订单.xlsx')
        sheet = f.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju


if __name__ == '__main__':
    aa=Zuoye_canshu()

    # a=aa.chaxun_1canshu()
    # print(a)

    # b=aa.peijian_2canshu()
    # print(b)

    # c=aa.dingdan_3canshu()
    # print(c)

    d=aa.suopei_4canshu()
    print(d)