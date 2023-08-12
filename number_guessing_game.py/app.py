import random

tries = 5

answer = random.randint(0, 100)


def guess_random_num_binary(tries, start, stop):
    answer = random.randint(start, stop)
    print('The number to guess is: ', answer)

    lower_bound = start
    higher_bound = stop

    while lower_bound <= higher_bound and tries > 0:
        pivot = (lower_bound + higher_bound) // 2
        print('Number of tries left:', tries)
        print('Program guessed the number:', pivot)
        if pivot == answer:
            print('Program Found the answer:', pivot)
            break
        elif pivot > answer:
            print('Guess lower!')
            tries -= 1
            higher_bound = pivot - 1
        elif pivot < answer:
            print('Guess higher!')
            tries -= 1
            lower_bound = pivot + 1

    if tries == 0 and pivot != answer:
        print('Program was unable to find the number!')


def guess_random_num_linear(tries, start, stop):
    print('The number for the program to guess is:', answer)
    for guess in range(start, stop, 1):
        print("Number of tries left:", tries)
        if tries > 0:
            print('Program is guessing...', guess)
            if guess == answer:
                print('Program guessed the correct number!')
                exit()
            else:
                tries -= 1
        else:
            print('Program was not able to guess the correct answer.')
            break


while tries > 0:
    print("Number of tries left:", tries)
    guess = int(input("Guess a number between 0 and 10: "))
    if guess == answer:
        print('You guessed the correct number!')
        quit()
    elif guess > answer:
        tries -= 1
        print('Guess lower!')
    elif guess < answer:
        tries -= 1
        print('Guess higher!')
    else:
        print('Please guess only the numbers between 0 and 10')

print('You have failed to guess the number: ', answer)
guess_random_num_linear(5, 0, 10)
guess_random_num_binary(10, 0, 200)
