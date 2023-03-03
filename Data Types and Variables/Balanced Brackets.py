n = int(input())
stack = []

for i in range(n):
    line = input().strip()
    if line == '(':
        stack.append('(')
    elif line == ')':
        if not stack or stack.pop() != '(':
            print("UNBALANCED")
            exit()
    else:
        continue

if not stack:
    print("BALANCED")
else:
    print("UNBALANCED")
