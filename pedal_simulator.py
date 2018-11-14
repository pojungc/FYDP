import sys
import numpy as np
import matplotlib.pyplot as plt
import gear_logic


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

def add_point():
    global pedal_speed
    global curr_time
    global gear_ratio

    index = get_index()
    ax_pedal.plot(curr_time, pedal_speed[index], 'go')

    gear_ratio = gear_logic.get_gear_ratio(pedal_speed[index-1], pedal_speed[index], gear_ratio)
    ax_gear.plot(curr_time, gear_ratio, 'bo')

    ax_speed.plot(curr_time, gear_logic.get_bike_speed(pedal_speed[index], gear_ratio), 'ro')

    print(pedal_speed)
    fig.canvas.draw()


def press(event):
    global pedal_speed
    global curr_time
    global available

    sys.stdout.flush()
    if event.key == 'z':
        if available:
            available = False
            change_pedal_speed(delta=-1)
            add_point()
            increase_time()
            available = True
    elif event.key == 'x':
        if available:
            available = False
            change_pedal_speed(delta=0)
            add_point()
            increase_time()
            available = True
    elif event.key == 'c':
        if available:
            available = False
            change_pedal_speed(delta=1)
            add_point()
            increase_time()
            available = True
    elif event.key == 'v':
        if available:
            available = False
            change_pedal_speed(absolute=0)
            add_point()
            increase_time()
            available = True

available = True

pedal_speed = np.zeros(5)+30
curr_time = 0
gear_ratio = 0

fig, axes = plt.subplots(nrows=2, ncols=1)
fig.canvas.mpl_connect('key_press_event', press)

ax_pedal = axes[0]
ax_speed = axes[1]

ax_pedal.set_title('Press a key')
ax_pedal.set_xlim([0, 100])
ax_pedal.set_ylim([0, 100])

ax_gear = ax_pedal.twinx()
ax_gear.set_xlim([0, 100])
ax_gear.set_ylim([0, 2])

ax_speed.set_xlim([0, 100])
ax_speed.set_ylim([0, 60])

plt.show()
