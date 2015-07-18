#-------------------------------------------------------------------------------
# Name:        Guess the Number
# Purpose:
#
# Author:      Ganesh
#
# Created:     11/06/2015
# Copyright:   (c) Ganesh 2015
# Licence:     <your licence>

#Description:
# There are two ranges 0-100 and 0-1000. Computer randomely select one
# number within this range. For range 0-100, 7 chances given to the playerand for range 0-1000,
# 10 chances given to user. User guess the number and computer prompts lower or
# higher clue if the guess is not the number. Based on the clue, the player will play
# for next guess. If chances are exhaused, then new game starts. Player can change the
# range and new game starts.
# This mini project is developed with simplegui library which is available on
# coursera.org online provided by Rice university. Therefore, it is not part of
# source code.
#-------------------------------------------------------------------------------

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui, random, math

secret_number = 0
num_range =100
numberOfTurn = 0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global numberOfTurn
    print ""
    if(num_range == 1000):
        print "New game. Range is from 0 to 1000"
        print "Number of remaining guesses is 10"
        numberOfTurn = 10
    else:
        print "New game. Range is from 0 to 100"
        print "Number of remaining guesses is 7"
        numberOfTurn = 7
    secret_number = random.randrange(0, num_range)



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100
    new_game()
    return


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000
    new_game()
    return


def input_guess(guess):
    print ""
    global secret_number
    global numberOfTurn
    # main game logic goes here
    print "Guess was",int(guess)
    numberOfTurn -= 1
    print "Number of remaining guesses is ",numberOfTurn

    if(int(guess) == secret_number):
        print "Correct!"
        new_game()
        return
    if numberOfTurn<1:
        print "You ran out of guesses."
        new_game()
        return
    if(int(guess)>secret_number):
        print "Lower!"
    elif(int(guess)<secret_number):
        print "Higher!"





# create frame
frame = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100]", range100, 200)
frame.add_button("Range is [0, 1000]", range1000, 200)
frame.add_input("input the guess", input_guess, 100)

# call new_game
new_game()


