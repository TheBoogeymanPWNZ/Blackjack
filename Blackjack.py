import random

hand = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(hand)

print ('You wanna play?')
count = 0

while True:
    choice = input('Need another card? y/n')
    if choice == 'y':
        current = hand.pop()
        print('You got the card %d' %current)
        count += current
        if count > 21:
            print('You Lose')
        elif count == 21:
            print('You have blackjack')
            break
        else:
            print('You have %d points' %count)
    elif choice == 'n':
        print('Finished the game with %d points' %count)
        break
