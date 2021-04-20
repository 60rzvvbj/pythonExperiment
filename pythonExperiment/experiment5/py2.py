f = open('resources/file.txt', 'w')
f.write(str(123))
f.close()

r = open('resources/file.txt', 'r')
num = int(r.readline())
print(num)
