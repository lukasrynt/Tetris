import pytest
import numpy as np

from tetris.Piece import Piece
from tetris.Tetris import Tetris


def test_tetris_move_down():
    tetris = Tetris(20, 10)
    tetris.new_piece()
    tetris.move_down()
    assert not tetris.collided()
    assert tetris.piece.x == 3
    assert tetris.piece.y == 1


def test_tetris_break_line():
    tetris = Tetris(20, 10)
    piece_i1 = Piece(0, 18)
    piece_i1.type, piece_i1.rotation = 0, 1
    tetris.piece = piece_i1
    tetris.imprint_piece()

    piece_i2 = piece_i1
    piece_i2.x = 4
    tetris.piece = piece_i2
    tetris.imprint_piece()

    piece_o = Piece(7, 17)
    piece_o.type = 1
    tetris.piece = piece_o
    tetris.imprint_piece()

    for i, full in enumerate(np.all(tetris.field > 0, axis=1)):
        if i == 19:
            assert full
        else: assert not full
    tetris.break_line()
    for i, full in enumerate(np.all(tetris.field > 0, axis=1)):
        assert not full


def test_tetris_handle_level():
    tetris = Tetris(20, 10)
    tetris.handle_level(20)
    assert tetris.level == 2 and tetris.lines == 0


@pytest.mark.parametrize("lines_broken, expected", [(1, 100), (2, 300), (3, 500), (4, 800)])
def test_tetris_handle_score(lines_broken: int, expected: int):
    tetris = Tetris(20, 10)
    tetris.level = 2
    tetris.handle_score(lines_broken)
    assert tetris.score == expected * tetris.level


def test_tetris_imprint_piece():
    tetris = Tetris(20, 10)
    tetris.new_piece()
    piece = tetris.piece
    tetris.imprint_piece()
    for p in piece.render():
        assert tetris.field[piece.y + p // 4][piece.x + p % 4] == piece.color + 1
    pass


def test_tetris_collided_old_pieces():
    tetris = Tetris(20, 10)
    tetris.new_piece()
    piece = tetris.piece
    tetris.imprint_piece()
    tetris.piece = piece
    assert tetris.collided()


def test_tetris_collided_sides():
    tetris = Tetris(20, 10)
    tetris.new_piece()
    tetris.piece.x = tetris.width
    assert tetris.collided()
    tetris.piece.x = 3
    tetris.piece.y = tetris.height
    assert tetris.collided()


def test_tetris_collided_pass():
    tetris = Tetris(20, 10)
    tetris.new_piece()
    assert not tetris.collided()




