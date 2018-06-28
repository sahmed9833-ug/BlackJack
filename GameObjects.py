import random as r


class Deck:

    def __init__(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4

    def draw_random_card(self):
        # pick out a random card from the deck
        card_position = r.randint(0, len(self.cards)-1)
        card = self.cards[card_position]
        self.cards.pop(card_position)
        return card


class Hand:

    def __init__(self, owner):
        self.cards = []
        self.owner = owner

    def show_hand(self):
        return "-> %s has : %s  Totals: %d" % (self.owner, self.cards, self.total())

    def add_card(self, card):
        self.cards.append(card)

    def total(self):
        # get hand's total value
        hand_val = sum(self.cards)
        aces = self.cards.count(11)
        # ace can equal 11 or 1, so...
        # if hand value is over 21, subtract 10 for each ace
        if hand_val > 21 and aces > 0:
            while aces > 0 and hand_val > 21:
                hand_val -= 10
                aces -= 1
        return hand_val


global dealer_hand, player_hand
deck = Deck()
player_name = input("Please enter your name: ")

while True:
    player_bust = False
    dealer_bust = False
    # draw initial hand
    print("-------------------------\n... dealing new cards")
    player_hand = Hand(player_name)
    for i in range(2):
        player_hand.add_card(deck.draw_random_card())
    while True:
        # loop for the player_hand's turn
        player_total = player_hand.total()
        print(player_hand.show_hand())
        if player_total > 21:
            print("--> %s is busted!" % player_name)
            player_bust = True
            break
        elif player_total == 21:
            print("--> Blackjack!")
            break
        else:
            hs = input("> Hit or Stand? (h or s): ").lower()
            if 'h' in hs:
                player_hand.add_card(deck.draw_random_card())
            else:
                break
    while True:
        # loop for the dealer's turn
        # dealer draws their initial hand
        dealer_hand = Hand("Dealer")
        for i in range(2):
            dealer_hand.add_card(deck.draw_random_card())

        while True:
            dealer_total = dealer_hand.total()
            # dealers typically stand at 18
            if dealer_total < 18:
                dealer_hand.add_card(deck.draw_random_card())
            else:
                break
        print(dealer_hand.show_hand())
        # results
        if dealer_total > 21:
            print("--> The dealer is busted!")
            dealer_bust = True
            if not player_bust:
                print("--> %s wins!" % player_name)
        elif dealer_total > player_total:
            print("--> The dealer wins!")
        elif dealer_total == player_total:
            print("--> It's a draw!")
        elif player_total > dealer_total:
            if not player_bust:
                print("--> %s wins!", player_name)
            elif not dealer_bust:
                print("--> The dealer wins!")
        break
    print("-------------------------")
    exit_prompt = input("> Play again? (y or n): ").lower()
    if 'n' in exit_prompt:
        break
