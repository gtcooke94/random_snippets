from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp", "res"],
    [
        (todo_in, todo_out),
    ],
)
def test_soln(inp, res):
    s = Solution()
    assert s(inp) == res
