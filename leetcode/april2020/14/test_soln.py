from soln import Solution
import pytest

@pytest.mark.parametrize(
    ["inp1", "inp2", "res"],
    [
        ("abc", [[0, 1], [1, 2]], "cab"),
        ("abcdefg", [[1,1],[1,1],[0,2],[1,3]], "efgabcd"),
    ],
)
def test_soln(inp1, inp2, res):
    s = Solution()
    assert s(inp1, inp2) == res
