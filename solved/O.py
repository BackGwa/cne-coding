from datetime import date

by, bm, bd = map(int, input().split())
ay, am, ad = map(int, input().split())

wd = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
bday = date(by, bm, bd)
aday = date(ay, am, ad)
dday = aday - bday

print(wd[bday.weekday()])
print(wd[aday.weekday()])
print(f"D-{dday.days}")