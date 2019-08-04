'''
我们可以通过zip()函数对多个序列进行并行迭代，zip()函数在最短序列“用完”时就会停止
'''

names = ('cwq','cwf','chy')
ages = (24,18,24,66)
jobs = ('ss','yy','dd')

for names,ages,jobs in zip(names,ages,jobs):
    print("{0}--{1}--{2}".format(names,ages,jobs))