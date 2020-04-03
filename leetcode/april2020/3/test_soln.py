from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp", "res"],
    [
       ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
       ([-2, 1, -3, 4, -1, 2, 1, -3, 4], 7),
       ([-1], -1),
       ([0, -1], 0),
       ([1, -1], 1),
       ([-1, 1], 1),

    ],
)
def test_maxSubArray(inp, res):
    s = Solution()
    assert s(inp) == res
