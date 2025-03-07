import pytest
import numpy as np

from sum_squared_error_func import sum_squared_error_function

@pytest.mark.parametrize(('t', 'y', 'expectation'), [
    (np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0]),
     np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]),
     0.097500000000000031),
    (np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0]),
     np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]),
     0.59750000000000003),
])
def test_step_func(t, y, expectation):
    assert np.array_equal(sum_squared_error_function(t, y), expectation)
