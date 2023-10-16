# Task 3: Write a program to implement the 3n+1 algorithm.

# The user will input n and your program should return the length L(n) and the terminating value T(n) of the 3n+1 algorithm.

# Use your program to create a table giving the length and terminating value for all starting values
# between 1 and 100 (both included).

def three_n_plus_1(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
            length += 1
        else:
            n = 3 * n + 1
            length += 1
    return length


while True:
    n = int(input("Enter the value of n: "))
    print(f"Length L(n) is {three_n_plus_1(n)}.")
    print(f"Terminating value T(n) is 1")
    print("-----------------------------------")
    if input("Do you want to continue? (y/n) ").upper() != "Y":
        break

for i in range(1, 51):
    print(f"i = {i}\tL({i}) = {three_n_plus_1(i)}\tT({i}) = 1"
          f"\t\t\ti = {i + 50}\tL({i+50}) = {three_n_plus_1(i + 50)}\t"
          f"T({i+50}) = 1")
