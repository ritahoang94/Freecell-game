from foundation import Foundation
from freecell import Freecell
from deck import Deck

class NotFreecell:
    # face_set is a list including all card face value.
    def __init__(self):
        self.card_deck = Deck(1,13,4)
        self.freecell= Freecell()
        self.face_set = ['Ac','02','03','04','05','06','07','08','09','10','Ja','Qe','Ki']
        self.foundation = Foundation()

    def __str__(self):
        new_string = ""
        new_string += str(self.freecell)
        new_string += 3*"\t"
        new_string += str(self.foundation)
        new_string += 2*"\n"
        new_string += str(self.card_deck)
        return new_string

    # Move to cascade
    def move_to_cascade(self, from_y, to_y, pickup):
        if pickup == "cascade":
            the_card1 = self.card_deck.get_card(from_y)
        if pickup == "foundation":
            the_card1 = self.foundation.get_card(from_y)
        if pickup == "freecell":
            the_card1 = self.freecell.get_card(from_y)

        if the_card1 != '--:-':
            suit1 = the_card1.get_suit()
            face1 = the_card1.get_face()
            the_card2 = self.card_deck.get_card(to_y)
            if the_card2 == '--:-':
                if pickup == "cascade":
                    self.card_deck.add(to_y,the_card1)
                    self.card_deck.remove(from_y)
                elif pickup == "foundation":
                    self.card_deck.add(to_y,the_card1)
                    self.foundation.remove(from_y)
                elif pickup == "freecell":
                    self.card_deck.add(to_y,the_card1)
                    self.freecell.remove(from_y)

            elif the_card2 != '--:-':
                suit2 = the_card2.get_suit()
                face2 = the_card2.get_face()
                if ((suit1 == 'H' and (suit2 == 'S' or suit2 == 'C')) or \
                    (suit1 == 'D' and (suit2 == 'S' or suit2 == 'C')) or\
                    (suit1 == 'C' and (suit2 == 'H' or suit2 == 'D')) or\
                    (suit1 == 'S' and (suit2 == 'H' or suit2 == 'D'))) and \
                    self.face_set.index(face1)+1 == self.face_set.index(face2):
                    self.card_deck.add(to_y,the_card1)

                    if pickup == "cascade":
                        self.card_deck.remove(from_y)
                    elif pickup == "foundation":
                        self.foundation.remove(from_y)
                    elif pickup == "freecell":
                        self.freecell.remove(from_y)
                else:
                    print("Oops! Check again!")
            else:
                print("Oops! Check again!")

    #Move to freecell
    def move_to_freecell(self,from_y, to_y, pickup):
        if pickup == "cascade":
            the_card1 = self.card_deck.get_card(from_y)
            if self.card_deck.get_card(from_y) != "No card selected." and \
                self.freecell.add(to_y,the_card1) != "It is not a freecell.":
                self.freecell.add(to_y,the_card1)
                self.card_deck.remove(from_y)
            else:
                print("Oops! Check again!")

        if pickup == "foundation":
            the_card1 = self.foundation.get_card(from_y)
            if self.foundation.get_card(from_y) != "No card selected." and \
                self.freecell.add(to_y,the_card1) != "It is not a freecell.":
                self.freecell.add(to_y,the_card1)
                self.foundation.remove(from_y)
            else:
                print("Oops! Check again!")

        if pickup == "freecell":
            the_card1 = self.freecell.get_card(from_y)
            if self.freecell.get_card(from_y) != "No card selected." and \
                self.freecell.add(to_y,the_card1) != "It is not a freecell.":
                self.freecell.add(to_y,the_card1)
                self.freecell.remove(from_y)
            else:
                print("Oops! Check again!")

    # Move to foundation
    def move_to_foundation(self,from_y,to_y, pickup):

        if pickup == "cascade":
            the_card1 = self.card_deck.get_card(from_y)
            if self.foundation.add(to_y,the_card1) == "Cannot add to this foundation.":
                print("Oops! Check again!")
            else:
                self.foundation.add(to_y,the_card1)
                self.card_deck.remove(from_y)

        elif pickup == "freecell":
            the_card1 = self.freecell.get_card(from_y)
            if self.foundation.add(to_y,the_card1) == "Cannot add to this foundation.":
                print("Oops! Check again!")
            else:
                self.foundation.add(to_y,the_card1)
                self.freecell.remove(from_y)

        elif pickup == "foundation":
            the_card1 = self.foundation.get_card(from_y)
            if self.foundation.add(to_y,the_card1) == "Cannot add to this foundation.":
                print("Oops! Check again!")
            else:
                self.foundation.add(to_y,the_card1)
                self.foundation.remove(from_y)

    def result_check (self):
        return self.foundation.win()

# Implement the main game
def main():
    test = NotFreecell()
    test.card_deck.shuffle()
    con= ''
    print(test)

    # Create while loop to run the game until this user wins or exists the game.
    while con.upper() != 'N' and test.result_check() != "You win!!!":
        # Set input limitation for players
        while True:
            pickup = input("Choose your pick up option? (Enter foundation, freecell or cascade) ").lower()
            if pickup in ('foundation','freecell','cascade'):
                break
        while True:
            pick_column = input("Choose your pickup column. (Start from 0) ")
            if pickup == 'cascade' and pick_column in ['0','1','2','3','4','5','6','7']:
                break
            if pickup in ('freecell','foundation') and pick_column in ['0','1','2','3']:
                break
        while True:
            destination = input("Choose your destination (foundation, freecell or cascade) ")
            if destination.lower() in ('foundation','freecell','cascade'):
                break
        while True:
            des_column = input("Choose your destination column.(Start from 0) ")
            if destination == 'cascade' and des_column in ['0','1','2','3','4','5','6','7']:
                break
            if destination in ('freecell','foundation') and des_column in ['0','1','2','3']:
                break

        #move cards during the game
        if destination.lower() == "cascade":
            test.move_to_cascade(int(pick_column),int(des_column),pickup)
        if destination.lower() == "freecell":
            test.move_to_freecell(int(pick_column),int(des_column),pickup)
        if destination.lower() == "foundation":
            test.move_to_foundation(int(pick_column),int(des_column), pickup)
        print(test)

        # Check result
        if test.result_check() == "You win!!!":
            print(test.result_check())

        # Check whether this player wants to continue
        con = input("Do you want to continue?(Y/N) ")

if __name__ == "__main__":
    main()
