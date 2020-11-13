from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp", "res"],
    [
        ([[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]], 22),
    ],
)
def test_soln(inp, res):
    s = Solution()
    assert s(inp) == res
