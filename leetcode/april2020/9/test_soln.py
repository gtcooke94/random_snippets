from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp1", "inp2", "res"],
    [
        ("j##yc##bs#srqpfzantto###########i#mwb", "j##yc##bs#srqpf#zantto###########i#mwb", False),
        ("xywrrmp", "xywrrmu#p", True),
        ("nzp#o#g", "nzp#o##g", False),
        ("y#fo##f", "y#fx#o##f", True),
        ("bxj##tw", "bxo#j##tw", True),
        ("ab#c", "ad#c", True),
        ("ab##", "c#d#", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
    ],
)
def test_soln(inp1, inp2, res):
    s = Solution()
    assert s(inp1, inp2) == res
