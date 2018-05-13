from collections import deque
from collections import Counter
from random import randint
import math


class Sudoku(object):
    # Argument: an array of cell objects arranged in a board
    # is_valid_initialisation returns True or False if board initialised correctly
    # is_valid_solution returns True or False if puzzle solved correctly

    # A Sudoku object is a matrix of numbers corresponding to the cell values in the board

    def __init__(self, board):
        self.board = [[], [], [], [], [], [], [], [], []]
        for row in range(len(board)):
            for col in range(len(board)):
                self.board[row].append(board[row][col].num_val[0])

    # Here we just need to check that no rules are violated, so no duplicates.

    def is_valid_initialisation(self):

        n = len(self.board)

        rootN = int(round(math.sqrt(n)))

        # Each group of 9 cells (rows,columns and mini squares) is made into a counter object

        rows_1 = [Counter([self.board[i][j] for j in range(n)]) for i in range(n)]

        transpose = [Counter([self.board[i][j] for i in range(n)]) for j in range(n)]

        squares = [Counter([self.board[p + x][q + y] for x in range(rootN)
                            for y in range(rootN)])
                   for p in range(0, n, rootN)
                   for q in range(0, n, rootN)]

        # Each group of 9 is checked for no duplicates

        for counter in rows_1:
            for item in counter:
                if str(item) in "123456789" and int(counter[item]) > 1:
                    return False

        for counter in transpose:
            for item in counter:
                if str(item) in "123456789" and int(counter[item]) > 1:
                    return False

        for counter in squares:
            for item in counter:
                if str(item) in "123456789" and int(counter[item]) > 1:
                    return False

        return True

    def is_valid_solution(self):
        n = len(self.board)
        rootN = int(round(math.sqrt(n)))
        isValidRow = lambda r: (isinstance(r, list) and
                                len(r) == n and
                                all(map(lambda x: type(x) == int, r)))
        if not all(map(isValidRow, self.board)):
            return False
        oneToN = set(range(1, n + 1))
        isOneToN = lambda l: set(l) == oneToN
        tranpose = [[self.board[j][i] for i in range(n)] for j in range(n)]
        squares = [[self.board[p + x][q + y] for x in range(rootN)
                    for y in range(rootN)]
                   for p in range(0, n, rootN)
                   for q in range(0, n, rootN)]
        return (all(map(isOneToN, self.board)) and
                all(map(isOneToN, tranpose)) and
                all(map(isOneToN, squares)))