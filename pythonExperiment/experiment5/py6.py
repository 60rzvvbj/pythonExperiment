import re
r = open('resources/story.txt', 'r')
m = {}
for s in r.readlines():
    for text in re.split('[., \\/-></?$%^&*#@!`\'\"\n]', s):
        if text.isalpha():
            text = text.lower()
            m[text] = m.get(text, 0) + 1

lst = [key for key in m]


def cmp(key):
    return m[key]


lst.sort(key=cmp, reverse=True)
for index in range(0, 10):
    print('{}:\t{}'.format(lst[index], m[lst[index]]))
