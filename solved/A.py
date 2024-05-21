student = int(input())
ki = list()

for _ in range(student):
    ki.append(int(input()))

ki.sort()
ag = int(sum(ki) / student)

if student % 2 == 0:
    x = ki[(student // 2) - 1]
    y = ki[(student // 2)]
    z = (x + y) / 2
else:
    z = ki[student // 2]

print(ag)
print(int(z))