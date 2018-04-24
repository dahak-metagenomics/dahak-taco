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

    args = parser.parse_args(sysargs)

    return args


def main(sysargs = sys.argv[1:]):

    args = get_argument_parser(sysargs)

    # Process the action/verb specified by the user.
    if len(args.action)==0:

        print("You need to get some help, man.")
        exit(1)

    elif(args.action[0]=='ls'):

        if len(args.action)==1:

            print("checking for rules")

            # print just the workflows
            if os.path.isdir('rules'):
                print("walking rules")
                print(next(os.walk('rules/'))[1])
            else:
                print("no rules, gonna quit now")
                exit(1)

        elif len(args.action)==2:

            workflow = args.action[1]

            # print just the workflows
            snakefile = os.path.join('rules',workflow,'Snakefile')
            if os.path.isfile(snakefile):
                print("Found a Snakefile in rules/%s/"%(workflow))
                config = dict(message="OHAIIIII")
                status = snakemake.snakemake(snakefile, 
                                             config=config,
                                             listrules=True)

            else:
                print("No Snakefile in rules/%s/"%(workflow))

        else:

            print("You need to get some help, man.")
            exit(1)



    # Note: args.action is a list because we specified nargs=1


    my_data = pkg_resources.resource_string(__name__, "data.txt")
    print(args.action)
    if(args.action[0]=='hello'):
        if(os.path.isfile('custom.txt')):
            with open('custom.txt') as f:
                print("\n".join(f.readlines()))
        else:
            print("NO CUSTOM FILE")





if __name__ == '__main__':
    main()
