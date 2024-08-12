from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Test Title")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("closing window")

    def close(self):
        self.__running = False

    def draw_line(self, Line, fill_color):
        Line.draw(Canvas, fill_color)

class Point():
    def __init__(self):
        self.x = 0
        self.y = 0

class Line():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, Canvas, fill_color):
        Canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )

def main():
    win = Window(800, 600)
    ln = Line(20, 45)
    win.draw_line(ln, "Black")
    win.wait_for_close()
    
main()