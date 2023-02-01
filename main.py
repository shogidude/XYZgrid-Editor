#!/usr/bin/env python3

"""
XYZgrid Editor

Using TK to create a basic editor for generating
XYZgrid maps for Evennia MUD projects.

Author: T Gene Davis (ShogiDude)
Website: backrooms.net
"""

from tkinter import Tk, Frame, Label, TOP, X, Y, LEFT
import ui.menus as me
import map.mapping_frame as mf




def main():
    root = Tk()
    root.title("XYZgrid Editor")
    root.geometry("800x640+300+300")

    # Menubar for the app
    me.config_menubar(root)

    # Top Frame
    top_frame = Frame(root, background="blue")
    top_label = Label(top_frame, text="Top Stuff")
    top_label.pack()
    top_frame.pack(expand=False, fill=X, side=TOP)

    # Left Frame
    side_frame = Frame(root, background="green")
    side_label = Label(side_frame, text="Side Stuff")
    side_label.pack()
    side_frame.pack(expand=False, fill=Y, side=LEFT)

    # Map grid for drawing map
    mf.XYZgridFrame(root)

    root.mainloop()


if __name__ == '__main__':
    main()
