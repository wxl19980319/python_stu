#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

import xlrd

class Canshu(object):

    def zhaohao_mima(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\WXL\Desktop\python_学习\框架\data\浙大教室.xlsx')
        sheet=f.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju

if __name__ == '__main__':
    aa=Canshu()
    a=aa.zhaohao_mima()
    print(a)