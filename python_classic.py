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
   """数学运算类"""
    abs(x)                              # 求绝对值，参数可以是整型，也可以是复数，若参数是复数，则返回复数的模
    complex([real[, imag]])             # 创建一个复数
    divmod(a, b)                        # 分别取商和余数，注意：整型、浮点型都可以
    float([x])                          # 将一个字符串或数转换为浮点数。如果无参数将返回0.0
    int([x[, base]])                    # 将一个字符串或浮点数转换为int类型，base表示进制
    long([x[, base]])                   # 将一个字符串或浮点数转换为long类型
    pow(x, y)                           # 返回x的y次幂
    range([start], stop[, step])        # 产生一个序列，默认从0开始
    round(x[, n])                       # 四舍五入
    sum(iterable[, start])              # 对集合求和
    oct(x)                              # 将一个数字转化为8进制字符串
    hex(x)                              # 将一个数字转换为16进制字符串
    chr(i)                              # 返回给定int类型对应的ASCII字符
    unichr(i)                           # 返回给定int类型的unicode
    ord(c)                              # 返回ASCII字符对应的整数
    bin(x)                              # 将整数x转换为二进制字符串
    bool([x])                           # 将x转换为Boolean类型
	
    """逻辑判断"""
    all(iterable)                       # 集合中的元素都为真的时候为真，特别的，若为空串返回为True
    any(iterable)                       # 集合中的元素有一个为真的时候为真，特别的，若为空串返回为False
    cmp(x, y)                           # 如果x < y ,返回负数；x == y, 返回0；x > y,返回正数
    
	"""集合类操作"""
    basestring()                        # str和unicode的超类，不能直接调用，可以用作isinstance判断
    enumerate(sequence[, start=0])      # 返回一个可枚举的对象，注意它有第二个参数
    iter(obj[, sentinel])               # 生成一个对象的迭代器，第二个参数表示分隔符
    max(iterable[, args...][key])       # 返回集合中的最大值
    min(iterable[, args...][key])       # 返回集合中的最小值
    dict([arg])                         # 创建数据字典
    list([iterable])                    # 将一个集合类转换为另外一个集合类
    set()                               # set对象实例化
    frozenset([iterable])               # 产生一个不可变的set
    tuple([iterable])                   # 生成一个tuple类型
    str([object])                       # 转换为string类型
    sorted(iterable[, cmp[, key[, reverse]]])             # 集合排序
        L = [('b',2),('a',1),('c',3),('d',4)]
        sorted(L, key=lambda x: x[1], reverse=True)       # 使用Key参数和reverse参数
        sorted(L, key=lambda x: (x[0], x[1]))             # 使用key参数进行多条件排序，即如果x[0]相同，则比较x[1]

	"""IO操作"""
    file(filename [, mode [, bufsize]]) # file类型的构造函数。
    input([prompt])                     # 获取用户输入，推荐使用raw_input，因为该函数将不会捕获用户的错误输入，意思是自行判断类型
    # 在 Built-in Functions 里有一句话是这样写的：Consider using the raw_input() function for general input from users.
    raw_input([prompt])                 # 设置输入，输入都是作为字符串处理
    open(name[, mode[, buffering]])     # 打开文件，与file有什么不同？推荐使用open
    
    """其他"""
    callable(object)                    # 检查对象object是否可调用
    classmethod(func)                   # 用来说明这个func是个类方法
    staticmethod(func)                  # 用来说明这个func为静态方法
    dir([object])                       # 不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
    help(obj)                           # 返回obj的帮助信息
    eval(expression)                    # 计算表达式expression的值，并返回
    exec(str)                           # 将str作为Python语句执行
    execfile(filename)                  # 用法类似exec()，不同的是execfile的参数filename为文件名，而exec的参数为字符串。
    filter(function, iterable)          # 构造一个序列，等价于[item for item in iterable if function(item)]，function返回值为True或False的函数
        list(filter(bool, range(-3, 4)))# 返回[-3, -2, -1, 1, 2, 3], 没有0
    hasattr(object, name)               # 判断对象object是否包含名为name的特性
    getattr(object, name [, defalut])   # 获取一个类的属性. 比如: getattr(x, 'foobar') is equivalent to x.foobar
    setattr(object, name, value)        # 设置属性值
    delattr(object, name)               # 删除object对象名为name的属性
    globals()                           # 返回一个描述当前全局符号表的字典
    hash(object)                        # 如果对象object为哈希表类型，返回对象object的哈希值
    id(object)                          # 返回对象的唯一标识，一串数字
    isinstance(object, classinfo)       # 判断object是否是class的实例
        isinstance(1, int)              # 判断是不是int类型
        isinstance(1, (int, float))     # isinstance的第二个参数接受一个元组类型
    issubclass(class, classinfo)        # 判断class是否为classinfo的子类
    locals()                            # 返回当前的变量列表
    map(function, iterable, ...)        # 遍历每个元素，执行function操作
        list(map(abs, range(-3, 4)))    # 返回[3, 2, 1, 0, 1, 2, 3]
    next(iterator[, default])           # 类似于iterator.next()
    property([fget[, fset[, fdel[, doc]]]])           # 属性访问的包装类，设置后可以通过c.x=value等来访问setter和getter
    reduce(function, iterable[, initializer])         # 合并操作，从第一个开始是前两个参数，然后是前两个的结果与第三个合并进行处理，以此类推
        def add(x,y):return x + y 
        reduce(add, range(1, 11))                     # 返回55 (注:1+2+3+4+5+6+7+8+9+10 = 55)
        reduce(add, range(1, 11), 20)                 # 返回75
    reload(module)                      # 重新加载模块
    repr(object)                        # 将一个对象变幻为可打印的格式
    slice(start, stop[, step])          # 产生分片对象
    type(object)                        # 返回该object的类型
    vars([object])                      # 返回对象的变量名、变量值的字典
        a = Class();                    # Class为一个空类
        a.name = 'qi', a.age = 9
        vars(a)                         # {'name':'qi', 'age':9}
    zip([iterable, ...])                # 返回对应数组
        list(zip([1, 2, 3], [4, 5, 6])) # [(1, 4), (2, 5), (3, 6)]
        a = [1, 2, 3],  b = ["a", "b", "c"]
        z = zip(a, b)                   # 压缩：[(1, "a"), (2, "b"), (3, "c")]
        zip(*z)                         # 解压缩：[(1, 2, 3), ("a", "b", "c")]
    unicode(string, encoding, errors)   # 将字符串string转化为unicode形式，string为encoded string。	
  

#-- 重要内置函数用法详解
	''' 由于一些内置函数经常用到，因此把好的写法总结起来'''
	# enumerate(): get the index and value at the sametime
	for (index,char) in enumerate(S):
		print index
		print char

	# zip(): iterate several list with same length
	ta = [1,2,3]
	tb = [9,8,7]
	tc = ['a','b','c']
	for (a,b,c) in zip(ta,tb,tc):
		print('ta is: %d \n tb is:%d \n tc is:%s' %(a,b,c))

	# 4.map(): 用函数批量处理iterable中的每个元素
	absfrom,absto = map(os.path.abspath,[fromfile,todir])  # making absolute paths

    



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



#-- 字典dictionary
	''' 创建字典有多种方式'''
	d={};animal_counts['horse'] = 1 	            # 1. set a null dict, then append
	d = {'hourse':1,'cats':2,'dogs':5,'snakes':0}  	# 2. set explictly 
	d=dict()  									    # 3. from two list which stores keys and values separately
	keys = ['hourse','cats','dogs','snakes']
	values = range(1,5)
	for k,v in zip(keys,values):
		animal_counts_1[k]=v
	
	s_dict = {k:v for k,v in enumerate(S)}			# 4. dict comprehension

	# dict functions
	animal_counts.keys() # return all keys
	animal_counts.values() # return all values
	animal_counts.update({'elepant':100}) # merge one dict with another
    dictMerged2=dict(dict1, **dict2) # merge two dict
	animal_counts.clear() # clear all the content
	for k,v in dict.items():  # iterate over a dictionary

#-- 集合set
    """
    set是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素。
    set支持union(联合), intersection(交), difference(差)和symmetric difference(对称差集)等数学运算。
    set支持x in set, len(set), for x in set。
    set不记录元素位置或者插入点, 因此不支持indexing, slicing, 或其它类序列的操作
    """
    s = {3,4,5}									 # 直接赋值创建
	s = set([3,5,9,10])                          # 通过list创建，返回{3, 5, 9, 10}
    t = set("Hello")                             # 创建一个字符的集合，返回{'l', 'H', 'e', 'o'}
    a = t | s;    t.union(s)                     # t 和 s的并集
    b = t & s;    t.intersection(s)              # t 和 s的交集
    c = t – s;    t.difference(s)                # 求差集（项在t中, 但不在s中）
    d = t ^ s;    t.symmetric_difference(s)      # 对称差集（项在t或s中, 但不会同时出现在二者中）
	t.union_update(s)							 # 做集合运算的时候顺带把t给改了，类似的还有difference_update
    t.add('x');   t.remove('H')                  # 增加/删除一个item
	s.pop()									     # 任意删除一个值
    s.update([10,37,42])                         # 利用[......]更新s集合
    x in s,  x not in s                          # 集合中是否存在某个值
    s.issubset(t);      s <= t                   # 测试是否 s 中的每一个元素都在 t 中
    s.issuperset(t);    s >= t                   # 测试是否 t 中的每一个元素都在 s 中 
    s.copy(); 
    s.discard(x);                                # 删除s中x. 如果x不存在，不会报keyerror
    s.clear()                                    # 清空s
    {x**2 for x in [1, 2, 3, 4]}                 # 集合解析，结果：{16, 1, 4, 9}
    {x for x in 'spam'}                          # 集合解析，结果：{'a', 'p', 's', 'm'}
    
#-- 集合frozenset，不可变对象
    """
    set是可变对象，即不存在hash值，不能作为字典的键值。同样的还有list等(tuple是可以作为字典key的)
    frozenset是不可变对象，即存在hash值，可作为字典的键值
    frozenset对象没有add、remove等方法，但有union/intersection/difference等方法
    """
    a = set([1, 2, 3])
    b = set()
    b.add(a)                     # error: set是不可哈希类型
    b.add(frozenset(a))          # ok，将set变为frozenset，可哈希
		
		
		
		
		
'''
函数参数传递
iterator， generator， 闭包
'''
#-- 函数参数传递 
	'''
	位置参数被打包为tuple，用*args表示
	关键字参数被打包为dict，用**kwargs表示
	'''
#-- 函数参数，不可变参数通过“值”传递，可变参数通过“引用”传递
    def f(a, b, c): print(a, b, c)
    f(1, 2, 3)                         # 参数位置匹配
    f(1, c = 3, b = 2)                 # 参数关键字匹配	
    def f(a, b=1, c=2): print(a, b, c)
    f(1)                               # 默认参数匹配。 输出(1, 1, 2)
    f(1, 2)                            # 默认参数匹配。 输出(1, 2, 2)
    f(a = 1, c = 3)                    # 关键字参数和默认参数的混合
    # Keyword-Only参数:出现在*args之后 必须用关键字进行匹配
    def keyOnly(a, *b, c): print('')   # c就为keyword-only匹配 必须使用关键字c = value匹配
    def keyOnly(a, *, b, c): ......    # b c为keyword-only匹配 必须使用关键字匹配
    def keyOnly(a, *, b = 1): ......   # b有默认值 或者省略 或者使用关键字参数b = value

#-- 可变参数匹配: * 和 **
    def f(*args): print(args)          # 在元组中收集不匹配的位置参数
    f(1, 2, 3)                         # 输出(1, 2, 3)
    def f(**args): print(args)         # 在字典中收集不匹配的关键字参数
    f(a = 1, b = 2)                    # 输出{'a':1, 'b':2}
    def f(a, *b, **c): print(a, b, c)  # 两者混合使用
    f(1, 2, 3, x=4, y=5)               # 输出1, (2, 3), {'x':4, 'y':5}
    
#-- 函数调用时的参数解包(unpacking): * 和 ** 分别解包元组和字典
    func(1, *(2, 3))  <==>  func(1, 2, 3)
    func(1, **{'c':3, 'b':2})  <==>  func(1, b = 2, c = 3)
    func(1, *(2, 3), **{'c':3, 'b':2})  <==>  func(1, 2, 3, b = 2, c = 3)
	A=[[1,2,3],[4,5]]; product(*A)   # list也能拆包



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

#------- file:文本文件的输入输出
	f=open('record.txt','w')
	f.write('tom,12,86\nlee,15,99\nlucy,11,58\njoseph,19,56\n')
	f.close()

	f=open('record.txt','r')
	print(f.read())
	f.close()

	with open(“testfile.txt”) as f: 
	for line in f: 
	print line, 


#------ os: interacting with operating system
	import os
	path = os.getcwd()  									# 获取当前工作路径 '/home/ads_inno/shawnma/py_practice'
	print(os.path.basename(path)) 							# py_practice
	print(os.path.dirname(path)) 							# /home/ads_inno/shawnma
	info = os.path.split(path) 								# 将路径名和文件名分开放
	os.chdir('') # 修改当前工作路径
	os.path.abspath(sub_dir)								# 将输入的子路径，构建成绝对路径。其实就是把当前的cwd加在前面
	os.path.exists(dir)										# 看某个路径是否存在
	os.mkdir(dir)											# 创建路径
	os.remove(dir) 											# 删除路径
	os.listdir(dir)											# 列出路径下的所有文件
	os.path.isabs(path)
	os.path.isfile(path)
	os.path.isdir(path)
	os.path.join(path, *paths)								# 用系统分隔符concatenate路径
	os.system(cmd)                                          # 万金油功能
	
#----- shutil: high level file management tools
	import shutil
	shutil.move(src, dst)
	shutil.copyfile(src, dst)

#------- sys
	import sys
	sys_argv = sys.argv        # 获得脚本的参数
	first_argv = sys_argv[0]
    sys.builtin_module_names            # 查找内建模块
    sys.platform                        # 返回当前平台 出现如： "win32" "linux" "darwin"等
    sys.modules                         # 查找已导入的模块
    sys.modules.keys()
    sys.stdout                          # stdout 和 stderr 都是类文件对象，但是它们都是只写的。它们都没有 read 方法，只有 write 方法
    sys.stdout.write("hello")
    sys.stderr
    sys.stdin 

'''
hackerrank中觉得比较使用的代码片段
'''
#-- 从stdin读入多个参数
n,m = map(int, raw_input().split()) #raw_input()读入的是string，必须转型

#-- print statement后面加逗号，可以把对象打在同一行,而不是newline \n
for n in range(1,5):
    print n,

#-- 在python2 中使用python3的print()
from __future__ import print_function

# 读入一个整数n，打印成“12345...N”
n = int(input())
print(*range(1,n+1),sep='')

# 从stdin中读入N个值
students=[]
for _ in range(int(raw_input())):  #这里_只是一个普通变量，只是我们不会去用它
    name = raw_input()
    score = float(raw_input())
    students.append([name,score])
