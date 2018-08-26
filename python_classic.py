'''
--------------------------------------
python 基本特性，主要数据结构，主要内置方法
--------------------------------------
'''
# --------List----------------
# CREATION
# 1. create a null list, then append.
dogs = []
dogs.append('a')
dogs.append('b')
dogs.append('c')
dogs.append('d')
# 2. set explicitly
dogs=['a','b','c','d']
# 3. list comprehension 
l1 = [i*2 for i in range(10)]
# a more complex version
xl = [1,3,5]
yl = [9,12,13]
l2  = [ x**2 for (x,y) in zip(xl,yl) if x+y > 10]
# 4. transform from tuple
l3 = list(t)  
l4 = list('string')

# list functions
dogs.append('a')
dogs.extend(dogs2) # append all items in dogs2 after dogs.
dogs.remove('b') #remove specific item

dogs.insert(4,'e') # insert item at specific place.
dogs.pop()  # delete the last item
dogs.pop(2) # delete specified item, reverse of insert()

dogs_a=['a','b','d','c']
dogs_a.sort() # 直接改变dogs对象本身。
dogs_b = sorted(dogs_a) # 不改变对象本身
dogs_b == dogs_a  # False
dogs.reverse()
del dogs # remove the list object from memory

'b' in dogs # False. evaluate if 'b' is in the list. Also works for tuple, and dictionary keys

#list indexing
a= [2, 19, 1, 4, 6, 88, 2]
a[1] #19
a[-1] #2
a[0:5] #[2, 19, 1, 4, 6]
a[0:5:2] #[2, 1, 6]
a[5:0:-2] #[88, 4, 19]
a[1:] #[19, 1, 4, 6, 88, 2]


# --------Tuple--------------
# CREATION
# 1. set explicitly
t = (1,2,3)
nest_t = t,(4,5)  # nested tuple
# 2. transform
string_t = tuple('string')
list_t = tuple([1,2,3,4,5])

# indexing: same as list
nest_t[1][0]  #4

# tuple functions
string_t = tuple('ahhhhhhhh')
string_t.count('h')  # 8 
longer_t = string_t + t  # ('a', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 'h', 1, 2, 3)
# unpacking
a,b,c=t
print b  #2


# -------String: a special tuple -----------
# use \ 转义
special_str1= 'I\nLove you'
special_str1.index('\n') #1

# STRING FUNCTIONS
filename = 'budget.csv          '
filename = filename.strip()

# transform case
heading = 'the best man in the world'
heading.title() # 'The Best Man In The World'
heading.title().swapcase()  # 'tHE bEST mAN iN tHE wORLD'
filename.upper()  # 'BUDGET.CSV'
filename.capitalize() #'Budget.csv'


# str.join(s):将s中的元素，以str为分割符，合并成为一个字符串。
'|'.join(filename) # 'b|u|d|g|e|t|.|c|s|v' 
heading_list = heading.split(' ')  # join的逆操作。return a list
len(heading_list) # 6 

# find & replace substring
str1 = 'oh ah ah oh yeah'
str1.find('oh') #0
str1.rfind('oh') #9
str1.count('oh') #2
str1.count(' yeah ') # 0
str1.replace('ah','B') #'oh B B oh yeB'  replace all matched items.

# logical operation
str2 = 'elephant'
str1.isalnum() # False. because of \n
str1.isalpha() # False. because of \n
str2.isalpha() # True
str2.isalnum() # True.
str3 = str2 + '3334'
str3.isalpha() # False

# string formatting with %
name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

template = '%.2f %s are worth $%d'  #可先创建一个格式字符串,再填充
template % (1.45, 'Argentine Pesos',1)
# '1.45 Argentine Pesos are worth $1'


# -------Sequence functions: for List and Tuple -----------
# common functions
'''
# s为一个序列
len(s)         返回： 序列中包含元素的个数

min(s)         返回： 序列中最小的元素

max(s)         返回： 序列中最大的元素

all(s)         返回： True, 如果所有元素都为True的话

any(s)         返回： True, 如果任一元素为True的话

 

下面的方法主要起查询功能，不改变序列本身, 可用于表和定值表:

sum(s)         返回：序列中所有元素的和

# x为元素值，i为下标(元素在序列中的位置)

s.count(x)     返回： x在s中出现的次数

s.index(x)     返回： x在s中第一次出现的下标
'''

S = 'abcdefghijk'
S.count('k') # 1
S.count('K') # 0
S.index('K') # ValueError: substring not found
S.index('k') # 10

# 1.range(): range(起点,终点,步长)
for i in range(0,len(S),2):
    print S[i]

# 2.enumerate(): get the index and value at the sametime
for (index,char) in enumerate(S):
    print index
    print char
# a perfect use case: to create dict
mapping = dict((v,i) for i,v in enumerate(S))

# 3.zip(): iterate several list with same length
ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
    print('ta is: %d \n tb is:%d \n tc is:%s' %(a,b,c))

zipped = zip(ta,tb,tc)  # zipped is a list
print(zipped)

na,nb,nc = zipped # unpacking. each is a tuple

# other useful built-in functions
# map
absfrom,absto = map(os.path.abspath,[fromfile,todir])  # making absolute paths


# --------Dictionary---------------
# CREATION
# 1. set a null dict, then append
animal_counts={}
animal_counts['horse'] = 1
animal_counts['cats'] = 2
animal_counts['dogs'] = 5
animal_counts['snakes'] = 0
# 2. set explictly 
animal_counts = {'hourse':1,'cats':2,'dogs':5,'snakes':0}
# 3. from list
animal_counts_1=dict()
keys = ['hourse','cats','dogs','snakes']
values = range(1,5)
for k,v in zip(keys,values):
	animal_counts_1[k]=v
# 4. dict comprehension
s_dict = {k:v for k,v in enumerate(S)}

# dict functions
animal_counts.keys() # return all keys
animal_counts.values() # return all values
animal_counts.update({'elepant':100}) # merge one dict with another
animal_counts.clear() # clear all the content

'''
函数参数传递
iterator， generator， 闭包
'''
# 位置参数被打包为tuple，用*args表示
# 关键字参数被打包为dict，用**kwargs表示
def func1(*name):
	print type(name)
	print name

# 多个参数作为一个tuple传入。
func1(1,4,6)
func1(1,4,"6")

# 多个参数作为dict传入
def func2(**dict):
    print type(dict)
    print dict


def add(a,b,c):
    print a+b+c

args = (1,3,4)
add(*args) # 8

kwargs = {'a':1,'b':2,'c':3}
func2(**kwargs) 

def say_hello_then_call_f(f, *args, **kwargs):
    print 'args is',args
    print 'kwargs is',kwargs
    print ("Hello, Now I'm going to call %s" % f)
    return f(*args,**kwargs)

def g(x,y,z=1):
    return (x+y)/z

say_hello_then_call_f(g,1,2,0.5)
# args is (1, 2, 0.5)
# kwargs is {}
# Hello, Now I'm going to call <function g at 0x10dfd11b8>
# Out[50]: 6.0



# 循环对象。可以被for语句用来循环的
# 从技术上来说，循环对象和for循环调用之间还有一个中间层，就是要将循环对象转换成迭代器(iterator)。这一转换是通过使用iter()函数实现的。但从逻辑层面上，常常可以忽略这一层，所以循环对象和迭代器常常相互指代对方。
for line in open('record.txt','r'):
    print line

# 或者，手动循环
f=open('record.txt','r')
f.next() # 1st row
f.next() # 2nd row ..


# generator 生成器的主要目的是构成一个用户自定义的循环对象。
# 1.生成器表达式 Generator Expression
G = (x for x in range(4))
# 2.一般写法. replace 'return' with yield
def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

g1 = gen() # <generator object gen at 0x10ddc7be0>
for i in g1:
	print i
# 100
# 800
# 1000
#-------------闭包:返回函数的函数----------------------------
def format_and_pad(template, space):
    def formatter(x):
        return (template % x).rjust(space)
    return formatter

fmt = format_and_pad('%.4f',15)
fmt(1.999999)
#'         2.0000'



'''
--------------------------------------
# 1/USING python datetime module  #
--------------------------------------
'''
import pandas as pd
import numpy as np
import sys
import types
import math
from datetime import date
from datetime import datetime
from datetime import timedelta


dp1 = '~/coryli/meritco/campaign_performance_tracking/touchpoint_input/Meritco_services_kol_performance_touchpoints_input_GB18030_20171120.csv'
df = pd.read_csv(dp1, sep=',', encoding ='gb18030' ,header=0, index_col=False)


df['search_start']=pd.to_datetime(df[u'检索时间（起始时间）'])
df['search_end']=pd.to_datetime(df[u'检索时间（终止时间）'])
df = df.drop([u'检索时间（起始时间）',u'检索时间（终止时间）'],axis=1)
df['search_start_epoch'] = df['search_start'].astype('int64') // 10**9
df['search_end_epoch'] = df['search_end'].astype('int64') // 10**9

df['search_lag'] = df['search_end_epoch'] - df['search_start_epoch']

df['search_lag_range'] = '<=30'
df.loc[df.search_lag > 30*24*3600,['search_lag_range']] = '>30'
df.loc[df.search_lag > 45*24*3600,['search_lag_range']] = '>45'

range_agg = df.groupby(['search_lag_range'],as_index=False).userid.count()


'''
####################################
 USING pandas.datetime64  class 
###################################
'''
imp_visits['impress_dt'] = pd.to_datetime(imp_visits.impress_time,unit='s').dt.date # datetime.date
imp_visits['pv_dt'] = pd.to_datetime(imp_visits.pv_time,unit='s').dt.date # datetime.date

end_date = pd.Series(pd.to_datetime(['2017-08-21','2017-08-28','2017-09-04','2017-09-11','2017-09-18','2017-09-25','2017-10-02'],format='%Y-%m-%d'))
end_date = end_date.dt.date  # convert timestamps to datetime.date

# datetime 包练习；
imp_ord_nov=pd.read_csv('imp_ord_nov.txt', sep='|', encoding='utf-8', header=None, names=['user_pin', 'sale_ord_dt','sale_ord_tm','sale_ord_time','sale_ord_id', 'sale_qtty', 'after_prefr_amount','item_sku_id','item_name','channel','campaign','device_id','device_type','mobile_type','imp_id','impress_time','impress_tm','ad_plan_id','dt'], index_col=False)
imp_ord_nov.sale_ord_dt = pd.to_datetime(imp_ord_nov.sale_ord_dt,format='%Y-%m-%d')
imp_ord_nov.dt=pd.to_datetime(imp_ord_nov.dt,format='%Y-%m-%d') # string转换为datetime64
imp_ord_lag_days = imp_ord_nov.sale_ord_dt - imp_ord_nov.dt  # 计算日期差，timedelta64类型
type(imp_ord_lag_days[1])
today=date.today()
today
birthday = date(1993,1,17)  # 构建方法
today == birthday
birthday.isoformat()  #输出标准日起  1993-01-17
birthday.weekday()  # sunday
birthday.isoweekday() # sunday is represented as 7
birthday.ctime()
print today.strftime("%d:%m:%Y"),today.strftime("%d-%m-%Y")
mylivingdays = today - birthday
print(type(mylivingdays),mylivingdays)
mylivingdays.days//365
interval_days = timedelta(days=5)  #构建方法
fivedayslater = today + interval_days  #date + timedelta = 新的date
fivedayslater.isoformat()



'''
--------------------------------------
python 标准库学习
--------------------------------------
'''

# file:文本文件的输入输出
f=open('record.txt','w')
f.write('tom,12,86\nlee,15,99\nlucy,11,58\njoseph,19,56\n')
f.close()
 
f=open('record.txt','r')
print(f.read())
f.close()

with open(“testfile.txt”) as f: 
for line in f: 
print line, 


# os.path
import os.path
import sys
sys_argv = sys.argv
path = '/home/ads_inno/shawnma/py_practice'
print(os.path.basename(path)) # py_practice
print(os.path.dirname(path)) # /home/ads_inno/shawnma
info = os.path.split(path) # 将路径名和文件名分开放

os.getcwd()


'''
to do: 
扫荡python知识空洞，按照python tutorial的顺序整理这个文档，上传GitHub
'''

# Read an integer N
# Without using any string methods, try to print the following:
# 12345...N
# Note that "" represents the values in between.
n = int(input())
print(*range(1,n+1),sep='')

