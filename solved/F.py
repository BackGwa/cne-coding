m = int(input())
don = 0

if m >= 24 * 60:
    don = 20
else:
    while (m > 0):
        if (m >= 60):
            don += 1
            m -= 60
        else:
            don += 1
            break

print(f"이용 요금은 {don * 1000}원 입니다.")