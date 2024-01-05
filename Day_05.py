# 1.First Approach
number,power = int(input("Enter A Number: ")),int(input("Enter A Power: "))
print(pow(number,power))

# 2.Second Approach
number,power = int(input("Enter A Number: ")),int(input("Enter A Power: "))
output=number
for i in range(1,power):
    output *= number
print(output)

# 3.Second Approach
number,power = int(input("Enter A Number: ")),int(input("Enter A Power: "))
print(number**power)

# 4.Second Approach
def recursive(number,power):
    if power == 0:
        return 1
    return number*recursive(number,power-1)

number,power = int(input("Enter A Number: ")),int(input("Enter A Power: "))
print(recursive(number,power))



