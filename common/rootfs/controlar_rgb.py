import subprocess
result = subprocess.run(['cat', '/proc/cpuinfo'], stdout=subprocess.PIPE)
print(result.stdout)
print("")
result = subprocess.run(['cat', '/proc/device-tree/system/linux,revision'], stdout=subprocess.PIPE)
print(result.stdout)


import time
import board
import neopixel
import random

pixel_pin = board.D18
pixels = neopixel.NeoPixel(board.D18, 16)
timer = 0.02

list_of_leds = range(0, 16)

old_r = 0
old_g = 0
old_b = 0

pixels.fill((0,0,0))

def get_array(old_color, new_color):
    if new_color > old_color:
        min_color = old_color
        max_color = new_color
    else:
        min_color = new_color
        max_color = old_color

    if max_color == 0:
        max_color = 1

    division = 10

    rslt = range(min_color, max_color, math.ceil(max_color/10))

    while len(rslt) < 10:
        division += 1
        rslt = range(min_color, max_color, math.ceil(max_color/division))

    rslt_rounded = [round(result) for result in rslt]
    
    if new_color > old_color:
        return rslt_rounded
    else:
        return rslt_rounded[::-1]

def smooth_color(color, led, increase=True):
    color_r, color_g, color_b = color
    color_range = []

    r_list = get_array(old_r, color_r)
    g_list = get_array(old_g, color_g)
    b_list = get_array(old_b, color_b)

    for position in range(0,10):
        color_range.append((r_list[position], g_list[position], b_list[position]))

    if increase:
        for new_color in color_range:
            pixels[led] = new_color
            time.sleep(timer)
        pixels[led] = color

while True:
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for led in list_of_leds:
        smooth_color(color, led)
        time.sleep(1)
    old_r, old_g, old_b = color

    new_list = random.sample(list_of_leds, len(list_of_leds))
    for led in new_list:
        smooth_color((0,0,0), led)
        time.sleep(0.01)

    old_r, old_g, old_b = (0,0,0)
