group_size = int(input())
days = int(input())
coins = 0

for every_day in range(1, days+1):
    if every_day % 10 == 0:
        group_size = group_size - 2
    if every_day % 15 == 0:
        group_size = group_size + 5

    coins = (coins + 50) - (2 * group_size)
    if every_day % 3 == 0:
        coins = coins - (3 * group_size)
    if every_day % 5 == 0:
        coins = coins + (20 * group_size)
        if every_day % 3 == 0:
            coins = coins - (2 * group_size)

coins_total_for_person = coins / group_size
print(f'{group_size} companions received {coins_total_for_person:.0f} coins each')
