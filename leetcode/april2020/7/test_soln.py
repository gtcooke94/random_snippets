from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp", "res"],
    [
        ([1,2,3], 2),
        ([1,1,3,3,5,5,7,7], 0),
        ([1,3,2,3,5,0], 3),
        ([1,1,2,2], 2),
        ([1,1,2], 2),
    ],
)
def test_soln(inp, res):
    s = Solution()
    assert s(inp) == res
