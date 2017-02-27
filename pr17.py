num = 100

a=0
b=1
sum = a+b
print("%d %d" %(a,b),end=" ")
for i in range(1,num-1):
    print(sum,end=" ")
    a=b
    b=sum
    sum=a+b