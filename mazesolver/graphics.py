from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.__root_widget = Tk()
        self.__root_widget.title("MazeSolver")
        self.__canvas = Canvas(width=self._width, height=self._height)
        self.__canvas.pack(fill="both")
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
