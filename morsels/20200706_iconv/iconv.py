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
