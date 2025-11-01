def num_to_word(number):
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    elif number % 3 == 0 and number % 5 != 0:
        return "Fizz"
    elif number % 3 != 0 and number % 5 == 0:
        return "Buzz"
    else:
        return number

first = input()
second = input()
third = input()

if first.isdigit():
    print(num_to_word(int(first) + 3))
elif second.isdigit():
    print(num_to_word(int(second)+2))
elif third.isdigit():
    print(num_to_word(int(third)+1))

