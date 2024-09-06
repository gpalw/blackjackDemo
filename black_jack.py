############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.


import random
from art import logo


# Define the Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Define the Deck class
class Deck:
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    ranks = (
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
        "Ace",
    )
    values = {
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11,
    }

    def __init__(self):
        self.deck = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


# Define the Hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += Deck.values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def deal_card(deck):
    """Returns a random card from the deck."""
    return deck.deal()


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    score = sum(Deck.values[card.rank] for card in cards)
    aces = sum(1 for card in cards if card.rank == "Ace")
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    # Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw.
    # If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses.
    # If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.


def compare(player_hand, dealer_hand):
    if player_hand.value > 21:
        print("Player busts! Dealer wins.")
    elif dealer_hand.value > 21:
        print("Dealer busts! Player wins.")
    elif dealer_hand.value > player_hand.value:
        print("Dealer wins.")
    elif dealer_hand.value < player_hand.value:
        print("Player wins.")
    else:
        print("It's a tie!")


def play_game():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # Initial dealing
    for _ in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    # Show cards
    print("Dealer's Hand:")
    print(" <card hidden>")
    print("", dealer_hand.cards[1])
    print("\nPlayer's Hand:", *player_hand.cards, sep="\n ")

    # Player's turn
    while player_hand.value < 21:
        action = input("Would you like to Hit or Stand? Enter 'h' or 's': ")
        if action.lower() == "h":
            player_hand.add_card(deck.deal())
            print("Player's Hand:", *player_hand.cards, sep="\n ")
        else:
            break

    # Dealer's turn
    while dealer_hand.value < 17:
        dealer_hand.add_card(deck.deal())

    # Show all cards
    print("\nDealer's Hand:", *dealer_hand.cards, sep="\n ")
    print("Dealer's Hand =", dealer_hand.value)
    print("Player's Hand =", player_hand.value)

    # Determine the winner
    compare(player_hand, dealer_hand)

    # Hint 5: Deal the user and computer 2 cards each using deal_card()
    # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List.
    # If no, then the game has ended.
    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.

# Run the game
if __name__ == "__main__":
    print(logo)
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        play_game()

    print("Thanks for playing!")
