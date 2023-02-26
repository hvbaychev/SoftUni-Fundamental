devisor = int(input())
boundary = int(input())
max_number = 0

for i in range(devisor, boundary+1):
    if i % devisor == 0:
        max_number = max(i, max_number)
print(max_number)

