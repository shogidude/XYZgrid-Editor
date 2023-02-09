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
import map.mapping_frame as mf




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

    direction_root = ttk.Frame(side_frame)

    lbl = ttk.Label(direction_root, text="Type direction:   ")
    lbl.pack(side=TOP)

    direction_frame = ttk.Frame(direction_root)

    selected = StringVar(direction_frame, 'E')

    # top row
    rnw = ttk.Radiobutton(direction_frame, text='', value='NW', variable=selected)
    rn = ttk.Radiobutton(direction_frame, text='', value='N', variable=selected)
    rne = ttk.Radiobutton(direction_frame, text='', value='NE', variable=selected)

    # middle row
    rw = ttk.Radiobutton(direction_frame, text='', value='W', variable=selected)
    lc = ttk.Label(direction_frame, textvariable=selected, font="TkFixedFont")
    re = ttk.Radiobutton(direction_frame, text='', value='E', variable=selected)

    # bottom row
    rsw = ttk.Radiobutton(direction_frame, text='', value='SW', variable=selected)
    rs = ttk.Radiobutton(direction_frame, text='', value='S', variable=selected)
    rse = ttk.Radiobutton(direction_frame, text='', value='SE', variable=selected)

    lc.grid(column=1, row=1)
    rnw.grid(column=0, row=0)
    rn.grid(column=1, row=0)
    rne.grid(column=2, row=0)
    rw.grid(column=0, row=1)
    re.grid(column=2, row=1)
    rsw.grid(column=0, row=2)
    rs.grid(column=1, row=2)
    rse.grid(column=2, row=2)

    direction_frame.pack()
    direction_root.pack()


    side_frame.pack(expand=False, fill=Y, side=LEFT)



    # Map grid for drawing map
    mf.XYZgridFrame(root)

    root.mainloop()


if __name__ == '__main__':
    main()
