# 1.First Approach

number = int(input("Enter A Number: "))
if number %2==0:
    print("Even")
else:
    print("Odd")

# 2.Second Approach

number = int(input("Enter A Number: "))
print("Even" if number%2==0 else "Odd")

# 3.Third Approach

def isEven(number):
    return not number&1

if __name__ == '__main__':
    number=int(input("Enter A Number: "))
    if isEven(number):
        print("Even")
    else:
        print("Odd")



