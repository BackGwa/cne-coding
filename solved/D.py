tcase = int(input())
tin = list(map(int, input().split()))

perfect = list()
over = 0

for i in tin:
    div = [j for j in range(1, i) if i % j == 0]
    result = sum(div)
    if result == i: perfect.append(i)
    if result > i: over += 1

for i in perfect:
    print(i, end=" ")
print()

print(f"{len(perfect)} {over}")