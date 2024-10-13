import pytest
import numpy as np

from relu_func import relu_func

@pytest.mark.parametrize(('x', 'expected'), [
    (np.array([-1, -0.1, 0, 0.1, 1]),
     np.array([ 0,    0, 0, 0.1, 1])),
])
def test_step_func(x, expected):
    assert np.array_equal(relu_func(x), expected)
