import os
from tempfile import mkdtemp
import shutil

class cd:

    def __init__(self, directory=None):
        self.temp_flag = directory is None
        if directory:
            self.directory = directory
        else:
            self.directory = mkdtemp()

    def __enter__(self):
        self.old_directory = os.getcwd()
        self.previous = self.old_directory
        os.chdir(self.directory)
        self.current = self.directory
        return self

    def __exit__(self, exc_type, exc_val, trace):
        os.chdir(self.old_directory)
        if self.temp_flag:
            shutil.rmtree(self.directory)
        return False

    def enter(self):
        self.__enter__()

    def exit(self):
        self.__exit__(None, None, None)
"""
From python docs on context managers:

Exit the runtime context and return a Boolean flag indicating if any exception that occurred should be suppressed. If an exception occurred while executing the body of the with statement, the arguments contain the exception type, value and traceback information. Otherwise, all three arguments are None.

Returning a true value from this method will cause the with statement to suppress the exception and continue execution with the statement immediately following the with statement. Otherwise the exception continues propagating after this method has finished executing. Exceptions that occur during execution of this method will replace any exception that occurred in the body of the with statement.

The exception passed in should never be reraised explicitly - instead, this method should return a false value to indicate that the method completed successfully and does not want to suppress the raised exception. This allows context management code to easily detect whether or not an __exit__() method has actually failed.
"""


