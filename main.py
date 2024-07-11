############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## 0 represents BlackJack that is score is 21.
## The Computer Should keep drawing the cards as long as it has a score less than 17.

import random
import os
from art import logo

def deal_card():
    """
    Returns a random card from the deck.
    
    The deck contains values representing Ace (11), numbered cards (2-10), and face cards (10).
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """
    Calculate the score of the given list of cards.
    
    Parameters:
        cards (list): List of integers representing the cards in hand.
        
    Returns:
        int: The total score of the cards.
        0: If the hand is a Blackjack (21 with two cards).
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        # Replace Ace value from 11 to 1 if the total score exceeds 21
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """
    Compare the user's score and the computer's score to determine the winner.
    
    Parameters:
        user_score (int): The total score of the user's cards.
        computer_score (int): The total score of the computer's cards.
        
    Returns:
        str: The result of the comparison.
    """
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose."

def play_game():
    """
    Main function to play a game of Blackjack.
    
    Deals initial cards to the user and the computer, and handles the game logic.
    """
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal two initial cards to both user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for Blackjack or if the user goes over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn to draw cards until it reaches a score of at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final results
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Main loop to start a new game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()