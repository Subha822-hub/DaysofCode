# 1.First Approach
number = int(input("Enter A Number: "))
sum1 = 0
p = number
l = []
while(number>0):
    x=number%10
    l.append(x)
    number=number//10
sum1 = sum(l)
if(p%sum1==0):
    print("Harshad Number")
else:
    print("Not Harshad Number")

# 2.Second Approach

number = int(input("Enter A Number: "))
sum1 = 0
p = number
while(number>0):
    sum1+=number%10
    number=number//10
if(p%sum1==0):
    print("Harshad Number")
else:
    print("Not Harshad Number")
