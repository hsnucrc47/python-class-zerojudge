import bisect

N, K = map(int, input().split()) # 數列長度與詢問數
arr = list(map(int, input().split())) # 數列（ n 個整數）
queries = list(map(int, input().split())) # 要找那些值

for x in queries:
    idx = bisect.bisect_left(arr, x) # 二分搜尋法取得位置
    if arr[idx] == x: #  如果數列在該位置找得到 x
        print(idx + 1) # 輸出位置（∵索引值從 0 開始 ∴要+1）
    else:
        print(0) # 該位置不是 x 的話輸出 0