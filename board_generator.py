'''
Michelle Chang, Michael Cho, and Yuecen Jin
Software Carpentry - Lazor Project
04/02/2021

This file was coded by Michelle Chang
'''

from itertools import permutations 
from read_bff import read_bff
import copy

def generator_board(grid, blocks):
    '''
    This function takes in a grid layout and available unplaced blocks
    and generates all possible boards that can be made

    **Parameters**
        grid: *2D list*
            0 - space on grid but no blocks allowed (x)
            1 - open space for blocks (o)
            2 - fixed reflect block (A)
            3 - fixed opaque block (B)
            4 - fixed refract block (C)
        blocks: *list* of integers
            type of blocks we are allowed to add to grid.
            2 indicates A or reflect block, 3 is A or opaque block,
            4 is C or refract block

    **Returns**
        boards: *3D list*
            a list of all grid layouts (2D list) that can be made with
            the given starting grid and available blocks that can be added
    '''

    possible_boards = []
    row_num = len(grid)
    col_num = len(grid[0])
    possible_spots = []
    copy_grid = []
    # if grid has 1, then we can place a block there
    # if grid has 0, 2, 3, or 4, then we cannot place a block there
    for i in range(row_num):
        for j in range(col_num):
            if grid[i][j] == 1:
                possible_spots.append([i,j])
    perm = permutations(possible_spots, 3)
    # perm is all the possible combinations of positions each
    # available block can be placed 

    temp_perm = []
    for i in list(perm): 
        temp_perm.append(list(i))

    # generating and storing all the boards that can be made
    for i in range(len(temp_perm)):
        positions = temp_perm[i]
        copy_grid = copy.deepcopy(grid)
        for j in range(len(positions)):
            row = positions[j][0]
            col = positions[j][1]
            copy_grid[row][col] = blocks[j]
        possible_boards.append(copy_grid)

    return(possible_boards)


if __name__ == '__main__':
    file_name = "/Users/michellechang/Desktop/boards/mad_1.bff"
    board = read_bff(file_name)
    grid = board[0]
    blocks = board[1]
    print(grid)
    print(blocks)
    all_boards = generator_board(grid, blocks)
