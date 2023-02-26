ORNAMENT_SET_PRICE = 2
TREE_SKIRT_PRICE = 5
TREE_GARLAND_PRICE = 3
TREE_LIGHTS_PRICE = 15

quantity_decoration = int(input())
days_to_christmas = int(input())
plus = 0

money = 0
christmas_spirit = 0

for remain_days in range(1, days_to_christmas+1):
    if remain_days % 11 == 0:
        quantity_decoration += 2
        continue
    if remain_days % 2 == 0:
        money += ORNAMENT_SET_PRICE * quantity_decoration
        christmas_spirit += 5
        plus += ORNAMENT_SET_PRICE * quantity_decoration
    if remain_days % 3 == 0:
        money += (TREE_SKIRT_PRICE * quantity_decoration + TREE_GARLAND_PRICE * quantity_decoration)
        christmas_spirit += 13
        plus += (TREE_SKIRT_PRICE * quantity_decoration + TREE_GARLAND_PRICE * quantity_decoration)
    if remain_days % 5 == 0:
        money += TREE_LIGHTS_PRICE * quantity_decoration
        plus += TREE_LIGHTS_PRICE * quantity_decoration
        if remain_days % 3 == 0:
            christmas_spirit += 30 + 17
        else:
            christmas_spirit += 17
    if remain_days % 10 == 0:
        if remain_days > 11:
            money += ORNAMENT_SET_PRICE + TREE_SKIRT_PRICE + TREE_GARLAND_PRICE
            christmas_spirit -= 20
    if remain_days == days_to_christmas and remain_days % 10 == 0:
        christmas_spirit -= 30

    plus = 0

print(money)
print(christmas_spirit)