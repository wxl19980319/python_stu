#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL

from  appium import webdriver
from  time import sleep

desired_caps = {'platformName':'Android',
                # 'platfromVersion':'6.0',
                'deviceName':'1dfccc61',
                'appPackage':'com.netease.cloudmusic',
                'appActivity':'.activity.LoadingActivity'}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

sleep(7)


driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
sleep(2)
driver.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('18339914556')
sleep(2)
driver.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('wxl0801')
sleep(2)
driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
sleep(2)
# a=driver.find_element_by_id('com.netease.cloudmusic:id/qc').text
# print(a)
#断言
driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()
sleep(2)
#
# aa = driver.find_element_by_id('com.netease.cloudmusic:id/af4').text
# print(aa)


# driver.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserName').send_keys('1138100001')
# sleep(2)
# driver.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserPas').send_keys('12456')
# sleep(2)
# driver.find_element_by_id('net.crigh.cgapp_schedule:id/btnLogin').click()
# sleep(2)
# aa=driver.find_element_by_id('net.crigh.cgapp_schedule:id/btnLogin').text
# print(aa)
# '登 录'
# driver.find_element_by_id('net.crigh.cgapp_schedule:id/cancel').click()
# sleep(2)

# a=driver.find_element_by_id('net.crigh.cgapp_schedule:id/tv_title').text
# print(a)






# driver.quit()

