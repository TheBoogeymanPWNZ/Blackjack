import random

hand = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(hand)


bank = float(input('How much do you buy chips: '))

while bank >= 0:
    a = current = hand.pop()
    x = current = hand.pop()
    b = current = hand.pop()
    c = current = hand.pop()

    print('Available for bet', bank)
    print('You wanna play?')
    player = None
    croupier = None
    player = a + x
    croupier = b + c
    bet = None
    bet = float(input('Place your bet ₽: '))
    if bank < bet:
        print('You bet more than you contributed')
    else:
        print('You were given two cards in total', a, 'and', x)
        print('The dealer took two cards, one of which', b)

        if player == 21:
            print('You have blackjack!!!')
            print('Your winnings: ', bet * 1.5)
            bank += bet
        elif player > 21:
            print('You have scored %d points' % player)
            print('--- Your bet is lost:', bet)
            bank -= bet

        while player < 21:
            if croupier >= 17:
                break
            choice = input('Need another card? y/n \n')
            if choice == 'y':
                current = hand.pop()
                print('You got the card %d' % current)
                player += current
                if player > 21:
                    print('You have scored %d points' % player)
                    print('--- Your bet is lost:', bet)
                    bank -= bet
                elif player == 21:
                    print('Finished the game with %d points' % player)
                    print('+++ Your winnings: ', bet * 2)
                    bank += bet
                else:
                    print('You have %d points' % player)
            elif choice == 'n':
                print('The dealer reveals the second card', b, 'and', c)
            while choice == 'n':
                if croupier < 17:
                    current = hand.pop()
                    print('The dealer draws a card %d ' % current)
                    croupier += current
                elif croupier > 21:
                    print('The dealer is too busy %d' % croupier)
                    print('Finished the game with %d points' % player)
                    print('+++ Your winnings: ', bet * 2)
                    bank += bet
                    break
                elif player == croupier:
                    print("Exactly!!!")
                    print('Finished the game with %d points' % player)
                    print("You haven't won anything, but you haven't lost either")
                    bank += bet
                    break
                elif player < croupier:
                    print('The dealer scored %d' % croupier)
                    print('--- Your bet is lost:', bet)
                    bank -= bet
                    break
                elif player > croupier:
                    print('Finished the game with %d points' % player)
                    print('+++ Your winnings: ', bet * 2)
                    bank += bet
                    break