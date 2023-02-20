string1 = input()
string2 = input()

result = ""

for i in range(len(string1)):
    result += string2[i]
    if result not in string1:
        print(result)
