from card import Card
class Foundation:
    def __init__(self):
        # face_set is a list including all card face value.
        # foundation is a list including 4 empty lists. It is used for add card in and remove card out
        self.face_set = ['Ac','02','03','04','05','06','07','08','09','10','Ja','Qe','Ki']
        self.foundation = [['--:-']]
        while len(self.foundation) <4:
            self.foundation.append(['--:-'])

    def __str__(self):
        new_string = ""
        for card in self.foundation:
            new_string += str(card[-1]) + "\t"
        new_string.strip("\t")
        return new_string

    # get card from foundation
    def get_card(self,y):
        if self.foundation[y][0] == '--:-':
            return self.foundation[y][0]
        else:
            return self.foundation[y][-1]

    # add card to a foundation (input by player)
    def add(self,y,the_card):
        if the_card == '--:-':
            return "Cannot add to this foundation."
        else:
            suit1 = the_card.get_suit()
            face1 = the_card.get_face()
            if self.foundation[y][0] == '--:-' and face1 == 'Ac':
                    self.foundation[y][0] = the_card
            elif self.foundation[y][0] == '--:-' and face1 != 'Ac':
                    return "Cannot add to this foundation."
            elif self.foundation[y][0] != '--:-':
                suit2 = self.foundation[y][-1].get_suit()
                face2 = self.foundation[y][-1].get_face()
                if suit1 == suit2 and self.face_set.index(face1) == self.face_set.index(face2)+1:
                    self.foundation[y].append(the_card)
                elif suit1 != suit2:
                    return "Cannot add to this foundation."
                elif self.face_set.index(face1) != self.face_set.index(face2)+1:
                    return "Cannot add to this foundation."

    # remove a card from a foundation (input by player)
    def remove(self,y):
        if self.foundation[y][0] == '--:-':
            print("No card selected.")
        else:
            if self.foundation[y][-1].get_face() != 'Ac':
                self.foundation[y].pop()
            else:
                self.foundation[y][-1] = '--:-'


    # check result.
    def win(self):
        if self.foundation[0][-1] == '--:-' or \
           self.foundation[1][-1] == '--:-' or \
           self.foundation[2][-1] == '--:-' or \
           self.foundation[3][-1] == '--:-':
           pass
        elif self.foundation[0][-1].get_face() == 'Ki' and \
           self.foundation[1][-1].get_face() == 'Ki' and \
           self.foundation[2][-1].get_face() == 'Ki' and \
           self.foundation[3][-1].get_face() == 'Ki':
           return "You win!!!"
        else:
            pass

def main():
    testfound = Foundation()
    testfound.add(0,Card('Ac','H'))
    testfound.add(0,Card('02','H'))
    testfound.add(0,Card('03','H'))
    print(testfound.foundation)
    print(testfound)
    testfound.remove(0)
    print(testfound.foundation)
    print(testfound)
    testfound.remove(0)
    print(testfound.foundation)
    print(testfound)

if __name__ == "__main__":
    main()
