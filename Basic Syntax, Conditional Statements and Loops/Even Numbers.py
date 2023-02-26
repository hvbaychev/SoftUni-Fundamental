n = int(input())

for number in range(n):
    num1 = int(input())

    if num1 % 2 != 0:
        print(f'{num1:.0f} is odd!')
        break
else:
    print('All numbers are even.')



