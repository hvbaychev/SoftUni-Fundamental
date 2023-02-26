capacity = 255
n = int(input())
total_fill = 0

for fill in range(n):
    fill_up = int(input())
    total_fill += fill_up
    if capacity < total_fill:
        print('Insufficient capacity!')
        total_fill -= fill_up

print(f'{total_fill}')