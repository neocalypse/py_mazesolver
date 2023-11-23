from tkinter import Tk, BOTH, Canvas
from line import *

class Window:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.__root_widget = Tk()
        self.__root_widget.title("MazeSolver")
        self._canvas = Canvas(width=self._width, height=self._height, background="black")
        self._canvas.pack(fill="both")
        self.__running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="white"):
        self._line = line
        self._line.draw(self._canvas, fill_color)