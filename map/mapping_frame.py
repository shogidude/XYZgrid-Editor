from tkinter import Canvas, Frame, BOTH, NW
from map.mapping_data import StandardMap

class XYZgridFrame(Frame):
    single_instance = None

    grid_width = 8
    grid_height = 5

    canvas = None

    current_map = StandardMap(grid_width, grid_height)

    def __init__(self, master):
        Frame.__init__(self, master)

        if XYZgridFrame.single_instance is None:

            XYZgridFrame.single_instance = self

            # XYZGrid Map
            XYZgridFrame.canvas = Canvas(self)

        self.initUI()


    @classmethod
    def draw_new_grid(cls, width, height):
        cls.grid_width = width
        cls.grid_height = height
        cls.current_map = StandardMap(cls.grid_width, cls.grid_height)
        cls.canvas.delete("all")
        cls.single_instance.initUI()
        #cls.canvas.update_idletasks

    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        XYZgridFrame.canvas.create_text(20, 20, anchor=NW, font="Purisa", text="Currently selected character: -")

        current_line_location = 30
        map_lines = XYZgridFrame.current_map.map.split('\n')
        for line in map_lines:
            XYZgridFrame.canvas.create_text(20, current_line_location, anchor=NW, font="Courier", text=line)
            current_line_location += 15

        XYZgridFrame.canvas.pack(fill=BOTH, expand=1)
