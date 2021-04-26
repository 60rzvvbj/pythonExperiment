num = 12345
f = open('resources/test.txt', 'w')
f.write(str(num))
f.close()
f = open('resources/test.exe', 'wb')
f.write(str(num).encode())
f.close()
