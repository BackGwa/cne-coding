import random

me = 100
ai = 100

seed = int(input())

for i in range(int(input())):
    if me <= 0 or ai <= 0: break
    random.seed((17 * seed + 35) % 10000)
    seed = (17 * seed + 35) % 10000
    act = int(input())
    if act == 0:
        ai -= 30
    elif act == 1:
        me += 20
    else:
        ai -= random.randint(0, 50)
        
    ai_act = random.randint(0, 2)
    if act == 0:
        me -= 30
    elif act == 1:
        ai += 20
    else:
        me -= random.randint(0, 50)

if me == ai:
    print("무승부")
elif me > ai:
    print("승리")
else:
    print("패배")