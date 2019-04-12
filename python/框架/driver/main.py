#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL


from 框架.report.baogao import  baogao

def run(aa):
    baogao(aa)

with open('回归.txt','r') as f:
    a=f.readlines()
    if a[0].strip()== 'all':
        run('*')
    else:
        run(a)