import math


class Variables:
    Acceleration = 0
    Elevation = 1
    FRICTION = 2

# ONE VARIABLE CHANGING

# LOW GEAR = HIGH GEAR RATIO


# ACCELERATION
# Case 1: Constant Elevation, Constant Acceleration, Constant Friction
# Maintain gear ratio

# Case 2: Constant Elevation, Increasing Acceleration, Constant Friction
# Shift to higher gear ratio

# Case 3: Constant Elevation, Decreasing Acceleration, Constant Friction
# Shift to lower gear ratio

# ELEVATION
# Case 4: Increasing Elevation, Constant Acceleration, Constant Friction
# Shift to lower gear ratio

# Case 5: Decreasing Elevation, Constant Acceleration, Constant Friction
# Shift to higher gear ratio

# FRICTION
# Case 6: Constant Elevation, Constant Acceleration, Increasing Friction
# Shift to lower gear ratio

# Case 7: Constant Elevation, Constant Acceleration, Decreasing Friction
# Shift to higher gear ratio


# SPECIAL CASES
# Coasting - User not Pedalling
# If the user is not pedalling, don't change gear ratio

# Bike Speed
# If Bike is stationary switch to Max gear ratio




class Constants:
    GEAR_RATIO = 1
    WHEEL_RADIUS = 0.311
    PEDAL_SPEED = 80

    MAX_GEAR_RATIO = 1
    MIN_GEAR_RATIO = 0.25
    DESIRED_CADENCE = 60
    AVERAGE_SPEED = 40 # km/h

PRINT_FLAG = False


def get_wheel_radius():
    return Constants.WHEEL_RADIUS


def get_pedal_speed(bike_speed, gear_ratio):
    bike_speed = float(bike_speed)/3.6*60
    output_gear_speed = bike_speed/(2*math.pi*Constants.WHEEL_RADIUS)
    pedal_speed = output_gear_speed * gear_ratio
    return pedal_speed


def get_bike_speed(pedal_speed, gear_ratio):
    output_gear_speed = float(pedal_speed) / gear_ratio
    bike_speed = 2 * math.pi * Constants.WHEEL_RADIUS * output_gear_speed / 60 * 3.6    # Speed in km/h
    return bike_speed


def get_gear_ratio(new_pedal_speed, old_gear_ratio):
    if new_pedal_speed == 0:
        new_gear_ratio = Constants.MAX_GEAR_RATIO
    else:
        new_gear_ratio = old_gear_ratio * Constants.DESIRED_CADENCE / new_pedal_speed

    new_gear_ratio = min(max(new_gear_ratio, Constants.MIN_GEAR_RATIO), Constants.MAX_GEAR_RATIO)
    if PRINT_FLAG:
        print('New Cadence: ', new_pedal_speed, ', Desired Cadence: ', Constants.DESIRED_CADENCE, 'Old Gear Ratio: ', old_gear_ratio, 'New Gear Ratio: ', new_gear_ratio)
    return new_gear_ratio

# print(get_pedal_speed(20, 0.5))