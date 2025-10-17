a1, n1, a2, n2 = input().split()
a1, n1 = float(a1), int(n1)
a2, n2 = float(a2), int(n2)

num1 = a1 * (10 ** n1)
num2 = a2 * (10 ** n2)

if num1 > num2:
    print(a1,"* 10 ^", n1)
elif num2 > num1:
    print(a2, "* 10 ^", n2)
else:
    print("Same")