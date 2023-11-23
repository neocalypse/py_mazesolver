from graphics import *

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

class Line:
    def __init__(self, x1, y1, x2, y2):
        self._p1 = Point(x1, y1)
        self._p2 = Point(x2, y2)
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self._p1._x, self._p1._y, self._p2._x, self._p2._y, fill=fill_color, width= 2
        )
        canvas.pack(fill="both")