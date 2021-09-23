def greet(name):
    print("Hi,", name, "!")

def multiply(a,b):
    c = a * b
    return c

def isPrime(a):
    isAPrime = False
    if a > 1:
        if a == 2 or a == 3 or a == 5:
            return True
        else:
            for i in range(2, a // 2):
                    if (a % i) == 0:
                        return False
                    else:
                        return True
    else:
        print(a, "is 1!")
        return

urName = str(input("What is your name?"))
greet(urName)
num1 = int(input("Please give me a number: "))
num2 = int(input("Please give me another number: "))
print(num1, "multiplied by", num2, "is" , multiply(num1,num2), "! \n")
num3 = int(input("Please give me a new number! I am going to check if it is a prime number."))
num3prime = isPrime(num3)
if num3prime == True:
    print(num3, "is a prime!")
else:
    print(num3, "is not a prime!")
