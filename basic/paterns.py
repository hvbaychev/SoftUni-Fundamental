# Write a program that receives a number and creates the following pattern.
# The number represents the largest count of stars on one row.

n = int(input())

for i in range(1, n+1):
    for j in range(0, i):
        print ("*", end='')
    print()

for x in range(n-1, 0, -1):
    for y in range(0, x):
        print("*", end='')
    print()