import inspect
import os
import sys
import unittest

__author__ = "David Juboor"
__version__ = "1.0"

# Can't use __file__ because when running with coverage via command line, ___file__ is not the full path
my_location = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))


def test_runner_suite():
    tests_sources_root = my_location #os.path.join(my_location,'tests')

    # region Needed to run when using coverage.py so the imports are properly resolved
    python_sources_root = os.path.join(my_location,'..', 'src')
    sys.path.append(python_sources_root)
    # endregion

    tests = unittest.TestLoader().discover(tests_sources_root)
    return unittest.runner.TextTestRunner().run(tests)


if __name__ == '__main__':
    print(test_runner_suite())

