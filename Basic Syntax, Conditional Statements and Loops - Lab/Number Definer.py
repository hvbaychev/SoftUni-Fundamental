n = float(input())

if n == 0:
    print('zero')
elif 0 < n <= 1:
    print('small positive')
elif 1 < n <= 1_000_000:
    print('positive')
elif n > 1_000_000:
    print('large positive')
elif 0 > n >= -1:
    print('small negative')
elif -1 > n >= -1_000_000:
    print('negative')
elif n < -1_000_000:
    print('large negative')

