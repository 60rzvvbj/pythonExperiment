mm = {}
mf = {}
for year in range(1951, 2001):
    r = open('resources/babynames/yob' + str(year) +
             '【瑞客论坛 www.ruike1.com】.txt', 'r')
    for row in r.readlines():
        row = row.split(',')
        if row[1] == 'F':
            mf[row[0]] = mf.get(row[0], 0) + int(row[2])
        else:
            mm[row[0]] = mm.get(row[0], 0) + int(row[2])


def show(m):

    def cmp(key):
        return m[key]

    lst = [key for key in m]
    lst.sort(key=cmp, reverse=True)
    print('{}:\t{}'.format(lst[0], m[lst[0]]))


show(mm)
show(mf)
