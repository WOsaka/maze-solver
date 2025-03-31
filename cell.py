from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        self._x1 = top_left_x
        self._x2 = bottom_right_x
        self._y1 = top_left_y
        self._y2 = bottom_right_y
        top_left = Point(top_left_x, top_left_y)
        top_right = Point(bottom_right_x, top_left_y)
        bottom_left = Point(top_left_x, bottom_right_y)
        bottom_right = Point(bottom_right_x, bottom_right_y)

        if self._win == None:
            return

        if self.has_top_wall:
            color = "black"
        else:
            color = "white"
        self._win.draw_line(Line(top_left, top_right), color)

        if self.has_left_wall:
            color = "black"
        else:
            color = "white"
        self._win.draw_line(Line(top_right, bottom_right), color)

        if self.has_bottom_wall:
            color = "black"
        else:
            color = "white"
        self._win.draw_line(Line(bottom_right, bottom_left), color)

        if self.has_left_wall:
            color = "black"
        else:
            color = "white"
        self._win.draw_line(Line(bottom_left, top_left), color)

    def draw_move(self, to_cell, undo=False):
        if not undo:
            color = "red"
        else:
            color = "gray"

        self_middle = Point(
            self._x1 + abs(self._x2 - self._x1) // 2,
            self._y1 + abs(self._y2 - self._y1) // 2,
        )

        to_cell_middle = Point(
            to_cell._x1 + abs(to_cell._x2 - to_cell._x1) // 2,
            to_cell._y1 + abs(to_cell._y2 - to_cell._y1) // 2,
        )

        self._win.draw_line(Line(self_middle, to_cell_middle), color)
