quantity = int(input())
days = int(input())

ornament_set = 2
three_skirt = 5
three_garland = 3
three_lights = 15

christmas_spirit = 0
sum_spent = 0

for day_number in range(1, days+1):
    if day_number % 11 == 0:
        quantity += 2
    if day_number % 2 == 0:
        sum_spent += ornament_set * quantity
        christmas_spirit += 5
    if day_number % 3 == 0:
        sum_spent += (three_skirt * quantity + three_garland * quantity)
        christmas_spirit += 13
    if day_number % 5 == 0:
        sum_spent += three_lights * quantity
        christmas_spirit += 17
        if day_number % 3 == 0:
            christmas_spirit += 30
    if day_number % 10 == 0:
        sum_spent += three_lights + three_garland + three_skirt
        christmas_spirit -= 20

    if day_number == days and day_number % 10 == 0:
        christmas_spirit -= 30

print(f'Total cost: {sum_spent}')
print(f'Total spirit: {christmas_spirit}')
