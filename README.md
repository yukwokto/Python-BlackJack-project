# Blackjack Terminal Game
This is a terminal-based blackjack game built in Python using Object Oriented Programming (OOP) concepts.

## Rules of Blackjack
Blackjack is a card game where the goal is to get a hand with a total value of 21 or as close to 21 as possible without going over. 
A hand consists of cards dealt from one or more decks.

In this project, the blackjack game uses 6 decks of cards. The value of the cards are:

-Cards 2-10 are worth their face value (e.g. a 2 of hearts is worth 2 points)
-Face cards (Jack, Queen, and King) are worth 10 points each
-An Ace can be worth either 1 or 11 points, depending on which value would be more beneficial for the player.

## Payoff Ratio
The payoff ratio for a blackjack game is typically 3:2, meaning that if a player wins with a blackjack (an Ace and a 10-point card), they are paid out at a rate of 3 to 2. In this project, the payoff ratio is also 3:2.

## Deck Reset
To ensure that the game remains fair, the deck will reset if the number of cards remaining in the deck is 10% less than the original deck size. This ensures that the game is not affected by card counting and that each hand is dealt from a fresh deck.

## How to Play
1. Run the blackjack.py file in your terminal.
2. The game will prompt you to enter the amount of your account and the bet you placed.
3. The player will be dealt two cards, and the dealer will be dealt one card face up and one card face down.
4. The player can choose to hit (receive another card) or stand (keep their current hand).
5. Once player have finished their turns, the dealer will reveal their face-down card and hit until their hand is worth 17 points or more.
6. The player  with a hand closest to 21 without going over win.
7. The game will display the winner(s) and their payoff.

## Object-Oriented Programming
This project was built using Object-Oriented Programming concepts in Python. The game logic is encapsulated in classes such as Dealer, Player, and Blackjack. This approach allows for modular code and easy extensibility.

## Contributions
Contributions to this project are welcome. If you would like to contribute, please fork the repository and submit a pull request.
