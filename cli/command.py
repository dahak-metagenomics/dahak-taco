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
        ###############
        # ls action
        ###############

        if len(args.action)==1:
            # taco ls just prints available workflows

            if os.path.isdir('rules'):
                available_workflows = next(os.walk('rules/'))[1]

                print("Available workflows:\n")
                print("\n".join(["\t{}\n".format(z) for z in available_workflows]))
                print("To list available rules, run:\n")
                print("\t{} ls <workflow>\n".format(_program))

                sys.exit(0)

            else:
                # no rules folder
                parser.print_help()
                sys.stderr.write('\n\nERROR: Could not find a rules/ directory.\n\n')
                sys.exit(-1)

        elif len(args.action)==2:
            # taco ls <workflow> lists rules in that workflow

            workflow = args.action[1]

            snakefile = os.path.join('rules',workflow,'Snakefile')
            if os.path.isfile(snakefile):

                print('--------')
                print('taco workflow details:')
                print('\tsnakefile: {}'.format(snakefile))
                print('\tconfig: {}'.format(workflowfile))
                print('\tparams: {}'.format(paramsfile))
                print('\ttargets: {}'.format(targets))
                print('--------')

                config = dict(data_dir='data/',
                              clean=args.clean)

                status = snakemake.snakemake(snakefile, 
                                             config=config,
                                             listrules=True)

            else:
                sys.stderr.write('\n\nERROR: Could not find a Snakefile in workflow dir rules/{}\n\n'.format(workflow))
                sys.exit(-1)

        else:

            # Too many arguments
            sys.stderr.write('\n\nERROR: Could not understand arguments to taco ls.')
            parser.print_help()
            sys.exit(-1)




    else:
        ###############
        # <workflow> action
        ###############

        workflow_action = args.action[0]

        if os.path.isdir('rules'):

            available_workflows = next(os.walk('rules/'))[1]
            if workflow_action not in available_workflows:

                # rules dir exists but workflow not found
                parser.print_help()
                sys.stderr.write('\n\nERROR: Could not find workflow {} in list of available workflows.\n\n'.format(workflow_action))
                sys.exit(-1)

        else:

            # no rules folder
            parser.print_help()
            sys.stderr.write('\n\nERROR: Could not find a rules/ directory.\n\n')
            sys.exit(-1)


        if params_file is None:
            pass
        elif not os.path.exists(params_file):
            # no parameters file
            parser.print_help()
            sys.stderr.write('\n\nERROR: Could not find parameters file {}\n\n'.format())
            sys.exit(-1)






if __name__ == '__main__':
    main()
