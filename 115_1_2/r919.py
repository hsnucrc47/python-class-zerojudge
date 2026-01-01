n, t = map(int, input().split()) # 機器數量、目標產品總數。
k = list(map(int, input().split())) 

'''計算：如果給我們 mid 秒，總共能做多少產品？'''
def cal(mid):
    ret = 0
    for i in range(n):
        # mid 秒 ÷ 該臺機器製造一個產品所需的時間 = 該機器的產量
        # 全部加總後就是總產量
        ret += mid // k[i] 
    return ret

# 假設最小需要 0 秒；最大需要 1 × 10¹⁸ 秒。
l, r = 0, 10 ** 18

'''二分搜尋'''
# 終止條件：當最小值（ l ）與最大值（ r ）相差不到 1 時結束
while l < r - 1:

    mid = (l + r) // 2 # 時間從中間值開始測試

    if cal(mid) < t: # 如果帶入函式計算後的產量 ＜ 目標產量

        # 將最小秒數設為 mid
        l = mid
    else:
        # 否則將最大秒數設為 mid
        r = mid

print(r) # 最終需要 r 秒