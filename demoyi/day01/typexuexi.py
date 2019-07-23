#变量名只能以字母或者下划线开头，
#""代表字符串类型
a="学生"
print(type(a))
print(a)
print("a的值是"+str(a))
#代表数字类型
b=10000
print(type(b))
print(b)
print("b的值是"+str(b))
#()代表一个列表，可以储存多个数据，每个数据之间用，隔开
c=["张三","李四","王五","马六","洪七"]
print(type(c))
print(c)
print("c的值是"+str(c))
#()代表一个元祖，可以储存多个数据，每个数据之间用，隔开
d=("A",1,2,3,4,"J","Q","K")
print(type(d))
print(d)
print("d的值是"+str(d))

#键值对数据，{}表示dict，代表一个字典，可以储存多个键值对数据，多个键值对中间用","隔开，key和value之间用：隔开
e={"姓名":"张三","性别":"女","电话":"12580","年龄":"18","科目":"语文","成绩":"80"}
print(type(e))
print(e)
print("e的值是"+str(e))


a=18
if(a>=18 and a<60):
    print("小明该买成人票")
elif(a>=60):
    print("小明该买老人票")
else:
    print("小明该买未成年票")


# 九九乘法表
for i in range (9):
    for u in range (i+1):
        print((i + 1),"X",(u +1 ),'=',(i + 1) * (u +1 ),'\t',end='')
    print()

#九九乘法表
for i in range (9):
    for a in range (9):
        if(a <= i):
            print(i+1,'x', a+1,'=',(i+1)*(a+1),"\t",end='')
    print()

# 新增单个值
a = []
a.append(1)
print(a)
a.append('hdsbfv')
b = [2,3,'jnfedf']
print(a+b)
c = ['abc']
# 删除单个值
print(a)
a.pop(0)
print(a)
# 为空时，删除最后一个值
print(b)
b.pop()
print(b)

# 按照扑克牌的规则，现在有6张牌，只要5张
# 牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
# 数据库存的是下面格式的数据，写脚
# 黑桃（S）红桃（H）方块（D）梅花（C）本验证满足3带2的牌型
# [''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
# ["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
# ["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]

def dbc(a):
    a = a.replace("''",'"')
    # print(a)
    a = a[2:-2]
    # print(a)
    b = a.split('" , "')
    # print(b)
    c = {}
    for i in b:
        d = i[1:]
        if(d in c):
            c[d] += 1
        else:
            c[d] = 1
    # print(c)
    v1 = 1
    v2 = 1
    for c[d] in c:
        if(c[d] == 3):
            v1 = 1
        if(c[d] == 2):
            v2 = 1
    if(v1 == 1 and v2 == 1):
        print('可以三带二')
    else:
        print('不可以三代二')

# open python 提供的一个内置函数，作用就是打开一个文件。参数一：文件路径；参数二：文件的打开模式  r:只读，w:写入 a：可读写写入。
# with open () as f类似于f = open()，它可以在with的代码执行出现问题时做一些资源释放的工作。
with open('D:\\softwareData\\Pycharm\\day1\\demoyi\\day04\\card.txt','r') as f:
    #读文件，readlines()的作用就是把文件的所有内容按行读出来，存到一个list中；read()把整个文件读出来，存到一个字符串中。
    h = f.readlines()
    #for循环遍历整个列表
    for n in h:
        n = n.replace('\n','')
        print(n)
        dbc(n)

# def dbc(a):
#     a = a.replace("''",'"')
#     # print(a)
#     a = a[2:-2]
#     # print(a)
#     b = a.split('" , "')
#     # print(b)
#     c = {}
#     for i in b:
#         d = i[1:]
#         if(d in c):
#             c[d] += 1
#         else:
#             c[d] = 1
#     # print(c)
#     v1 = 1
#     v2 = 1
#     for c[d] in c:
#         if(c[d] == 3):
#             v1 = 1
#         if(c[d] == 2):
#             v2 = 1
#     if(v1 == 1 and v2 == 1):
#         print('可以三带二')
#     else:
#         print('不可以三代二')
#
# with open('D:\\softwareData\\Pycharm\\day1\\demoyi\\day04\\card.txt','r') as f:
#     h = f.readlines()
#     print(h)
#     for n in h:
#         n = n.replace('\n','')
#         print(n)
#         dbc(n)



# def aheb(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
# aheb(3, 5)
# def aheb(a,b):
#     print(a+b)
# with open('D:\\softwareData\\Pycharm\\day1\\demoyi\\day04\\suanshu.txt','r') as l:
#     h = l.readlines()
#     for m in h:
#         m = m.replace('\n','')
#         x = m.split(',')
#         aheb(int(x[0]),int(x[1]))

# def aheb(a,b):
#     print(a-b)
# with open('D:\\softwareData\\Pycharm\\day1\\demoyi\\day04\\suanshu.txt','r') as l:
#     h = l.readlines()
#     for m in h:
#         m = m.replace('\n','')
#         x = m.split(',')
#         aheb(int(x[0]),int(x[1]))
#
# def aheb(a,b):
#     print(a*b)
# with open('D:\\softwareData\\Pycharm\\day1\\demoyi\\day04\\suanshu.txt','r') as l:
#     h = l.readlines()
#     for m in h:
#         m = m.replace('\n','')
#         x = m.split(',')
#         aheb(int(x[0]),int(x[1]))
#
# def aheb(a,b):
#     print(a/b)
# with open('D:\\softwareData\\Pycharm\\day1\\demoyi\\day04\\suanshu.txt','r') as l:
#     h = l.readlines()
#     for m in h:
#         m = m.replace('\n','')
#         x = m.split(',')
#         aheb(int(x[0]),int(x[1]))

# def sum(a,b):
#     s = a+b
#     print(a,'+',b,'=',s)
#     return s
# sum(2,3)
# def sub(a,b):
#     s = a-b
#     print(a,'-',b,'=',s)
# sub(2,3)
# def mul(a,b):
#     s = a*b
#     print(a,'x',b,'=',s)
# mul(2,3)
# def div(a,b):
#     s = a/b
#     if(b != 0):
#         print(a,'÷',b,'=',s)
#     else:
#         print('无意义')
# div(2,1)
# sum(sum(2,3),3)

# def c():
#     print('大白菜')
# c()
# def a(shui):
#     print(shui,'大白菜')
# a('谁买')
# def i():
#     return '周口的大白菜'
# print(i())
# def cai(c1,c2,c3):
#     return '{}的{}{}元'.format(c1,c2,c3)
# print(cai('周口','大白菜','一斤5'))

# def buy_coffees(cash,cups=2):
#     #去咖啡店
#     print("去咖啡店")
#     #告诉服务员要几杯咖啡
#     cup_num = cups
#     print("告诉服务员要",cup_num,"杯咖啡")
#     #服务员告诉你要多少钱
#     print("服务员告诉你要",cup_num*30,"钱")
#     #你给服务员多少钱
#     money = cash
#     print("你给服务员",money,"钱")
#     #服务员找零，给你咖啡
#     print("服务员找零",money-cup_num*30,"，给你",cup_num,"杯咖啡")
# buy_coffees(100)