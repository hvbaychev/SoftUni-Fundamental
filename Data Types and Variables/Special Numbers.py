number = input()

for num in range(1, int(number)+1):
    new_number = str(num)
    calculate = 0
    for num_str in new_number:
        calculate += int(num_str)
    if calculate == 5 or calculate == 7 or calculate == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
