# 1.First Approach

number = int(input("Enter A Number: "))
num = number
digit,sum = 0,0
length = len(str(num))
for i in range(length):
    digit = int(num%10)
    num = num/10
    sum += pow(digit,length)
if sum == number:
    print("Armstrong")
else:
    print("Not Armstrong")

# 2.Second Approach

number = int(input("Enter A Number: "))
num = number
sum = 0
length = len(str(num))
def checkArmstrong(num,length,sum):
    if num == 0:
        return sum
    sum += pow(int(num%10),length)
    return checkArmstrong(num/10,length,sum)

if checkArmstrong(num,length,sum)==number:
    print("Armstrong")
else:
    print("Not Armstrong")

