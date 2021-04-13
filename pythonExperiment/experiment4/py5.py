# 5．定义一个yield生成器函数，生成200以下5的所有倍数。
def y():
    for x in range(1, 200):
        if not x % 5:
            yield x
    return


res = [i for i in y()]
print(res)
