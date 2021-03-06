**Software Carpentry Spring 2021 Lazor Project**

Authors: Michelle Chang, Hyunwoo (Michael) Cho, Yuecen Jin

The project aims to automatically find solutions to the "Lazors" game with the specific cases listed in the bff files folder. 

The code in read_bff takes in the text file from the bff files and store information about the board, lasers (starting direction and position), and target points.

The board_generator file is coded to generate all possible boards that can be made given the starting grid layout and available blocks to place on grid.

The Blocks_Lazors file uses class objects for defining block and laser classes and for updating the position and direction of lasers accordingly based on the block type (refract, reflect, or opaque) it hits.

The find_solution_board file is coded to check each potential board if it is the correct solution - that is the laser(s) will go through target points. The output file is the text file with solution grid. In order for checking time taken for all the codes, the time module is utilized to compute how long it take to get the solution. 

To solve the game, run the function in find_solution_board.py with the correct file_name and file_path for each bff file in the bff files folder. After waiting for it to solve, the output text file layout should represent the solution grid with different type of blocks in the positions on the grid for easier understanding. The solution file will also list the laser path(s) and target points we wish the laser(s) to pass through, in order for us to verify the board found is indeed the solution. If no solution is find for a grid layout, the code will print out "no solution found" and a text file will not be generated.

Thank you. 

Note:
All bff files will run through the code in less than 2 mins, but we only find solution boards for dark_1 and numbered_6.
