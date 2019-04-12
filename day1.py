#!/usr/bin/python
#-*-coding:utf-8 -*-

# print(123)
# print('lalalala@#$%')
# print("河南")

# print(123)
# print('ddd')
# a,b,c=1,2,3
# print(a,b,c)
# fg=12.3
# qwe=12
# qew=float(qwe)
# print(type(qew))
# asd = None
# print(type(asd))
# ert = 4>3
# print(ert)
# a='qWerPe'
# print(a.endswith('Pe'))
# ab='eregregregrerergwg'
# f=ab.endswith('e')
# print(f)
# abc={'name':['小明','lala'],
#      'age':19,
#      'sex':'男'
#      }
# bc={'gdg':2323,'sfsf':234}
# abc.update(bc)
# # print(abc)
# # kkk={56,23,23,435,56,'dfadf'}
# # kkk.remove(435)
# # print(kkk)
# # a=(123,)
# # print(type(a))
# # print('df')
# # a='dfgkjg8778b'
# # print(a.split('jg'))

#1、、、、、
# a=input('成绩')
# a=int(a)
# if a>90 and a<=100:
# 	print('优秀')
# elif a<90 and a>=80:
# 	print('良好')
# elif a<80 and a>=70:
# 	print('及格')
# else:
# 	print('渣渣')

#2、、、、
# q=input('输入：')
# if q.startswith('a'):
#     if q.endswith('c'):
#       print('hello word')
# elif (q[0])=='a' and (q[-1])!='c':
#     print('hello')
# elif (q[0])!='a' and (q[-1])=='c':
#     print('word')
# else:
#     print('123')
# a={'name':'ldld','age':123}

#3、、、、、
# a=0
# for i in range(2,99,2):
#   a=a+i-1-i
# a+=99
# print(a)

#4、、、、、
# a=0
# b=0
# for i in range(1,100,2):
#     a+=i
# for i in range(2,100,2):
#     b+=i
# c=a-b
# print(c)

#1-2+3-4+5....-98+99
# a=0
# for i in range(1,100):
#     if i%2==0:
#         a-=i
#     else:
#         a+=i
# print(a)


# a=['abc'','df','Aghfc','AHDHDH','afhdfgh','dgfdc']
# for i in a:
#     if i[0]=='a' and i[-1]=='c':
#         print(i)
#     elif i[0]=='A' and i[-1]=='c':
#         print(i)



# import  random
# a=random.randint(1,10)
# #从一到10随机选中一个数，赋值给a
# print(a)


#猜数字
# import random
# b = random.randint(1, 10)
# for i in range(1,4):
#    a=input('输入一个数：')
#    a=int(a)
#    if a==b:
#       print('恭喜')
#       break
#    elif a<b:
#       print('小了')
#    else:
#       print('大了')
# else:
#    print('拿来吧你')


#判断三角形
# a=int(input('输入一个数：'))
# b=int(input('输入一个数：'))
# c=int(input('输入一个数：'))
# d = [a, b, c]
# d.sort()
# if d[0]+d[1]>d[2]:
#    if d[0]**2+d[1]**2>d[2]**2:
#       print('锐角')
#    elif d[0]**2+d[1]**2==d[2]**2:
#       print('直角')
#    else:
#       print('钝角')
# else:
#    print('不是三角形')


#水仙花数
# for i in range(100,1001):
#    a=str(i)
#    b=int(a[0])
#    c=int(a[1])
#    d=int(a[2])
#    if b**3+c**3+d**3==i:
#      print(i)
# #    else:
# #      continue

# for i in range(100,1000):
#    a=i//100
#    b=i//10%10
#    c=i%10
#    if a**3+b**3+c**3==i:
#       print(i)
#    else:
#       continue

#九九乘法表
# for i in range(1,10):
#    for j in range(1,i+1):
#       print('{}*{}={}'.format(j,i,j*i),end='\t')
#    print()

#100内质数之和
# a=0
# for i in range(2,100):
#    for j in range(2,i+1):
#       if i%j==0:
#          break
#    if i==j:
#     a+=i
# print(a)

#回文
# a=input('输入字符串：')
# x=len(a)//2
# for i in range(x):
#    if a[i]!=a[-i-1]:
#       print('不是回文')
#       break
# else:
#    print('回文')
#
# a=['sfSF','SDFDF','rrer']
# for i,j in enumerate(a):
#    print(i,j)




#
# z=int(input('输入总资产：'))
# """仓库"""
# a=[['电脑',1900],['空调',2000],["计算机",10],["电视",2500]]
# for i,j in enumerate(a):
#    print(i+1,j)
# """购买程序"""
# c=[]
# while True:
#     try:
#         b=input('您已进入购买程序，请输入商品号,如果想要退出，请输入EXIT')
#         if  b =='EXIT':
#             break
#         else:
#             b=int(b)
#             c.append(b)
#             print("成功添加{}".format(a[b-1][0]))
#             print('购物车',c)
#     except:
#         print('错')
#         e=input('是否结算：y结算，n不结算')
#         if e[0]=='y':
#             sum = 0
#             for i in c:
#                 sum+=a[i-1][1]
#             print('您共消费',sum)
#             if z>sum:
#                 print('购买成功','您还剩余',z-sum)
#                 break
#             else:
#                 print('余额不足')
#                 u = input('是否充值：y充值，n不充值移除商品')
#                 if u[0] == 'y':
#                     while z < sum:
#                         d = int(input('请输入充值金额：'))
#                         z+=d
#                         print('充值成功，当前余额', z)
#                         if z < sum:
#                             print('充的不够')
#                     print('购买成功', '您还剩余：', z - sum)
#                     break
#                 else:
#                     while z<sum:
#                         h = []
#                         g=input('请输入退掉的商品号：')
#                         g=int(g)
#                         h.append(g)
#                         for j in h:
#                             sum-=a[j-1][1]
#                             print('当前消费',sum)
#                             if sum>z:
#                                 print('余额不足')
#                             else:
#                                 print('购买成功，您还剩余',z-sum)
#                                 break
#         else:
#             continue







# while True:
# b=input('请输入商品号:')
# b=b.split(',')
# print('购物车',b)
# if b[0]=='1' and b[1]=='2' and b[2]=='3' and b[3]=='4':
#     for z in range(z,99999):
#         if z>6509:
#             print('购买成功','您还剩余',z-6509)
#             break
#         else:
#             print('余额不足')
#             c=input('是否充值：y充值，n不充值移除商品')
#             if c[0]=='y':
#                 while z<6509:
#                     d=int(input('请输入充值金额：'))
#                     z=z+d
#                     print('充值成功', z)
#                     if z<6509:
#                         print('充的不够')
#                 print('购买成功','您还剩余：',z-6509)
#





    # b[0]=1999
    # b[1]=2000
    # b[3]=10
    # b[4]=2500
    # if b[0]+b[1]>z:
    #     print('余额不足')
    # else:
    #     print('购买成功')



   #  if int(a[0][1])+int(a[1][1])>z:
   #     print('余额不足')
   # else:
   #     print('购买成功')
   # # if b=='exit':
   #    break
   # else:
   #    b=int(b)
   #    print(a[b-1])

#去虫
# ab=input('qingshuru:')
# a=ab.split(',')
# print(a)
# c=[]
# for i in a:
#     if i not in c:
#         c.append(i)
#     else:
#         continue
# print(c)

# c=[]
# a=[12,'ds',45,'fsaf']
# for i in a:
#     b=i
#     if type(b)!=str:
#         c.append(i)
#     else:
#         continue
# print(c)


#1+2+3+4+...+100
# print(c)
# a=0
# b=0
# while a<100:
#     a+=1
#     b+=a
# print(b)
#


# a=0
# while a<len(b):
#     print(b[a])
#     a+=1

# a=[]
# while True:
#     b=int(input(''))

#无限循环
# class Infinit:
#     def __iter__(self):
#         return self
#     def __next__(self):
#         return None
# for i in Infinit():
#     print("Python的无限循环!")

# def foe():
#     while True:
#         yield None
#
# for i in foe():
#     print('lalala')
#
# a=[17,'sdsd']
# print(type(a[0]))

# a=[]
# b=0
# d=0
# while True:
#     c=int(input('输入成绩：'))
#     if c<0:
#         break
#     else:
#        a.append(c)
#        b+=c
#        x=len(a)
#        d=b//x
#        print('平均分',d)
#        if c < d:
#         print('低于平均分的分数',c)

#平均分
# while True
#     b=input('>>>')
#     if b[0]=='-':
#         break
#     else:
#         a=b.split(',')
#         sum=0
#         for i in a:
#             sum+=int(i)
#         print('平均数为：',sum/len(a))
#         for j in a:
#             if int(j)<=sum/len(a):
#                 print('低于平均分的分数',j)

#冒泡法
# a=[56,45,78,88]
# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j] > a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]    #换位置
# print(a)

#冒泡法
# a=input('>>>>>')
# a=a.split(',')
# for i in range(len(a)):
#     for j in range(len(a)-1-i):
#         if int(a[j]) > int(a[j+1]):
#             a[j],a[j+1]=a[j+1],a[j]    #换位置
# print(a)

# 一个函数，传两个参数a,b，a是数组，b是一个数字，找出a数组中两数只和等于b，打印出来这两个数
# a=input('>>>>>')
# a=a.split(',')
# b=int(input('输入数字：'))
# for i in range(len(a)-1):
#     if int(a[i])+int(a[i+1])==b:
#         print(a[i],a[i+1])
# # # #
# a=input('>>>>>')
# a=a.split(',')
# b=int(input('输入数字：'))
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if int(a[i])+int(a[j])==b:
#           print(a[i],a[j])




# try:
#     a='123'
#     print(a+1)
# except Exception:
#     print('cuo')
# else:
#     print('wucuo')
# finally:
#     print('hello')





#结乘之和
# a=int(input('shu'))
# b=1
# c=0
# for i in range(1,a+1):
#     b*=i
#     c+=b
# print(c)


# 打印列表中的第一大和第二大的元素(所有)
# a=[12,34,56,56,34]
# b=a.copy()
# b=list(set(b))
# b.sort()
# for i in a:
#     if i==b[-1] or i==b[-2]:
#             print(i)

#(2)
# a=[12,34,56,56,34]
# b=a.copy()
# b.sort()
# x=b[-1]
# y=[]
# n=[]
# for i in b:
#     if i<x:
#         y.append(i)
#     else:
#         n.append(i)
# print('a列表中数第一大',n)
# z=y[-1]
# g=[]
# j=[]
# for p in y:
#     if p<z:
#         g.append(p)
#     else:
#         j.append(p)
# print('a列表中数第二大',j)


#1000以内因数之和等于本身的数
# for i in range(2,1000):
#     a = 0
#     for j in range(1,i):
#         if i%j==0:
#             a+=j
#     if i==a:
#         print(i)

# 公鸡、母鸡、小鸡
# for i in range(1,100):
#     for j in range(1,100):
#         for k in range(1,100):
#             if i*2+j*1+k*0.5==100 and i+j+k==100:
#                 print('公鸡{}，母鸡{}，小鸡{}'.format(i,j,k))

# 任意4个数字，组成不相同的三位数
# a=input('输入4个数：')
# b=a.split(',')
# for i in range(len(b)):
#     for j in range(len(b)):
#         for k in range(len(b)):
#             if b[i]!=b[j] and b[i]!=b[k] and b[j]!=b[k]:
#                 print(b[i],b[j],b[k])


# 一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# a=[1,2,2,4,5]
# b=int(input('输入一个数：'))
# for i in range(len(a)):
#     if b>a[i] and b<a[i+1]:
#         a.insert(i+1,b)
#     elif b>a[-1]:
#         a.append(b)
#     elif b<a[0]:
#         a.insert(0,b)
# print(a)


# 函数不用int将字符串变成整数
# def intstr(a):
#     # a=input('数：')
#     a=a[::-1]
#     sum=0
#     for i in range(len(a)):
#         for j in range(10):
#             if str(j)==a[i]:
#                 sum+=j*10**i
#     print(sum)
# intstr('12345')



# 将列表中最大的放在最后一位，最小的放在第一位
# b=1000%16
# a=1000//16%16
# c=1000//16//16%16
# print(c,a,b)



# 十进制转换成十六进制
# z=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']
# a=int(input('输入一个十进制数：'))
# c=[]
# while True:
#     b=a%16
#     a=a//16
#     c.append(z[b])
#     if a==0:
#         break
# c.reverse()
# d=''
# for i in c:
#     d+=i
# print(d)



# 将列表中的元素向左挪一位
# a=[1,2,3,4,5]
# a.insert(len(a),a[0])
# a.remove(a[0])
# print(a)


#
# a=open(r'C:\Users\WXL\Desktop\b.txt','w',encoding='utf-8')
# for i in range(10):
#     if i!=9:
#         a.write('{}\n'.format('abc'))
#     else:
#         a.write('{}'.format('abc'))
# a.close()


#九九乘法表写入文件
# a=open(r'C:\Users\WXL\Desktop\a.txt','w',encoding='utf-8')
# for i in range(1,10):
#    for j in range(1,i+1):
#       a.write('{}*{}={}\t'.format(j,i,j*i))
#    a.write ('\n')
# a.close()



# 图片
# a = open(r'asd.gif', 'rb')
# a1=a.read()
# a.close()
# print(a1)
#
# b=open('qwe.gif','wb')
# b.write(a1)
# b.close()



# #统计a.txt文件有多少行，统计的时候将文件中的空行、单行注释的行去除
# a=open('a.txt','r',encoding='utf-8')
# b=a.readlines()
# a.close()
# print(b)
# c=[]
# for i in range(len(b)):
#     if b[i][0]!='#' and b[i][0]!='\n':
#         c.append(b[i])
# print(c)
# print(len(c))




# #自定义了一个名为：九九的函数
# def 九九():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(j,i,j*i),end='\t')
#         print()

# 九九()


# 将局部变量变为全局变量
# a=1
# def abc():
#     global a
#     a=12
#     print(a)
# abc()
# print(a)

#
# def abc():
#     b=sum(range(101))
#     print(156)
    # return b+10
# print(abc())



# def 行数(x):
#     a=open(x,'r',encoding='utf-8')
#     b=a.readlines()
#     print(len(b))
#
#
# 行数('a.txt')

# a=123
# b=str(a)
# c=int(b[1])
# print(type(c))



#从文件中读取第几行到第几行
# f=open('a.txt','r',encoding='utf-8')
# a=f.readlines()
# f.close()
# for i in range(4,9):
#     d=a[i].replace('\n','')
#     print(d)





# 函数阶乘之和加10
# def asd():
#     a=int(input('shu'))
#     b=1
#     c=0
#     for i in range(1,a+1):
#         b*=i
#         c+=b
#     return c+10
# print(asd())


#显示文件中带有ABC的行
# a=open('a.txt','r',encoding='utf-8')
# b=a.readlines()
# a.close()
# for i in b:
#     if 'ABC' in i:
#         a=i.rstrip()
#         # a=i.replace('\n','')
#         print(a)



# def a(x,y=10,**kwargs):
#     print(kwargs)
#     print(x)
#     print(y)
# a(20,name='dsdf',age=20)




#函数必须参数阶乘之和
# def asd(a):
#     b=1
#     c=0
#     for i in range(1,a+1):
#         b*=i
#         c+=b
#     print(c)
# asd(5)



# #函数任意范围的质数之和
# def asd(x,y):
#     a = 0
#     for i in range(x,y):
#        for j in range(2,i+1):
#           if i%j==0:
#              break
#        if i==j:
#         a+=i
#     return a
#
# print(asd(2,100))


#
# #计算器
# def sum(x,y):
#     return x+y
# def jian(x,y):
#     return x-y
# def cheng(x,y):
#     return x*y
# def chu(x,y):
#     return x/y
# while True:
#     a=input('>>>')
#     if '+' in a:
#         a=a.split('+')
#         print(sum(int(a[0]),int(a[1])))
#     elif '-' in a:
#         a = a.split('-')
#         print(jian(int(a[0]), int(a[1])))
#     elif '*' in a:
#         a = a.split('*')
#         print(cheng(int(a[0]), int(a[1])))
#     elif '/' in a:
#         a = a.split('/')
#         print(chu(int(a[0]), int(a[1])))
#     else:
#         break

#计算器
# def jisuanqi(x,y,z):
#     if z=='+':
#         print(x+y)
#     elif z=='-':
#         print(x-y)
#     elif z=='*':
#         print(x*y)
#     else:
#         print(x/y)
#
# jisuanqi(2.1,1.1,'/')

#匿名函数
# sum=lambda x,y:print(x+y)
# sum(1,2)


# #列表推导式
# # a=[]
# # for i in range(10):
# #     a.append(i)
# # print(a)

# a=[i for i in range(10) if i >5]
# print(a)

# a=['{}*{}={}'.format(j,i,j*i) for i in range(1,10) for j in range(1,i+1)]
# print(a)


# #三元表达式
# x=7
# x=x+1 if x%2==1 else x
# print(x)



#整除求余
# a,b,=divmod(1000,16)
# print(a,b)



# print(hex(16))#十进制转十六进制
# print(oct(8))#十进制转八进制
# print(bin(2))#十进制转二进制
# print(int(0x10))#任意进制转十进制



#参数传递任意范围内因数之和等于本身的数
# def asd(x,y):
#     for i in range(x,y):
#         a = 0
#         for j in range(1,i):
#             if i%j==0:
#                 a+=j
#         if i==a:
#             print(i)
# asd(2,100)




# 函数十进制转换成十六进制
# def abc(x):
#     z=[str(i) for i in range(10)] + [chr(j) for j in range(97,103)]
#     c=[]
#     while True:
#         x,b=divmod(x,16)
#         c.append(z[b])
#         if x==0:
#             break
#     c.reverse()
#     d=''
#     for i in c:
#         d+=i
#     print(d)

# abc(1000)




# a='fhffgjj'
# b='-'
# print(b.join(a))


# #*三角
# for i in range(3):
#      j=3-i
#      print(' '*i,end='')
#      print('* '*j)



# a=5
# while a>20:
#     a-=1
# print(a)


# with open('a.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# print(a)

# import random
# a=random.randint(1,10)
# print(a)

# print(__name__)
# if __name__ == '__main__':
#     print('hello')

# b=[1,2,2,3,5,5,6,2,12,5,87,56]
# b=list(set(b))
# b.sort()
# print(b)


# def asd(*args):
#     print(args)
# asd(12,1,2,3)





#写写写写写写写写写写写写写写写写写写写写v
# import xlwt
# #
# f=xlwt.Workbook(encoding='utf-8')  #打开一个excel表格文件
# sheet = f.add_sheet('excel学习')   #添加一个标签页（标签页的名字）
# for i in range(1,10):
#     for j in range(1, i + 1):
#         sheet.write(i-1,j-1,'{}*{}={}'.format(j,i,j*i))   #给sheet标签页中写入；write(行、列、内容)
#         # sheet.write(4,0,'dfiiid')
# f.save('软件测试.xls')             #保存


################把文件内容放到表格###### 追加########################
# with open('a.txt','r',encoding='utf-8') as f:
#     b=f.readlines()
# with open('b.txt','r',encoding='utf-8') as g:
#     c=g.readlines()
# import xlwt
# import xlrd
# a=xlwt.Workbook()
# sheet=a.add_sheet('excel学生表')
# for i in range(len(b)):
#     g=b[i].replace('\n','').split(',')
#     for j in range(len(g)):
#         sheet.write(i,j,g[j])
# a.save('信息表.xls')
# b=xlrd.open_workbook('信息表.xls')
# sheet1=b.sheets()[0]
# h=(sheet1.nrows)
# from xlutils.copy import copy
# f=xlrd.open_workbook('信息表.xls')
# new_f=copy(f)
# sheet2=new_f.get_sheet(0)
# for i in range(len(c)):
#     g=c[i].replace('\n','').split(',')
#     for j in range(len(g)):
#         sheet2.write(i+h,j,g[j])
# new_f.save('信息表.xls')
###############################################


#读读读读读读读读读读读
# import xlrd
# f=xlrd.open_workbook('信息表.xls')

# print(f.nsheets)
# # print(f.sheet_names())

# sheet=f.sheets()[0]
# # new_sheet=f.sheet_by_name('excel学生表')
#
# for i in range(sheet.nrows):
# print(sheet.nrows)
#     print(sheet.row_values(i))
#
# print(sheet.ncols)
# print(sheet.col_values(0))
#
# print(sheet.cell(0,4).value)

#追加追加追加追加追加追加追加追加
# import xlrd
# from xlutils.copy import copy
# f=xlrd.open_workbook('信息表.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# sheet.write(0,5,'lalala')  #追加的行、列、内容
# new_f.save('信息表.xls')



###################表格中信息写回到文件
# import xlrd
# f=xlrd.open_workbook('信息表.xls')
# sheet=f.sheets()[0]
# b=[]
# for i in range(sheet.nrows):
#     j=','.join(sheet.row_values(i))  #变成一个字符串
#     # print(j)
#     if j[-1]==',':
#         j=j.split(',')
#         # print(j)
#         j.pop(-1)
#         j=','.join(j)
#         # print(j)
#         b.append(j)
#     else:
#         b.append(j)
# print(b)
# with open('c.txt','w',encoding='utf-8') as qq:
#     for i in b:
#         if i==b[-1]:
#             qq.write(i)
#         else:
#             qq.write(i)
#             qq.write('\n')
###############################################

# a=['fhffgjj','45','hhh']
# b='-'
# print(type(b.join(a)))

######################重利用追加
# with open('a.txt','r',encoding='utf-8') as f:
#     b=f.readlines()
# with open('b.txt','r',encoding='utf-8') as g:
#     c=g.readlines()
# with open('d.txt','r',encoding='utf-8') as y:
#     h=y.readlines()
# x=b+c+h
# import xlwt
# import xlrd
# a=xlwt.Workbook()
# sheet=a.add_sheet('excel学生表')
# for i in range(len(x)):
#     g=x[i].replace('\n','').split(',')
#     for j in range(len(g)):
#         sheet.write(i,j,g[j])
# a.save('信息表1.xls')
#############################################

# import os

# a=os.getcwd()
# a=os.listdir()
# print(a)
# os.rename()
# os.chdir(r'C:/Users/WXL/Desktop')
# a=os.getcwd()
# print(a)

# os.mkdir('aaa')
# os.makedirs(r'bbb\ccc')
# os.rmdir('aaa')
# os.removedirs('bbb\ccc')

# a=os.popen('route print')
# print(a.read())

# a=os.path.splitext('day1.py')
# print(a)

# a=[i for i in os.listdir() if os.path.splitext(i)[1]=='.py']
# print(a)

#增
# for i in range(1,11):
#     os.mkdir('user{}'.format(i))
#删
# for i in range(1,11):
#     os.rmdir('user{}'.format(i))


# import re
# a='Sfsf12g3rdgdfsgr'
# c=re.compile('s(.*?)r',re.I)
# e=c.findall(a)
# print(e)
# b=re.findall('s(.*)g',a,re.S)
# print(b)
# d=re.sub('[0-9]+','^&*',a)
# print(d)

#################过滤文件中手机号
# import re
# with open('d.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# for i in a:
#     b=re.findall('181[0-9]{8}|158[0-9]{8}|153[0-9]{8}',i)
#     if b !=[]:
#         c=''.join(b)
#         print(c)
###############################

##########过滤ip地址
# import re
# with open('d.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# for i in a:
#     b=re.findall('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]',i)
#     if b != []:
#         c=''.join(b)
#         print(c)
##################################

# a={1,456,789}
# b={1,528,564}
# print(a|b) #并集
# print(a&b) #交集名
# print(a-b) #差集



# import os
# r=os.getcwd()
# print(r)

# b=os.listdir()
# print(b)

# os.chdir(r'C:/Users/WXL')
# a=os.getcwd()
# print(a)

# a=os.path.splitext(r'C:/Users/WXL/Desktop/python_学习/day1.py')
# print(a)

# for i in os.listdir():
#     if os.path.splitext(i)[1]=='.py':
#         print(i)
#
# a=[i for i in os.listdir() if os.path.splitext(i)[1]=='.py']
# print(a)


# class 小艾():
#     def bo(self):
#         self.asd()
#         print('ge qu')
#     def dui(self):
#         print('dui hua')
#     def asd(self):
#         print('hllow')
#         pass
# 小艾().bo()

# class asdf():
#     def __init__(self):
#         print('hello')
# asdf()


# class 小度():
#     def jisuan(self):
#         print('zhishu')
#         pass
# a=小艾()
# a.bo()


# class new_小艾():
#     def asda(self):
#         print('dsf')
#     pass


# class qwe(小艾,new_小艾):
#     pass
# qwe().asda()

# class asd():
#     def __init__(self,x):
#         self.name=x
#     def duihua(self):
#         print('hello {}'.format(self.name))
#
# a=asd('hh')
# b=asd('dd')
# a.duihua()
# b.duihua()


# import os
# class wenjian():
#     def abc(self):
#         for i in range(1,11):
#             os.mkdir('文件{}'.format(i))
#             with open('{}.txt'.format(i),'w',encoding='utf-8') as f:
#                f.write('lalala')
#
# a=wenjian()
# a.abc()

# with open('C:/Users/WXL/Desktop/python_学习/新建文件夹/iii.txt', 'w', encoding='utf-8') as f:
#     f.write('lalala')





# 爬虫（保存到表格）#################################################################
# import xlwt
# import requests
# import re
# shuju=[]
# class 新鲜_Spider(object):
#     def qingqiu(self,page):
#         url='https://www.qiushibaike.com/textnew/page/{}/?s=5167695'.format(page)
#         head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
#
#         }
#         res=requests.get(url=url,headers=head)
#         html=(res.content.decode('utf-8'))
#         return html
#     def guolv(self,a):
#         # shuju=[]
#         patt=re.compile(r'<div class="content">(.*?)</span>',re.S)
#         items=patt.findall(a)
#         for i in items:
#             i=i.replace('\n','').replace('<span>','').replace('<br/>','')
#             shuju.append(i)
#         return shuju
#     def save(self,d):
#         f=xlwt.Workbook(encoding='utf-8')
#         sheet=f.add_sheet('lala')
#         for i in range(len(d)):
#             sheet.write(i,0,d[i])
#         f.save('新鲜.xls')
#
#
# xin=新鲜_Spider()
# for i in range(1,5):
#     a=xin.qingqiu(i)
#     b=xin.guolv(a)
# xin.save(b)



# ## ## ## ## ## ## #爬取图片并保存# ## ## ## ## ## ## #################################
# import requests
# import re
# import os
# shuju=[]
# class 图片_Spider(object):
#     a=0
#     def qingqiu(self,page):
#         url='https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
#         head={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
#         }
#         res=requests.get(url=url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,a):
#         #过滤的是图片的网址
#         # shuju=[]
#         patt0=re.compile(r'<div class="thumb">(.*?)</a>',re.S)
#         item=patt0.findall(a)
#         for j in item:
#             patt=re.compile(r' src="(.*?)"',re.S)
#             items=patt.findall(j)
#             items=''.join(items)
#             items='https:'+items
#             # print(items)
#             shuju.append(items)
#         return shuju
#     def save(self,qwe):
#         #任何图片都是二进制（字节码）
#         #请求图片的网址，得到图片的源码
#         os.mkdir('图片')
#         for j,i in enumerate (qwe):
#             res=requests.get(i)
#             ht=res.content   #二进制
#             with open(r'C:/Users/WXL/Desktop/python_学习/图片/{}.jpg'.format(j+1),'wb') as f:
#                 f.write(ht)
#             # self.a+=1
#
#
# tu=图片_Spider()
# for i in range(1,4):
#     a=tu.qingqiu(i)
#     b=tu.guolv(a)
# tu.save(b)
#

#删除图片
# import os
# a=os.listdir(r'C:/Users/WXL/Desktop/python_学习/图片')
# for i in range(len(a)):
#     os.remove(r'C:/Users/WXL/Desktop/python_学习/图片/{}.jpg'.format(i+1))
######################################################################################








# import xlrd
# f=xlrd.open_workbook('豆瓣1.xls')
# sheet=f.sheets()[0]
# aa=[]
# for i in range(sheet.nrows):
#     aa.append((sheet.row_values(i)))
# print(aa)
# #对数据库的操作
# import pymysql
# conn=pymysql.connect(host='192.168.0.118',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
#创建游标（控制器）
# abc=conn.cursor()
# while True:
#     a=input('请输入命令：')
#     if a=='exit':
#         conn.close()
#         break
#     elif 'insert' in a:
#         for i in range(len(aa)):
#             for j in range(len(aa[i])):
#                 abc.execute(a)
#                 conn.commit()
#     else:
#         try:
#             abc.execute(a)
#             print(abc.fetchall())
#         except:
#             continue

# abc.execute('insert into douban values("{}","{}","{}","{}")'.format(aa[i][j],aa[i][j+1],aa[i][j+2],aa[i][j+3])')


# abc.execute('show databases;')
# print(abc.fetchall())

# abc.execute('create database lala;')
# abc.execute('show databases;')
# abc.execute('use lala;')
# abc.execute('show tables;')
# print(abc.fetchall())
# abc.execute('create table douban(mingc char(255),daoy char(255),miaos char(255),renshu int);')
# abc.execute('show tables;')
# print(abc.fetchall())
# j=0
# for i in range(len(aa)):
        # abc.execute('insert into douban values("{}","{}","{}","{}");'.format(aa[i][j],aa[i][j+1],aa[i][j+2],aa[i][j+3]))
        # conn.commit()
#提交

# abc.execute('select * from douban;')
# abc.execute('show tables;')
# print(abc.fetchall())
# print(abc.fetchmany(3))
# print(abc.fetchone())
# print(abc.fetchone())

# abc.execute('use test3')
# abc.execute('show tables')
# print(abc.fetchall())
# abc.execute('select * from ordenritem')
# a=(abc.fetchall())
# for i in a:
#     print(i)


# print()

############################txt文件写入数据库###############################################################
# import pymysql
# conn=pymysql.connect(host='192.168.0.118',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
# abc=conn.cursor()
# abc.execute('create database ku1;')
# abc.execute('use ku1;')
# c=[]
# with open('b.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# for i in a:
#     a=i.replace('\n','').split(',')
#     c.append(a)
# print(c)
# for i in c:
#     if i==c[0]:
#         abc.execute('create table biao1({} char(255),{} char(255),{} char(255));'.format(i[0],i[1],i[2]))
#     else:
#         abc.execute('insert into biao1 values("{}","{}","{}");'.format(i[0],i[1],i[2]))
#         conn.commit()
# abc.execute('select * from biao1;')
# print(abc.fetchall())
# conn.close()
#################################################################################################



# from time import sleep
# import threading
# def asd():
#     for i in range(3):
#         print('lalal')
#         sleep(2)
# def qwe():
#     for i in range(3):
#         print('hihih')
#         sleep(1)
# threading.Thread(target=asd).start()
# threading.Thread(target=qwe).start()
# import time
# dd=time.time()
# print(dd)
#
# a=time.localtime()
# print(a)

# # print(time.localtime()[0])
# print(time.strftime('%Y-%m-%d %H:%M:%S',a))

# qq=(time.strptime('2019-02-22','%Y-%m-%d'))
# print(qq)

# print(time.mktime(qq))
# time.sleep(3)
# print(time.mktime((2019,2,22,0,0,0,0,0,0)))


############判断是否闰年########################################
# import time
# while True:
#     a=input('>>>>')
#     qq=(time.strptime(a,'%Y-%m-%d'))
#     # print(qq[0])
#     if qq[0]%400==0:
#         if qq[0]%400==0:
#             print(qq[0],'是世纪闰年')
#         else:
#             print(qq[0],'不是闰年')
#     else:
#         if qq[0]%4==0:
#             print(qq[0], '是闰年')
#         else:
#             print(qq[0], '不是闰年')
#     print('今天是星期{}'.format(qq[6]+1))
#     print('今天是一年中的第{}天'.format(qq[7]))
############################################################




###############发送邮件######################
# import smtplib
# import email.mime.multipart
# import email.mime.text
#
# server='smtp.163.com'        #邮件服务器
# from_user='18339914556@163.com' #发件人
# res='18348326189@163.com'          #收件人
# passwd='wxl0801'  #授权码  允许登录  客户端的密码
#
# #创建一个空邮件
# message=email.mime.multipart.MIMEMultipart()
#
# message['From']=from_user             #邮件的发件人
# message['To']=res                     #邮件的接收者
# message['Subject']='laji'           #邮件主题
# text="游龙当归海，海不迎我自来也！"     #正文
#
# #对正文进行编码
# tet=email.mime.text.MIMEText(text,'plain','utf-8')
# #将正文添加到邮件中
# message.attach(tet)
#
# #带附件de
# #对附件进行读取和编码
# att2=email.mime.text.MIMEText(open('asd.gif','rb').read(),'base64','utf-8')
# #给邮件添加头部信息
# att2["Content-Type"]='application/octet-stream'
# att2["Content-Disposition"]='attachment;filename="asd.gif"'
# #将附件添加到邮件中
# message.attach(att2)
#
# #连接服务器
# smtp123=smtplib.SMTP_SSL(server,465)
# #登录服务器
# smtp123.login(from_user,passwd)
# #发送邮件
# smtp123.sendmail(from_user,res,message.as_string())
# #断开连接
# smtp123.close()
#################################################################################



# ###############前一天#############################
# import time
# while True:
#     aa=input('>>>')
#     qq=(time.strptime(aa,'%Y-%m-%d'))
#     # print(qq)
#     a=(time.mktime(qq))
#     # print(a)
#     b=time.localtime(a-86400)
#     # print(b)
#     c=time.strftime('%Y-%m-%d' ,b)
#     print('前一天',c)
##############################################


###############数据库写入excel表格#########################
# import xlwt
# import pymysql
# conn=pymysql.connect(host='192.168.0.118',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
# asd=conn.cursor()
# asd.execute('use ku')
# asd.execute('select * from biao1;')
# a=asd.fetchall()
# print(a)
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('lala')
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         sheet.write(i,j,a[i][j])
# f.save('ihihi.xls')
###########################################################

################数据库写入txt文件############################
# import pymysql
# conn=pymysql.connect(host='192.168.0.118',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
# asd=conn.cursor()
# asd.execute('use ku')
# asd.execute('select * from biao1;')
# a=asd.fetchall()
# # print(a)
# b=[]
# for i in a:
#     i=','.join(i)
#     b.append(i)
# # print(b)
# with open('aaaa.txt','w',encoding='utf-8') as f:
#     for j in b:
#         if j==b[-1]:
#             f.write(j)
#         else:
#             f.write(j+'\n')
########################################################


############连接linux###################################
# import paramiko
# with paramiko.SSHClient() as ssh123:
#     ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#     ssh123.connect(hostname='192.168.0.95',
#                    port=22,
#                    username='root',
#                    password='123456')
#     while True:
#         aa=input('>>>>')
#         if aa!='exit':
#             try:
#                 a,b,c= ssh123.exec_command(aa)
#                 print(b.read().decode())
#             except:
#                 continue
#         else:
#             break

###########传输文件##############################
# import paramiko
# ssh123=paramiko.Transport('192.168.0.95',22)
# ssh123.connect(username='root',password='123456')
# sftp=paramiko.SFTPClient.from_transport(ssh123)
# # sftp.get('install.log',r'.\install.log')
# sftp.put('day1.py',r'/home/day1.py')
# ssh123.close()
#############################################


#   # tcp######################
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('127.0.0.1',8888))
# s.listen(3)
# while True:
#
#     conn,addr=s.accept()
#
#     reg=conn.recv(1024)
#     print(reg.decode('utf-8'))
#     # print(conn,addr)
#
#     msg='hello'
#     conn.send(msg.encode('utf-8'))


# ########### udp #################
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #绑定主机
# s.bind(('127.0.0.1',8888))
# while True:
#     #
#     conn,addr=s.recvfrom(1024)
#     print(conn.decode('utf-8'))
#
#     s.sendto('响应的数据'.encode('utf-8'),addr)


#
# from tkinter import  *
# from tkinter import messagebox
# from PIL import Image
# from PIL import ImageTk
#
# def closewindow():
#     messagebox.showinfo(title='警告',message='吃我一记龟派气功')
#     #关闭窗口
#     window.destroy()
#     return
#
# def closehao():
#     messagebox.showinfo(title='哈哈哈', message='hahaha')
#     window.destroy()
#     return
#
# def hao():
#     #创建一个顶级窗口，依赖原始窗口存在3
#
#     hao=Toplevel(window)
#     hao.title('lalala')
#     hao .geometry("300x100+520+260")
#     # hao.mainloop()
#     label = Label(hao, text="lala", font=("微软雅黑", 20))
#     label.pack()
#     btn = Button(hao, text='确定', width=0, height=0, command=closewindow)
#     btn.pack()
#     hao.protocol('WM_DELETE_WINDOW', closehao)
#     hao.mainloop()
#
# def buhao():
#     buhao = Toplevel(window)
#     buhao.title('lalala')
#     buhao.mainloop()
#
#
# #创建一个窗口
# window= Tk()
#
# #名名窗口标题
# window.title('自在极易功')
#
# #设置窗口的大小
# window.geometry('605x450+350+50')
# #设置窗口位置
# # windows.geometry('+350+50')
#
# #当用户关闭窗口时触发
# window.protocol('WM_DELETE_WINDOW',closewindow)
#
# #添加文本标签(控件)
# label=Label(window,text='做好觉悟吧',font=("微软雅黑",20))
# #显示标签
# label.grid(row=0,column=0,sticky=E) # 行、列、哪边对齐（W:西；E：东；N ;S ）
#
# #添加图片控件
# #1
# # imag=PhotoImage(file='asd.gif')
# # image=Label(window,image=imag)
# # image.grid(row=1,columnspan=1)
# #2任意图片都能添加
# photo=Image.open('asd.gif')
# phot=ImageTk.PhotoImage(photo)
# pho=Label(window,image=phot)
# pho.grid(row=2,columnspan=2)  #哪行哪列显示
#
# #添加一个按钮控件
# botten=Button(window,text='好的',width=8,height=2,command=hao)
# botten.grid(row=4,column=0,sticky=W)
#
# botten=Button(window,text='不',width=8,height=2,command=buhao)
# botten.grid(row=4,column=1,sticky=E)
#
# #显示窗口
# window.mainloop()

# import pymysql
# conn=pymysql.connect(host='192.168.0.118',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
# asd=conn.cursor()
# asd.execute('create database ku2223')
# asd.execute('use ku2223')
# b=[]
# with open('b.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# for i in a:
#     i=i.replace('\n','').split(',')
#     b.append(i)
# print(b)
# for j in b:
#     if j==b[0]:
#         asd.execute('create table biao({} char(255),{} char(255),{} char(255));'.format(j[0],j[1],j[2]))
#     else:
#         asd.execute('insert into biao values("{}","{}","{}");'.format(j[0],j[1],j[2]))
#         conn.commit()
# asd.execute('select * from biao;')
# print(asd.fetchall())
# conn.close()



# class sdf(object):
#     x=1
# class asd(sdf):
#     pass
# class asdi(sdf):
#     pass
#
# print(sdf.x,asd.x,asdi.x)
# asd.x=2
# print(sdf.x,asd.x,asdi.x)
# sdf.x=3
# print(sdf.x,asd.x,asdi.x)

# def aa(a,b,c):
#     if b==0:
#         return 1
#     else:
#         num=aa(a,b/2,c)
#         if b%2==0:
#             return num*num%a
#         else:
#             return num*num*a%c
# print(aa(5,6,7))


# a={'name':123}
# print(a['name'])

# import json
# import requests
#
# url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch"
#
# payload = "{\r\n \"pageNum\":\"1\",\r\n \"pgeSize\":\"10\",\r\n \"queryTerms\":\r\n {\r\n  \"orderNo\":\"V2100880181219390\"\r\n }\r\n}"
# headers = {
#     'Content-Type': "application/json",
#     'x-dealer-code': "2100005",
#     'x-position-code': "D_PO_1028",
#     'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
#     'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
#     'x-user-code': "dhxc1u",
#     'x-access-token': "0da5606a534fa727dfd7f502df38be65",
#     'cache-control': "no-cache",
#     'Postman-Token': "4a6795df-dd2e-4106-8414-16a2daa4ba47"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# a=response.text
# aa=json.loads(a)
# print(a)
# print(aa)
# if aa['totalSize'] == 0:
#     print('pass')


#
# from selenium import webdriver
# from time import sleep
#
# dr= webdriver.Chrome()
# dr.get('https://www.qzone.qq.com')
# sleep(2)
#
# print(dr.title)
#
# dr.switch_to.frame('login_frame')
# sleep(2)
#
# dr.find_element_by_css_selector('#switcher_plogin').click()
# sleep(2)
#
# dr.find_element_by_id('u').send_keys('1147695719')
# sleep(2)
# dr.find_element_by_id('p').send_keys('18339914556.0801')
# sleep(2)
# dr.find_element_by_id('login_button').click()
# sleep(20)
# print(dr.title)
# dr.find_element_by_css_selector('#tab_applist_show > li:nth-child(4) > a > div.qz-main > span').click()
# sleep(2)



# from selenium import webdriver
# from time import sleep
#
#
#
# dr= webdriver.Chrome()
# dr.get('https://www.baidu.com')
# sleep(2)
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
# sleep(20)
# dr.find_element_by_xpath('//*[@id="key"]').send_keys('python')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="search"]/div/div[2]/button/i').click()
# sleep(2)

# yi=dr.find_element_by_class_name('gl-warp clearfix')
# wd=dr.find_elements_by_class_name('gl-item')
# for i in wd:
#     print(i)
# for i in range(21):
#     a=dr.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[%s]/div/div[7]/a[3]') % (i)
#     a.click()
#     sleep(2)
#     dr.back()

# dr.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[7]/a[3]').click()
# sleep(2)
#
# import unittest
# from ddt import ddt, file_data,data,unpack
#
# @ddt
# class MyTesting(unittest.TestCase):
#     def setUp(self):
#         print('this is the setUp')
#
#     # @data(['1147695719,18339914556.0801','qwe,18339914556.0801'])
#     @file_data(r'C:\Users\WXL\Desktop\python_学习\框架\data\canshu.json')
#     def test_1(self,value):
#         print(value[0])
#         for i in value:
#             print(i)
#             print(i['username'])
#             print(i['password'])



    # @data([3,2,1],[5,3,2],[10,4,6])
    # @unpack
    # def test_minus(self,a,b,expected):
    #     actual = int(a) - int(b)
    #     expected = int(expected)
    #     self.assertEqual(actual, expected)
    #
    # @data([2,3],[4,5])
    # def test_compare(self,a,b):
    #     self.assertEqual(a,b)
#
#     def tearDown(self):
#         print('this is tearDown')
# #
# if __name__ == '__main__':
#     unittest.main()

# from ddt import ddt, file_data, data, unpack

a=0
if a:
    print('dfg')



