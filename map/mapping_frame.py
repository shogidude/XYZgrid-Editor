from tkinter import Canvas, Frame, BOTH, W
from map.mapping_data import StandardMap

class XYZgridFrame(Frame):
    grid_width = 8
    grid_height = 5

    current_map = StandardMap(grid_width, grid_height)

    def __init__(self, master):
        Frame.__init__(self, master)
        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        # XYZGrid Map
        canvas = Canvas(self)

        canvas.create_text(20, 20, anchor=W, font="Purisa", text="Currently selected character: -")

        current_line_location = 30
        map_lines = self.current_map.map.split('\n')
        for line in map_lines:
            canvas.create_text(20, current_line_location, anchor=W, font="Courier", text=line)
            current_line_location += 15

        canvas.pack(fill=BOTH, expand=1)
