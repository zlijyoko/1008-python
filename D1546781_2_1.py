A = int(input())
B = int(input())

if (A != 0 and A != 1) or (B != 0 and B != 1):
    print("輸入錯誤")
else:
    if A == 1 or B == 1:
        or1 = 1
    else:
        or1 = 0

    if A == 1 and B == 1:
        and1 = 1
    else:
        and1 = 0

    if A != B:
        xor1 = 1
    else:
        xor1 = 0

    print(f"OR={or1}")
    print(f"AND={and1}")
    print(f"XOR={xor1}")