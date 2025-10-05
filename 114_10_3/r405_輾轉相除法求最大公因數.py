a = int(input())
b = int(input())
print("gcd(", a,", ", b, ") = ", sep ="", end="")

r = a % b
while r > 0:
    a = b
    b = r
    r = a % b

print(b)
