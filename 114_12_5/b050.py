count = 0

while True:
    n = int(input())
    if n == 0:
        break

    count += 1
    data_set = []

    for _ in range(n):
        input_str = input().strip().lower()  # 讀取並轉為小寫
        data_set.append(sorted(set(input_str)))  # 使用 set 去重，然後排序

    print(f"Test Case {count}:")

    # 輸出每個集合
    for i in range(n):
        name = chr(65 + i)  # 'A' + i
        print(f"{name}: {{{''.join(data_set[i])}}}")

    # 聯集和交集
    for i in range(n):
        set_name = chr(65 + i)
        for j in range(i + 1, n):
            name = chr(65 + j)

            # 聯集
            set_union = sorted(set(data_set[i]) | set(data_set[j]))
            print(f"{set_name}+{name}: {{{''.join(set_union)}}}")

            # 交集
            set_intersection = sorted(set(data_set[i]) & set(data_set[j]))
            print(f"{set_name}*{name}: {{{''.join(set_intersection)}}}")

    # 差集
    for i in range(n):
        set_name = chr(65 + i)
        for j in range(n):
            if i != j:
                difference = sorted(set(data_set[i]) - set(data_set[j]))
                print(f"{set_name}-{chr(65 + j)}: {{{''.join(difference)}}}")

    # 包含檢查
    for i in range(n):
        set_name = chr(65 + i)
        for j in range(n):
            if i != j:
                if set(data_set[i]) >= set(data_set[j]):
                    print(f"{set_name} contains {chr(65 + j)}")
                else:
                    print(f"{set_name} does not contain {chr(65 + j)}")
