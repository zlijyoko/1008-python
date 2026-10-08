A = int(input('A (0 or 1): '))
B = int(input('B (0 or 1): '))
S = int(input('S (0 or 1): '))

if (A != 0 and A != 1) or (B != 0 and B != 1) or (S != 0 and S != 1):
    print("輸入錯誤")
else:
    if A != B:
        middle = 1
    else:
        middle = 0

    if middle == 1 and S == 1:
        start = 1
    else:
        start = 0

    print(f"第一個閘輸出={middle}")
    print(f"允許啟動={start}")