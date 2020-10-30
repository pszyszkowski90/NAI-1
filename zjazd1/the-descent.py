# Braian Kreft s16723
# https://www.codingame.com/ide/puzzle/the-descent
# the-descent

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    curr_h = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        if mountain_h > curr_h:
            curr_h = mountain_h
            curr_i = i

    # The index of the mountain to fire on.
    print(curr_i)
