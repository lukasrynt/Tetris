import pytest

from tetris.Piece import Piece
from tetris.Tetrominoes import shapes


@pytest.mark.parametrize('rotations', [1, 2, 3, 4, 5])
def test_piece_rotate(rotations: int):
    piece = Piece(3, 0)
    for _ in range(rotations):
        piece.rotate()
    assert piece.rotation == rotations % len(shapes[piece.type])


@pytest.mark.parametrize('change', [0, -1, 1])
def test_piece_move_down(change: int):
    piece = Piece(0, 0)
    piece.move_down(change)
    assert piece.y == change


@pytest.mark.parametrize('change', [0, -1, 1])
def test_piece_move_sides(change: int):
    piece = Piece(0, 0)
    piece.move_sides(change)
    assert piece.x == change
