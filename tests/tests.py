import pytest
from matrix_transformations.transformations import (
    rotate_90,
    rotate_180,
    rotate_270,
    horizontal_reflection,
    vertical_reflection,
    main_diagonal_reflection,
    anti_diagonal_reflection,
)

test_case = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

answers = [
    [
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        [[9, 8, 7], [6, 5, 4], [3, 2, 1]],
        [[3, 6, 9], [2, 5, 8], [1, 4, 7]],
        [[7, 8, 9], [4, 5, 6], [1, 2, 3]],
        [[3, 2, 1], [6, 5, 4], [9, 8, 7]],
        [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
        [[9, 6, 3], [8, 5, 2], [7, 4, 1]],
    ]
]


def test_90():
    rotated_90 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert rotate_90(test_case) == rotated_90


def test_180():
    rotated_180 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    assert rotate_180(test_case) == rotated_180


def test_270():
    rotated_270 = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    assert rotate_270(test_case) == rotated_270


def test_horizontal_reflection():
    horizontally_reflected = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    assert horizontal_reflection(test_case) == horizontally_reflected


def test_vertical_reflection():
    vertically_reflected = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    assert vertical_reflection(test_case) == vertically_reflected


def test_main_diagonal_reflection():
    main_diagonal_reflected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert main_diagonal_reflection(test_case) == main_diagonal_reflected


def test_anti_diagonal_reflection():
    anti_diagonal_reflected = [[9, 6, 3], [8, 5, 2], [7, 4, 1]]
    assert anti_diagonal_reflection(test_case) == anti_diagonal_reflected
