x = input()
n = set()
k = dict()
m = list()

for i in x:
    if i in n:
        k[i] += 1
    else:
        n.add(i)
        k[i] = 1

for i, j in k.items():
    m.append([i, j])
    
m.sort()

for i, j in m:
    print(f"{i} : {j}")