from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp", "res"],
    [
        ([3, -2, 2, -3], 3),
        ([5, -3, 5], 10),
        ([-5, -2, 5, 6, -2, -7, 0, 2, 8], 14),
        ([0, 5, 8, -9, 9, -7, 3, -2], 16),
        ([-2, -2], -2),
        ([-2], -2),
        ([1, -2, 3, -2], 3),
        ([3, -1, 2, -1], 4),
        ([-2, -3, -1], -1),
    ],
)
def test_soln(inp, res):
    s = Solution()
    assert s(inp) == res
