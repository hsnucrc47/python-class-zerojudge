while True:
    try:
        s1 = input()
        s2 = input()
        a = ord(s1[0])  # 取得 s1 的第一個字元的 ASCII 值
        b = ord(s2[0])  # 取得 s2 的第一個字元的 ASCII 值

        if b >= a:
            k = b - a
        else:
            k = 26 - (a - b)

        print(k)
    except EOFError:
        break  # 當沒有更多輸入時退出循環