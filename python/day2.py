#!/usr/bin/python
#-*- coding:utf-8 -*-
#User:WXL



# from day1 import sum
#
#
# print(sum(12,3))
# print(__name__)

# # 1
# a=input('>>>>')
# b=len(a)//2
# for i in range(b):
#     if a[i]!=a[-i-1]:
#         print('不是回文')
#         break
# else:
#     print('回文')

# # 2
# a=int(input('>>>'))
# b=int(input('>>>'))
# c=int(input('>>>'))
# d=[a,b,c]
# d.sort()
# if d[0]+d[1]>d[2]:
#     if d[0]**2+d[1]**2>d[2]**2:
#         print('锐角')
#     elif d[0]**2+d[1]**2==d[2]**2:
#         print('直角')
#     else:
#         print('钝角')

# # 3
# a=['1','5','p']
# b=''.join(a)
# print(b)
#
# asd={'name':'小明','age':19,'sex':'男'}
# print(asd.keys())
# print(asd.values())
# print(asd.items())

# # 4
# for i in range(1,100):
#     for j in range(1,100):
#         for k in range(1,100):
#             if i+j+k==100 and 2*i+j+0.5*k==100:
#                 print('公鸡{},母鸡{},小鸡{}'.format(i,j,k))

# # 5
# a=[1,2,3,4,3,5,2]
# # b=list(set(a))
# # print(b)

# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#     else:
#         continue
# print(b)



# # 8
# def asd(x,y):
#     for i in range(len(x)):
#         for j in range(i+1,len(x)):
#             if x[i]+x[j]==y:
#                 print(x[i],x[j])
#
# asd([1,2,5,6,3],7)


# 9
# import xlrd
# f=xlrd.open_workbook('信息表.xls')
# sheet=f.sheets()[0]
# c=[]
# for i in range(sheet.nrows):
#     a=sheet.row_values(i)
#     # print(a)
#     j=','.join(a)
#     # print(j)
#     if j[-1]==',':
#         j=j.split(',')
#         j.pop(-1)
#         j=','.join(j)
#         c.append(j)
#     else:
#         c.append(j)
# print(c)
# with open('f.txt','w',encoding='utf-8') as q:
#     for i in c:
#         if i==c[-1]:
#             q.write(i)
#         else:
#             q.write(i)
#             q.write('\n')


# 10
# with open('f.txt','r',encoding='utf-8') as qq:
#     a=qq.readlines()
# # print(a)
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('lianxi')
# for i in range(len(a)):
#     b=a[i].replace('\n','').split(',')
#     # print(b)
#     for j in range(len(b)):
#         sheet.write(i,j,b[j])
# f.save('lianxi.xls')


# # 11
# a=[12,56,56,4,2,3,1,1]
# b=a.copy()
# b=list(set(a))
# b.sort()
# for i in a:
#     if i==b[-1] or i==b[-2]:
#         print(i)

# # 12

# 13# a='12345'
# # a=a[::-1]
# # sum=0
# # for i in range(10):
# #     for j in range(len(a)):
# #         if str(i)==a[j]:
# #            sum+=i*10**j
# # print(sum)
# def shu(x):
#     z=[str(i) for i in range(10)]+[chr(j) for j in range(97,103)]
#     a=[]
#     while True:
#         x,b=divmod(x,16)
#         a.append(z[b])
#         if x==0:
#             break
#     a.reverse()
#     b=''.join(a)
#     return b
#     # c=''
#     # for i in a:
#     #     c+=i
#     # print(c)
# print(shu(1000))


# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('la')
# sheet1=f.add_sheet('hi')
# f.save('suibian.xls')


# def asd():
#     a=[]
#     for i in range(5):
#         b=input('>>>')
#         a.append(b)
#     import random
#     x=random.randint(0,4)
#     print(a[x])
# asd()

#
# class qwe():
#     def asd(self):
#         a=[]
#         for i in range(2,100):
#             for j in range(2,i+1):
#                 if i%j==0:
#                     break
#             if i==j:
#                 a.append(i)
#         for k in range(6,101,2):
#             for h in range(len(a)):
#                 for l in range(h+1,len(a)):
#                     if a[h]+a[l]==k:
#                         print(k ,a[h],a[l])



# import day1
# a=day1.小艾()
# a.bo()
# a.dui()




# def abc(s,x,y=0):
#     a=list(s)
#     for i in range(y):
#         # if y==0:
#         #     print(s)
#         #     break
#         # elif y>len(s)-1:
#         #     break
#         if y>0:
#             a.pop(x+1)
#     c = ''.join(a)
#     print(c)
# abc('abcdef',0,4)






# import requests
# import re
# class 糗事_Spider(object):
#     def 发送请求(self,page):
#         url='https://www.qiushibaike.com/text/page/{}/'.format(page)
#         #伪装成浏览器
#         head={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
#         }
#         #发送请求
#         响应=requests.get(url=url,headers=head)
#         #读取响应 1、text 2、content
#         # with open('ff.html','w',encoding='utf-8')as f:
#         #     f.write(响应.text)
#         html=(响应.content.decode('utf-8'))
#         #返回结果并赋值
#         return html
#     def guolv(self,asd):
#         shuju=[]
#         #将正则表达式编译
#         patt=re.compile(r'<div class="content">(.*?)</span>',re.S)
#         #将编译后的条件到字符串中查找
#         items=patt.findall(asd)
#         for i in items:
#             a=i.replace('\n','').replace('<span>','').replace('<br/>','')
#             shuju.append(a)
#         return shuju
#     def save(self,q):
#         with open('aa.txt','a',encoding='utf-8') as f:
#             for i in q:
#                 f.write(i+'\n')
#
# qiu = 糗事_Spider()
#
# html=qiu.发送请求(1)
# shuju=qiu.guolv(asd=html)
# qiu.save(shuju)


# # ####################豆瓣电影############################################
# import requests
# import re
# import xlwt
# mingc = []
# daoy = []
# miaoshu = []
# renshu = []
# class 豆瓣_Spider(object):
#     def qingqiu(self,page):
#         url='https://movie.douban.com/top250?start={}&filter='.format(page)
#         head={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
#         }
#         res=requests.get(url=url,headers=head)
#         html=(res.content.decode('utf-8'))
#         return html
#     def guolv(self,a):
#         # mingc=[]
#         # daoy=[]
#         # miaoshu=[]
#         # renshu=[]
#         patt0=re.compile(r'<ol class="grid_view">(.*?)</ol>',re.S)
#         items0=patt0.findall(a)
#         patt1= re.compile(r'<li>(.*?)</li>', re.S)
#         items1 = patt1.findall(items0[0])
#         # print(items1)
#         for i in items1:
#             patt2= re.compile(r'<span class="title">(.*?)</span>', re.S)
#             items2 = patt2.findall(i)
#             mingc.append(items2[0])
#         # print(mingc)
#         for i in items1:
#             patt3 = re.compile(r'导演:(.*?)&nbsp;&nbsp')
#             items3 = patt3.findall(i)
#             items3=''.join(items3)
#             daoy.append(items3)
#         # print(daoy)
#         for i in items1:
#             patt4 = re.compile(r'<span class="inq">(.*?)</span>', re.S)
#             items4 = patt4.findall(i)
#             items4 = ''.join(items4)
#             miaoshu.append(items4)
#         # print(miaoshu)
#         for i in items1:
#             patt5= re.compile(r'<span>(.*?)人', re.S)
#             items5 = patt5.findall(i)
#             items5 = ''.join(items5)
#             renshu.append(items5)
#         # print(renshu)
#         return mingc,daoy,miaoshu,renshu
#     def save(self,aa,bb,cc,dd):
#         ee=list(zip(aa,bb,cc,dd))
#         # print(ee)
#         f = xlwt.Workbook(encoding='utf-8')
#         sheet = f.add_sheet('lala')
#         sheet.write(0,0,'名称')
#         sheet.write(0, 1, '导演')
#         sheet.write(0, 2, '描述')
#         sheet.write(0, 3, '评价人数')
#         for i in range(len(ee)):
#             for j in range(len(ee[i])):
#                 sheet.write(i+1,j,ee[i][j])
#         f.save('豆瓣2.xls')
#
#
# #         for i in range(len(aa)):
# #             sheet.write(i+1,0,aa[i])
# #         for j in range(len(bb)):
# #             sheet.write(j+1,1,bb[j])
# #         for k in range(len(cc)):
# #             sheet.write(k+1,2,cc[k])
# #         for l in range(len(dd)):
# #             sheet.write(l+1,3,dd[l])
# #         f.save('豆瓣.xls')
# #
# dou=豆瓣_Spider()
# for i in range(0,226,25):
#     a=dou.qingqiu(i)
#     aa,bb,cc,dd=dou.guolv(a)
# dou.save(aa,bb,cc,dd)
#################################################################


# a=['asd','asdf']
# b=[1,2]
# c=list(zip(a,b))
# print(c[1][0])

# import json
# a={'name':123}
#
# #将字典变成json数据
# json_data=json.dumps(a)
# print(json_data)
#
# #将json数据变成字典
# asd=json.loads(json_data)
# print(asd)




############################智联招聘信息############################
# import xlwt
# import json
# import requests
# class 智联_Spider(object):
#     def qingqiu(self,page):
#         url='https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.66660019&x-zp-page-request-id=807fef8685a042a2b85172f0e0aee46e-1550652455429-9742'.format(page)
#         head={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
#         }
#         res=requests.get(url=url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,a):
#         mingc=[]
#         diqu=[]
#         xueli=[]
#         xinzi=[]
#         daiyu=[]
#         asd=json.loads(a)
#         for i in range(90):
#             aa=(asd['data']['results'][i]['company']['name'])
#             mingc.append(aa)
#             bb=(asd['data']['results'][i]['city']['display'])
#             diqu.append(bb)
#             cc=(asd['data']['results'][i]['eduLevel']['name'])
#             xueli.append(cc)
#             dd=(asd['data']['results'][i]['salary'])
#             xinzi.append(dd)
#             ee=(asd['data']['results'][i]['welfare'])
#             eee=','.join(ee)
#             daiyu.append(eee)
#         print(mingc)
#         print(diqu)
#         print(xueli)
#         print(xinzi)
#         print(daiyu)
#         return mingc,diqu,xueli,xinzi,daiyu
#     def save(self,aa,bb,cc,dd,ee):
#         ff= list(zip(aa, bb, cc, dd,ee))
#         print(ff)
#         f = xlwt.Workbook(encoding='utf-8')
#         sheet = f.add_sheet('智联')
#         sheet.write(0,0,'公司名称')
#         sheet.write(0, 1, '地区')
#         sheet.write(0, 2, '要求学历')
#         sheet.write(0, 3, '薪资')
#         sheet.write(0,4,'福利待遇')
#         for i in range(len(ff)):
#             for j in range(len(ff[i])):
#                 sheet.write(i+1,j,ff[i][j])
#             f.save('智联1.xls')
#
# zhi=智联_Spider()
# a=zhi.qingqiu(0)
# aa,bb,cc,dd,ee=zhi.guolv(a)
# zhi.save(aa,bb,cc,dd,ee)
####################################################################################

###################斗图###################
# import requests
# import re
# import os
# mingz=[]
# wangz=[]
# shuju=[]
# class 斗图_spider(object):
#     def qingqiu(self,page):
#         url='http://www.doutula.com/article/list/?page={}'.format(page)
#         head={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
#         }
#         res=requests.get(url=url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,a):
#         # mingz=[]
#         # wangz=[]
#         # shuju=[]
#         patt0=re.compile(r'<div class="random_title">(.*?)<div class="date">')
#         items0=patt0.findall(a)
#         for i in items0:
#             mingz.append(i)
#         # print(mingz)
#         patt1=re.compile(r'<a href="(.*?)" class="list-group-item')
#         items1=patt1.findall(a)
#         # print(items1)
#         for j in items1:
#             wangz.append(j)
#         # print(wangz)
#         for k in wangz:
#             url1=k
#             head1={
#                 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
#             }
#             res1=requests.get(url=url1,headers=head1)
#             html1=res1.content.decode('utf-8')
#             patt2=re.compile(r"this.src='(.*?)'")
#             itmes2=patt2.findall(html1)
#             shuju.append(itmes2)
#         # print(shuju)
#         ff = list(zip(mingz,shuju))
#         print(ff)
#         return ff
#     def save(self,ff):
#         for rr in mingz:
#             os.mkdir(rr)
#         for r in ff:
#             aa=r[1][0].split('.')
#             if aa[-1] == 'jpg':
#                 for jj,ii in enumerate(r[1]):
#                     res2=requests.get(ii)
#                     ht=res2.content
#                     with open(r'C:/Users/WXL/Desktop/python_学习/{}/{}.jpg'.format(r[0],jj + 1), 'wb') as f:
#                                     f.write(ht)
#             else:
#                 for jj,ii in enumerate(r[1]):
#                     res2=requests.get(ii)
#                     ht1=res2.content
#                     with open(r'C:/Users/WXL/Desktop/python_学习/{}/{}.gif'.format(r[0],jj + 1), 'wb') as f:
#                                     f.write(ht1)
#
#
# dou=斗图_spider()
# # for i in range(1,4):
# a=dou.qingqiu(3)    #页数
# ff=dou.guolv(a)
# dou.save(ff)
###############################################################################################


###############TCP ##################################
# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('127.0.0.1',8888))
# while True:
#     msg=input('>>>>')
#     if msg!='exit':
#         sock.send(msg.encode('utf-8'))
#
#         reg = sock.recv(1024)
#         print(reg.decode('utf-8'))
#     else:
#         sock.close()
#         break


#################################

####### UDP######################
# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# while True:
#     a=input('>>>>>')
#     if a!='exit':
#         host=('127.0.0.1',8888)
#         sock.sendto(a.encode('utf-8'),host)
#
#         msg=sock.recv(1024)
#         print(msg.decode('utf-8'))
#     else:
#         sock.close()
#         break

# a={'sss':45}
# print(a['sss'])

# a=[sum(range(101))]
# print(a)


# import requests
# # import json
# url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
#
# # body = "{\r\t\"method\": \"getOrderQueryList\",\r\t\"queryMethod\": \"全部\",\r\t\"code\": \"\",\r\t\"queryDate\": \"\",\r\t\"queryEndDate\": \"\",\r\t\"orderStatus\": \"未签收\",\r\t\"orderPriority\": \"全部\",\r\t\"orderException\": \"全部\",\r\t\"status\": \"全部\",\r\t\"pageSize\": 10,\r\t\"curPage\": 1\r}"
# head = {
#     'Content-Type': "application/json",
#     'x-dealer-code': "2100150",
#     'x-position-code': "D_PO_1028",
#     'x-resource-code': "BASIC_DATA",
#     'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#     'x-user-code': "djy0mx",
#     'x-access-token': "0da5606a534fa727dfd7f502df38be65",
#     # 'cache-control': "no-cache",
#     # 'Postman-Token': "da05ee37e5676e7b27972b2892e0fdeb"
#     }
# body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode('utf-8')
#
# res=requests.post(url=url,headers=head,data=body)
# mes=res.json()
# # mes=json.loads(res.text)
# print(mes)
# # assert  mes['data']['applicationType'][0]['name']=='多装'
# # assert  mes['data']['applicationType'][0]['value']=='1'



# def jiekou():
#     url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4return/App/basicData"
#     head = {
#         'Content-Type': "application/json",
#         'x-dealer-code': "2100150",
#         'x-position-code': "D_PO_1028",
#         'x-resource-code': "BASIC_DATA",
#         'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#         'x-user-code': "djy0mx",
#         'x-access-token': "0da5606a534fa727dfd7f502df38be65",
#         # 'cache-control': "no-cache",
#         # 'Postman-Token': "da05ee37e5676e7b27972b2892e0fdeb"
#     }
#     body = '{"method": "getOrderQueryList","queryMethod": "全部","code": "","queryDate": "","queryEndDate": "","orderStatus": "未签收","orderPriority": "全部","orderException": "全部","status": "全部","pageSize": 10,"curPage": 1}'.encode(
#         'utf-8')
#
#     res = requests.post(url=url, headers=head, data=body)
#     mes = res.json()
#     return mes
#
# mes=jiekou()
#
# import time
# import HTMLTestRunner  #产生测试报告的
# import requests
# import unittest
# class Suopei(unittest.TestCase):
#     def test_1(self):
#         # mes=jiekou()
#         self.assertEqual(mes['data']['applicationType'][0]['name'],'多装')
#
#     def test_2(self):
#         # mes=jiekou()
#         self.assertNotEqual(mes['data']['applicationType'][0]['name'], '装')
#
#     def test_3(self):
#         # mes=jiekou()
#         self.assertTrue(mes['data']['applicationType'][0]['name'])
#
#     def setUp(self):
#         print('hello')
#
#     def tearDown(self):
#         print('lala')
#
#     def test_4(self):
#         self.assertEqual(123,123)
#
#
# if __name__ == '__main__': #main：检测类中所有以test开头的函数  比较test后面的字符，谁在前就执行谁
#     #创建一个测试套件
#     suit = unittest.TestSuite()
#     #添加测试用例
#     for i in range(1,5):
#         suit.addTest(Suopei('test_{}'.format(i)))
#     now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#     f= open('abcde.html','wb')
#     #定义测试报告的内容
#     runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='索赔测试报告',tester='位晓磊',description='结果如下')
#     runner.run(suit)
#     f.close()






# from selenium import webdriver
# from time import sleep
#
# #定义使用什么浏览器
# dr= webdriver.Chrome()
#
# #打开网址
# # dr.get('https://www.baidu.com')
# # sleep(2)
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


#关闭浏览器 ,断开连接
# dr.quit()

# 关闭浏览器，不断开连接
# dr.close()



# class 小艾(object):
# #     def bo(self):
# #         self.asd()
# #         print('ge qu')
# #     def dui(self):
# #         print('dui hua')
# #     def asd(self):
# #         print('hllow')
# #         pass
# # 小艾().bo()
# from selenium import webdriver
# def dr():
#     dr=webdriver.Chrome()
#     return dr
# print(dr())