from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp1", "inp2", "res"],
    [
        ("112", 1, "11"),
        ("11000002000304", 4, "4"),
        ("9119801020", 6, "20"),
        ("111111", 3, "111"),
        ("1432219", 3, "1219"),
        ("10200", 1, "200"),
        ("10", 2, "0"),
        ("10", 1, "0"),
    ],
)
def test_soln(inp1, inp2, res):
    s = Solution()
    assert s(inp1, inp2) == res
