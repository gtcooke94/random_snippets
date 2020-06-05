# solution through bonus 2
def last_lines(filename):
    data = ''
    with open(filename) as file_object:
        file_object.seek(0, 2)  # Seek to end of file
    position = file_object.tell()
        while position:
            prev_position = position
            if position < 8192:
                position = 0
            else:
                position -= 8192
            file_object.seek(position)
            data = file_object.read(prev_position - position) + data
            data, sep, remaining = data.partition('\n')
            data += sep
            lines = []
            while '\n' in remaining:
                line, sep, remaining = remaining.partition('\n')
                lines.append(line+sep)
            if remaining:
                lines.append(remaining)
            for line in reversed(lines):
                yield line
        yield data


# Cleaner solution
import io
import os
import re


def last_lines(filename, *, chunk_size=io.DEFAULT_BUFFER_SIZE):
    data = ''
    with open(filename) as file_object:
        position = file_object.seek(0, os.SEEK_END)
        while position:
            previous = position
            position = max(0, position-chunk_size)
            file_object.seek(position, os.SEEK_SET)
            data = file_object.read(previous-position) + data
            data, *lines = re.findall(r'.*\n|.+$', data)
            yield from reversed(lines)
        yield data
