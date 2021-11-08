import random
K = 10
J = 10
Q = 10
A = 11
suit = ['♥️', '♠️', '♦️', '♣️']
number = [2, 3, 4, 5, 6, 7, 8, 9, 10, K, Q, J, A]
game = "yes"
playing = "yes"
draw = ""
bust ='no'

print("Welcome to Black Jack !!!")

class Card:
    def __init__(self):
        self.number = random.choice(number)
        self.suit = random.choice(suit)

    def __repr__(self):
        return str(self.suit) + str(self.number)

class Initial:
    def __init__(self):
        self.card1 = Card()
        self.card2 = Card()
        hand.extend((self.card1, self.card2))
        handnum.append(self.card1.number)
        handnum.append(self.card2.number)

class InitialDealer:
    def __init__(self):
        self.card1 = Card()
        self.card2 = Card()
        Dealerhand.extend((self.card1, self.card2))
        Dealerhandnum.append(self.card1.number)
        Dealerhandnum.append(self.card2.number)


while game == "yes":
    
    playing=input("\nDo you you wish to play a game?\nType Yes or No.\n").lower()

    if playing=='yes':        #Player
        hand = []
        handnum = []
        Dealerhand=[]
        Dealerhandnum=[]
        InitialDealer()
        Initial()
        print('\nYour initial hand is...', hand, "\n")

        if sum(handnum) == 21:
            print("Dang.. BlackJack just like that.\nCongrats!!!")
            answer="no"
            playing = "no"

        while playing == 'yes':
            answer = input("Do you want to draw?\nType Yes or No.\n").lower()

            if answer == "no":    #Player stay
                print("\nAlright.. you stay.\n")
                
            elif answer == "yes":    #Player draw

                while answer == "yes":  # To draw and avoid doubles
                    
                    draw = Card()

                    if str(draw) not in str(hand):

                        handnum.append(draw.number)
                        hand.append(draw)
                        print('\nYour hand is...', hand, "\n")


                        if sum(handnum) > 21:
                            print("You busted\n")
                            bust ='yes'
                            answer="no"
                            playing = "no"
                        elif sum(handnum) == 21:
                            print("Dang.. you really just won.\nCongrats!!!")
                            answer="no"
                            playing = "no"
                        else:
                            answer="no"
                    else:
                        answer="no"        
            else:
                print("\n'", answer, "'", " is not a valid answer...")

            if sum(Dealerhandnum) == 21:                     #dealer draw
                pass
            elif bust=="yes":
                pass
            elif sum(Dealerhandnum) < 11 :

                draw = Card()

                if str(draw) not in str(Dealerhand):

                    Dealerhandnum.append(draw.number)
                    Dealerhand.append(draw)

                    if sum(Dealerhandnum) > 21:
                        print("The dealer hit and busted...\nYOU WIN!!!")
                        answer="no"
                        playing = "no"
                        game="no"

                    elif sum(Dealerhandnum)== 21:
                        pass

                    else:
                        pass
            elif sum(Dealerhandnum) > 11 and sum(Dealerhandnum) < 18:

                draw = Card()

                if str(draw) not in str(Dealerhand):

                    Dealerhandnum.append(draw.number)
                    Dealerhand.append(draw)

                    if sum(Dealerhandnum) > 21:
                        print("The dealer hit and busted...\nYOU WIN!!!")
                        answer="no"
                        playing = "no"
                        game="no"

                    elif sum(Dealerhandnum)== 21:
                        pass

                    else:
                        pass
            else:
                pass

            if playing=="no" and bust == "no ":         #to determine who won
                
                if sum(Dealerhandnum) > sum(handnum):
                    print ("Your hand was",hand,"\n")
                    print ("The dealer's hand was",Dealerhand,"\n\nThe dealer Wins")
                elif sum(Dealerhandnum) < sum(handnum):
                    print ("Your hand was",hand,"\n")
                    print ("The dealer's hand was",Dealerhand,"\n\nYOU WIN!!!")
                elif sum(Dealerhandnum) == sum(handnum):
                    print ("Your hand was",hand,"\n")
                    print ("The dealer's hand was",Dealerhand,"\n\n")
                    print ("There seems to be a tie")
                
                else:
                    pass
                    
               
    elif playing == "no":       
        print("Thanks for playing!!")
        game="no"
    else:
        print("\n'", playing, "'", " is not a valid answer...")