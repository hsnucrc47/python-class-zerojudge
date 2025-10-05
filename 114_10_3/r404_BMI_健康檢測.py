name = input()
height = float(input()) 
weight = float(input())
bmi = weight / (height * height)

print(name, "的BMI為", bmi)

if bmi >= 24:
    print("體重過重！")
elif bmi < 18:
    print("體重過輕！")
else:
    print("健康體位")
