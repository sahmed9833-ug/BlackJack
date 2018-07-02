import random as r


class Deck:

    def __init__(self):
        # currently set to just one 52 card deck
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]*4

    def random_card(self):
        # pick out a random card from the deck
        card_position = r.randint(0, len(self.cards)-1)
        card = self.cards[card_position]
        self.cards.pop(card_position)
        return card


class Hand:

    def __init__(self, owner):
        self.cards = []
        self.owner = owner

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

    def __str__(self):
        # if there are any aces in the player's hand these will be presented as 'A'
        real_hand = ['A' if x == 11 else x for x in self.cards]
        return "%s has : %s  for a total of: %d" % (self.owner, real_hand, self.total())


def new_game():
    print("-------------------------\n... Dealing new cards")
    # give player and dealer 2 cards each
    for i in range(2):
        player_hand.add_card(deck.random_card())
        dealer_hand.add_card(deck.random_card())
    # display hands
    print(player_hand)
    show_dealer_hand()

    player_turn()
    # if the player goes bust they will lose immediately
    if player_hand.total() > 21:
        return
    dealer_turn()


def player_turn():
    # player has the choice to hit or stand so long as their score is less than 21
    while player_hand.total() < 21:
        if 'h' in input("-> Hit or Stand? (h or s): ").lower():
            player_hand.add_card(deck.random_card())
            print(player_hand)
        else:
            break


def dealer_turn():
    # dealer must keep drawing cards if their score is 16 or lower
    while dealer_hand.total() < 17:
        dealer_hand.add_card(deck.random_card())


def show_dealer_hand():
    # initially the player only sees one of the dealer's cards
    if len(dealer_hand.cards) == 2 and len(player_hand.cards) == 2:
        print("The dealer drew: [%s] and a face-down card." % (dealer_hand.cards[1]))
    else:
        print(dealer_hand)


def calc_results():
    if player_hand.total() > 21:
        print("%s has gone bust! The dealer wins!" % player_name)
        return
    show_dealer_hand()
    if player_hand.total() < dealer_hand.total() <= 21:
        print("The dealer wins!")
    elif player_hand.total() > dealer_hand.total():
        print("%s wins!" % player_name)
    elif dealer_hand.total() > 21:
        print("The dealer has gone bust!\n%s wins!" % player_name)
    elif player_hand.total() == dealer_hand.total():
        print("It's a draw!")


if __name__ == "__main__":
    deck = Deck()
    player_name = input("-> Please enter your name: ")
    while True:
        player_hand = Hand(player_name)
        dealer_hand = Hand("Dealer")
        new_game()
        calc_results()
        if "n" in input("-------------------------\n-> Play again? (y or n): ").lower():
            break
