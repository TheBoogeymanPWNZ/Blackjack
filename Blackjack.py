import random

hand = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(hand)

a = current = hand.pop()
x = current = hand.pop()
print('You wanna play?')
count = a + x
bet = int(input('Place your bet ₽: '))
print('You were given two cards in total', a, 'and', x)

while count <= 21:
    choice = input('Need another card? y/n \n')
    if choice == 'y':
        current = hand.pop()
        print('You got the card %d' % current)
        count += current
        if count > 21:
            print('You have scored %d points' % count)
            print('Your bet is lost:', bet)
        elif count == 21:
            print('You have blackjack!!!')
            print('Your winnings: ', bet * 1,5)
            break
        else:
            print('You have %d points' % count)
    elif choice == 'n':
        print('Finished the game with %d points' % count)
        print('Your winnings: ', bet * 2)
        break
