import pytest
import numpy as np

from step_func import step_function

# @pytest.mark.parametrize(('x', 'expected'), [
#     (-1, 0),
#     (-0.1, 0),
#     (0, 0),
#     (0.1, 1),
#     (1, 1),
# ])
# def test_step_func(x, expected):
#     assert step_function(x) == expected

@pytest.mark.parametrize(('x', 'expected'), [
    (np.array([-1, -0.1, 0, 0.1, 1]),
     np.array([ 0,    0, 0,   1, 1])),
])
def test_step_func(x, expected):
    assert np.array_equal(step_function(x), expected)
