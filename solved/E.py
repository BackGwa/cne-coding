rsum = 0
flip = False
x = int(input())

for i in range(1, x + 1):
    if flip:
        rsum -= i
    else:
        rsum += i
    flip = not flip

print(rsum)