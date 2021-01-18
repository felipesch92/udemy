numCats = input('How many cats do you have? ')
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    elif int(numCats) > 0:
        print('That is not many cats.')
    else:
        print('Please a number bigger then 0.')
except ValueError:
    print('You did not enter a number.')
