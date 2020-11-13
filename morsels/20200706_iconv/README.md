### Base:
This solves the base problem

```
import argparse
import sys
import pathlib


def main():
    parser = setup_parser()
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output
    from_code = args.from_code
    to_code = args.to_code
    in_string = pathlib.Path(input_file).open("rb").read()
    converted_string = convert_string_from_to(in_string, from_code, to_code)
    pathlib.Path(output_file).open("wb").write(converted_string)


def convert_string_from_to(in_string, from_code, to_code):
    return in_string.decode(from_code).encode(to_code)


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("-f", "--from-code", default=sys.getdefaultencoding())
    parser.add_argument("-t", "--to-code", default=sys.getdefaultencoding())
    return parser


if __name__ == "__main__":
    main()
```

I discovered that the above was really bad. Here's a better solution
```
import argparse
import sys
import pathlib


def main():
    parser = setup_parser()
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output
    from_code = args.from_code
    to_code = args.to_code
    to_write = pathlib.Path(input_file).open("r", encoding=from_code).read()
    pathlib.Path(output_file).open("w", encoding=to_code).write(to_write)




def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("-f", "--from-code", default=sys.getdefaultencoding())
    parser.add_argument("-t", "--to-code", default=sys.getdefaultencoding())
    return parser


if __name__ == "__main__":
    main()
```

### Bonus 1:
Do some niceness to get stdout to the same write interface
```
import argparse
import sys
import pathlib


def main():
    parser = setup_parser()
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output
    from_code = args.from_code
    to_code = args.to_code
    in_string = pathlib.Path(input_file).open("r", encoding=from_code).read()
    writer = get_writer(output_file, to_code)
    writer(in_string)


def get_writer(output_file, to_code):
    if output_file:
        writer = pathlib.Path(output_file).open("w", encoding=to_code).write
    else:
        sys.stdout.reconfigure(encoding=to_code)
        writer = sys.stdout.write
    return writer


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("-o", "--output", default=None)
    parser.add_argument("-f", "--from-code", default=sys.getdefaultencoding())
    parser.add_argument("-t", "--to-code", default=sys.getdefaultencoding())
    return parser


if __name__ == "__main__":
    main()
```

### Bonus 2:
Reading about this, we can get even cleaner by using `argparse` to do files for us
Argparse knows that `-` means stdout/stdin, so this just works
(Python 3.7+ because that's when we get the `sys.std[out/in].reconfigure`)
```
import argparse
import sys


def main():
    parser = setup_parser()
    args = parser.parse_args()
    inp = args.input_file
    output = args.output
    from_code = args.from_code
    to_code = args.to_code
    inp.reconfigure(encoding=from_code)
    output.reconfigure(encoding=to_code)
    output.write(inp.read())


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file", nargs="?", default="-", type=argparse.FileType("r")
    )
    parser.add_argument("-o", "--output", default="-", type=argparse.FileType("w"))
    parser.add_argument("-f", "--from-code", default=sys.getdefaultencoding())
    parser.add_argument("-t", "--to-code", default=sys.getdefaultencoding())
    return parser


if __name__ == "__main__":
    main()
```

### Bonus 3:
Lets us get deeper into the niceness of argparse
```
import argparse
import sys


def main():
    parser = setup_parser()
    args = parser.parse_args()
    inp = args.input_file
    output = args.output
    from_code = args.from_code
    to_code = args.to_code
    errors = args.errors
    inp.reconfigure(encoding=from_code, errors=errors)
    output.reconfigure(encoding=to_code)
    output.write(inp.read())


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file", nargs="?", default="-", type=argparse.FileType("r")
    )
    parser.add_argument("-o", "--output", default="-", type=argparse.FileType("w"))
    parser.add_argument("-f", "--from-code", default=sys.getdefaultencoding())
    parser.add_argument("-t", "--to-code", default=sys.getdefaultencoding())
    parser.add_argument("-c", dest="errors", action="store_const", const="ignore")
    return parser


if __name__ == "__main__":
    main()
```


For reference, here's the provided solution pre Python 3.7 when you can't use reconfigure
```
from io import TextIOWrapper
from argparse import ArgumentParser
import sys


parser = ArgumentParser()
parser.add_argument('-f', '--from-code', help="encoding of original text")
parser.add_argument('-t', '--to-code', help="encoding of output")
parser.add_argument('-c', dest="errors", action='store_const', const='ignore',
                    help="omit invalid characters from output")
parser.add_argument('-o', '--output', help="output file")
parser.add_argument('file', help="input file", nargs='?', default='-')
args = parser.parse_args()


if args.output:
    output_file = open(args.output, encoding=args.to_code, mode='wt')
else:
    output_file = TextIOWrapper(sys.stdout.buffer, encoding=args.to_code)

with output_file:
    if args.file != '-':
        input_file = open(
            args.file,
            encoding=args.from_code,
            mode='rt',
            errors=args.errors,
        )
    else:
        input_file = TextIOWrapper(
            sys.stdin.buffer,
            encoding=args.from_code,
            errors=args.errors,
        )
    with input_file:
        for line in input_file:
            output_file.write(line)
```
