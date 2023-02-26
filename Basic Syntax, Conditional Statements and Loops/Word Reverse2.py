word = input()
revers_word = ''

for char in range(len(word) - 1, - 1, -1):
    revers_word += word[char]
print(revers_word)
