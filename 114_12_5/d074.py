n = int(input())
a = list(map(int, input().split()))
max_value = 0
for i in range(n):
    if a[i] > max_value:
        max_value = a[i]
print(max_value)
    