import sys

print("This is a python fizzbuzz program. Numbers divisible by 3 will return \"fizz\", numbers divisible by 5 will return \"buzz\", and numbers divisible by both 3 and 5 will return \"fizz buzz.\"")  

while True:
    number_choice = input("Enter a number between 1 and 500: ")
    try:
        val = int(number_choice)
        if val < 0:
            print("Input must be greater than 0.")
            continue
        elif val > 500:
            print("Input must be 500 or less.")
            continue
        break
    except ValueError:
        print("Input must be a number.")

for n in range(1,val+1):
    if n % 3 == 0 and n % 5 == 0:
        print("fizz buzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)
