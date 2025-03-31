from graphics import Line, Point


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = window

    def draw(self, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        self._x1 = top_left_x
        self._x2 = bottom_right_x
        self._y1 = top_left_y
        self._y2 = bottom_right_y
        top_left = Point(top_left_x, top_left_y)
        top_right = Point(bottom_right_x, top_left_y)
        bottom_left = Point(top_left_x, bottom_right_y)
        bottom_right = Point(bottom_right_x, bottom_right_y)

        if self.has_top_wall:
            self._win.draw_line(Line(top_left, top_right))
        if self.has_right_wall:
            self._win.draw_line(Line(top_right, bottom_right))
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_right, bottom_left))
        if self.has_left_wall:
            self._win.draw_line(Line(bottom_left, top_left))
