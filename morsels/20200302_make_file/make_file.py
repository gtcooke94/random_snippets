import tempfile
import os

class make_file:

    def __init__(self, *, contents=None, directory=None, mode="r+", encoding=None, newline=None):
        self.initial_content = contents
        self.directory = directory
        self.mode = mode
        self.encoding = encoding
        self.newline = newline

    def __enter__(self):
        self.file, self.filename = tempfile.mkstemp(self.mode, dir=self.directory)
        if self.initial_content:
            with open(self.filename, self.mode, encoding=self.encoding, newline=self.newline) as f:
                f.write(self.initial_content)
        return self.filename

    def __exit__(self, exc_type, exc_value, traceback):
        os.close(self.file)
        os.remove(self.filename)
        

