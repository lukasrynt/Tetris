import numpy as np
from tetris.Piece import Piece
from typing import List


class Tetris:
    """
    Represents a single game of tetris, evaluates game logic

    level: the current level of the game
    score: current score of player
    game_on: check whether the game is running
    field: the field represented in numpy array
    height: the height of the field
    width: the width of the lines
    lines: lines broken since last level up
    x: x position of the field relative to game screen
    y: y position of the field relative to game screen
    zoom: determines the zoom of the field - size of individual squares
    piece: the current tetromino piece
    """

    level = 1
    score = 0
    game_on = True
    field = np.array
    height = 0
    lines = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    piece = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = np.zeros((height, width))

    def new_piece(self):
        """
        Creates a new tetromino piece at starting position 3, 0
        """
        self.piece = Piece(3, 0)

    def rotate(self):
        """
        Rotate the current piece
        """

        orig_rotation = self.piece.rotation
        self.piece.rotate()
        if self.collided():
            self.piece.rotation = orig_rotation

    def move_down(self):
        """
        Move the current piece down, imprint it if it collided and clear lines if some are filled
        """

        self.piece.move_down(1)
        if self.collided():
            self.piece.move_down(-1)
            self.imprint_piece()
            self.break_line()

    def move_side(self, change: int):
        """
        Move the current piece along the x axis
        :param change: number of steps to move along x
        """

        self.piece.move_sides(change)
        if self.collided():
            self.piece.move_sides(-change)

    def break_line(self):
        """
        Check if some of the lines were filled in the last row and clear them if needed

        Move the pieces down and update score and level
        """

        broken = 0
        for i, full in enumerate(np.all(self.field > 0, axis=1)):
            if full:
                broken += 1
                for row in range(i, 1, -1):
                    self.field[row] = self.field[row - 1]
        self.handle_score(broken)
        self.handle_level(broken)

    def handle_level(self, lines_broken: int):
        """
        Update the level if we have broken enough lines already

        :param lines_broken: number of lines we have cleared
        """

        self.lines += lines_broken
        req = (self.level + 1) * 10
        if self.lines >= req:
            self.lines %= req
            self.level += 1

    def handle_score(self, lines_broken: int):
        """
        Update the score based on level and how many lines we have broken

        :param lines_broken: number of lines we have cleared
        """

        if lines_broken == 1:
            self.score += 100 * self.level  # single
        elif lines_broken == 2:
            self.score += 300 * self.level  # double
        elif lines_broken == 3:
            self.score += 500 * self.level  # triple
        elif lines_broken == 4:
            self.score += 800 * self.level  # tetris

    def imprint_piece(self):
        """
        Stamps the current piece on the field

        Add color of the piece on the piece current position, remove the piece and check if we have not lost
        """

        for p in self.piece.render():
            self.field[self.piece.y + p // 4][self.piece.x + p % 4] = self.piece.color + 1
        self.new_piece()
        if self.collided():
            self.game_on = False

    def collided(self) -> bool:
        """
        Check whether the current piece collides with something

        First determine whether the piece has not reached side and then whether it doesn't collide with other blocks

        :return: True if the current piece collided
        """

        for p in self.piece.render():
            if self.piece.x + p % 4 >= self.width \
                    or self.piece.x + p % 4 < 0 \
                    or self.piece.y + p // 4 >= self.height \
                    or self.piece.y + p // 4 < 0:
                return True
            if self.field[self.piece.y + p // 4][self.piece.x + p % 4] > 0:
                return True
        return False

    def render_filled_elem_size(self, x: int, y: int) -> List[int]:
        """
        Create list of filled cell size

        Uses zoom to calculate how large a single filled cell will be in the field.

        :param x: x offset of the cell start
        :param y: y offset of the cell start
        :returns: a list with x and y position of the cell and its size
        """

        return [self.x + self.zoom * x + 1,
                self.y + self.zoom * y + 1,
                self.zoom - 2,
                self.zoom - 2]

    def render_blank_elem_size(self, x: int, y: int) -> List[int]:
        """
        Create list of blank cell size

        Uses zoom to calculate how large a single empty cell will be in the field.

        :param x: x offset of the cell start
        :param y: y offset of the cell start
        :returns: a list with x and y position of the cell and its size
        """

        return [self.x + self.zoom * x,
                self.y + self.zoom * y,
                self.zoom, self.zoom]
