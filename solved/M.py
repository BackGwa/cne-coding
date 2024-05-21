def sh(n):
    pak = list()
    x = list()
    y = list()
    for i, j in enumerate(n):
        if i < 5:
            x.append(j)
        else:
            y.append(j)
    for i in range(5):
        if i + 1 % 2 != 0:
            pak.append(x[i])
            pak.append(y[i])
        else:
            pak.append(y[i])
            pak.append(x[i])
    return pak

rs = int(input())
x = range(1, 11)

for _ in range(rs):
    x = sh(x)
    
print(" ".join(list(map(str, x))))