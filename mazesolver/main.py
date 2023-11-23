from graphics import *
from line import *
from cell import *

win = Window(800, 600)
c = Cell(win)
c.draw(50, 50, 100, 100)
win.wait_for_close()