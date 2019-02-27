# Freecell-game

The program is designed for developing a card game called “Free Cells” by Python Language. Free Cells was first developed by Microsoft on the Windows operating system. It was born in 1995 and until now, Free Cells is still one of the most well-known games among Microsoft users. In the recent years, along with the many different versions of Free Cells have been developed and tested in both Window operating system and other game websites. Basically, the game mentioned in this document follows the traditional game with 52 cards in a deck and the rules and mechanism found at https://en.wikipedia.org/wiki/FreeCell. This program support creating random deck, therefore, some decks are unsolvable.

# File description

1. Card.py is a fundamental class for this game. It contains 2 main attributes including the face value (face) and suit of the card (suit) respectively. 
2. Deck.py creates a deck of cards. Each deck contains 8 cascades. Inside class Deck, a card set will be created based on user the start value, the end value and the number of suits. From this card set, a randomized deck will be initialized. Moreover, methods for adding card, removing card and get card from deck also written inside class Deck.
3. Foundation.py is used to generate 4 foundations and set its corresponding movement methods. In particular, each foundation is a list of same suit cards. Cards move into the foundation in the order from the smallest face (Ace) to the highest face (King). 
4. Freecell.py is written for representing 4 free cells in an actual game. In fact, there are 4 free cells that cards can be moved in and out. Class Freecell creates a list with 4 empty items playing the role of free cells.  Similarly, three methods for card movement (add, remove, get) also created inside Freecell.
5. Notfreecell.py inherits methods written in 4 mentioned classes. In other words, this class tells how a card move in and out from one place to another place. At the end, the main function is responsible for implement the whole game by the user input. 
6. Mannual.pdf documents the game idea and user guide.

# Brief user guide

Users start the game by running the freecell.py file. 

*Please find the full instruction to run the code in the user guide section in the mannual file.*

1.	What is the pickup location? A user will choose among 3 pickup options (freecell, cascade, foundation). 
2.	What is the pickup column? A user will give a number as an input, start with 0 and end with 7 (for deck option) or 3 (for freecell and foundation options)
3.	What is the destination location? A user will choose among 3 destination options (freecell, cascade, foundation). 
4.	What is the destination column? A user will give a number as an input, start with 0 and end with 7 (for deck option) or 3 (for freecell and foundation options)
5.	Check win or not? It is not a question for the player. In the background, the code will check whether this user wins or not. If yes, the game finishes.
6.	Do you want to continue? This question checks whether this user wants to quit. They can press ‘N’ to quit the game and ‘Y’ to continue the game.
