n = int(input())

for char in range(n):
    text = input()

    for symbol in text:
        if symbol == '_' or symbol == '.' or symbol == ',':
            print(f'{text} is not pure!')
            exit()

    print(f'{text} is pure.')
