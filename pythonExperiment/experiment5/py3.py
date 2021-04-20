r = open('resources/data.txt', 'r')
lst = []
while True:
    s = r.readline()
    if s == '':
        break
    lst.append(sum(eval(s)))
print('最小值为：{}'.format(min(lst)))
