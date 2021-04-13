# 9.编写函数，接收任意数量的整数作为参数，返回一个元组
# 元组的第一个元素是所有参数的中位数
# 第二个元素是所有小于中位数参数的平均值
# 第三个元素是所有大于中位数参数的平均值。
def fun(*args):
    lst = list(args)
    lst.sort()
    mid = None
    if len(lst) & 1:
        mid = lst[len(lst) // 2]
    else:
        mid = (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
    l = list(filter(lambda x: x < mid, lst))
    left = sum(l) / len(l)
    l = list(filter(lambda x: x > mid, lst))
    right = sum(l) / len(l)
    return mid, left, right


print(fun(2, 3, 6, 4, 1, 5))
