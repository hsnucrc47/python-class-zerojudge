import random

ans = random.randint(2, 98) #答案隨機選一個。
min_num = 1 #預設答案大於 1 。
max_num = 99 #預設答案小於 99 。

while True:

    #輸出範圍。
    print(min_num, "~", max_num) 

    #若只剩一個數字可以選，輸出你輸了並結束迴圈。
    if max_num - min_num == 2:
        print("你輸了。正確答案為", ans ,"。") 
        break

    #輸入要猜的數字。
    guess = int(input())

    #若超出範圍，迴圈直接跳到下一輪。
    if guess >= max_num or guess <= min_num:
        print("超出範圍，請重新輸入。")
        continue

    #若比答案大，將 max_num 設為這次的猜測，更新完後迴圈跳到下一輪
    elif guess > ans:
        print("太大了！")
        max_num = guess 
        continue

    #若比答案小，將 min_num 設為這次的猜測 ，更新完後迴圈跳到下一輪
    elif guess < ans:
        print("太小了！")
        min_num = guess
        continue

    #若上述條件皆不成立，表示猜對了。輸出答對了並結束迴圈。
    else:
        print("恭喜你答對了！")
        break
