#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

import xlrd

class kuaicha_shuju(object):

    def didian_mingcheng(self):
        shuju=[]
        ff=xlrd.open_workbook(r'C:\Users\WXL\Desktop\python_学习\框架\data\didian.xlsx')
        sheet=ff.sheets()[0]
        for i in range(sheet.nrows):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return  shuju

if __name__ == '__main__':
    cc = kuaicha_shuju()
    print(cc.didian_mingcheng())