def evenWhileCounter1():
    counter = 1
    while counter <= 20:
        if counter % 2 == 0:
            print(counter)
        counter = counter + 1


def evenWhileCounter3():
    counter = 2
    while True:
        print(counter)
        counter = counter + 2

        if counter == 22:
            break


def evenWhileCounter2():
    counter = 2
    while counter <= 20:
        print(counter)
        counter = counter + 2
        # Easier way to write this : counter += 2

def evenForCounter1():
    for counter in range(1, 21):
        if counter % 2 == 0:
            print(counter)


def evenForCounter2():
    step = 2
    for counter in range(2, 21, step):
        print(counter)


def evenForCounter3():
    for counter in range(1,21):
        if counter % 2 != 0:
            continue
        print(counter)

def hitchhikers():
    # Keep taking the loop
    while True:
        # Take the user input
        number = int(input())

        # Check if it's 42
        if number == 42:
            # print
            print('Answer to life, and...')

            # Stop asking and looping
            break


def printStars(n):
    for row in range(1, n+1):
        for star in range(1, row + 1):
            print ('*', end='')
        print('')


def printStarsWhile(n):
    row = 1
    while row <= n:
        star = 1
        while star <= row:
            print('*', end='')
        print('')
        row += 1

printStars(10)


def printCharacters(word):
    for index in range(0, len(word)):
        print(word[index])

    for character in word:
        print(character)

printCharacters('Hello')