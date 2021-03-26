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


def check_solution(board, laser_position, laser_direction, targets):
    '''
    This function takes in a potential solution of the board layout and
    and checks to see if the lasers (with their given position and
    direction) will pass through all target points as they interact
    with the blocks on the board

    **Parameters**
        board: *2D list*
            0 - empty/open space on grid 
            2 - reflect block (A)
            3 - opaque block (B)
            4 - refract block (C)
        laser_position: *tuple* of lists
            position of lasers on grid 
            (first list is x position, second is y)
        laser_direction: *tuple* of lists
            direction of lasers on grid 
            (first list is x direction, second is y)
        targets: *list* of tuples
            the target points in grid we wish the lasers to intersect

    **Returns**
        check: *bool*
           True if the given board is the correct solution or False if
           it is not
    '''
    h = 0 # placeholder for now
    

def print_solution(file_name, board):
    '''
    This function takes in the solution board layout and format the solution
    into a user friendly form. Grid spaces will have o, A, B, or C. o is 
    empty/open space on grid, A is a reflect block, B is an opaque block, 
    and C is a refract block.

    **Parameters**
        file_name: *str*
            name of bff file of interest
        board: *2D list*
            the particular layout that solves the board

    **Returns**
        None (generates a txt file of the solution board)
    '''

    base_name = file_name.split(".bff")[0]
    file_path = base_name + "_solution.txt"
    file = open(file_path, "w+")
    
    # formatting description of solution board below
    file.write("Solution board layout:\n\n")
    file.write("GRID START\n")
    for i in range(len(board)):
        board_row = ""
        index = 1
        while index < len(board[i]):
            if board[i][index] == 0:
                board_row = board_row + "o "
            elif board[i][index] == 2:
                board_row = board_row + "A "
            elif board[i][index] == 3:
                board_row = board_row + "B "
            elif board[i][index] == 4:
                board_row = board_row + "C "
            index = index + 2
        file.write(board_row + "\n")
    file.write("GRID STOP")
    file.close()


if __name__ == '__main__':
    file_name = "/Users/michellechang/Desktop/boards/mad_1.bff"
    board = read_bff(file_name)
    grid = board[0]
    blocks = board[1]
    laser_position = board[2]
    laser_direction = board[3]
    targets = board[4]
    t0 = time.time()

    all_boards = generator_board(grid, blocks)
    # iterating through all the potential boards until we find the solution
    for i in all_boards:
        potential_solution = i
        if check_solution(potential_solution, laser_position, laser_direction, targets):
            solution_board = potential_solution
            break

    print_solution(file_name, solution_board)
    tf = time.time()
    solution_time = tf - t0
    print("Solution found in %0.5f secs" % solution_time)
