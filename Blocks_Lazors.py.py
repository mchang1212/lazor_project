'''
EN.540.635 Software Carpentry - Lazor Project
Blocks and Lazors
04/02/2021
Author: Hyunwoo (Michael) Cho
'''


class Block:

    def __init__(self, b_position):
        '''
        Initializes the block
        **Parameters**
                none
        **Returns**
                none
        '''
        self.b_position = b_position

    def __call__(self, b_type):
        '''
        Returns the block type of the input
        **Parameters**
            none
        **Returns**
            block type
        '''
        self.b_type = b_type

    def block_condition(self, laser_position, laser_direction):
        '''
        Updates lazor's position and direction depending on the block type
        **Parameters**
            laser_positions: position of the lazor
            laser_directions: direction of the lazor
        **Returns**
            position
            direction
        '''
        b_type = self.b_type
        if b_type == 2:  # Reflect
            # if x coordinate of laser is divisble by 2, laser hits E/W
            # if not, laser hits N/S of block
            if laser_position[0] % 2 == 1:
                return [(laser_position, (-laser_direction[0],
                                          laser_direction[1]))]
            else:
                return [(laser_position, (laser_direction[0],
                                          -laser_direction[1]))]
        elif b_type == 3:  # Opaque
            return 'End of Laser'
        elif b_type == 4:  # Refract
            if laser_position[0] % 2 == 1:
                return [(laser_position, (-laser_direction[0],
                          laser_direction[1])), ((laser_position
                          [0] + laser_direction[0], laser_position
                          [1] + laser_direction[1]), laser_direction)]
            else:
                return [(laser_position, (laser_direction[0], -laser_
                          direction[1])), ((laser_position[0] + laser_
                            direction[0], laser_position[1] + laser_
                            direction[1]), laser_direction)]