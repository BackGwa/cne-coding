w, h = map(int, input().split())

for idx_h in range(h):
    if idx_h == 0 or idx_h + 1 == h:
        for idx_w in range(w):
            if idx_w == 0 or idx_w + 1 == w:
                print("+", end="")
            else:
                print("-", end="")
    else:
        for idx_w in range(w):
            if idx_w == 0 or idx_w + 1 == w:
                print("|", end="")
            else:
                print(" ", end="")
    print()