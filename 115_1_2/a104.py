while True:
    try:
        n = int(input())
        k = list(map(int, input().split()))
        print(*sorted(k))
    except EOFError:
        break