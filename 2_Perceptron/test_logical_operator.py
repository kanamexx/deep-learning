import pytest

from logical_operator import AND, NAND, OR

# def test_AND():
#     assert AND(0, 0) == 0
#     assert AND(1, 0) == 0
#     assert AND(0, 1) == 0
#     assert AND(1, 1) == 1

@pytest.mark.parametrize(('x1', 'x2', 'expected'), [
    (0, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (1, 1, 1),
])
def test_AND(x1, x2, expected):
    assert AND(x1, x2) == expected


@pytest.mark.parametrize(('x1', 'x2', 'expected'), [
    (0, 0, 1),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 0),
])
def test_NAND(x1, x2, expected):
    assert NAND(x1, x2) == expected

@pytest.mark.parametrize(('x1', 'x2', 'expected'), [
    (0, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
])
def test_OR(x1, x2, expected):
    assert OR(x1, x2) == expected