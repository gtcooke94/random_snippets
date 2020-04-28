from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp1", "inp2", "res"],
    [
        ([-1, -1, 1], 0, 1),
        ([1], 1, 1),
        ([1, 1, 1, -2, 2, -1, 1], 2, 7),
        ([1, 1, 1], 2, 2),
    ],
)
def test_soln(inp1, inp2, res):
    s = Solution()
    assert s(inp1, inp2) == res
