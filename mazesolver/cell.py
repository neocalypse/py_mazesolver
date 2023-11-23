from graphics import *
from line import *

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wal = True
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win == None:
            return
        if x1 <= x2 and y1 <= y2:
            self._x1 = x1
            self._y1 = y1
            self._x2 = x2
            self._y2 = y2
        if self.has_left_wall:
            self._win.draw_line(Line(self._x1, self._y1, self._x1, self._y2))
        if self.has_right_wall:
            self._win.draw_line(Line(self._x2, self._y1, self._x2, self._y2))
        if self.has_bottom_wal:
            self._win.draw_line(Line(self._x1, self._y2, self._x2, self._y2))
        if self.has_top_wall:
            self._win.draw_line(Line(self._x1, self._y1, self._x2, self._y1))
