tcase = int(input())
tree = dict()
for i in range(tcase):
    ch, bin = input().split()
    tree[ch] = bin

bint = input()
ko = list()

for key, value in tree.items():
    ko.append([key, value])
    
ko.sort(reverse=True)

for key, value in ko:
    bint = bint.replace(value, key)

print(bint)