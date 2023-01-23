import map.mapping_utils as mu

class StandardMap:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.map = ""
        self.make_empty_map(width, height)

    def make_empty_map(self, width, height):

        # top numbers
        self.map += mu.make_top_number_row(width, height)

        # center rows
        self.map += mu.make_center_rows(width, height)

        # blank row
        self.map += mu.make_empty_row(width, height)

        # top numbers
        self.map += mu.make_bottom_number_row(width, height)

