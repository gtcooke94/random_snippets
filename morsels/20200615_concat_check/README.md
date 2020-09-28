### Base problem

This works for the first part of the question
`SAME_LINE_LITERAL_CONCAT = r"(\'|\").*(\'|\")[ \t]+(\'|\").*(\'|\")"`

This matched `" "` and `' '`. I'm not sure why adding the `.` in front of the stars mattered
`SAME_LINE_LITERAL_CONCAT = r"(\'|\")*(\'|\")[ \t]+(\'|\")*(\'|\")"`

```
import re
import sys
import pathlib

SAME_LINE_LITERAL_CONCAT = r"(\'|\").*(\'|\")[ \t\n]+(\'|\").*(\'|\")"

def concat_check(lines, file_string=None):
    for line_number, line in enumerate(lines):
        matches = re.findall(SAME_LINE_LITERAL_CONCAT, line, re.DOTALL)
        for match in matches:
            print(f"{file_string}, line {line_number + 1}: implicit concatenation")



if __name__ == "__main__":
    args = sys.argv[1:]
    for file_string in args:
        with pathlib.Path(file_string).open() as f:
            contents = f.readlines()
            concat_check(contents, file_string=file_string)
```



### Base with Tokenize and Bonus 1/2 - handle multiline strings and other types of strings.

I had a lot of trouble doing this with regex, so I peeked at the solutions to find the statement
> Regex is probably not the right choice at this point. We should use Python's tokenizer module instead.

I've never used that, so time to learn.

Here's the help for tokenize:
```
Signature: tokenize(readline)
Docstring:
The tokenize() generator requires one argument, readline, which
must be a callable object which provides the same interface as the
readline() method of built-in file objects.  Each call to the function
should return one line of input as bytes.  Alternatively, readline
can be a callable function terminating with StopIteration:
    readline = open(myfile, 'rb').__next__  # Example of alternate readline

The generator produces 5-tuples with these members: the token type; the
token string; a 2-tuple (srow, scol) of ints specifying the row and
column where the token begins in the source; a 2-tuple (erow, ecol) of
ints specifying the row and column where the token ends in the source;
and the line on which the token was found.  The line passed is the
physical line.

The first token sequence will always be an ENCODING token
which tells you which encoding was used to decode the bytes stream.
```

Wow does this library make this a lot easier - it's definitely the right thing to use for this task, _not_ regex.

Here's a tokenizer solution that gets the base problem and first bonus.
LIES: tests are named wrong - this passed bonus 2

```
import sys
import pathlib
from tokenize import tokenize, STRING


def concat_check(filename):
    filepath = pathlib.Path(filename)
    with filepath.open("rb") as f:
        tokenizer = tokenize(f.readline)
        prev_token = next(tokenizer)
        for token in tokenizer:
            if token.type == STRING and prev_token.type == STRING:
                print(f"{filename}, line {token.start[0]}: implicit concatenation")
            prev_token = token


if __name__ == "__main__":
    args = sys.argv[1:]
    for filename in args:
        concat_check(filename)

```

To get multiline stuff working a little bit better, we just don't care about newline tokens, and to get the right line number of where the implicit concatenation occurs we used `prev_token.end[0]`

```
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
                print(f"{filename}, line {prev_token.end[0]}: implicit concatenation")
            if token.type != NL:
                prev_token = token


if __name__ == "__main__":
    args = sys.argv[1:]
    for filename in args:
        concat_check(filename)
```

### Bonus 3 - actually print the strings where the implicit concat occurs
This was pretty easy, just change the print line to use `token.string`

```
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
                print(f"{filename}, line {prev_token.end[0]} between {prev_token.string} and {token.string}")
            if token.type != NL:
                prev_token = token


if __name__ == "__main__":
    args = sys.argv[1:]
    for filename in args:
        concat_check(filename)
```

