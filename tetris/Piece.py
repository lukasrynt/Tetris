from random import randint
import numpy as np

from tetris.Colors import colors
from tetris.Tetrominoes import shapes


class Piece:
    """
    Class to represent single Tetromino piece

    x: x coordinate of the piece
    y: y coordinate of the piece
    rotation: current rotation of the piece
    color: color of the piece
    type: shape of the piece
    """

    def __init__(self, x: int, y: int):  # top left corner is the position
        self.x = x
        self.y = y
        self.rotation = 0
        self.type = randint(0, len(shapes) - 1)
        self.color = randint(0, len(colors) - 1)

    def render(self) -> np.array:
        """
        Get image of the current piece rotated

        :return: numpy array with the rotated tetromino
        """

        return shapes[self.type][self.rotation]

    def rotate(self):
        """
        Rotates the piece
        """
        self.rotation = (self.rotation + 1) % len(shapes[self.type])

    def move_down(self, change: int):
        """
        Moves the piece along the y axis for the amount provided in change

        :param change: The number of steps we want to move the piece along y axes
        """
        self.y += change

    def move_sides(self, change: int):
        """
        Moves the piece along the x axis for the amount provided in change

        :param change: The number of steps we want to move the piece along x axes
        """
        self.x += change
