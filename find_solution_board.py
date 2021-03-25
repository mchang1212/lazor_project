'''
Michelle Chang, Michael Cho, and Yuecen Jin
Software Carpentry - Lazor Project
04/02/2021

Author(s): Michelle Chang
'''

import time
from read_bff import read_bff
from board_generator import generator_board
import Blocks_Lazors


def check_solution(board, lasers, targets):
    '''
    This function takes in a potential solution of the board layout and
    and checks to see if the lasers (with their given position and
    direction) will pass through all target points as they interact
    with the blocks on the board

    **Parameters**
        board: *2D list*
            0 - space on grid but no blocks allowed (x)
            1 - open space for blocks (o)
            2 - fixed reflect block (A)
            3 - fixed opaque block (B)
            4 - fixed refract block (C)
        lasers: *dict*
            position and direction of lasers on grid
        targets: *list* of tuples
            the target points in grid we wish the lasers to intersect

    **Returns**
        check: *bool*
           True if the given board is the correct solution or False if
           it is not
    '''


def print_solution(file_name, board):
        '''
    This function takes in a potential solution of the board layout and
    and checks to see if the lasers (with their given position and
    direction) will pass through all target points as they interact
    with the blocks on the board

    **Parameters**
        file_name: *str*
            name of bff file of interest
        board: *2D list*
            the particular layout that solves the board

    **Returns**
        None (generates a txt file of the solution board)
    '''

    base_name = "name" # name without bff at end
    file_path = base_name + "_solution.txt"
    file = open(file_path, "w+")
    # stuff here to format description of solution board

    file.close()


if __name__ == '__main__':
    file_name = "/Users/michellechang/Desktop/boards/mad_1.bff"
    board = read_bff(file_name)
    grid = board[0]
    blocks = board[1]
    lasers = board[2]
    targets = board[3]
    t0 = time.time()

    all_boards = generator_board(grid, blocks)
    # iterating through all the potential boards to find the solution
    for i in all_boards:
        potential_solution = i
        if check_solution(potential_solution, lasers, targets):
            solution_board = potential_solution
            break

    print_solution(file_name, solution_board)
    tf = time.time()
    solution_time = tf - t0
    print("Solution found in %0.5f secs" % solution_time)