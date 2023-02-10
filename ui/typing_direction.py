from tkinter import *
from tkinter import ttk


class TypingDirection(ttk.Frame):
    single_instance = None

    def __init__(self, master):
        super().__init__(master)

        if TypingDirection.single_instance is None:
            TypingDirection.single_instance = self

        # setting up canvas
        self.initUI()

    # @classmethod
    # def draw_new_grid(cls, width, height):
    #     cls.grid_width = width
    #     cls.grid_height = height
    #     cls.current_map = StandardMap(cls.grid_width, cls.grid_height)
    #     cls.canvas.delete("all")
    #     cls.single_instance.initUI()
    #     #cls.canvas.update_idletasks
    #
    #     # update the scrolling region
    #     cls.canvas.configure(scrollregion=cls.canvas.bbox("all"))

    def initUI(self):

        lbl = ttk.Label(self, text="Type direction:   ")
        lbl.pack(side=TOP)

        direction_frame = ttk.Frame(self)
        TypingDirection.selected = StringVar(direction_frame, "E")

        # top row
        rnw = ttk.Radiobutton(direction_frame, text='', value='NW', variable=TypingDirection.selected)
        rn = ttk.Radiobutton(direction_frame, text='', value='N', variable=TypingDirection.selected)
        rne = ttk.Radiobutton(direction_frame, text='', value='NE', variable=TypingDirection.selected)

        # middle row
        rw = ttk.Radiobutton(direction_frame, text='', value='W', variable=TypingDirection.selected)
        lc = ttk.Label(direction_frame, textvariable=TypingDirection.selected, font="TkFixedFont")
        re = ttk.Radiobutton(direction_frame, text='', value='E', variable=TypingDirection.selected)

        # bottom row
        rsw = ttk.Radiobutton(direction_frame, text='', value='SW', variable=TypingDirection.selected)
        rs = ttk.Radiobutton(direction_frame, text='', value='S', variable=TypingDirection.selected)
        rse = ttk.Radiobutton(direction_frame, text='', value='SE', variable=TypingDirection.selected)

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
        self.pack()
