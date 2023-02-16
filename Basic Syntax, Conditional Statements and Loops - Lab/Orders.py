n = int(input())
total_price = 0
price = 0


for orders in range(1, n+1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if price_per_capsule < 0.01 or days < 1 or capsules_needed_per_day < 1:
        continue

    total_price += price_per_capsule * days * capsules_needed_per_day
    price = price_per_capsule * days * capsules_needed_per_day

    print(f'The price for the coffee is: ${price:.2f}')

if total_price >= 0:
    print(f'Total: ${total_price:.2f}')