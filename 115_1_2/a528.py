'''
這題題目忘記說要 EOFError 終止了
'''

while True:
    try:
        arr = []
        n = int(input())
        for i in range(n):
            k = int(input())
            arr.append(k)
        arr.sort()
        for i in range(n):
            print(arr[i])
    except EOFError:
        break

