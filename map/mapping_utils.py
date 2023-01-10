"""
mapping_utils

Utility functions for the XYZgrid Editor.

Author: ShogiDude
Website: backrooms.net
"""


def make_empty_row(width):
    retval = ""
    for x in range(width * 2 + 1 + len(str(width))):
        retval += " "
    retval += "*\n" #TODO: remove the '*'

    return retval


def make_top_number_row(width):
    retval = ""

    # TODO: top grid (only handling 0-9 currently. Need to expand to multiple digits)
    for x in range(width):
        retval += str(x) + " "
    retval += "*\n" #TODO: remove the '*'

    return retval


def make_empty_map(width, height):
    new_map = "\n+ "

    # top numbers
    new_map += make_top_number_row(width)

    # blank row
    new_map += make_empty_row(width)

    return new_map
