#!/usr/bin/env python3

"""
XYZgrid Editor

Using TK to create a basic editor for generating
XYZgrid maps for Evennia MUD projects.

Author: T Gene Davis (ShogiDude)
Website: backrooms.net
"""

from tkinter import Tk
import ui.menus as me
import map.mapping_frame as mf




def main():
    root = Tk()
    root.title("XYZgrid Editor")
    root.geometry("800x640+300+300")

    # Menubar for the app
    me.config_menubar(root)

    # Map grid for drawing map
    mf.XYZgridFrame(root)

    root.mainloop()


if __name__ == '__main__':
    main()
