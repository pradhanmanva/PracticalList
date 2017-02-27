def getBinary(num):
    dummy = num
    bin=[]
    while(dummy>0):
        bin.append(dummy%2)
        dummy=int(dummy/2)
    return bin


bin = getBinary(50)
Binary = 0
for i in range(len(bin)):
    Binary += bin[i]*(10**i)
print(bin)
print(Binary)