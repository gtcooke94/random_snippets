import sys
import pathlib
from tokenize import tokenize, STRING, NL


def concat_check(filename):
    filepath = pathlib.Path(filename)
    with filepath.open("rb") as f:
        tokenizer = tokenize(f.readline)
        prev_token = next(tokenizer)
        for token in tokenizer:
            if token.type == STRING and prev_token.type == STRING:
                print(
                    f"{filename}, line {prev_token.end[0]} between {prev_token.string} and {token.string}"
                )
            if token.type != NL:
                prev_token = token


if __name__ == "__main__":
    args = sys.argv[1:]
    for filename in args:
        concat_check(filename)
