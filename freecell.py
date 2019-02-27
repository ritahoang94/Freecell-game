class Freecell:
    def __init__(self):
        # freecell is a list including 4 empty items. It is used for add card in and remove card out
        self.freecell= ['--:-']*4

    def __str__(self):
        new_string = ""
        for card in self.freecell:
            new_string += str(card) + 2*"\t"
        return new_string

    # get card from a freecell (input by player)
     # y is the position of the freecell
    def get_card(self,y):
        if self.freecell[y] == '--:-':
            return self.freecell[y]
        else:
            return self.freecell[y]

    # add card to a freecell (input by player)
    # y is the position of the freecell
    def add(self,y,the_card):
        if self.freecell[y] == '--:-':
            self.freecell[y] = the_card
        else:
            return "It is not a freecell."

    # remove card from a freecell (input by player)
    def remove(self,y):
        if self.freecell[y] == '--:-':
            print("It is a freecell")
        else:
            self.freecell[y] = '--:-'

def main():
    testfound = Freecell()
    print(testfound)
if __name__ == "__main__":
    main()
