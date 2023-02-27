from Player import *
from Dealer import *
from random import shuffle

class Blackjack:
    # class variables for card pictures
    heart_uni = chr(9829)
    diamond_uni = chr(9830)
    spade_uni = chr(9824)
    club_uni = chr(9827)
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                   '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def __init__(self):
        self.deck = self.make_deck()
        self.bet = 0

    # create a 6-deck based new deck
    # shuffle the deck and return it
    def make_deck(self):
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        ranks = ['A', 'K', 'Q', 'J', '10', '9',
                 '8', '7', '6', '5', '4', '3', '2']
        decks = [(suit, rank) for _ in range(6)
                 for suit in suits for rank in ranks]
        shuffle(decks)
        return decks

    # ask for bet amount of player
    def bet_prompt(self, player):
        bet = eval(input('Enter your bet for this round: $'))
        while bet <= 0 or bet > player.get_account_balance():
            bet = eval(input('Please enter a valid bet: $'))
        self.bet = bet
        print(f'You have bet ${self.bet}')

    # deal cards to player or dealer
    def hit(self):
        new_card = self.deck.pop()
        return new_card

    # display the cards of player/ dealer, use show = False to hide the first card of dealer
    def display_cards(self, person, deck, show=False):
        if person == 'dealer':
            print('Dealer\'s hands')
        elif person == 'player':
            print('player\'s hands')
        
        row1 = row2 = row3 = row4 = row5 = '     '
        theDeck = deck[:]
        
        if not show:
            theDeck.pop(0)
            row1 += '-----     '
            row2 += '|?  |     '
            row3 += '| # |     '
            row4 += '|  ?|     '
            row5 += '-----     '

        for card in theDeck:
            if card[0] == 'clubs':
                pattern = Blackjack.club_uni
            elif card[0] == 'diamonds':
                pattern = Blackjack.diamond_uni
            elif card[0] == 'hearts':
                pattern = Blackjack.heart_uni
            else:
                pattern = Blackjack.spade_uni
            if card[1] == '10':
                row1 += '-----     '
                row2 += f'|{card[1]} |     '
                row3 += f'| {pattern} |     '
                row4 += f'| {card[1]}|     '
                row5 += '-----     '
            else:
                row1 += '-----     '
                row2 += f'|{card[1]}  |     '
                row3 += f'| {pattern} |     '
                row4 += f'|  {card[1]}|     '
                row5 += '-----     '

        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print(row5)

    # check the hand value for dealer or player
    def check_card_value(self, hands):
        total_value = 0
        num_aces = 0
        for card in hands:
            card_value = Blackjack.card_values[card[1]]
            if card_value == 11:
                num_aces += 1

            total_value += card_value

        while total_value > 21 and num_aces > 0:
            total_value -= 10
            num_aces -= 1

        return total_value

        # hand_value = 0
        # for i in range(len(hands)):
        #     if hands[i][1] in 'KQJ':
        #         hand_value += 10
        #     elif hands[i][1] in 'A':
        #         temp = 11
        #         if temp + hand_value > 21:
        #             hand_value += 1
        #         else:
        #             hand_value += 11
        #     else:
        #         hand_value += int(hands[i][1])

        # def need_insurance(self, dealer_hands):
        #     d_hands = dealer_hands[:]
        #     if d_hands[1][0] == 'A':
        #         insurance_required = input('Do you require insurace (Y/N)? ')
        #         if insurance_required == 'Y':
        #             insurance = self.bet//2


if __name__ == '__main__':
    # start a new game
    game = Blackjack()
    # instantiate a dealer
    dealer = Dealer()
    # instantiate a player
    player = Player()
    # set the account balance of the player
    player.set_account_balance()

    # set the game statu
    in_game = True
    # The while loop for a round starts from here
    while in_game:
        # ask for bet amount of this round
        game.bet_prompt(player)

        # card dealing to player and dealer
        player.deal_card(game.hit())
        dealer.deal_card(game.hit())
        player.deal_card(game.hit())
        dealer.deal_card(game.hit())

        # display card of dealer/ player
        game.display_cards('dealer', dealer.get_dealer_hands())
        game.display_cards('player', player.get_player_hands(), True)

        # set the hands value of dealer/ player
        dealer_value = game.check_card_value(dealer.get_dealer_hands())
        dealer.set_hands_value(dealer_value)
        player_value = game.check_card_value(player.get_player_hands())
        player.set_hands_value(player_value)

        HAS_BLACKJACK = False
        # check if the player get a Blackjack in the first round
        if player.get_hands_value() == 21:
            print('Blackjack 21 !')
            HAS_BLACKJACK = True

        # while loop for the player action
        decision_round = 1
        in_player_decision = True
        player_busted = False
        while in_player_decision and not player_busted and not HAS_BLACKJACK:
            # player decision if not busted
            option = input(
                'Please choose your choice:    h)it    s)tay    d)ouble:   ')
            # if player decides to get 1 more card
            if option == 'h':
                new_card = game.hit()
                player.add_card(new_card)
                print('A new card is dealt')
                decision_round += 1

            # if player decides not to get anymore card, exits the player action loop
            elif option == 's':
                in_player_decision = False

            # if player decides to double the amount of the bet,
            # the player can only get one more card after
            elif option == 'd':
                if decision_round == 1:
                    game.bet *= 2
                    print('Doubled the bet')
                    new_card = game.hit()
                    player.add_card(new_card)
                    print('A new card is dealt')
                    in_player_decision = False
                else:
                    print('double is not allowed after the first round!')

            # display the hands of player and dealer
            game.display_cards('dealer', dealer.get_dealer_hands())
            game.display_cards('player', player.get_player_hands(), True)

            # update the player's hands value
            player_value = game.check_card_value(player.get_player_hands())
            player.set_hands_value(player_value)

            # check if player is busted or having a Blackjack
            if player.get_hands_value() > 21:
                print('Busted!')
                player_busted = True

            # need to check if player has blackjack as well
            elif player.get_hands_value() == 21:
                HAS_BLACKJACK = True

        # while loop for dealer action
        in_dealer_decision = True
        dealer_busted = False

        while in_dealer_decision and not player_busted:
            # if dealer's hands value is lower or equal to 16,
            # the dealer must keep dealing.
            if dealer.get_hands_value() <= 16:
                new_card = game.hit()
                dealer.add_card(new_card)
                print('A new card is dealt to the dealer.')

                # display the new hands of dealer and the current hands for player
                game.display_cards('dealer', dealer.get_dealer_hands(), True)
                game.display_cards('player', player.get_player_hands(), True)

                dealer_value = game.check_card_value(dealer.get_dealer_hands())
                dealer.set_hands_value(dealer_value)

            # if dealer's hands value is greater than 16, the dealer cannot draw more cards
            elif dealer.get_hands_value() > 16:
                in_dealer_decision = False
            # if dealer's hands is greater than 21, the dealer busted
                if dealer.get_hands_value() > 21:
                    dealer_busted = True
                    print('Dealer busted')

        # show the final outcome
        print()
        print('--------------------------------------------------------------------------------------')
        print('The final outcome: ')
        game.display_cards('dealer', dealer.get_dealer_hands(), True)
        game.display_cards('player', player.get_player_hands(), True)

        # payout calculation
        # case 1: the player busted, or dealer's hands are greater than player when no one busted
        if player_busted or (dealer.get_hands_value() > player.get_hands_value() and not player_busted and not dealer_busted):
            player.withdraw_for_bet(game.bet)

        # case 2: if the hands values of the dealer and the player is the same (a push),
        #         player get back the original bet, no action is needed

        # case 3: if the dealer is busted, and the player do not have a blackjack
        if dealer_busted and not HAS_BLACKJACK:
            player.add_account_balance(game.bet)

        # case 4: if the dealer is busted, and the player have a blackjack,
        #         the payout will be 3:2
        if dealer_busted and HAS_BLACKJACK:
            player.add_account_balance(game.bet * 1.5)

        # case 5: if the dealer did not busted, and the player has a blackjack
        if not dealer_busted and HAS_BLACKJACK:
            player.add_account_balance(game.bet * 1.5)

        # case 6: if the player hands are greater than the dealer, and no one busted
        if player.get_hands_value() > dealer.get_hands_value() and not dealer_busted and not player_busted:
            player.add_account_balance(game.bet)

        # print the account balance of player
        print(f'Your account balance is: {player.get_account_balance()}')

        # reset the amount of bet
        game.bet = 0

        # reset the hands of the dealers and players, and the decision round
        player.reset_hands()
        dealer.reset_hands()
        decision_round = 0
        
        # reset the deck if the card number is 10% less than the original deck
        if len(game.deck) < int(52 * 6 *  0.9):
            game.deck = game.make_deck()
        
        # ask if player want to continue to play 21
        continue_game = input('Another round? (Y/N): ')
        if continue_game == 'N':
            print('Thank You for playing!')
            in_game = False
