money = int(input())
total_sum = 0
command = input()
while command != 'End':
    command_int = int(command)
    if total_sum + command_int > money:
        print('You went in overdraft!')
        exit()

    total_sum += command_int
    command = input()

print('You bought everything needed.')
