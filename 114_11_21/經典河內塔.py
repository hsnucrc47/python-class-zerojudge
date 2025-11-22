def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disc 1 from {source} to {target}")
    else:
        hanoi(n - 1, source, target, auxiliary)
        print(f"Move disc {n} from {source} to {target}")
        hanoi(n - 1, auxiliary, source, target)
 
n = int(input())
hanoi(n, 'A', 'B', 'C')