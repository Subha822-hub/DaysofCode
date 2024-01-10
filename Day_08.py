# 1.First Approach

number = int(input("Enter A Number: "))
sum = 0
for i in range(1,number):
    if number%i==0:
        sum = sum + i
if(sum>number):
    print("Abundant Number")
else:
    print("Not Abundant Number")

        


