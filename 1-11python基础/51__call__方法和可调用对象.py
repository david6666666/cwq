'''
定义了__call__方法的对象，称为“可调用对象”，即该对象可以像函数一样被调用。
'''

class SalaryAccount:
    '''工资计算类'''
    def __call__(self, salary):
        yearSalary = salary*12
        daySalary = salary//30
        hourSalary = daySalary//8
        return dict(monthSalary=salary,yearSalary=yearSalary,daySalary=daySalary
                ,hourSalary=hourSalary)

s = SalaryAccount()

print(s(5000)) #可以像调用函数一样调用对象的__call__方法