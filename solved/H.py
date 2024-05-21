x = list(map(int, input().split()))

neko = 1
meow = 1
tmp = 0

for index, item in enumerate(x):
    if index == 0:
        neko = 1
        tmp = item
    else:
        if item - 1 == tmp:
            meow += 1
            if meow > neko: neko = meow
        else:
            meow = 1
        tmp = item
        
print(neko)