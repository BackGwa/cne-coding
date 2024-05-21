tcase = int(input())
size = list(map(int, input().split()))
size.sort()

tmp = list()
cost = 0

if tcase % 2 == 0:
    for i in range(0, tcase, 2):
        tmp.append(size[i] + size[i + 1])
else:
    for i in range(0, tcase, 2):
        if i == tcase - 1:
            tmp.append(size[i])
        else:
            tmp.append(size[i] + size[i + 1])

print(sum(tmp) * 2)