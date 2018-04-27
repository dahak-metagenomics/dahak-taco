from setuptools import setup, find_packages
import glob
import os
import unittest

with open('requirements.txt') as f:
    required = [x for x in f.read().splitlines() if not x.startswith("#")]

# Note: the _program variable is set
# in __init__.py and determines the name
# of the installed python package, 
# and the name of the final cli tool.
# 
# Personally, I like wooflebog_plinkendorf
from cli import __version__, _program


# auto-detect unit tests in the tests/ directory
# (note: each tests/ dir needs to have an __init__.py to be discoverable)
def taco_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setup(name=_program,
      version=__version__,
      packages=['cli'],
      package_data={
          '':'*.txt'
      },
      test_suite='setup.taco_test_suite',
      description='dahak taco, the command line interface for running dahak workflows',
      url='https://dahak-metagenomics.github.com/dahak-taco',
      author='DIB Lab',
      author_email='cmreid@ucdavis.edu',
      license='BSD-3-Clause',
      entry_points="""
      [console_scripts]
      {program} = cli.command:main
      """.format(program = _program),
      keywords=[],
      tests_require=['pytest', 'coveralls'],
      zip_safe=False)

