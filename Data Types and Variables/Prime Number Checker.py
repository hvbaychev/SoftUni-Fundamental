num = int(input())

# To take input from the user
# num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print('False')
            break
    else:
        print("True")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")