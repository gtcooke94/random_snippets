from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp", "res"],
    [
        ([["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]], 3),
        ([[]], 0),
    ],
)
def test_soln(inp, res):
    s = Solution()
    assert s(inp) == res
