for i in range(1, 10):
    for j in range(1, 10):
        if j != 9:
            print(i, "*", j, "=", i*j, sep="", end="\t")
        else:
            print(i, "*", j, "=", i*j, sep="", end="\n")

'''
備註：「\t」的意思是縮排，也就是按 Tab 。
'''
