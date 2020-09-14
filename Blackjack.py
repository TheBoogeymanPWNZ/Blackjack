import random


deck0 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 999
deck1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 999
deck2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 999
deck3 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 999
hand = deck0 + deck1 + deck2 + deck3
mast = ['♦', '♥', '♣', '♠'] * 999

random.shuffle(hand)

bank = int(input('How much do you buy chips: '))


def calc(bank):
    return bet * 2


while bank >= 0:
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
    croupier = b
    bet = None
    bet = int(input('Place your bet ₽: '))

    if bank < bet:
        print('You bet more than you contributed')
    elif bank >= bet:
        bank -= bet
        print('You were given two cards in total', a, learA, 'and', x, learX)
        print('The dealer took two cards, one of which', b, learB)

        if player == 21:
            print('You have blackjack!!!')
            print('Your winnings: ', bet)
            bank += bet * 1.5
        elif player > 21:
            print('You have scored %d points' % player)
            print('--- Your bet is lost:', bet)

        dable = input('Want to split the cards? y/n\n')
        
        if dable == 'y':
            a1 = current0 = hand.pop()
            x1 = current1 = hand.pop()
            print('You were given two cards in total', a, learA, 'and', a1, learX)
            print('You were given two cards in total', x, learA, 'and', x1, learX)
        while player < 21:
            if croupier >= 17:
                break

            choice = input('Need another card? y/n\n')

            if choice == 'y':
                current = hand.pop()
                lear = mast.pop()
                print('You got the card %d' % current, lear)
                player += current
                if player > 21:
                    print('You have scored %d points' % player)
                    print('--- Your bet is lost:', bet)
                elif player == 21:
                    print('Finished the game with %d points' % player)
                    print('+++ Your winnings: ', bet * 2)
                    bank += bet * 2
                else:
                    print('You have %d points' % player)
            elif choice == 'n':
                print('The dealer reveals the second card',
                      b, learB, 'and', c, learC)

            while choice == 'n':
                croupier += c
                if croupier < 17:
                    current = hand.pop()
                    lear = mast.pop()
                    print('The dealer draws a card %d ' % current, lear)
                    croupier += current
                elif croupier > 21:
                    print('The dealer is too busy %d' % croupier)
                    print('Finished the game with %d points' % player)
                    print('+++ Your winnings: ', bet * 2)
                    bank += bet * 2
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
                    break
                elif player > croupier:
                    print('Finished the game with %d points' % player)
                    print('+++ Your winnings: ', bet * 2)
                    bank += bet * 2
                    break
