import random
attempts_list = []
def show_score():
    if len(attempts_list) <=0:
        print("there is currently no high score. its your for taking")
    else:
        print("the current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1,10))
    print('hello traveler, welcome to the game of the guess')
    player_name = input('what is your name?')
    wanna_play = input('HI, {}, would you like to play the guessing game? enter (yes/no)'.format(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower() ==  'yes':
        try:
            guess = input('pick a number between 1 and 10')
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError('please guess the number within the number range')
            if int(guess) == random_number:
                print('nice you got it')
                attempts+= 1
                attempts_list.append(attempts)
                print('it took you {} attempts'.format(attempts))
                play_again = input('would you like to play again? yes/no')
                attempts = 0 
                show_score()
                random_number = int(random.randint(1,10))
                if play_again.lower() == 'no':
                    print('this is cool, have a good one')
                    break
            elif int(guess) < random_number:
                print('its lower')
                attempts += 1
            elif int(guess) > random_number:
                print('its higher')
                attempts =+ 1
        except ValueError as err:
            print('this is not correct')
            print('({})'.format(err))
    else:
        print('thats cool have a good one')
if __name__ == '__main__':
    start_game()
    