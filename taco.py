#!/usr/bin/env python
import colorama
import argparse
import long_strings as tacos

"""
 _______  _______  _______  _______
|       ||   _   ||       ||       |
|_     _||  |_|  ||       ||   _   |
  |   |  |       ||       ||  | |  |
  |   |  |       ||      _||  |_|  |
  |   |  |   _   ||     |_ |       |
  |___|  |__| |__||_______||_______|

experimental CL interface for dahak workflows
"""

class Taco(object):

    def __init__(self):
        """
        Taco object constructor processes the first command,
        and determines how to proeed.
        """
        self.logo = tacos.logo
        parser = argparse.ArgumentParser(
            description = tacos.taco_description,
            usage = tacos.taco_usage)

        parser.add_argument('command', help='Subcommand to run')

        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command: %s\n'%(args.command))
            parser.print_help()
            exit(1)

        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()



    ####################################################
    # Trim sequence reads workflow

    def trim_reads(self):
        """
        Create a TacoParams_TrimReads object 
        """
        parser = argparse.ArgumentParser(
                description = tacos.trim_reads_description,
                usage = tacos.trim_reads_usage)

        # We should do something here...
