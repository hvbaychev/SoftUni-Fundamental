num1 = int(input())
num2 = int(input())

num1, num2 = num2, num1

print(f'Before:\na = {num2}\nb = {num1}\nAfter:\na = {num1}\nb = {num2}')
