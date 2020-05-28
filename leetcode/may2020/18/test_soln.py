from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["s1", "s2", "res"],
    [
        ("ab", "eidbaooo", True),
        ("ab", "eidbooao", False),
    ],
)
def test_soln(s1, s2, res):
    s = Solution()
    assert s(s1, s2) == res
