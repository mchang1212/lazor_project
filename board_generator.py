'''
Michelle Chang, Michael Cho, and Yuecen Jin
Software Carpentry - Lazor Project
04/02/2021

This file was coded by Michelle Chang
'''

from itertools import permutations, combinations
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
            0 - empty space
            2 - fixed reflect block (A)
            3 - fixed opaque block (B)          
            4 - fixed refract block (C)
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
                possible_spots.append([i, j])
    perm = permutations(possible_spots, len(blocks))
    comb = combinations(possible_spots, len(blocks))
    # perm is all the possible combinations of positions each
    # available block can be placed

    def check_if_all_same(blocks):
        element = blocks[0]
        check = True
        # Comparing each element with first item 
        for i in blocks:
            if element != i:
                check = False
                break
        return check

    temp_perm = []
    temp_comb = []
    if check_if_all_same(blocks):
        for i in list(comb):
            temp_comb.append(list(i))
        temp_perm = temp_comb
    else:
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

        # adding in the empty positions between block spaces that
        # lasers can pass through and making all empty spaces of value 0
        expanded_grid = []
        length = len(copy_grid[0])
        for j in range(len(copy_grid)):
            expanded_line = [0]*(2*length+1)
            for k in range(length):
                if copy_grid[j][k] != 0 and copy_grid[j][k] != 1:
                    index = k*2
                    expanded_line[index] = copy_grid[j][k]
                    expanded_line[index+1] = copy_grid[j][k]
                    expanded_line[index+2] = copy_grid[j][k]
            expanded_grid.append(expanded_line)
        copy_egrid = copy.deepcopy(expanded_grid)
        for j in range(len(expanded_grid)):
            expanded_grid.append([0]*len(expanded_line))
        expanded_grid.append([0]*len(expanded_line))
        for j in range(int((len(expanded_grid)-1)/2)):
            index = j*2
            vec = copy_egrid[j]
            if sum(vec) != 0:
                expanded_grid[index] = vec
                expanded_grid[index+1] = vec
                expanded_grid[index+2] = vec

        for j in range(len(expanded_grid)):
            if j % 2 == 0 and j > 0 and j < len(expanded_grid)-1:
                before = copy.deepcopy(expanded_grid[j-1])
                after = copy.deepcopy(expanded_grid[j+1])
                half = int((len(before)-1)/2)
                if sum(before) != 0 and sum(after) != 0:
                    combined = before[0:half] + after[half:len(after)]
                    expanded_grid[j] = combined        
    
        possible_boards.append(expanded_grid)

    return(possible_boards)


if __name__ == '__main__':
    file_name = "/Users/michellechang/Desktop/boards/mad_4.bff"
    board = read_bff(file_name)
    grid = board[0]
    blocks = board[1]
    all_boards = generator_board(grid, blocks)

    print(all_boards[0])
