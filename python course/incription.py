st = 'malak and chafia and aicha are the best programers in the world'

ss = []
for i in st:
    ss.append(ord(i))

s = ''
for i in ss:
    s += chr(i)


with open('test.txt', 'w') as f:
    for i in ss:
        f.write(str(i) + ',')
print(st)
print(ss)
print(s)
