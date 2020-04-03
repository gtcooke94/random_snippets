from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp", "res"],
    [
        (19, True),
        (1, True),
        (10000, True),
        (36, False),
        (1000000000000000, True),
        (1000000000000000000000000000000, True),
    ],
)
def test_isHappy(inp, res):
    s = Solution()
    assert s(inp) == res
