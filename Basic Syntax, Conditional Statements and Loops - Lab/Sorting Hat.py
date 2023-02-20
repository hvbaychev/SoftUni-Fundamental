command = input()

while command != 'Welcome!':
    len_of_the_name = len(command)
    if command == 'Voldemort':
        print('You must not speak of that name!')
        exit()

    if len_of_the_name < 5:
        print(f'{command} goes to Gryffindor.')
    elif len_of_the_name == 5:
        print(f'{command} goes to Slytherin.')
    elif len_of_the_name == 6:
        print(f'{command} goes to Ravenclaw.')
    elif len_of_the_name > 6:
        print(f'{command} goes to Hufflepuff.')

    command = input()

print('Welcome to Hogwarts.')
