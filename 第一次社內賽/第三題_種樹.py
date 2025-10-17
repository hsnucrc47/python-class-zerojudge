n = int(input())
k = int(input())

# 樹的葉子
for i in range(2, n + 2):
    for j in range(1, i + 1):
        print('B' * (n + 1 - j) + 'A' * (j * 2 - 1) + 'B' * (n + 1 - j))

# 樹幹
for _ in range(k):
    print('B' * n + 'C' + 'B' * n)