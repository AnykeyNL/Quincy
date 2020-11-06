import numpy as np



LEFT_CLOSE_ARM = 11
LEFT_FAR_ARM = 11

RIGHT_CLOSE_ARM = 11
RIGHT_FAR_ARM = 11

MOTOR_SPACE = 2.5

def angles_to_coord(left_arm_angle, right_arm_angle):

    ''' Function inputs the motor angle relative to a perpindicular line from
    the robot body (in degrees)

    OUTPUT:
    x and y coordinates of the target node in cm

    Coordinate system:
    -center of robot (between to motors) is origin
    -left is negative values
    -right is positive values
    -down is positive values
    '''

    # Converting to radians
    left_arm_angle_rad = (left_arm_angle) * (np.pi / 180)
    right_arm_angle_rad = (180-right_arm_angle) * (np.pi / 180)

    # Finding coord for left pivot
    opp_left = np.cos(left_arm_angle_rad) * LEFT_CLOSE_ARM
    adj_left = np.sin(left_arm_angle_rad) * LEFT_CLOSE_ARM

    opp_left = -(opp_left + (MOTOR_SPACE / 2)) # Adjusting for space b/w motors

    # Finding coord for right pivot
    opp_right = np.cos(right_arm_angle_rad) * RIGHT_CLOSE_ARM
    adj_right = np.sin(right_arm_angle_rad) * RIGHT_CLOSE_ARM

    opp_right = opp_right + (MOTOR_SPACE / 2)

    # Finding triangle height (base is between to pivots and peak is the target)
    a = np.absolute(opp_right - opp_left)
    b = np.absolute(adj_right - adj_left)
    base = np.sqrt((a**2) + (b**2))

    _c = RIGHT_FAR_ARM
    _a = base / 2
    if _c > _a:
        height = np.sqrt((_c**2) - (_a**2))
    else:
        height = np.sqrt((_a**2) - (_c**2))

    # Finding midpoint between two pivots
    mid_x = (opp_right + opp_left) / 2
    mid_y = (adj_right + adj_left) / 2

    # Finding direction from midpoint to target
    end_angle = np.arctan(mid_x / mid_y)

    # Calculating target coord
    x_add = np.sin(end_angle) * height
    y_add = np.cos(end_angle) * height

    x = mid_x + x_add
    y = mid_y + y_add

    return x, y


def coord_to_angles(x, y):
    ''' Function inputs the coordinates of the target in cm with up to one
    decimal persion (e.g. 12.3) and outputs angles to set the motor to achieve
    the desired coordinates. If no possible angles are found, a print statement
    will say so.

    OUTPUT
    - left_angle: angle to set left motor
    - right_angle: angle to set right motor
    '''
    x = round(x, 1)
    y = round(y, 1)

    margin = 0.2
    ANGLES_FOUND = False
    while ANGLES_FOUND==False:
        # Testing all possible combinations
        for l in np.arange(10, 110, 0.2):
            for r in np.arange(70, 170, 0.2):
                _x, _y = angles_to_coord(l, r)
                _x = round(_x, 1)
                _y = round(_y, 1)
                # Allowing for some margin to enable more results
                if ((_x-margin) <= x <= (_x+margin)) and ((_y-margin) <= y <= (_y+margin)):
                    ANGLES_FOUND=True
                    left_angle = l
                    right_angle = r
                    return left_angle, right_angle
        ANGLES_FOUND=True
        print('No valid combination!')

# Samples and tests (uncomment or comment)

#print(angles_to_coord(45, 45))
#print(coord_to_angles(0, 10.0))
#
# angles_to_coord(45, 45)
print(coord_to_angles(-5, 10))
