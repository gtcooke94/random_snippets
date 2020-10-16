from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp1", "inp2", "res"],
    [
        ([1, 2, 3, 4], 2, [3, 4, 1, 2]),
        ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5, 6], 2, [5, 6, 1, 2, 3, 4])
    ],
)
def test_soln(inp1, inp2, res):
    s = Solution()
    assert s(inp1, inp2) == res
