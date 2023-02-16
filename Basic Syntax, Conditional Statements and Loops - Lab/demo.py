import sys
import math

max_score = -sys.maxsize
strongest_word = None
word = input()

while word != 'End of words':
    sum_word = 0

    for char in word:
        sum_word += ord(char)

    if word[0] in ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'):
        sum_word *= len(word)
    else:
        sum_word /= len(word)

    if sum_word >= max_score:
        max_score = sum_word
        strongest_word = word

    word = input()

print(f"The most powerful word is {strongest_word} - {math.floor(max_score)}")