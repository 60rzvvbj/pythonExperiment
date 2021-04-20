import docx
f = docx.Document('resources/test.docx')
m = {}
for p in f.paragraphs:
    for ch in p.text:
        m[ch] = m.get(ch, 0) + 1
for key in m:
    print("{}:\t{}".format(key, m.get(key)))
