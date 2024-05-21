person = int(input())
sec = list(map(int, input().split()))
x = 0

sec.sort()

for i in range(person):
    for j in range(i + 1):
        x += sec[j]

print(x)