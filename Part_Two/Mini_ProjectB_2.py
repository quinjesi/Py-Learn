secret_number = 10
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess the secret number(between 1 and 20): '))
    guess_count += 1
    if guess == secret_number:
        print('Hurray! You guessed the secret number!')
        break
else:
        print('Sorry, you have reached the maximum number of guesses.')
       
