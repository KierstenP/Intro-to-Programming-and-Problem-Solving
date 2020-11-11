import random

class Die:
    def __init__(self, number_of_faces = 6 ):
        self.number_of_faces = number_of_faces
        self.curr_face_value = 0

    def __repr__(self):
        return str("You rolled a " + str(self.curr_face_value))

    def Roll(self):
        self.curr_face_value = random.randint(1, 6)
        return self.curr_face_value

class PigGamePlayer:
    def __init__(self, name):
        self.name = name
        self.die = Die()
        self.score = 0

    def play_turn(self):
        print(str(self.name), "'s turn:", sep = "" )
        flag = True
        turnScore = 0
        rollAgain = ""
        while flag == True:
            turnScore += self.die.Roll()
            print(repr(self.die))
            if self.die.curr_face_value != 1:
                print("Your score for this turn is:", turnScore)
                if (self.score + turnScore) >= 100:
                    self.score += turnScore
                    print("You scored", turnScore, "points this turn. Your total score is", (self.score))
                    flag = False
                    break
                rollAgain = input("Roll again? (type 'r' for roll, or 'h' for hold): ")
                if rollAgain == 'h':
                    self.score += turnScore
                    print("You scored", turnScore, "points this turn. Your total score is", (self.score))
                    flag = False
            else:
                turnScore = 0
                print("You score 0 points for this turn. You total score is", self.score)
                flag = False
        print()

class PigGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = PigGamePlayer(player1_name)
        self.player2_name = PigGamePlayer(player2_name)

    def play(self):
        continueGame = True
        while continueGame == True:
            self.player1_name.play_turn()
            if self.player1_name.score >= 100:
                continueGame = False
            self.player2_name.play_turn()
            if self.player2_name.score >= 100:
                continueGame = False
        if self.player1_name.score >= 100:
            print(str(self.player1_name.name), "won!")
        else:
            print(str(self.player2_name.name), "won!")


def main():
    name1 = input("Player #1, enter your name: ")
    name2 = input("Player #2, enter your name: ")
    game1 = PigGame(name1, name2)
    game1.play()

main()
