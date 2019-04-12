#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL



#定义登录函数
from  appium import webdriver
from  time import sleep


def denglu(arg,u,p):
    arg.find_element_by_id('com.netease.cloudmusic:id/qc').click()
    sleep(2)
    arg.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('{}'.format(u))
    sleep(2)
    arg.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('{}'.format(p))
    sleep(2)
    arg.find_element_by_id('com.netease.cloudmusic:id/qc').click()
    sleep(6)
    arg.find_element_by_id('com.netease.cloudmusic:id/qn').click()
    sleep(2)

    aa = arg.find_element_by_id('com.netease.cloudmusic:id/af4').text
    return aa


def denglu1(arg1,u,p):
    arg1.find_element_by_id('com.netease.cloudmusic:id/qc').click()
    sleep(2)
    arg1.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('{}'.format(u))
    sleep(2)
    arg1.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('{}'.format(p))
    sleep(2)
    arg1.find_element_by_id('com.netease.cloudmusic:id/qc').click()
    sleep(6)
    a = arg1.find_element_by_id('com.netease.cloudmusic:id/qc').text
    return a