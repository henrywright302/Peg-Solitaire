import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: Peg Rectangle Solitaire    |
# Henry Wright                          |
# Last Modified: April 24, 2020         |
# ---------------------------------------
# This program will mimic Peg Solitaire |
# ---------------------------------------

# ---------------------------------------
# Start of PegRectangleSolitaire Class  |
# ---------------------------------------

class PegRectangleSolitaire:

    def __init__(self, rows, columns, empty_row, empty_col):
        #defines board as a 2D array - rows and columns
        #.full -> fills with boolian 'True'
        self.board = np.full((rows, columns), True)
        #overwrites 1 spot at [empty_row][empty_col] from 'True' to 'False' 
        self.board[empty_row][empty_col] = False
        #The number of pegs at the start is one less than the total number of squares
        self.pegs_left = rows * columns - 1
        
        
# ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):   #.shape -> 2D array shape is (n,m) where n is rows and m is columns.
            answer += " " + str(column + 1) + "  "  #so shape[1] returns the number of columns
                                                    #Right now, answer = # of columns
        answer += "\n"

        #I think this chunk adds the numbers on the sides and tops of the column, with blank spaces where the squares should be:
        #   1 2 3
        # 1
        # 2
        # 3

        answer += self.separator()                  #Adds '+--------+'
        for row in range(self.board.shape[0]):      #shape[0]
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                
                if self.board[row][col]: #not sure. In general I can guess that it adds a filled spot, but idk what [row][col] does. 
                    
                    answer += " o |"
                else:
                    answer += "   |"    #if not a full row, must be empty row
            answer += "\n"
            answer += self.separator()  #adds +------+ under each row
        #returns a string representation of the board 
        return answer
        
    
# ---------------------------------------

    def separator(self):
        #Guessing this adds the '+-----+' in between the rows
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer

# ---------------------------------------
# The four missing methods go here.  Do |
# not modify anything else.             |
# --------------------------------------|

    def game_over(self):
        num_rows = self.board.shape[0]    
        num_columns = self.board.shape[1]
        for col in range(num_columns):
            for row in range(num_rows):
                if (col + 2) <= (num_columns - 1) and self.board[row][col]:
                    if self.board[row][col + 2] == False and self.board[row][col + 1]:
                        return False
                if (col - 2) >= 0 and self.board[row][col]:
                    if self.board[row][col - 2] == False and self.board[row][col - 1]:
                        return False
                if (row + 2) <= (num_rows - 1) and self.board[row][col]:
                    if self.board[row + 2][col] == False and self.board[row + 1][col]:
                        return False
                if (row - 2) >= 0 and self.board[row][col]:
                    if self.board[row - 2][col] == False and self.board[row-1][col]:
                        return False
        return True
    

    def legal_move(self, row_start, col_start, row_end, col_end):
        if self.board[row_start][col_start] == True and self.board[row_end][col_end] == False:  #If there is a peg where you are moving from and no peg where you are moving to, continue
            if row_start == row_end or col_start == col_end:                                    #Checks if you moving diagonally
                if row_start + 2 == row_end and self.board[row_start + 1][col_start] == True or col_start + 2 == col_end and self.board[row_start][col_start + 1] == True or row_start - 2 == row_end and self.board[row_start - 1][col_start] == True or col_start - 2 == col_end and self.board[row_start][col_start - 1] == True:
                #^Checks if you are moving more than 2 spaces
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
          

    def make_move(self, row_start, col_start, row_end, col_end):
        self.pegs_left -= 1
        self.board[row_start][col_start] = False            #Gets rid of jumping 'o'
        #Get rid of jumped 'o' 
        if row_start == row_end:                            #Jump sideways, just change column number
            if col_start < col_end:                         #Determines if you are jumping right 
                self.board[row_start][col_end - 1] = False                                                     
            else:                                           #Assumes you are jumping left 
                self.board[row_start][col_end + 1] = False
                
        elif col_start == col_end:                          #Jump up and down, just changes row
            if row_start < row_end:                         #Determines if you are jumping down
                self.board[row_start + 1][col_start] = False
            else:                                           #Assumes you are jumping up
                self.board[row_start - 1][col_start] = False
            
        self.board[row_end][col_end] = True                 #Lands the 'o'
        

    def final_message(self):
        print("Number of pegs left:",self.pegs_left)
        if self.pegs_left >= 7:
            print("You're a DigiPeg Igno-Ra-Moose.")
        if self.pegs_left == 5 or self.pegs_left == 6:
            print("That's nothing to write home about")
        if self.pegs_left == 3 or self.pegs_left == 4:
            print("Not too shabby, rookie")
        if self.pegs_left <= 2:
            print("You're a DigiPeg Genius!")
        
        
# ---------------------------------------
# End of PegRectangleSolitaire Class    |
# ---------------------------------------

def get_choice(low, high, message):
    #gives range of options based on dimensions of board
    message += " [" + str(low) + " - " + str(high) + "]: "
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            #if you pick a letter, it won't let you
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            #if you pick an invalid number, it won't let you
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer


# ---------------------------------------

def main():
    print("Welcome to Peg Rectangle Solitaire!")
    print("-----------------------------------\n")

    
    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    #empty row
    row = get_choice(1, rows, "Enter the empty space row") - 1          #Minus 1? - numpy counts from 0, we count from 1. 
    #Empty column
    column = get_choice(1, columns, "Enter empty space column") - 1   
    game = PegRectangleSolitaire(rows, columns, row, column)
    print()

    print(game)
    while (not game.game_over()):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is not allowed.")
        print()
        print(game)

    game.final_message()

# ---------------------------------------

main()
