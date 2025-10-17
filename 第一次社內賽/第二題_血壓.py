systolic = int(input()) # 收縮壓
diastolic = int(input()) # 舒張壓
if systolic >= 160 or diastolic >= 100:
    print("第二期高血壓")
elif 140 <= systolic <= 159 or 90 <= diastolic <= 99:
    print("第一期高血壓")
elif 120 <= systolic <= 139 or 80 <= diastolic <= 89:
    print("高血壓前期")
else:
    print("正常血壓")