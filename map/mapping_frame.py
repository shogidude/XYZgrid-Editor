from tkinter import Canvas, Scrollbar, Frame, BOTH, NW, BOTTOM, X, RIGHT, Y
from map.mapping_data import StandardMap

class XYZgridFrame(Frame):
    single_instance = None

    grid_width = 8
    grid_height = 5

    canvas = None
    scrollregion = None

    current_map = StandardMap(grid_width, grid_height)

    def __init__(self, master):
        Frame.__init__(self, master)

        if XYZgridFrame.single_instance is None:

            XYZgridFrame.single_instance = self

            # XYZGrid Map
            XYZgridFrame.canvas = Canvas(self)

        # Scrollbars
        scroll_x = Scrollbar(self, orient="horizontal", command=XYZgridFrame.canvas.xview)
        scroll_x.pack(side=BOTTOM, fill=X)#.grid(row=1, column=0, sticky="ew")

        scroll_y = Scrollbar(self, orient="vertical", command=XYZgridFrame.canvas.yview)
        scroll_y.pack(side=RIGHT, fill=Y)#.grid(row=0, column=1, sticky="ns")

        XYZgridFrame.canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        # setting up canvas
        self.initUI()


    @classmethod
    def draw_new_grid(cls, width, height):
        cls.grid_width = width
        cls.grid_height = height
        cls.current_map = StandardMap(cls.grid_width, cls.grid_height)
        cls.canvas.delete("all")
        cls.single_instance.initUI()
        #cls.canvas.update_idletasks

        # update the scrolling region
        cls.canvas.configure(scrollregion=cls.canvas.bbox("all"))

    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        XYZgridFrame.canvas.create_text(20, 20, anchor=NW, font="Purisa", text="Currently selected character: -")

        current_line_location = 30
        map_lines = XYZgridFrame.current_map.map.split('\n')
        for line in map_lines:
            XYZgridFrame.canvas.create_text(20, current_line_location, anchor=NW, font="Courier", text=line)
            current_line_location += 15

        XYZgridFrame.canvas.pack(fill=BOTH, expand=1)#.grid(row=0, column=0)#pack(fill=BOTH, expand=1)
