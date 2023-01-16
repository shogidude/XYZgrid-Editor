from tkinter import Canvas, Frame, BOTH, W
import map.mapping_utils as mu

class XYZgridFrame(Frame):
    grid_width = 8
    grid_height = 5

    current_map = mu.make_empty_map(grid_width, grid_height)

    def __init__(self, master):
        Frame.__init__(self, master)
        self.initUI()

    def initUI(self):
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
