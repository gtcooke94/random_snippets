from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["m", "n", "res"],
    [
        (5, 7, 4),
        (0, 1, 0),
        (3, 19, 16),

    ],
)
def test_soln(m, n, res):
    s = Solution()
    assert s(m, n) == res
