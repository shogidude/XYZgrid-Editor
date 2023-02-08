#!/usr/bin/env python3

"""
XYZgrid Editor

Using TK to create a basic editor for generating
XYZgrid maps for Evennia MUD projects.

Author: T Gene Davis (ShogiDude)
Website: backrooms.net
"""

from tkinter import Tk, Frame, Label, TOP, X, Y, LEFT, Radiobutton, StringVar, NW
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
    top_label = Label(top_frame, text="Top Stuff 1")
    top_label.pack(side=LEFT)
    top_label = Label(top_frame, text="Top Stuff 2")
    top_label.pack(side=LEFT)
    top_label = Label(top_frame, text="Top Stuff 3")
    top_label.pack(side=LEFT)
    top_frame.pack(expand=False, fill=X, side=TOP)

    # Left Frame
    side_frame = Frame(root, background="green")
    side_label = Label(side_frame, text="Side Stuff 1")
    side_label.pack(side=TOP)
    side_label = Label(side_frame, text="Side Stuff 2")
    side_label.pack(side=TOP)
    side_label = Label(side_frame, text="Side Stuff 3")
    side_label.pack(side=TOP)
    side_frame.pack(expand=False, fill=Y, side=LEFT)

    direction_root = Frame(side_frame)

    lbl = Label(direction_root, text="Type direction:   ")
    lbl.pack(side=TOP)

    direction_frame = Frame(direction_root)

    selected = StringVar(direction_frame, 'E')

    # top row
    rnw = Radiobutton(direction_frame, text='', value='NW', var=selected)
    rn = Radiobutton(direction_frame, text='', value='N', var=selected)
    rne = Radiobutton(direction_frame, text='', value='NE', var=selected)

    # middle row
    rw = Radiobutton(direction_frame, text='', value='W', var=selected)
    lc = Label(direction_frame, textvariable=selected)
    re = Radiobutton(direction_frame, text='', value='E', var=selected)

    # bottom row
    rsw = Radiobutton(direction_frame, text='', value='SW', var=selected)
    rs = Radiobutton(direction_frame, text='', value='S', var=selected)
    rse = Radiobutton(direction_frame, text='', value='SE', var=selected)

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


    # Map grid for drawing map
    mf.XYZgridFrame(root)

    root.mainloop()


if __name__ == '__main__':
    main()
