#!/usr/bin/env python3

"""
XYZgrid Editor

Using TK to create a basic editor for generating
XYZgrid maps for Evennia MUD projects.

Author: ShogiDude
Website: backrooms.net
"""

from tkinter import Tk, Canvas, Frame, BOTH, W, Menu
import map.mapping_utils as mu



class XYZgridFrame(Frame):

    grid_width = 8
    grid_height = 5

    current_map = mu.make_empty_map( grid_width, grid_height)

    def __init__(self, master):
        Frame.__init__(self, master)
        self.initUI()


    def initUI(self):

        self.master.title("XYZgrid Editor")
        self.pack(fill=BOTH, expand=1)

        # XYZGrid Map
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
    ex = XYZgridFrame(root)
    root.geometry("800x640+300+300")

    # Menu for the app
    menubar = Menu(root)
    root.config(menu=menubar)

    file_menu = Menu(menubar)
    file_menu.add_command(
        label='Exit',
        command=root.destroy,
    )

    root.mainloop()


if __name__ == '__main__':
    main()