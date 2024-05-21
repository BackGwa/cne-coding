h = 0
m = 0

def hm(hh, mm):
    print(str(hh).zfill(2), str(mm).zfill(2))

def x():
    global h, m
    m += 5

    if m >= 60:
        h += 1
        m = m - 60
        hm(h, m)
    else:
        hm(h, m)

h, m = map(int, input().split())

hm(h, m)
x()
x()