tin = int(input())

def chk(tin):
    for i in range(2, tin):
        if tin % i == 0:
            return False
    return True
        
if chk(tin):
    print(f"{tin} 는(은) 소수입니다.")
else:
    print(f"{tin} 는(은) 소수가 아닙니다.")
    