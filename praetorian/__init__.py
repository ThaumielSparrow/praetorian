"""
Praetorian wraps Sentry function in a Python package.
It is designed to operate with efficiency in mind and is
theoretically scalable within volumes in a seamless manner.

    https://github.com/ThaumielSparrow/praetorian
"""

from .praetorian import *

from .utils import parallelize