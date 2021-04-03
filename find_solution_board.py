'''
Michelle Chang, Michael Cho, and Yuecen Jin
Software Carpentry - Lazor Project
04/02/2021

Author(s): Michelle Chang (with contributions from Yuecen Jin)
'''
import time
from read_bff import read_bff
from board_generator import generator_board
from Blocks_Lazors import Block, Lazer


def inbounds(x, y, x_dimension, y_dimension):
    '''
    Validate if the laser positions specified (x and y) are within the grid.

    **Parameters**
        x: *int*
            x position of laser
        y: *int*
            y position of laser
        x_dimension: *int*
            the grid boundary in the x direction
        y_dimension: *int*
            the grid boundary in the y direction

    **Returns**
        check: *bool*
            if the position is valid, return True and if not return False
    '''

    if x > 0 and x < x_dimension-1 and y > 0 and y < y_dimension-1:
        return True
    else:
        return False


def check_solution(board, laser_position, laser_direction, targets):
    '''
    This function takes in a potential solution of the board layout and
    and checks to see if the lasers(with their given position and
    direction) will pass through all target points as they interact
    with the blocks on the board

    **Parameters**
        board: *2D list*
            0 - empty/open space on grid
            2 - reflect block(A)
            3 - opaque block(B)
            4 - refract block(C)
        laser_position: *tuple * of lists
            position of lasers on grid
            (first list is x position, second is y)
        laser_direction: *tuple * of lists
            direction of lasers on grid
            (first list is x direction, second is y)
        targets: *list * of tuples
            the target points in grid we wish the lasers to intersect

    **Returns**
        check: *bool*
           True if the given board is the correct solution or False if
           it is not
    '''

    width = len(board[0])
    height = len(board)

    num_lasers = len(laser_position[0])
    lasers = []
    new_lasers = []
    laser_paths = []
    for i in range(num_lasers):
        pos = [laser_position[0][i], laser_position[1][i]]
        direction = [laser_direction[0][i], laser_direction[1][i]]
        lasers.append(Lazer(pos, direction))
    for i in range(len(lasers)):
        position = lasers[i].position
        direction = lasers[i].direction
        path = lasers[i].path

        # this means laser starts at the board boundaries
        if inbounds(position[0], position[1], height,
                    width) == False or board[position[1]][position[0]] != 0:
            position[0] = position[0]+direction[0]
            position[1] = position[1]+direction[1]

        while inbounds(position[0], position[1], height, width):
            block = Block(board[position[1]][position[0]])
            update = block.block_condition(position, direction)
            if len(update) == 2:
                # updating with a new position and direction
                position = update[0]
                direction = update[1]
                path.append(position)
                if inbounds(position[0], position[1], height, width):
                    position = [position[0]+direction[0],
                                position[1]+direction[1]]
                    path.append(position)
            elif len(update) == 4:
                position = update[0]
                direction = update[1]
                position2 = update[2]
                direction2 = update[3]
                new_lasers.append(Lazer(position2, direction2))
                path.append(position)
                if inbounds(position[0], position[1], height, width):
                    position = [position[0]+direction[0],
                                position[1]+direction[1]]
                    path.append(position)
            else:
                break
            if inbounds(position[0], position[1], width, height) == False:
                break
        laser_paths.append(path)

    new_num_lasers = len(new_lasers)
    if new_num_lasers != 0:
        for i in range(len(new_lasers)):
            position = new_lasers[i].position
            direction = new_lasers[i].direction
            path = new_lasers[i].path
            while inbounds(position[0], position[1], height, width):
                block = Block(board[position[1]][position[0]])
                update = block.block_condition(position, direction)
                if len(update) == 2:
                    # updating with a new position and direction
                    position = update[0]
                    direction = update[1]
                    path.append(position)
                    if inbounds(position[0], position[1], height, width):
                        position = [position[0]+direction[0],
                                    position[1]+direction[1]]
                        path.append(position)
                elif len(update) == 4:
                    position = update[0]
                    direction = update[1]
                    position2 = update[2]
                    direction2 = update[3]
                    new_lasers.append(Lazer(position2, direction2))
                    path.append(position)
                    if inbounds(position[0], position[1], height, width):
                        position = [position[0]+direction[0],
                                    position[1]+direction[1]]
                        path.append(position)
                else:
                    break
                    if inbounds(position[0], position[1],
                                height, width) == False:
                        break
            laser_paths.append(path)

    # iterate through laser path(s) to see if target point(s) are included
    found_targets = []
    for i in range(len(targets)):
        for j in range(len(laser_paths)):
            for k in range(len(laser_paths[j])):
                if laser_paths[j][k] == list(targets[i]):
                    if targets[i] not in found_targets:
                        found_targets.append(targets[i])

    if len(targets) == len(found_targets):
        check = True
    else:
        check = False

    # print(check)
    # print(laser_paths)

    return (check, laser_paths)


def print_solution(file_name, board, laser_paths, targets):
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
        laser_path: *list * of lists
            points on board that laser(s) will pass through with the
            given board layout

    **Returns**
        None (generates a txt file of the solution board or prints
        out no solution found)
    '''

    base_name = file_name.split(".bff")[0]
    file_path = base_name + "_solution.txt"
    file = open(file_path, "w+")

    index = 1
    cut_board = []
    length = len(board)
    while index < length:
        cut_board.append(board[index])
        index = index + 2

    # formatting description of solution board
    file.write("Solution board layout:\n\n")
    file.write("GRID START\n")
    for i in range(len(cut_board)):
        board_row = ""
        index = 1
        while index < len(cut_board[i]):
            if cut_board[i][index] == 0:
                board_row = board_row + "o "
            elif cut_board[i][index] == 2:
                board_row = board_row + "A "
            elif cut_board[i][index] == 3:
                board_row = board_row + "B "
            elif cut_board[i][index] == 4:
                board_row = board_row + "C "
            index = index + 2
        file.write(board_row + "\n")
    file.write("GRID STOP\n\n")

    # formatting description of laser path(s)
    for i in range(len(laser_paths)):
        file.write("laser %d path:\n" % (i+1))
        for j in range(len(laser_paths[i])):
            if j != len(laser_paths[i])-1:
                file.write(str(laser_paths[i][j]) + " -> ")
            else:
                file.write(str(laser_paths[i][j]))
        file.write("\n\n")

    file.write("Target points are: " + str(targets))

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
        check = check_solution(
            potential_solution, laser_position, laser_direction, targets)
        if check[0]:
            solution_board = potential_solution
            laser_paths = check[1]
            break
    tf = time.time()
    solution_time = tf - t0
    if 'solution_board' in locals():
        print_solution(file_name, solution_board, laser_paths, targets)
        print("Solution found in %0.5f secs" % solution_time)
    else:
        print("No solution was found in %0.5f secs" % solution_time)
