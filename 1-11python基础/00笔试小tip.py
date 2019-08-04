#多行输入
import sys
while True:
    try:
        n = int(sys.stdin.readline())
        print(n)
        ret = []
        for i in range(n):
            ret.append(int(sys.stdin.readline()))
            print(ret)
        result = sorted(set(ret))
        for i in result:
            print(i)
    except:
        break



'''
while True:
    try:
        count = int(input())
        kv = {}
        for i in range(count):
            key,value = input().split(' ')
            key = int(key)
            value = int(value)
            if key in kv:
                kv[key] = kv[key]+value
            else:
                kv[key] = value
        for x,y in kv.items():
            print(x, y)
    except:
        break
'''


#单行输入
while True:
    try:
        a = input()
        # s = list(map(int, input().split(' ')))
    except:
        break



#字典序排序
#sorted()    sort()都行


#ASCII码
#ord()

#不能有长度超过2的子串重复
def fun3(s):
    for i in range((len(s)-3)):
        if s[i:i+3] in s[i+1:]:
            return False
            break
    return True