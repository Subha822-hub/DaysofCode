# 1.First Approach

number = int(input("Enter A Number: "))
sum = 0
for i in range(0,number+1):
    sum = sum+i
print(sum)


# 2.Second Approach

number = int(input("Enter A Number: "))
print(int(number*(number+1)/2))


# 3.Second Approach

def getSum(number):
    if number == 1:
        return number
    return number+getSum(number-1)

number = int(input("Enter A Number: "))
print(getSum(number))

