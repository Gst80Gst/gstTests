#!/usr/bin/python
SCR_WIDTH = 42
RUN_CHAR = "0"
RUN_SPACE = " "

#WARNING: This code works incorrect

def print_row(position):
    _row_str = RUN_SPACE*(position - 1)\
             + RUN_CHAR + RUN_SPACE *(
            SCR_WIDTH - position)
    print(_row_str)

def print_screen():
    _shift = 1
    _curr_pos = 1
    while(True):
        print_row(_curr_pos)
        if (_curr_pos >= SCR_WIDTH):
            _shift = -1
        elif (_curr_pos <= 0):
            _shift = -1
        _curr_pos += _shift

print_screen()
