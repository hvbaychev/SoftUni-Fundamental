command = input()
while command != 'End':
    for char in command:
        if command == 'SoftUni':
            continue
        print(f'{char*2}', end='')
    if command != 'SoftUni':
        print()
    command = input()