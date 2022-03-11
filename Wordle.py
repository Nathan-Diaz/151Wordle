"""
UPADATED.
"""
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, MISSING_COLOR, PRESENT_COLOR, WordleGWindow, N_ROWS, N_COLS
import random

def wordle():
    gw = WordleGWindow()
    answer = FIVE_LETTER_WORDS[random.randint(0, len(FIVE_LETTER_WORDS))].upper()
    # print(answer)
    #[gw.set_square_label(0, i, answer[i]) for i in range(N_COLS)]
    
    # Determines eligibility of word and color key/square
    def enter_action():
        nonlocal current_row

        # Create a String of User Inputs titled letters, a string
        letters = ""
        for i in range(N_COLS):
            letters += gw.get_square_label(current_row,i)
        letters = letters.lower()
        print(letters, "are the letters being guessed")

        # Compares letters to Five Letter Word Dictionary
        # If it is a valid word, it moves to coloring the cells 
        # If it is an invalid word, wordle requires new input
        if letters in FIVE_LETTER_WORDS:
            hidden = answer.lower()
            guess = letters
            color_square_and_key(guess, hidden)
            current_row += 1 # kepps track of current row
        else: print("Not in word list. Please Try Again.")
        
        # Keeps Track of Current Row
        gw.set_current_row(current_row)
        print(current_row, "is the current row.")

    # Adds color to squares and keys, with two string inputs 
    def color_square_and_key(guess, hidden):
        nonlocal current_row
        unmatched = hidden

        # Creates a List of Letters are unmatched, which will be used as a reference
        for i in range(len(guess)):
            if hidden[i] == guess[i]:
                unmatched = unmatched.replace(guess[i], "", 1)

        # Compares the guess to the hidden string and to the unmatched list
        # Once categorized then both the key and square are colored accordingly
        for i in range(len(guess)):
            if hidden[i] == guess[i]: # Correct Letter and Position
                gw.set_square_state(current_row, i, "CORRECT")
                gw.set_key_state(guess[i].upper(), "CORRECT")
            elif guess[i] in unmatched: # Correct Letter
                gw.set_square_state(current_row, i, "PRESENT")
                unmatched = unmatched.replace(guess[i], "", 1)
                gw.set_key_state(guess[i].upper(), "PRESENT")
            else: # Missing Letter
                gw.set_square_state(current_row, i, "MISSING")
                gw.set_key_state(guess[i].upper(), "MISSING")

    # Determines starting word position
    current_row = gw.get_current_row() 
    print(current_row, "is the current row.") 

    gw.add_enter_listener(enter_action)

wordle()