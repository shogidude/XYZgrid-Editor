class GridDescriptions:
    """
    Rooms are stored in the __descriptions dictionary keyed off strings in the format "x,y".
    The default room is stored in key "*,*".
    """

    __instance = None

    def __new__(cls):
        if GridDescriptions.__instance is None:
            GridDescriptions.__instance = object.__new__(cls)
            GridDescriptions.__instance.__descriptions = {}
        return GridDescriptions.__instance

    @staticmethod
    def create_position_string(x, y):
        position_tuple = (x, y)
        return ','.join(position_tuple)

    @classmethod
    def set_room_description(cls, x, y, room):
        position = GridDescriptions.create_position_string(x, y)
        GridDescriptions.__instance.__descriptions[position] = room

    @classmethod
    def get_room_description(cls, x, y):
        position = GridDescriptions.create_position_string(x, y)
        return GridDescriptions.__instance.__descriptions[position]

    @classmethod
    def delete_room_description(cls, x, y):
        position = GridDescriptions.create_position_string(x, y)
        return GridDescriptions.__instance.__descriptions.pop(position)

    @classmethod
    def get_room_positions(cls):
        """
        Returns keys of rooms as strings in the format "x,y"
        """
        return GridDescriptions.__instance.__descriptions.keys()
