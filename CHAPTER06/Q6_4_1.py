f = open('some.txt')
c = 0
for 1 in f:
    print(1, end='')
    if c == 2:
        break
    c += 1
f.close()
