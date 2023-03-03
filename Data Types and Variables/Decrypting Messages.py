key = int(input())
number_of_lines = int(input())
new_word = ''

for decrypting in range(number_of_lines):
    char_input = input()
    int_shifted = ord(char_input) + key
    new_word += chr(int_shifted)

print(new_word)
