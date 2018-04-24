import sys, os, glob, argparse
import pkg_resources
import snakemake
from . import _program
from clint.textui import puts, indent, colored

logo = """
 _______  _______  _______  _______
|       ||   _   ||       ||       |
|_     _||  |_|  ||       ||   _   |
  |   |  |       ||       ||  | |  |
  |   |  |       ||      _||  |_|  |
  |   |  |   _   ||     |_ |       |
  |___|  |__| |__||_______||_______|

experimental CL interface for dahak workflows
"""

def get_argument_parser(sysargs):
    """
    Construct an ArgumentParser object to parse
    command line arguments.
    """

    parser = argparse.ArgumentParser(prog = _program)

    parser.add_argument("action",
                        help="The action to perform or the name of the workflow to run",
                        nargs='*')


    cfggroup = parser.add_mutually_exclusive_group()
    cfggroup.add_argument("--config-json",
                       help = "Specify a workflow configuration file in JSON format",
                       nargs=1)
    cfggroup.add_argument("--config-yaml",
                       help = "Specify a workflow configuration file in YAML format",
                       nargs=1)


    prmgroup = parser.add_mutually_exclusive_group()
    prmgroup.add_argument("--param-json",
                       help = "Specify a workflow parameters file in JSON format",
                       nargs=1)
    prmgroup.add_argument("--param-yaml",
                       help = "Specify a workflow parameters file in YAML format",
                       nargs=1)


    parser.add_argument('-n', '--dry-run', action='store_true', 
            help="""Do a dry run with Snakemake: assemble but do not run the task graph.""")

    parser.add_argument('-c', '--clean', action='store_true', 
            help="""Use a clean, empty default Snakemake parameters dictionary. Used for testing and debugging.""")


    args = parser.parse_args(sysargs)

    return parser, args


def main(sysargs = sys.argv[1:]):

    parser, args = get_argument_parser(sysargs)

    # Process the action/verb specified by the user.
    if len(args.action)==0:

        parser.print_help()
        sys.exit(-1)


    elif(args.action[0]=='ls'):

        if len(args.action)==1:

            # Just print the available workflows
            if os.path.isdir('rules'):
                available_workflows = next(os.walk('rules/'))[1]

                print("Available workflows:\n")
                print("\n".join(["\t{}\n".format(z) for z in available_workflows]))
                print("To list available rules, run:\n")
                print("\t{} ls <workflow>\n".format(_program))

                sys.exit(0)

            else:
                parser.print_help()
                sys.stderr.write('\n\nERROR: Could not find a rules/ directory.\n\n')
                sys.exit(-1)

        elif len(args.action)==2:

            workflow = args.action[1]

            # print just the workflows
            snakefile = os.path.join('rules',workflow,'Snakefile')
            if os.path.isfile(snakefile):
                print("Found a Snakefile in rules/%s/"%(workflow))
                config = dict(data_dir='data/',
                              clean=args.clean)
                status = snakemake.snakemake(snakefile, 
                                             config=config,
                                             listrules=True)

            else:
                sys.stderr.write('\n\nERROR: Could not find a Snakefile in workflow dir rules/{}\n\n'.format(workflow))
                sys.exit(-1)

        else:

            parser.print_help()
            sys.exit(-1)


if __name__ == '__main__':
    main()
