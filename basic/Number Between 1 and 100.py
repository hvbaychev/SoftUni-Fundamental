# Write a program that reads different floating-point numbers from the console.
# When it receives a number between 1 and 100 inclusive, the program should stop reading
# and should print "The number {number} is between 1 and 100".


n = float(input())


while not 1 <= n <= 100:
    n = float(input())

print(f'The number {n} is between 1 and 100')