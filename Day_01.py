# 1.First Approach

number = int(input("Enter A Number: "))
if number >0:
    print("Positive")
elif number <0:
    print("Negative")
else:
    print("Zero")

# 2.Second Approach

number = int(input("Enter A Number: "))
if (number>=0):
    if (number==0):
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

# 3.Second Approach

number = int(input("Enter A Number: "))
print("Positive" if number>=0 else "Negative")
