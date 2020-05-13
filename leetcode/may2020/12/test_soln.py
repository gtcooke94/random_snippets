from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp", "res"],
    [
        ([1,1,2,3,3,4,4,8,8], 2),
    ],
)
def test_soln(inp, res):
    s = Solution()
    assert s(inp) == res
