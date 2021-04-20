r = open('resources/stock.txt')
stock = [float(v) for v in r.readlines()]
res = []
s = 0
for index in range(0, 5):
    s += stock[index]
    res.append(s / (index + 1))
for index in range(5, len(stock)):
    s += stock[index] - stock[index - 5]
    res.append(s / 5)
for v in res:
    print("{:.6}".format(v))
