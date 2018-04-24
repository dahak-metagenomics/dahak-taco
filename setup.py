from setuptools import setup, find_packages
import glob
import os

with open('requirements.txt') as f:
    required = [x for x in f.read().splitlines() if not x.startswith("#")]

# Note: the _program variable is set
# in __init__.py and determines the name
# of the installed python package, 
# and the name of the final cli tool.
# 
# Personally, I like wooflebog_plinkendorf
from cli import __version__, _program

setup(name=_program,
      version=__version__,
      packages=['cli'],
      package_data={
          '':'*.txt'
      },
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