#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL


import xlrd

class QQkongjian_canshu(object):

    def zhanghao_mima(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\WXL\Desktop\python_学习\框架\data\qq空间.xlsx')
        sheet=f.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju


if __name__ == '__main__':
    bb=QQkongjian_canshu()
    b=bb.zhanghao_mima()
    print(b)