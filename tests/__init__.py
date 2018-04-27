import unittest

# auto-detect unit tests in the tests/ directory
# (note: each tests/ dir needs to have an __init__.py to be discoverable)
def taco_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite
