#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL


# from selenium import webdriver
# from time import sleep
#
# #定义使用什么浏览器
# dr= webdriver.Chrome()

#打开网址
# dr.get('https://www.baidu.com')
# sleep(2)
# dr.get('https://www.ctrip.com')
# sleep(2)

# #获取网址的标题
# print(dr.title)
# #获取打开网页的网址
# print(dr.current_url)
#
# dr.get('https://www.jd.com')
# sleep(2)
#
# #回退
# dr.back()
# sleep(2)
#
# #前进
# dr.forward()
# sleep(2)
#
# #设置浏览器的大小
# dr.set_window_size(400,400)
# sleep(2)
#
# #设置浏览器的位置
# dr.set_window_position(600,100)
# sleep(2)
#
# #设置浏览器最大化（全屏）
# dr.maximize_window()
# sleep(2)
#
# #设置浏览器最小化
# dr.minimize_window()
# sleep(2)

#定位 1、通过 id 来定位 （标签的id属性）
# dr.find_element_by_id('kw').send_keys('python')
# sleep(2)
#
# dr.find_element_by_id('su').click()
# sleep(2)

#定位 2、通过 class_name 来定位 （标签的class属性）
# dr.find_element_by_class_name('s_ipt').send_keys('python')
# sleep(2)
#
# # dr.find_element_by_class_name('bg b_btn').click()
# # sleep(2)

# 定位 3、通过 name 来定位 （标签的name属性）
# dr.find_element_by_name('wd').send_keys('python')
# sleep(2)
#
# dr.find_element_by_id('su').click()
# sleep(2)

# 定位 4、通过 text 来定位 （标签的文本属性）
# dr.find_element_by_link_text('hao123').click()
# sleep(2)

# 定位 5、通过 标签的模糊文本 来定位 （标签的文本属性）
# dr.find_element_by_partial_link_text('hao').click()
# sleep(2)

# 定位 6、通过 标签的名称 来定位 （标签的  属性） 最不唯一的定位，通常用来定位一组数据
# dr.find_elements_by_tag_name('')

# 定位 7、通过 css 来定位 （标签的  属性）
# dr.find_element_by_css_selector('#kw').send_keys('python')
# sleep(2)

# 定位 8、通过 xpath 来定位 （标签的  属性） xpath:路径标记语言、 xml:可扩展性标记语言
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
# sleep(2)

#定位一组数据 同时对多个数据进行操作时
# wd=dr.find_elements_by_class_name('mnav')
# for i in wd:
#     # print(i.text)
#     a='i.text'
#     if a =='hao123':
#         continue
#     else:
#         dr.find_element_by_link_text('a').click()
#         sleep(2)
#         dr.back()


#层级定位  遇到复杂的元素定位时

# qwe=dr.find_element_by_id('searchHotelLevelSelect')
# wd=qwe.find_elements_by_tag_name('option')
# for i in wd:
#     i.click()
#     sleep(2)


#处理框架
# #ifarme(窗口)
# dr.switch_to.frame('login_frame') #切换到某一个框架
#
# dr.switch_to.default_content() #回到最开始的页面上
#
# dr.switch_to.parent_frame() #回到父框架页面中



#处理浏览器窗口
#
# from selenium import webdriver
# from time import sleep
#
# #定义使用什么浏览器
# dr= webdriver.Chrome()
#
# #打开网址
# dr.get('https://www.douban.com')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# sleep(2)
#
# #获取当前窗口的字符串（句柄）
# print(dr.current_window_handle)
# print(dr.title)
#
# #获取所有窗口的句柄
# qq=dr.window_handles
# print(qq)
#
# #切换句柄  参数只能是句柄
# dr.switch_to.window(qq[-1])
# print(dr.title)



# ###########对鼠标的操作###########################################
#
# #move_to_element  把鼠标移动到元素的中心点
#
#
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
#
# #定义使用什么浏览器
# dr= webdriver.Chrome()
# dr.maximize_window()
# #打开网址
# dr.get('https://www.jd.com')
# sleep(2)
#
# w=dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_tag_name('li')
# # print(len(w))
#
# for i in w:
#     #控制鼠标来移动到元素的位置上          执行
#     ActionChains(dr).move_to_element(i).perform()   #动作链  控制动作（鼠标）
#     sleep(2)
#
# # ActionChains(dr).move_by_offset(20,10).perform()  #移动到某一个方位上面
#
# dr.quit()
###########################################################





###################鼠标拖拽  drag_and_drop 拖拽#########################################
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
#
# dr= webdriver.Chrome()
# dr.get('https://www.baidu.com')
# sleep(2)
# dr.maximize_window()
#
# dr.find_element_by_id('kw').send_keys('京东')
# sleep(2)
# dr.find_element_by_id('su').click()
# sleep(2)
#
#
# dr.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
# sleep(2)
#
# #获取当前窗口的字符串（句柄）
# print(dr.current_window_handle)
# print(dr.title)
#
# #获取所有窗口的句柄
# jd=dr.window_handles
# print(jd)
#
# #切换句柄  参数只能是句柄
# dr.switch_to.window(jd[-1])
# print(dr.title)
# sleep(5)
#
# dr.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="loginname"]').send_keys('18339914556')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('wxl18339914556')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="loginsubmit"]').click()
# sleep(10)
#
# start=dr.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
# # sleep(5)
#
# ##drag_and_drop (起始位置  结束位置)
# ##drag_and_drop_offset(起始位置，x粥坐标，y轴坐标)
#
#
# ActionChains(dr).drag_and_drop_by_offset(start,68,0).perform()
# sleep(2)
#
# dr.quit()
############################################################################


# ###############处理弹出框#####################
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
#
# dr= webdriver.Chrome()
# dr.get('http://www.lwfree.cn/yurenjie/yuerenjie1.html')
# sleep(2)
# # dr.maximize_window()
#
# ##切换到弹出框
# ww=dr.switch_to_alert()
# #获取弹出框上的内容  print(ww.text)
# while True:
#     print(ww.text)
#     #点击确定
#     ww.accept()
#     sleep(2)

#ww.dismiss() 点击取消
#ww.send_keys('内容') 输入
#################################################################



############3处理页面滚动条######################################
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
#
# dr= webdriver.Chrome()
# dr.get('https://www.jd.com')
# sleep(2)
# dr.maximize_window()
#
# #处理页面滚动条  Javascript代码
# for i in range(1,10000,2000):
#     js="var q=document.documentElement.scrollTop={}".format(i)
#     #执行Javascript语句
#     dr.execute_script(js)
#     sleep(2)
#########################################################



######智能等待  wait################################3
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# import selenium.webdriver.support.ui as ui
#
#
# dr= webdriver.Chrome()
# dr.get('https://www.jd.com')
#
# sleep(2)  #强制等待
# dr.maximize_window()
#
# #智能等待 设置一个最大等待时间  检测某个元素出现，就不会等待下去
#
# #设置最大等待时间
# unit=ui.WebDriverWait(dr,10)
# #直到定位的元素出现了就 不等待了
# unit.until(lambda dr:dr.find_element_by_xpath('//*[@id="navitems-group1"]/li[1]/a'))
#
# print('hello')
#########################################################



##############获取定位到的元素某个属性的值#############
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# import selenium.webdriver.support.ui as ui
#
#
# dr= webdriver.Chrome()
# dr.get('https://www.jd.com')
#
# sleep(2)  #强制等待
# dr.maximize_window()
#
# w=dr.find_element_by_xpath('//*[@id="navitems-group1"]/li[1]/a')
# #获取定位到的元素某个属性的值
# a=w.get_attribute('href')
# print(a)
# dr.quit()
##############################################################