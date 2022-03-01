"""
Two distinguishable types of errors
- Syntax errors
- Exceptions
"""

# Handling Exceptions
try:
    num = int(input("Enter an integer: "))
except (RuntimeError, TypeError, NameError, ValueError):
    print("Invalid!")

"""
All exceptions inherit from BaseException. It can also be used to print an error
message and then re-raise the exception (allowing a caller to handle that exception
as well
"""
import sys
try:
    x = int(input("Enter an integer: "))
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Invalid!")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

"""
The raise statement allows programmers to force a specified exception to occur
"""


