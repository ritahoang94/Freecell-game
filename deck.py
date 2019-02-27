from card import Card
import random
class Deck:
    def __init__(self, start=1, end=13, n =4):
        self.value_start = start
        self.value_end = end
        self.suits_number = n
        self.thedeck = []
        self.cardset = []
        self.total_card = (end - start+1)*n
        self.total_value = end -start +1

        # create a card deck with number of item = (end value -start value + 1)*n
        # total number of cascades = 8
        # Number of row (in default card deck) = total_card //8 +1
        i = 0
        t =0

        while(i < (self.total_card)/8):
            self.thedeck.append([])
            while len(self.thedeck[i]) <8 and t < self.total_card:
                self.thedeck[i].append('--:-')
                t = t + 1
            i = i + 1

    def shuffle(self):
        # Create a card set. Cardset is a list including all cards used in the game
        set_face = ['Ac','02','03','04','05','06','07','08','09','10','Ja','Qe','Ki']
        set_suit = ['C','H','D','S']
        for s in range(self.suits_number):
            for f in range(self.total_value):
                cardface = set_face[f]
                cardsuit = set_suit[s]
                self.cardset.append(Card(cardface,cardsuit))
        self.cardset = random.sample(self.cardset, self.total_card)

        #append into deck
        count =0
        for r in range (self.total_card//8+1):
            for c in range(len(self.thedeck[r])):
                self.thedeck[r][c] = self.cardset[count]
                count += 1
        while len(self.thedeck[-1]) <8:
            self.thedeck[-1].append('--:-')

        return self.thedeck

    #reference to lecture code (week 8)
    def __str__(self):
        new_string = ""
        for row in self.thedeck:
            for item in row:
                new_string += str(item) + "\t"
            new_string.strip("\t")
            new_string += "\n"
        return new_string

    #get card from the column (input by player)
    # y is the position of the cascade
    def get_card(self,y):
        if self.thedeck[-1][y] != '--:-':
            return self.thedeck[-1][y]
        else:
            row =0
            while self.thedeck[row][y] != '--:-':
                row +=1
            if row > 0:
                return self.thedeck[row-1][y]
            elif row == 0:
                return self.thedeck[0][y]

    # Add card to the column (input by player)
    # y is the position of the destination cascade. The card is the card added to the cascade
    def add(self,y,the_card):
        if self.thedeck[0][y] == '--:-':
            self.thedeck[0][y] = the_card
        elif self.thedeck[0][y] != '--:-':
            if self.thedeck[-2][y] != '--:-':
                if self.thedeck[-1][y] != '--:-':
                    self.thedeck.append(['--:-']*8)
                    self.thedeck[-1][y] = the_card
                else:
                    self.thedeck[-1][y] = the_card
            else:
                d =0
                while self.thedeck[d][y] != '--:-':
                    d+=1
                self.thedeck[d][y] = the_card

    # Remove card from a column (input by player)
    # y is the position of the cascade
    def remove(self,y):
        rm=0
        if self.thedeck[-1][y] != '--:-':
            self.thedeck[-1][y] = '--:-'
        else:
            while self.thedeck[rm][y] != '--:-':
                rm+=1
            self.thedeck[rm-1][y] = '--:-'

#Test deck
def main():
    testdeck = Deck(1,13,1)
    testdeck.shuffle()
    print(testdeck)

if __name__ == "__main__":
    main()
