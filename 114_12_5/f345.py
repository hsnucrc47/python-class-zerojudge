#---- 方法一 ----
n = int(input())  # 串列長度
a = list(map(int, input().split()))

# 用迴圈從後往前印
for i in range(n - 1, -1, -1):
    print(a[i], end=" ")
n = int(input())
a = list(map(int, input().split()))
print(*a[::-1])


#---- 方法二 ----
n = int(input())
a = list(map(int, input().split())) 
print(*a[::-1])