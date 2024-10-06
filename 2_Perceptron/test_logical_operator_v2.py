
import pytest

from logical_operator_v2 import AND, NAND, OR, XOR

@pytest.mark.parametrize(('x', 'expected'), [
    ([0, 0], 0),
    ([1, 0], 0),
    ([0, 1], 0),
    ([1, 1], 1),
])
def test_AND(x, expected):
    assert AND(x) == expected

@pytest.mark.parametrize(('x', 'expected'), [
    ([0, 0], 1),
    ([1, 0], 1),
    ([0, 1], 1),
    ([1, 1], 0),
])
def test_NAND(x, expected):
    assert NAND(x) == expected

@pytest.mark.parametrize(('x', 'expected'), [
    ([0, 0], 0),
    ([1, 0], 1),
    ([0, 1], 1),
    ([1, 1], 1),
])
def test_OR(x, expected):
    assert OR(x) == expected

@pytest.mark.parametrize(('x', 'expected'), [
    ([0, 0], 0),
    ([1, 0], 1),
    ([0, 1], 1),
    ([1, 1], 0),
])
def test_XOR(x, expected):
    assert XOR(x) == expected