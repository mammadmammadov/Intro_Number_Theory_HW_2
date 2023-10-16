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


n = int(input("Enter the value of n: "))
print(f"Length L(n) is {three_n_plus_1(n)}.")
print(f"Terminating value T(n) is 1")
print("-----------------------------------")

for i in range(1, 51):
    print(f"i = {i}\tL(n) = {three_n_plus_1(i)}\tT(n) = 1"
          f"\t\t\ti = {i + 50}\tL(n) = {three_n_plus_1(i + 50)}\tT(n) = 1")
