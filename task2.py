# Task 2: Write a program to compute the greatest common divisor gcd(a, b) of two integers a and b.
#
# Your program should work even if one of a or b is zero.
#
# Make sure that you don’t go into an infinite loop if a and b are both zero!

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
    except ValueError:
        print("Input is not valid. Please enter a number.")
        continue

    if a == 0 or b == 0:
        print(f"GCD of {a} and {b} is undefined.\n")
    else:
        print(f"GCD of {a} and {b} is {gcd(a, b)}")

    if input("Do you want to continue? (y/n) ").upper() != "Y":
        break
