money = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk_liter = price_flour * 1.25
for_one_bread = price_eggs + price_flour + (price_milk_liter / 4)


count_bread = 0
count_eggs = 0

while money >= for_one_bread:
    money -= for_one_bread
    count_eggs += 3
    count_bread += 1
    if count_bread % 3 == 0:
        count_eggs -= count_bread - 2

print(f"You made {count_bread} loaves of Easter bread! Now you have {count_eggs} eggs and {money:.2f}BGN left.")

        