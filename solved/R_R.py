n = int(input())
f = list()
r = list()

for i in range(n):
    f.append(list(map(int, input().split())))

for i in f:
    r.append(min(i))

print(sum(r))