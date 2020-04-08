from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp", "res"],
    [
        ([0,1,0,3,12], [1,3,12,0,0]),
    ],
)
def test_soln(inp, res):
    s = Solution()
    s(inp)
    assert inp == res

