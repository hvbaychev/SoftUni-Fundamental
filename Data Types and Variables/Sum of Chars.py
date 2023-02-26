number_of_char = int(input())
sum_of_char = 0

for char in range(number_of_char):
    text = input()
    sum_of_char += ord(text)

print(f'The sum equals: {sum_of_char:.0f}')