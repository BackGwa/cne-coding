x = int(input())
y = 0

zan = x // 15
tul = x // 13
aca = x // 10

zan1 = x % 15
tul1 = x % 13
aca1 = x % 10

if tul > zan < aca:
    y = zan
elif zan > tul < aca:
    y = tul
elif tul > aca < zan:
    y = aca
elif zan1 != 0 or tul1 != 0 or aca1 != 0:
    y += 1
print(y)