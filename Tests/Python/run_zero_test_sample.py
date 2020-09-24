#!/usr/bin/python

import os

ITER_COUNT = 5
SCR_WIDTH = 42
RUN_CHAR = "0"
RUN_SPACE = " "


def print_row(position):
    _row_str = RUN_SPACE*(position - 1)\
             + RUN_CHAR + RUN_SPACE *(
            SCR_WIDTH - position)
    print(_row_str)

def print_screen_infinite():
    _shift = 1
    _curr_pos = 1
    while True:
        #Draw next text line
        print_row(_curr_pos)

        #Switch dirrection of char moving
        if (_curr_pos >= SCR_WIDTH):
            _shift = -1
        elif (_curr_pos <= 0):
            _shift = 1
        _curr_pos += _shift

def print_screen_one_iter():
    _shift = 1
    _curr_pos = 1
    while True:
        #Draw next text line
        print_row(_curr_pos)

        #Switch dirrection of char moving
        if (_curr_pos >= SCR_WIDTH):
            _shift = -1
        elif (_shift == -1 and _curr_pos <= 2):
            return
        _curr_pos += _shift


def print_cycle(iter_count):
    _iter = iter_count
    while True:
        print_screen_one_iter()
        _iter -= 1
        if (_iter <= 0):
            _char = input("Continue? (y/n): ")
            if (_char != "n" and _char != "N"):
                _iter = iter_count
            else:
                return
            
print_cycle(ITER_COUNT)
