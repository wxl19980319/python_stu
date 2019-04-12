#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL


from selenium import webdriver
from time import sleep

# def dr():
#     dr=webdriver.Chrome()
#     return dr


class QQ_kongjian(object):

    def kongjian_denglu(self,u,p):
        # global dr
        dr= webdriver.Chrome()
        dr.get('https://www.qzone.qq.com')
        sleep(2)

        dr.switch_to.frame('login_frame')
        sleep(2)

        dr.find_element_by_css_selector('#switcher_plogin').click()
        sleep(2)

        dr.find_element_by_id('u').send_keys('{}'.format(u))
        sleep(2)
        dr.find_element_by_id('p').send_keys('{}'.format(p))
        sleep(2)
        dr.find_element_by_id('login_button').click()
        sleep(10)



        return dr.title


if __name__ == '__main__':
    aa=QQ_kongjian()
    a=aa.kongjian_denglu('1147695719','18339914556.080')
    print(a)
