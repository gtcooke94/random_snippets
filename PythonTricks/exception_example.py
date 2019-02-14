# The following structure is easy and make stack traces much nicer for others
class BaseValidationError(ValueError):
    pass

class NameTooShortError(BaseValidationError):
    pass

def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)

# This would print the following stack trace
# validate('joe')
#
#  NameTooShortError                         Traceback (most recent call last)
#  /Users/gcooke/repos/random_snippets/PythonTricks/exception_example.py in <module>()
#        9         raise NameTooShortError(name)
#       10
#  ---> 11 validate('joe')
#
#  /Users/gcooke/repos/random_snippets/PythonTricks/exception_example.py in validate(name)
#        7 def validate(name):
#        8     if len(name) < 10:
#  ----> 9         raise NameTooShortError(name)
#       10
#       11 validate('joe')
#
#  NameTooShortError: joe

# By having the BaseValidationError, you could catch different kinds of
# validation errors cleanly, i.e. if there was a NameTooShortError,
# NameTooLongError, NameBadCharactersError, they could all be caught with a
# BaseValidationError and handled correctly, keeping you from catching all
# ValueError, for example.

def handle_validation_error(err):
    print(repr(err) + ". Need another name")

try:
    validate('joe')
except BaseValidationError as err:
    handle_validation_error(err)
