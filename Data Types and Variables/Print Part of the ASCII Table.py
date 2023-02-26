start = int(input())
end = int(input())

for ascii_table in range(start, end+1):
    new_char = chr(ascii_table)
    print(f'{new_char}', end=" ")