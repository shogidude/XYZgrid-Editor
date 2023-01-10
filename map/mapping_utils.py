"""
mapping_utils

Utility functions for the XYZgrid Editor.

Author: ShogiDude
Website: backrooms.net
"""


def make_empty_row(width, height):
    #TODO: Y prefix size needs to be dynamic
    retval = ""
    prefix_space = ""
    for x in range(len(str(height))-1):
        prefix_space += " "

    retval += prefix_space

    for x in range(width * 2 + 2):
        retval += " "
    retval += "*\n" #TODO: remove the '*'

    return retval


def make_top_number_row(width, height):
    retval = ""
    row100s = ""
    row10s = ""
    row1s = ""

    prefix_space = ""
    for x in range(len(str(height))-1):
        prefix_space += " "

    number_of_digits = (len(str(width-1)))

    # top grid only handling 0-999 currently.
    for x in range(width):
        print(str(x))
        if width > 100:
            if x > 99:
                row100s += str((divmod(x, 1000)[1])//100) + " "
            else:
                row100s += "  "

        if width > 10:
            if x > 9:
                row10s += str((divmod(x, 100)[1])//10) + " "
            else:
                row10s += "  "

        row1s += str(divmod(x, 10)[1]) + " "

    # TODO: Y prefix size needs to be dynamic
    if len(row100s) > 0:
        row100s = prefix_space + "  " + row100s + "\n"

    if len(row10s) > 0:
        row10s = prefix_space + "  " + row10s + "\n"

    row1s = prefix_space + "+ " + row1s + "*\n" #TODO: remove the '*'

    retval += "\n" + row100s + row10s + row1s

    return retval


def make_empty_map(width, height):
    new_map = ""

    # top numbers
    new_map += make_top_number_row(width, height)

    # blank row
    new_map += make_empty_row(width, height)

    return new_map
