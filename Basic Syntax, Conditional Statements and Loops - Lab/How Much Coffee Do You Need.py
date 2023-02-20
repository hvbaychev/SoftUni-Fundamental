number_of_coffee = 0
command = input()
while command != 'END':
    if number_of_coffee == 5:
        break
    if command == 'DOG' or command == 'CAT' or command == 'MOVIE' or command == 'CODING':
        number_of_coffee += 2
    elif command == 'dog' or command == 'cat' or command == 'movie' or command == 'coding':
        number_of_coffee += 1
    else:
        number_of_coffee += 0

    command = input()

if command == 'END':
    print(number_of_coffee)
else:
    print('You need extra sleep')