#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL


from  time import sleep

def denglu(arg,u,p):
    arg.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserName').send_keys('{}'.format(u))
    sleep(2)
    arg.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserPas').send_keys('{}'.format(p))
    sleep(2)
    arg.find_element_by_id('net.crigh.cgapp_schedule:id/btnLogin').click()
    sleep(2)
    arg.find_element_by_id('net.crigh.cgapp_schedule:id/cancel').click()
    sleep(2)

    a =arg.find_element_by_id('net.crigh.cgapp_schedule:id/tv_title').text
    return a

def denglu1(arg,u,p):
    arg.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserName').send_keys('{}'.format(u))
    sleep(2)
    arg.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserPas').send_keys('{}'.format(p))
    sleep(2)
    arg.find_element_by_id('net.crigh.cgapp_schedule:id/btnLogin').click()
    sleep(2)
    aa=arg.find_element_by_id('net.crigh.cgapp_schedule:id/btnLogin').text
    return aa