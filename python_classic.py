'''
--------------------------------------
python 基本特性，主要数据结构及其方法，主要内置方法
--------------------------------------
'''

#-- 寻求帮助:
    dir(obj)            # 简单的列出对象obj所包含的方法名称，返回一个字符串列表
    help(obj.func)      # 查询obj.func的具体介绍和用法
    
#-- 测试对象的类型，推荐第二种
    if type(L) == list:
        print("L is list")
    if isinstance(L, list):
        print("L is list")
        
#-- Python数据类型：哈希类型、不可哈希类型
    # 哈希类型，即在原地不能改变的变量类型，不可变类型。可利用hash函数查看其hash值，也可以作为字典的key
    "数字类型：int, float, decimal.Decimal, fractions.Fraction, complex"
    "字符串类型：str, bytes"
    "元组：tuple"
    "冻结集合：frozenset"
    "布尔类型：True, False"
    "None"
    # 不可hash类型：原地可变类型：list、dict和set。它们不可以作为字典的key。

#-- 数字常量
    1234, -1234, 0, 999999999                    # 整数
    1.23, 1., 3.14e-10, 4E210, 4.0e+210          # 浮点数
    0o177, 0x9ff, 0X9FF, 0b101010                # 八进制、十六进制、二进制数字
    3+4j, 3.0+4.0j, 3J                           # 复数常量，也可以用complex(real, image)来创建
    hex(I), oct(I), bin(I)                       # 将十进制数转化为十六进制、八进制、二进制表示的“字符串”
    int(string, base)                            # 将字符串转化为整数，base为进制数
    # 2.x中，有两种整数类型：一般整数（32位）和长整数（无穷精度）。可以用l或L结尾，迫使一般整数成为长整数
    float('inf'), float('-inf'), float('nan')    # 无穷大, 无穷小, 非数

#-- 数字的表达式操作符
    yield x                                      # 生成器函数发送协议
    lambda args: expression                      # 生成匿名函数
    x if y else z                                # 三元选择表达式
    x and y, x or y, not x                       # 逻辑与、逻辑或、逻辑非
    x in y, x not in y                           # 成员对象测试
    x is y, x is not y                           # 对象实体测试
    x<y, x<=y, x>y, x>=y, x==y, x!=y             # 大小比较，集合子集或超集值相等性操作符
    1 < a < 3                                    # Python中允许连续比较
    x|y, x&y, x^y                                # 位或、位与、位异或
    x<<y, x>>y                                   # 位操作：x左移、右移y位
    +, -, *, /, //, %, **                        # 真除法、floor除法：返回不大于真除法结果的整数值、取余、幂运算
    -x, +x, ~x                                   # 一元减法、识别、按位求补（取反）
    x[i], x[i:j:k]                               # 索引、分片
    int(3.14), float(3)                          # 强制类型转换

#-- 默认内置函数
    abs(x)                                      # 返回绝对值
    all(iterable)                               # 所有元素都为true才返回true
    any(iterable)                               # 只要有一个元素为true就返回true
    bin(x)                                      # 把int转为binary string
    callable(object)                            # 测试对象是否可以被call
    enumerate(sequence, start=0)                # 返回序列的索引和值。遍历序列的时候很有用
    zip()
    map(function, iterable, ...)                # 把function应用到每一个元素上去，返回一个list
    reduce()                                    #
    filter()
    len(s)                                       # 返回sequence对象的长度
    dict(),list(),set(),str(),float(),dict(),tuple()  # 数据类型创建
    slice()
    sorted()
    max(iterable[, key])
    min(iterable[, key])
    sum(iterable[, start])                           # 求最大，最小，总和
    


#-- 列表List 
    L = []                                            # 初始化空列表
    L = [[1, 2], 'string', {}]                        # 嵌套列表
    L = list('spam')                                  # 列表初始化
    L = list(range(0, 4))                             # 列表初始化
    list(map(ord, 'spam'))                            # 列表解析
    len(L)                                            # 求列表长度
    L.count(value)                                    # 求列表中某个值的个数
    L.append(obj)                                     # 向列表的尾部添加数据，比如append(2)，添加元素2
    L.insert(index, obj)                              # 向列表的指定index位置添加数据，index及其之后的数据后移
    L.extend(interable)                               # 通过添加iterable中的元素来扩展列表，比如extend([2])，添加元素2，注意和append的区别
    L.index(value, [start, [stop]])                   # 返回列表中值value的第一个索引
    L.pop([index])                                    # 删除并返回index处的元素，默认为删除并返回最后一个元素
    L.remove(value)                                   # 删除列表中的value值，只删除第一次出现的value的值
    L.reverse()                                       # 反转列表
    L.sort(cmp=None, key=None, reverse=False)         # 排序列表，会改变 L本身
    L_new = sorted(L)                                 # 排序，不改变对象本身
    a = [1, 2, 3], b = a[10:]                         # 注意，这里不会引发IndexError异常，只会返回一个空的列表[]
    a = [], a += [1]                                  # 这里实在原有列表的基础上进行操作，即列表的id没有改变
    a = [], a = a + [1]                               # 这里最后的a要构建一个新的列表，即a的id发生了变化

#-- 列表推导式 list comprehension 
    l1 = [i*2 for i in range(10)]
    
    xl = [1,3,5]              
    yl = [9,12,13]
    l2  = [ x**2 for (x,y) in zip(xl,yl) if x+y > 10]  # 带条件判读的推导

#---- 常见字符串常量和表达式
    S = ''                                  # 空字符串
    S = "spam’s"                            # 双引号和单引号相同
    S = "s\np\ta\x00m"                      # 用"\"转义字符
    S = """spam"""                          # 三重引号字符串，一般用于函数说明
    S = r'\temp'                            # Raw字符串，不会进行转义，抑制转义
    S = b'Spam'                             # Python3中的字节字符串
    S = u'spam'                             # Python2.6中的Unicode字符串
    s1+s2, s1*3, s[i], s[i:j], len(s)       # 拼接；重复某字符；字符索引；字符长度
    'a %s parrot' % 'kind'                  # 字符串格式化表达式（旧方式，与python 3.x不兼容，不建议使用）
    'a {1} {0} parrot'.format('kind', 'red')# 字符串格式化方法
    for x in s: print(x)                    # 打印s中的每一个字符
    

#----- 内置str处理函数：
    ','.join(['a', 'b', 'c'])               # 字符串输出，结果：a,b,c
    str1 = "stringobject"
    str1.upper(); str1.lower(); str1.swapcase(); str1.capitalize(); str1.title()        # 全部大写，全部小写、大小写转换，首字母大写，每个单词的首字母都大写
    str1.ljust(width)                       # 获取固定长度，左对齐，右边不够用空格补齐
    str1.rjust(width)                       # 获取固定长度，右对齐，左边不够用空格补齐
    str1.center(width)                      # 获取固定长度，中间对齐，两边不够用空格补齐
    str1.zfill(width)                       # 获取固定长度，右对齐，左边不足用0补齐
    str1.find('t',start,end)                # 查找子串，可以指定起始及结束位置搜索
    str1.rfind('t')                         # 从右边开始查找子串
    str1.count('t')                         # 查找不重复出现的子串的次数
    #上面所有方法都可用index代替，不同的是使用index查找不到会抛ValueError异常，而find返回-1
    str1.index(sub[, start[, end]])
    str1.replace('old','new')               # 替换函数，替换old为new，参数中可以指定maxReplaceTimes，即替换指定次数的old为new
    str1.strip();                           # 默认删除空白符
    str1.strip('abc');                        # 删除str1字符串中开头、结尾处，所有"abc"组合出来的字符
    #例如：
        '   spacious   '.strip()                #输出'spacious'
        'www.example.com'.strip('cmowz.')       #输出'example'
    str1.rstrip(); str1.lstrip()            # 同理
    str1.startswith('start')                # 是否以start开头
    str1.endswith('end')                    # 是否以end结尾
    str1.isalnum(); str1.isalpha(); str1.isdigit(); str1.islower(); str1.isupper()      # 判断字符串是否全为字符、数字、小写、大写

#-- Python中的字符串格式化实现2--字符串格式化调用方法
    # 普通调用
    "{0}, {1} and {2}".format('spam', 'ham', 'eggs')            # 基于位置的调用
    "{motto} and {pork}".format(motto = 'spam', pork = 'ham')   # 基于Key的调用
    "{motto} and {0}".format('ham', motto = 'spam')             # 混合调用
    # 添加键 属性 偏移量 (import sys)
    "my {1[spam]} runs {0.platform}".format(sys, {'spam':'laptop'})                 # 基于位置的键和属性
    "{config[spam]} {sys.platform}".format(sys = sys, config = {'spam':'laptop'})   # 基于Key的键和属性
    "first = {0[0]}, second = {0[1]}".format(['A', 'B', 'C'])                       # 基于位置的偏移量
    # 具体格式化
    "{0:e}, {1:.3e}, {2:g}".format(3.14159, 3.14159, 3.14159)   # 输出'3.141590e+00, 3.142e+00, 3.14159'
    "{fieldname:format_spec}".format(......)
    # 说明:
    """
        fieldname是指定参数的一个数字或关键字, 后边可跟可选的".name"或"[index]"成分引用
        format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
        fill        ::=  <any character>              #填充字符
        align       ::=  "<" | ">" | "=" | "^"        #对齐方式
        sign        ::=  "+" | "-" | " "              #符号说明
        width       ::=  integer                      #字符串宽度
        precision   ::=  integer                      #浮点数精度
        type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
    """
    # 例子:
        '={0:10} = {1:10}'.format('spam', 123.456)    # 输出'=spam       =    123.456'
        '={0:>10}='.format('test')                    # 输出'=      test='
        '={0:<10}='.format('test')                    # 输出'=test      ='
        '={0:^10}='.format('test')                    # 输出'=   test   ='
        '{0:X}, {1:o}, {2:b}'.format(255, 255, 255)   # 输出'FF, 377, 11111111'
        'My name is {0:{1}}.'.format('Fred', 8)       # 输出'My name is Fred    .'  动态指定参数
        'add percentage: {0:.2%}'.format(0.6999)      # 输出'add percentage: 69.99%'
        'specify precision: {0:,.2f}'.format(1492845.009)  #输出specify precision: 1,492,845.01'
        

#--- Tuple元组
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

# -------Sequence functions: for List and Tuple -----------
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


# ---字典
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
TO DO: 
扫荡python知识空洞，按照python tutorial的顺序整理这个文档，上传GitHub
'''

# Read an integer N
# Without using any string methods, try to print the following:
# 12345...N
# Note that "" represents the values in between.
n = int(input())
print(*range(1,n+1),sep='')

