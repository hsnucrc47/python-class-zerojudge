row, column = map(int, input().split()) #輸入列與行
list1=[] #先創空白的 list1 備用

for i in range(row): 
    list2=list(map(int,input().split())) #輸入第 i 列的資料
    list1.append(list2) #將第 i 列的資料放入 list1

for i in range(column):
    for j in range(row): 
        print(list1[j][i],end=" ") #將列與行顛倒輸出
    print() #換行