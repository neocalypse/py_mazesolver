from graphics import *
from line import *

win = Window(800, 600)
l = Line(1, 1, 100, 100)
win.draw_line(l, "red")
win.wait_for_close()