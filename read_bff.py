'''
Michelle Chang, Michael Cho, and Yuecen Jin
Software Carpentry - Lazor Project
04/02/2021

This file was coded by Michelle Chang
'''


def read_bff(file_name):
    '''
    This function reads an input bff file and stores information
    into respective objects

    **Parameters**
            file_name: *str*
                name of bff file of interest

    **Returns**
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
            lasers: *dict*
                    position and direction of lasers on grid
            targets: *list* of tuples
                    the target points in grid we wish the lasers to intersect
    '''

    file = open(file_name)
    info = file.readlines()
    file.close()

    # initializing objects we need to store information
    grid = []
    grid_temp = []
    grid_line = []
    blocks = []
    lasers = dict()
    laser_positions = []
    laser_directions = []
    targets = []

    search1 = "GRID START"
    search2 = "GRID STOP"
    search3 = "L"
    search4 = "P"
    mark = False

    # creating a temporary grid list to next parse through
    for i, line in enumerate(info):
        if mark:
            if any([x in line for x in ['x', 'o', 'A', 'B', 'C']]):
                grid_temp.append(line)
            if search2 in line:
                mark = False
        if search1 in line:
            mark = True

    # parsing through temporary grid list and making grid layout
    for i in range(len(grid_temp)):
        for j in range(len(grid_temp[i])):
            if grid_temp[i][j] == 'x':
                grid_line.append(0)
            elif grid_temp[i][j] == 'o':
                grid_line.append(1)
            elif grid_temp[i][j] == 'A':
                grid_line.append(2)
            elif grid_temp[i][j] == 'B':
                grid_line.append(3)
            elif grid_temp[i][j] == 'C':
                grid_line.append(4)
        grid.append(grid_line)
        grid_line = []

    for i, line in enumerate(info):
        exception = '#'
        # a comment in bff will be ignored
        # finding and storing information about blocks
        if mark:
            search5 = ['A', 'B', 'C']
            if any([x in line for x in search5]):
                if exception in line:
                    h = 0
                    # do nothing because the line is a comment
                else:
                    block_info = line.split(' ')
                    block_num = int(block_info[1])
                    for j in range(block_num):
                        for k in range(len(search5)):
                            if search5[k] in line:
                                blocks.append(k+2)
            if search3 in line:
                mark = False
        if search2 in line:
            mark = True
        # finding and storing information about lasers
        if search3 in line:
            if exception in line:
                h = 0
                # do nothing because the line is a comment
            else:
                laser_info = line.split(' ')
                x_pos = int(laser_info[1])
                y_pos = int(laser_info[2])
                laser_positions.append((x_pos, y_pos))
                x_dir = int(laser_info[3])
                y_dir = int(laser_info[4])
                laser_directions.append((x_dir, y_dir))
        # finding and storing information about points
        if mark == False and search4 in line:
            if exception in line:
                h = 0
                # do nothing because the line is a comment
            else:
                target_position = line.split(' ')
                x_pos = int(target_position[1])
                y_pos = int(target_position[2])
                targets.append((x_pos, y_pos))

    lasers['position'] = laser_positions
    lasers['direction'] = laser_directions

#     print("grid is " + str(grid))
#     print("blocks are " + str(blocks))
#     print("lasers are " + str(lasers))
#     print("target points are " + str(targets))
    
    return (grid, blocks, lasers, targets)


if __name__ == '__main__':
    file_name = "/Users/michellechang/Desktop/boards/mad_1.bff"
    board = read_bff(file_name)
    grid = board[0]
    blocks = board[1]
    lasers = board[2]
    targets = board[3]
