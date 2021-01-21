from random import randint

random_number = randint(1, 10)
c = 1
while True:
    number = int(input('Try to guess the number: '))
    if number == random_number:
        print(f'Congratulations! You guessed computer number in {c} guesses!')
        break
    elif number > random_number:
        print('Your number is too high.')
    elif number < random_number:
        print('Your number is too low.')
    c += 1
