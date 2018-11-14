import sys
import numpy as np
import matplotlib.pyplot as plt
import gear_logic


CHANGE_PEDAL = False


def get_index():
    return curr_time % len(pedal_speed)


def increase_time():
    global curr_time
    curr_time += 1


def change_pedal_speed(delta=None, absolute=None):
    global pedal_speed
    global curr_time

    index = curr_time % len(pedal_speed)

    if delta is not None:
        pedal_speed[index] = pedal_speed[index-1] + delta
    elif absolute is not None:
        pedal_speed[index] = absolute


def change_bike_speed(delta=None, absolute=None):
    global bike_speed
    global curr_time

    index = curr_time % len(bike_speed)

    if delta is not None:
        bike_speed[index] = bike_speed[index-1] + delta
    elif absolute is not None:
        bike_speed[index] = absolute


def add_point():
    global pedal_speed
    global curr_time
    global gear_ratio

    index = get_index()

    if CHANGE_PEDAL:
        ax_pedal.plot(curr_time, pedal_speed[index], 'go')
        gear_ratio = gear_logic.get_gear_ratio(pedal_speed[index], gear_ratio)
        ax_gear.plot(curr_time, gear_ratio, 'bo')

        ax_speed.plot(curr_time, gear_logic.get_bike_speed(pedal_speed[index], gear_ratio), 'ro')
    else:
        ax_speed.plot(curr_time, bike_speed[index], 'ro')
        pedal_speed[index] = gear_logic.get_pedal_speed(bike_speed[index], gear_ratio)
        gear_ratio = gear_logic.get_gear_ratio(pedal_speed[index], gear_ratio)
        ax_gear.plot(curr_time, gear_ratio, 'bo')

        ax_pedal.plot(curr_time, pedal_speed[index], 'go')

    fig.canvas.draw()


def press(event):
    global pedal_speed
    global curr_time
    global available

    sys.stdout.flush()
    if event.key == 'z':
        if available:
            available = False

            if CHANGE_PEDAL:
                change_pedal_speed(delta=-1)
            else:
                change_bike_speed(delta=-1)

            add_point()
            increase_time()
            available = True
    elif event.key == 'x':
        if available:
            available = False
            if CHANGE_PEDAL:
                change_pedal_speed(delta=0)
            else:
                change_bike_speed(delta=0)
            add_point()
            increase_time()
            available = True
    elif event.key == 'c':
        if available:
            available = False
            if CHANGE_PEDAL:
                change_pedal_speed(delta=1)
            else:
                change_bike_speed(delta=1)
            add_point()
            increase_time()
            available = True
    elif event.key == 'v':
        if available:
            available = False
            if CHANGE_PEDAL:
                change_pedal_speed(absolute=0)
            else:
                change_bike_speed(absolute=0)
            add_point()
            increase_time()
            available = True

available = True

pedal_speed = np.zeros(5)  #+30
bike_speed = np.zeros(5)
curr_time = 0
gear_ratio = 0

fig, axes = plt.subplots(nrows=2, ncols=1)
fig.canvas.mpl_connect('key_press_event', press)

ax_pedal = axes[0]
ax_speed = axes[1]
title = 'Desired Cadence: ' + str(gear_logic.Constants.DESIRED_CADENCE) + ' RPM, Gear Ratios: ' + \
        str(gear_logic.Constants.MIN_GEAR_RATIO) + '-' + str(gear_logic.Constants.MAX_GEAR_RATIO)

ax_pedal.set_title(title)
ax_pedal.set_xlim([0, 100])
ax_pedal.set_ylim([0, 200])
ax_pedal.plot(0, 0, 'go')
ax_pedal.legend(['Biker Cadence'], loc=2)
ax_pedal.set_xlabel('Time (s)')
ax_pedal.set_ylabel('Cadence (rpm)')

ax_gear = ax_pedal.twinx()
ax_gear.set_xlim([0, 100])
ax_gear.set_ylim([0, 2])
ax_gear.plot(0, 0, 'bo')
ax_gear.legend(['Gear Ratio'], loc=1)
ax_gear.set_ylabel('Gear Ratio')

ax_speed.set_xlim([0, 100])
ax_speed.set_ylim([0, 60])
ax_speed.plot(0, 0, 'ro')
ax_speed.legend(['Bike Speed'])
ax_speed.set_xlabel('Time (s)')
ax_speed.set_ylabel('Biker Speed (km/h)')

plt.show()
