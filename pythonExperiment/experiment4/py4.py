# 4．编写一个lambda表达式，对给定的列表[1, 2, 3, 4, 5]
# 把它的每个元素值分别加上10，生成一个新列表。
lst = [1, 2, 3, 4, 5]


def fun(l): return [x + 10 for x in l]


print(fun(lst))
