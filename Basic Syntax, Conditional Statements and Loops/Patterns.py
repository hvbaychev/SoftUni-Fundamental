n = int(input())

for row in range(1, n+1):
    print('*'*row)

for col in range(n-1, -1, -1):
    print('*'*col)