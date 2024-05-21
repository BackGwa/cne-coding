_ = input()
tomato = list(map(int, input().split()))

A = 0
B = 0
C = 0

for i in tomato:
    if i >= 300:
        A += 1
    elif i >= 200:
        B += 1
    else:
        C += 1

print(f"A({A}) B({B}) C({C})")

print("A ", end="")
for i in range(A):
    print("*", end=" ")
print()

print("B ", end="")
for i in range(B):
    print("*", end=" ")
print()

print("C ", end="")
for i in range(C):
    print("*", end=" ")
print()