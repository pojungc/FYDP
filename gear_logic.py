import math

class Variables:
    Acceleration = 0
    Elevation = 1
    FRICTION = 2

# ONE VARIABLE CHANGING

# LOW GEAR = HIGH GEAR RATIO

# Coasting
# If the user is not pedalling, don't change gear ratio

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

class Constants:
    GEAR_RATIO = 1
    WHEEL_RADIUS = 0.311
    PEDAL_SPEED = 80

    MAX_GEAR_RATIO = 2
    MIN_GEAR_RATIO = 0.5
    DESIRED_CADENCE = 60
    AVERAGE_SPEED = 40 # km/h

def get_wheel_radius():
    return Constants.WHEEL_RADIUS


def get_cadence():
    return Constants.PEDAL_SPEED


def get_bike_speed(pedal_speed, gear_ratio):
    output_gear_speed = pedal_speed / gear_ratio
    bike_speed = 2 * math.pi * Constants.WHEEL_RADIUS * output_gear_speed / 60 * 3.6    # Speed in km/h
    return bike_speed


def get_gear_ratio(old_pedal_speed, new_pedal_speed, old_gear_ratio):
    if old_pedal_speed == 0:
        new_gear_ratio = Constants.MAX_GEAR_RATIO
    else:
        #new_gear_ratio = old_gear_ratio*old_pedal_speed/new_pedal_speed
        new_gear_ratio = old_gear_ratio * Constants.DESIRED_CADENCE / new_pedal_speed

    new_gear_ratio = min(max(new_gear_ratio, Constants.MIN_GEAR_RATIO), Constants.MAX_GEAR_RATIO)
    print('New Speed: ', new_pedal_speed, ', Old Speed: ', old_pedal_speed, 'Old Gear Ratio: ', old_gear_ratio, 'New Gear Ratio: ', new_gear_ratio)
    return new_gear_ratio
