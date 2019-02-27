class Card:
    def __init__(self,face, suit):
        self.card_face = face
        self.card_suit = suit

    def __str__(self):
        return str(self.card_face) + ":" + str(self.card_suit)

    def __repr__(self):
        return 'Card {!r}, {!r}'.format(self.card_face, self.card_suit)

    def get_face(self):
        return str(self.card_face)

    def get_suit(self):
        return str(self.card_suit)

# set face: Ac = Ace, Ja = Jack, Qe = Queen, Ki = King
# set suit: C = Club, H = Heart, D = Diamond, S = Spade
# main function: Test Card

def main():
    set_face = ['Ac','02','03','04','05','06','07','08','09','10','Ja','Qe','Ki']
    set_suit = ['C','H','D','S']
    li =[]
    li.append(Card(set_face[1],set_suit[0]))
    print(li)

if __name__ == "__main__":
    main()

