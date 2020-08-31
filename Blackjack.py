import random

hand = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 999
mast = ['♦','♥','♣','♠'] * 999

random.shuffle(hand)

bank = int(input('How much do you buy chips: '))

while bank >= 0:
    current = hand.pop()
    lear = mast.pop()
    learA = mast.pop()
    learX = mast.pop()
    learB = mast.pop()
    learC = mast.pop()
    a = current0 = hand.pop()
    x = current1 = hand.pop()
    b = current2 = hand.pop()
    c = current3 = hand.pop()
    print('Available for bet', bank)
    print('You wanna play?')
    player = None
    croupier = None
    player = a + x
    croupier = b + c
    bet = None
    bet = int(input('Place your bet ₽: '))
    if bank < bet:
        print('You bet more than you contributed')
    elif bank >= bet:
        print('You were given two cards in total', a, learA, 'and', x, learX)
        print('The dealer took two cards, one of which', b, learB)

        if player == 21:
            print('You have blackjack!!!')
            print('Your winnings: ', bet)
            bank -= bet  # This is a crutch due to a re-bet error
            bank += bet * 1.5
        elif player > 21:
            print('You have scored %d points' % player)
            print('--- Your bet is lost:', bet)
            bank -= bet

        while player < 21:
            if croupier >= 17:
                break
            choice = input('Need another card? y/n \n')
            if choice == 'y':
                print('You got the card %d' % current, lear)
                player += current
                if player > 21:
                    print('You have scored %d points' % player)
                    print('--- Your bet is lost:', bet)
                    bank -= bet
                elif player == 21:
                    print('Finished the game with %d points' % player)
                    print('+++ Your winnings: ', bet * 2)
                    bank -= bet
                    bank += bet * 2
                else:
                    print('You have %d points' % player)
            elif choice == 'n':
                print('The dealer reveals the second card', b, learB, 'and', c, learC)
            while choice == 'n':
                if croupier < 17:
                    current = hand.pop()
                    print('The dealer draws a card %d ' % current, lear)
                    croupier += current
                elif croupier > 21:
                    print('The dealer is too busy %d' % croupier)
                    print('Finished the game with %d points' % player)
                    print('+++ Your winnings: ', bet * 2)
                    bank -= bet
                    bank += bet * 2
                    break
                elif player == croupier:
                    print("Exactly!!!")
                    print('Finished the game with %d points' % player)
                    print("You haven't won anything, but you haven't lost either")
                    break
                elif player < croupier:
                    print('The dealer scored %d' % croupier)
                    print('--- Your bet is lost:', bet)
                    bank -= bet
                    break
                elif player > croupier:
                    print('Finished the game with %d points' % player)
                    print('+++ Your winnings: ', bet * 2)
                    bank -= bet
                    bank += bet * 2
                    break
