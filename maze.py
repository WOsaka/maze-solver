from time import sleep
from random import seed as s, randint
from cell import Cell


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed != None:
            self.seed = s(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win == None:
            return
        top_left_x = self._x1 + i * self._cell_size_x
        top_left_y = self._y1 + j * self._cell_size_y
        bottom_right_x = top_left_x + self._cell_size_x
        bottom_right_y = top_left_y + self._cell_size_y

        self._cells[i][j].draw(top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        self._animate()

    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        sleep(0.005)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible = []
            if i > 0:
                possible.append((i - 1, j))
            if i < self._num_cols - 1:
                possible.append((i + 1, j))
            if j > 0:
                possible.append((i, j - 1))
            if j < self._num_rows - 1:
                possible.append((i, j + 1))

            not_visited = [x for x in possible if not self._cells[x[0]][x[1]].visited]

            if len(not_visited) == 0:
                self._draw_cell(i, j)
                return

            x, y = not_visited[randint(0, len(not_visited) - 1)]

            if i + 1 == x:
                self._cells[i][j].has_right_wall = False
                self._cells[x][y].has_left_wall = False
            if i - 1 == x:
                self._cells[i][j].has_left_wall = False
                self._cells[x][y].has_right_wall = False
            if j + 1 == y:
                self._cells[i][j].has_bottom_wall = False
                self._cells[x][y].has_top_wall = False
            if j - 1 == y:
                self._cells[i][j].has_top_wall = False
                self._cells[x][y].has_bottom_wall = False

            self._break_walls_r(x, y)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
            # and not self._cells[i - 1][j].has_right_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])

            result = self._solve_r(i - 1, j)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)

        if (
            i < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
            # and not self._cells[i + 1][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])

            result = self._solve_r(i + 1, j)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)

        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
            # and not self._cells[i][j - 1].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])

            result = self._solve_r(i, j - 1)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)

        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
            # and not self._cells[i][j + 1].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])

            result = self._solve_r(i, j + 1)
            if result:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)

        return False
