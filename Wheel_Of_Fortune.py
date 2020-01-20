import random
import time


# Used to reveal the alphabet that the player choose if it contains in the puzzle
def change_char(text, position, new_char):
    return text[:position] + new_char + text[position + 1:]


# Display the current player's turn and amount of money collected throughout the game
def player_turn():
    if player1turn == 1:
        print(Player1 + "'s turn")
        print("Current money:${}".format(play1score))
    else:
        print(Player2 + "'s turn")
        print("Current money:${}".format(play2score))


# Spin the wheel and display the result
def spin():
    num = random.randint(0, 10)
    print("Spinning the wheel....May the luck be with you..")
    time.sleep(2)
    if num == 0:
        print("You land on \"lose turn\"")
    if num == 1:
        print("You land on \"bankrupt\"")
    elif num > 1:
        print("You land on ${}!".format(num * 50))
    return num


# Player's will try to solve the puzzle where correct answer ends the game
def solve():
    global wrong
    global player1turn
    print(blank1)
    guess = input("The word is?")
    if guess == word[choose][0]:
        print("Congratulation!you have won the game!")
        print(desc[choose])
        wrong = False
    else:
        print("Sorry!Wrong Answer!You lose your turn")
        change_turn(player1turn)


def change_turn(turn):
    global player1turn
    if turn:
        player1turn = False
    else:
        player1turn = True


# Based on the spin wheel outcome, player can either lose turn,go bankrupt or get to choose an alphabet
def evaluate(eva, turn):
    global player1turn
    global play1score
    global play2score
    global temp
    global blank1
    # lose turn
    if eva == 0:
        print("Sorry,you just lose your turn.")
        change_turn(turn)
    # bankrupt
    if eva == 1:
        print("It's a disaster!")
        if turn:
            play1score = 0
            change_turn(turn)
        else:
            play2score = 0
            change_turn(turn)
    # money
    elif eva > 1:
        print("The hint is " + word[choose][1])
        print(blank1)
        syl = input("Select a character(A-Z):")
        print("Let us see....")
        time.sleep(2)
        check = temp.find(syl, 0, len(temp))
        if check == -1:
            print("Wrong guess!Bad luck")
            change_turn(turn)
        else:
            print("Nice one buddy!You guess correctly!")
            space = 0
            for check1, cha in enumerate(temp):
                if cha == " ":
                    space = space + 1

                elif syl == cha:
                    # update the money won if the player guess correctly.The amount won is alphabet times the money.
                    if player1turn:
                        play1score = play1score + eva * 50
                    else:
                        play2score = play2score + eva * 50
                    # reveal the alphabet contain in the puzzle
                    # temp is used when checking the alphabet in the puzzle.Chosen alphabet is replaced with #
                    # this is to avoid bug where if we compare to the original word,it will consider alphabet
                    # that has already been chosen as valid, which is wrong
                    blank1 = change_char(blank1, check1 * 2 - space, syl)
                    temp = change_char(temp, check1, "#")
            # display the current state of the puzzle
            print(blank1)


# Array containing word to be chosen for the puzzle.Contain alongside the keyword to the puzzle
word = [["GUIDO VAN ROSSUM", "programming language creator"], ["CRISTIANO RONALDO", "football player"],
        ["VLADIMIR PUTIN", "President"], ["CHERNOBYL", "a place where the worst nuclear disaster occured"],
        ["SATOSHI NAKAMOTO", "Founder of a controversial technology(anonymous)"]]
# Based on the word chosen for the puzzle, a brief description will be provided for general knowledge
desc = ["He is the creator of Python programming language.", "Regarded as one of the best player in the world" +
        ".Currently playing in Juventus.", "President of Russia. from 2012-2016, Forbes ranked him as the most "
                                           "powerful man" +
        " in the world.", "It is a place somewhere in Ukraine, which when it happens in 1986, still under"+
         " the Soviet Union. Soviet Union was dissolved in 1991. Mikhail Gorbachev, who was the president of "+
         "the Soviet Union when the incident happen until it dissolved, wrote in 2006,that \"The nuclear"
         " meltdown in Chernobyl..was perhaps the true cause of the collapse of the Soviet Union.\"",
        "Presumably the founder of Bitcoin, a cryptocurrency which is controversial. Underlying it is a technology "
        "called Blockchain\n"
        + "which some believe has the potential to disrupt the traditional financial ecosystem in a radical way."]
choose = random.randint(0, 4)
# randomly choose the word contain in the array for the puzzle
temp = word[choose][0]
i = 0
blank1 = ""
# the initial state of the puzzle where all the characters is replaced with an underscore
while i < len(word[choose][0]):
    if temp[i] == " ":
        blank1 = blank1 + " "
        i = i + 1
    else:
        blank1 = blank1 + "_" + " "
        i = i + 1
print("=========================== WHEEL OF FORTUNE ==========================")
print("Welcome to Wheel of Fortune!The rule of the game is simple where you need to solve the puzzle in order to win")
print("the game.You will have 2 options to choose, 1 is to spin the wheel, 2 is to solve.Spinning the wheel will have")
print("different outcome and only if you land on the money, you will get to choose an alphabet to reveal the puzzle.")
print("Goodluck and have fun!")
Player1 = input("Player 1 Name?")
play1score = 0
Player2 = input("Player 2 Name?")
play2score = 0
player1turn = True
wrong = True
while wrong:
    player_turn()
    print("The hint is " + word[choose][1])
    print(blank1)
    op = (input("Select your option:\n1 Spin the Wheel\n2 Solve\n"))
    if op == '1':
        res = spin()
        evaluate(res, player1turn)
    elif op == '2':
        solve()
    else:
        print("Wrong input.Please enter again")
# The winner would be announced and display the amount of money won
if player1turn:
    print("{} wins ${}".format(Player1, play1score))
else:
    print("{} wins ${}".format(Player2, play2score))
