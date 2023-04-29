budjet = int(input())
total_money = 0
command_line = input()
while command_line != "End":
    command = int(command_line)
    if total_money + command > budjet:
        print('You went in overdraft!')
        exit()

    total_money += command
    command_line = input()

print('You bought everything needed.')


