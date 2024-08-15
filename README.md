# 🎲 Blackjack Game

## Overview

Welcome to the Blackjack Game! This Python implementation of the classic card game allows you to challenge a computer dealer with an unlimited deck. Play with standard Blackjack rules and enjoy a fun, interactive experience.

## Features

- **Unlimited Deck Size**: The deck is virtually infinite, with each card having an equal probability of being drawn.
- **Blackjack Detection**: Automatically detects and handles Blackjack (21 with two cards).
- **Dealer Rules**: The dealer draws cards until their score is at least 17.
- **Replay Option**: Play as many rounds as you like without restarting the program.

## Rules

- **Deck Composition**: The deck includes cards with values `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`. Face cards (Jack, Queen, King) are valued at 10.
- **Ace Handling**: An Ace can be worth either 1 or 11. If the total score exceeds 21, Aces are adjusted from 11 to 1.
- **Dealer's Turn**: The dealer will keep drawing cards until reaching a score of at least 17.
- **Winning Conditions**:
  - A score of 21 with two cards is a Blackjack.
  - If the player’s score exceeds 21, they lose.
  - If the dealer’s score exceeds 21, the player wins.

## Installation

To get started, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DanielThuoMuhia/Black-Jack-Game.git
