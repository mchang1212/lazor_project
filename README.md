lazor_project

Authors: Michelle Chang, Hyunwoo (Michael) Cho, Yuecen Jin

The project aims to automatically find solutions to the "Lazors" game with the specific cases listed in the bff files. 

The code in read_bff takes in the text file from the bff files and store information about board, lasers, and target points.

The board_generator file is coded to generate all possible boards.

The Blocks_Lazors file uses class objects for defining block and laser classes.

The find_solution_board file is coded to check each potential board if it is the correct solution - that is the laser(s) will go through target points. The output file is the text file with solution grid. In order for checking time taken for all the codes, the time module is utilized to compute how long it take to get the solution. 

To solve the game, run the function in find_solution_board.py with the file_name within our bff files. After waiting for it to solve, the output should represent the solution grid with different type of blocks in the positions on the grid for easier understanding. 

Thank you. 