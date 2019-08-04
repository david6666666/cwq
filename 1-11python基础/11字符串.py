'''
字符串本质：字符序列。
python不支持单字符类型，单字符也作为一个字符串使用
python3默认是16位Unicode编码
使用内置函数ord()可以把字符串转换成对于的Unicode码
使用内置函数chr()可以把十进制数字转换成对应的字符
'''
print("--------字符串本质-----------")
print(ord('A'))
print(chr(66))


'''
引号创建字符串
三个'可以帮组我们创建多行字符串
'''
print("---------创建字符串----------")
a = "I'm a teacher"
print(a)
b = '''sadfasfagfaga\
gagagagagag\
sdasfag'''
print(b)


'''
空字符串和len()函数
'''
print("---------空字符串和len()函数----------")
c = ''
print(len(c))


'''
转义字符
\\      反斜杠符号
\'      单引号
\"      双引号
\b      退格
\n      换行
\t      横向制表符
\r      回车
'''
print("---------转义字符----------")
a = "I\nlove\nu"
print(a)


'''
字符串拼接       +   'a' + 'b' == ab
或者是直接放到一起
'''
print("---------字符串拼接----------")
a = 'abc' + 'def'
b = 'def''abc'
print(a)
print(b)


'''
字符串复制   使用*
'''
print("----------字符串复制---------")
a = 'sxt'*3
print(a)


'''
不换行打印
    我们调用print时，会自动打印一个换行符，
    我们可以通过end = "任意字符串"，实现末尾添加任何内容
'''
print("--------不换行打印-----------")
print("sxt",end='')
print("sxt",end='##')
print("sxt")


'''
从控制台读取字符串
    我们可以使用input()从控制台读取键盘输入的内容
'''
print("--------从控制台读取字符串-----------")
#myname = input("请输入名字：")
#print(myname)

'''
使用[]提取字符
    正向搜索：最左侧第一个字符，偏移量是0，第二个是1，直到len(str)-1为止
    反向搜索：最右侧第一个字符，偏移量-1，第二个是-2，直到-len(str)为止
'''
print("--------使用[]提取字符-----------")
a = "asfasgabvagbasgasg"
print(a[0],a[-1])

'''
replace()实现字符串替换
'''
print("--------字符串替换-----------")
a = "asfasgabvagbasgasg"
b = a.replace('a','陈')
print(b)

'''
字符串切片slice操作
    [起始偏移量start:终止偏移量end:步长step]
'''
print("--------字符串切片-----------")

a = "abcdef"
print(a[:])         #提取整个字符串
print(a[2:])        #从start到结尾
print(a[:2])        #从头到end-1
print(a[2:4])       #从start到end-1
print(a[1:5:2])     #步长为2
print(a[-3:])
print(a[-5:-3])
print(a[::-1])      #步长为负 从右到左

'''
split()分割和join()合并
    split()可以基于制定分隔符将字符串分割成多个子字符串(存储到列表中)
    如果不指定分割符，则默认使用空白字符(换行符/空格/制表符)
    join() 比 + 快 
'''
print("--------字符串分割和合并-----------")

a = "to be or not to be"
b = a.split(" ")
print(b)
print("*".join(b))

'''
字符串常用方法
    常用查找方法：
        len()       字符串长度
        startwith() 以指定字符串开头
        endswith()  以指定字符串结尾
        find()      第一次出现指定字符串的位置
        rfind()     最后一次出现指定字符串的位置    
        count()     指定字符串出现多少次
        isalnum     所有字符全是字母或数字
    去除首尾信息
        我们可以通过strip()去除字符串首尾指定信息。通过lstrip()去除
        字符串左边指定信息，rstrip()去除字符串右边指定信息
    大小写转换
        c.capitalize()      首字母大写
        c.capitalize()      每个单词首字母大写
        c.upper()           所有字符大写
        c.lower()           所有字符小写
        c.swapcase()        所有字母大小写转换
    格式排版
        center()    ljust()     rjust()
    其他方法
        isalnum()   是否为字母或数字
        isalpha()   检测是否只有字母组成(含汉字)
        isdigit()   检测是否只由数字构成
        isspace()
        isupper()
        islower()
'''
print("--------字符串常用方法-----------")
a = "我叫陈炜青,我很陈帅"
print(len(a))
print(a.startswith("我"))
print(a.endswith("帅"))
print(a.find("青"))
print(a.rfind("陈"))
print(a.count("陈"))
print(a.isalnum())

b = "**s*x*t**"
print(b.strip("*"))
print(b.lstrip("*"))
print(b.rstrip("*"))
print("   sxt   ".strip())

c = "cwq love programming, love CR"
print(c.capitalize())
print(c.capitalize())
print(c.upper())
print(c.lower())
print(c.swapcase())

d = "CWQ"
print(d.center(10, "*"))
print(d.ljust(10, "*"))
print(d.rjust(10, "*"))

'''
    字符串的格式化
        基本语法是通过{}和：来代替以前的%
    填充和对齐
        ^ < > 分别是居中，左对齐，右对齐，后面带宽度
        :号后面带填充的字符，只能是一个字符，不指定默认用空格
    数字格式化
        浮点数通过f，整数通过d进行所需要的格式化。
'''
print("--------字符串格式化-----------")
a = "名字是:{0}, 年龄是:{1}"
print(a.format("陈炜青", "25"))
b = "名字是:{name}, 年龄是:{age}"
print(b.format(age=19, name="陈炜青"))

print("{:*>8}".format("245"))

c = "我是{0}, 我的存款有{1:.2f}"
print(c.format("陈炜青", 88888.77777))

'''
    可变字符串
        io.StringIO
'''
print("--------可变字符串-----------")
a = "hello, cwq"
import io
sio = io.StringIO(a)
print(sio.getvalue())
print(sio.seek(7))
print(sio.write("g"))
