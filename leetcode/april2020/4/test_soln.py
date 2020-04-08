from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp", "res"],
    [
        ([7,1,5,3,6,4], 7),
        ([1,2,3,4,5], 4),
        ([7,6,4,3,1], 0),
        ([], 0),
    ],
)
def test_soln(inp, res):
    s = Solution()
    assert s(inp) == res
