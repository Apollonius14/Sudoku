# First attempt at interactive grids - Sudoku (defaulted and hard-coded to 9X9)

from Cell import cell
from Sudoku import Sudoku
from random import randint


def empty_board(h, w, N):
    # Takes a window width w and height h and generates an N sized Sudoku board
    # (N being a square number, default = 9, hardcorded for now)
    # returning board, a grid of cell objects with indexing of form cells[i][j]

    eBoard = [[], [], [], [], [], [], [], [], []]

    # Initialise empty board
    for yindex in range(int((w / 50))):
        row = []
        for xindex in range(int((w / 50))):
            row.append(cell(xindex * 50, yindex * 50, 50, 50))
        eBoard[yindex] = row
    return eBoard


def generate_solution(board, startx, starty):

    for i in range(len(board)):

        for j in range(len(board[i])):

            if (i >= starty and j >= startx) or i>= starty:

                board[i][j].chosen = True
                board[i][j].num_val.rotate(randint(1, 9))
                Sboard = Sudoku(board)
                check = Sboard.is_valid_initialisation()
                attempted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                backtrack_needed = False

                while not check or board[i][j].num_val[0] == " ":

                    print "____________________"
                    for p in range(len(board)):
                        print str([board[p][q].num_val[0] for q in range(len(board[p]))]) + "\n"
                    print "____________________"

                    board[i][j].num_val.rotate(randint(1, 9))

                    if board[i][j].num_val[0] in attempted:
                        attempted.remove(board[i][j].num_val[0])

                    Sboard = Sudoku(board)
                    check = Sboard.is_valid_initialisation()

                    if check == False and len(attempted) == 0:
                        backtrack_needed = True
                        break

                if backtrack_needed == True:

                    # If no valid solution possible, backtrack X steps
                    # manually setting X (back_steps) now to 8

                    back_steps = 8

                    for mess in range(10):
                        print "BACKTRACK" + "\n"

                    # Firstly clear the previous X entries

                    new_i = i
                    new_j = j

                    for back in range(back_steps):
                        while board[new_i][new_j].num_val[0] != " ":
                            board[new_i][new_j].num_val.rotate(1)
                        if new_j>0:
                            new_j -=1
                        else:
                            new_i -=1
                            new_j = 8

                    # Secondly call the generate solution function again X locations

                    generate_solution(board, new_j, new_i)

    Sboard = Sudoku(board)

    print "____________"
    print "FINAL BOARD:"
    print "____________________"
    for p in range(len(board)):
        print str([board[p][q].num_val[0] for q in range(len(board[p]))]) + "\n"
    print Sboard.is_valid_solution()
    print "____________________"

    return board

    # Add cells for a correct solution

    # Remove cells for a playable game

def generate_game(board, empties):

    # takes a valid Sudoku board object and sets a proportion (empties in %)
    # to blank cells

    for i in range(len(board)):
        for j in range(len(board[i])):
            if randint(0,100) > empties:
                board[i][j].chosen = False
                while board[i][j].num_val[0] != " ":
                    board[i][j].num_val.rotate(1)

    return board


Empty_Board = empty_board(450, 450, 9)
Solved_Board = generate_solution(Empty_Board, 0, 0)
Game_Board = generate_game(Solved_Board, 50)

def setup():
    size(450,450)
    frameRate(8)
        
def draw():
    global Game_Board
    for row in Game_Board:
        for location in row:
            location.display()
            location.listen()
    stroke(50)
    strokeWeight(5)
    line(150,0,150,450)
    line(0,150,450,150)
    line(300,0,300,450)
    line(0,300,450,300)
