start  = 100
end = 500

for i in range(start, end):
    flag = 1
    for j in range(2, i-1):
        if(i%j==0):
            flag = 0
            break
    if flag == 0:
        print("",end="")
    else:
        print("%d" %(i),end=" ")