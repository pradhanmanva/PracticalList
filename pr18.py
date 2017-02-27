def checkArmstrong(num):
    dummy = num;
    sum = 0
    while num > 0:
        sum = sum + (num % 10) ** 3
        num = int(num / 10)
    if dummy == sum:
        return True
    else:
        return False

start = 1
end = 1000

for i in range(start,end+1):
    check = checkArm    strong(i)
    if check == True:
        print(i,end=" ")