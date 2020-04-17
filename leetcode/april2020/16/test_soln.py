from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp", "res"],
    [
        ("(*))", True),
        ("((*()))(", False),
        ("(())(())(((()*()()()))()((()()(*()())))(((*)()", False),
        ("**((*", False),
        ("*(((*)", False),
        ("(())((())()()(*)(*()(())())())()()((()())((()))(*", False),
        ("((*", False),
        ("()", True),
        ("(*)", True),
        ("(*", True),
        (")(", False),
        ("", True),
        ("*)", True),
        ("(((*))())", True),
    ],
)
def test_soln(inp, res):
    s = Solution()
    assert s(inp) == res
