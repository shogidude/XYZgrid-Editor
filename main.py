#!/usr/bin/env python3

"""
XYZgrid Editor

Using TK to create a basic editor for generating
XYZgrid maps for Evennia MUD projects.

Author: ShogiDude
Website: backrooms.net
"""

from tkinter import Tk, Canvas, Frame, BOTH, W
import map.mapping_utils as mu

grid_width = 1
grid_height = 19


class XYZgridEditor(Frame):
    current_map = r"""
    + 0 1 2 3

    3

    2

    1

    0 

    + 0 1 2 3

    """

    def __init__(self):
        super().__init__()

        self.current_map = mu.make_empty_map( grid_width, grid_height)

        self.initUI()

    def initUI(self):

        self.master.title("XYZgrid Editor")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        canvas.create_text(20, 20, anchor=W, font="Purisa", text="Currently selected character: -")

        current_line_location = 30
        map_lines = self.current_map.split('\n')
        for line in map_lines:
            canvas.create_text(20, current_line_location, anchor=W, font="Courier", text=line)
            current_line_location += 15

        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = XYZgridEditor()
    root.geometry("800x640+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()