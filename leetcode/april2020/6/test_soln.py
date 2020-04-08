from soln import Solution
import pytest


@pytest.mark.parametrize(
    ["inp", "res"],
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]],
        ),
        (["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"],
            [["sol"],["wow"],["gap"],["hem"],["yap"],["bum"],["ugh","ugh"],["aha"],["jab"],["eve"],["bop"],["lyx"],["jed"],["iva"],["rod"],["boo"],["brr"],["hog"],["nay"],["mir"],["deb","deb"],["aft"],["dis"],["yea"],["hos"],["rye"],["hey"],["doc"],["bob"],["eel"],["pen"],["job"],["max"],["oho"],["lye"],["ram"],["nap"],["elf"],["qua"],["pup","pup"],["let"],["gym"],["nam"],["bye"],["lon"]]
        ),

    ],
)
def test_solution(inp, res):
    s = Solution()
    out = s(inp)
    assert sort_ll(out) == sort_ll(res)


def sort_ll(ll):
    new_ll = []
    for item in ll:
        sorted_item = sorted(item)
        new_ll.append(sorted_item)
    return sorted(new_ll)
