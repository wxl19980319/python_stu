#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL


import xlrd

class dingdan_shuju(object):

    def dingdan_duqu(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\WXL\Desktop\python_学习\框架\data\dingdan.xlsx')
        sheet=f.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return  shuju

if __name__ == '__main__':
    qq=dingdan_shuju()
    a=qq.dingdan_duqu()
    print(a)