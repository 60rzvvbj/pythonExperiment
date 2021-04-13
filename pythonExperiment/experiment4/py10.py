# 10. 编写一个函数，其参数为两个正整数，将这两个正整数之间的所有素数以一个元组的形式返回。
import math


def isPrime(x):
    for t in range(2, int(math.sqrt(x)) + 1):
        if not x % t:
            return False
    return True


def run(left, right):
    lst = []
    for x in range(left, right + 1):
        if isPrime(x):
            lst.append(x)
    return tuple(lst)


a, b = eval(input('输两个数：'))
print(run(a, b))
