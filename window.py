import os
from screen import Screen


class Window:
    def __init__(self, width=Screen.max_width, height=Screen.max_height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height


