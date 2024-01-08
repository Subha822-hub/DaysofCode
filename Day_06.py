# 1.First Approach
number = int(input("Enter A Number: "))
square =  pow(number,2)
mod = pow(10,len(str(number)))
if square%mod == number:
    print("It's an Automorphic Number")
else:
    print("It's not an Automorphic Number")

# 2.Second Approach
number = int(input("Enter A Number: "))
a=str(number)
square =  pow(number,2)
b=str(square)

if b.endswith(a):
    print("It's an Automorphic Number")
else:
    print("It's not an Automorphic Number")

# 3.Third Approach
number = int(input("Enter A Number: "))
print("It's an Automorphic Number" if int(str(number**2)[-len(str(number))::])==number else "It's not an Automorphic Number")
