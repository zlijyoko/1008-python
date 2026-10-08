n = int(input('請輸入一個整數(0~15): '))

if n < 0 or n > 15:
    print('輸入錯誤')
else:
    a0 = n % 2
    f1 = n // 2 

    a1 = f1 % 2
    f2 = f1 // 2

    a2 = f2 % 2
    f3 = f2 // 2

    a3 = f3 % 2

    print(f"二進制: {a3}{a2}{a1}{a0}")

    b0 = n % 8  
    b1 = n // 8  

    print(f"八進制: {b1}{b0}")

    c = n % 16
    if c == 10:
        c0 = "A"
    elif c == 11:
        c0 = "B"
    elif c == 12:
        c0 = "C"
    elif c == 13:
        c0 = "D"
    elif c == 14:
        c0 = "E"
    elif c == 15:
        c0 = "F"
    else:
        c0 = str(c)

    print(f"十六進制: {c0}")