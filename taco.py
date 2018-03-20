#!/usr/bin/env python
import argparse
import os, sys
import snakemake
import json

"""
 _______  _______  _______  _______
|       ||   _   ||       ||       |
|_     _||  |_|  ||       ||   _   |
  |   |  |       ||       ||  | |  |
  |   |  |       ||      _||  |_|  |
  |   |  |   _   ||     |_ |       |
  |___|  |__| |__||_______||_______|

experimental CL interface for dahak workflows


just call taco.

main method:
    - find snakefile
    - find workflow config file (sets target)
    - find workflow params file
    - print info: snakefile/config/params/target
    - call snakemake

__main__ method:
    - create argparser
    - add argument
    - add -n arguments
    - sys.exit(main(args))
"""




