#!/usr/bin/env python3

"""
XYZgrid Editor

Using TK to create a basic editor for generating
XYZgrid maps for Evennia MUD projects.

Author: T Gene Davis (ShogiDude)
Website: backrooms.net
"""

from tkinter import Tk, TOP, X, Y, LEFT, StringVar
from tkinter import ttk
import ui.menus as me
from map.mapping_frame import XYZgridFrame
from ui.typing_direction import TypingDirection


def main():
    root = Tk()
    root.title("XYZgrid Editor")
    root.geometry("800x640+300+300")

    # Menubar for the app
    me.config_menubar(root)

    # Top Frame
    top_frame = ttk.Frame(root)
    top_label = ttk.Label(top_frame, text="Top Stuff 1")
    top_label.pack(side=LEFT)
    top_frame.pack(expand=False, fill=X, side=TOP)

    # Left Frame
    side_frame = ttk.Frame(root)

    TypingDirection(side_frame)

    side_frame.pack(expand=False, fill=Y, side=LEFT)



    # Map grid for drawing map
    XYZgridFrame(root)

    root.mainloop()


if __name__ == '__main__':
    main()
