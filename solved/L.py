ln = input()
t = input()

vln = 1
kln = 1
tmp = ""

for idx, itm in enumerate(t):
    if idx == 0:
        tmp = itm
        vln = 1
    else:
        if tmp == itm:
            vln += 1
            if vln > kln:
                kln = vln
            else:
                vln = 1
        else:
            vln = 1
            
print(kln)