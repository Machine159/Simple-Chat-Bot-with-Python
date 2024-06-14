def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")

    print("Which of the following statements about Python lists is true?\n"
          "1. Python lists can only contain elements of the same data type.\n"
          "2. The elements in a Python list are indexed starting from 1.\n"
          "3. Python lists are mutable, meaning their elements can be changed after the list is created.\n"
          "4. Python lists do not support slicing operations.")

    answer = 0

    while answer != 3:
        answer = int(input())
        if answer == 3:
            print('Completed, have a nice day!')
        else:
            print("Please, try again.")


def end():
    print('Congratulations, have a nice day!')


greet('Albert', '2024')
remind_name()
guess_age()
count()
test()
end()
