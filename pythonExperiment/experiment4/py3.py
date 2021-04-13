# 3．定义一个函数，函数参数为一个小于10000的正整数
# 分解它的各位数字，并以一个元组的形式返回。在主程序中调用该函数。
num = int(input('请输入一个数：'))


def fun(num):
    return tuple([int(x) for x in str(num)[::]])


print(fun(num))
