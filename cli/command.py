import sys, os, glob, argparse
import pkg_resources
import snakemake
from . import _program
import yaml, json


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


def main(sysargs = sys.argv[1:]):

    parser, args = get_argument_parser(sysargs)

    # Make sure the user provided SOME arguments
    if(len(sys.argv)==1):
        sys.stderr.write(logo)
        parser.print_help(sys.stderr)
        sys.exit(1)

    # Process the verb specified by the user.
    if len(args.verb)==0:
        die('No verb specified',parser)

    elif(args.verb[0]=='ls'):
        ls_verb(parser, args)

    else:
        workflow_verb(parser, args)




def get_argument_parser(sysargs):
    """
    Construct an ArgumentParser object to parse
    command line arguments.
    """

    parser = argparse.ArgumentParser(prog = _program)

    parser.add_argument("verb",
                        help="The verb to perform or the name of the workflow to run",
                        nargs="*")


    parser.add_argument("--config",
                       help = "Specify a workflow configuration file in JSON or YAML format (configuration controls what process is run)",
                       nargs=1)
    parser.add_argument("--params",
                       help = "Specify a workflow parameters file in JSON or YAML format (parameters control how a process is run)",
                       nargs=1)


    parser.add_argument('-c', '--clean', action='store_true', 
            help="""Use a (clean) empty, default Snakemake parameters dictionary. Used for testing and debugging.""")

    parser.add_argument('-f', '--force', action='store_true', 
            help="""Force Snakemake to run all rules in the workflow, even if the files the rule outputs already exist.""")

    parser.add_argument('-n', '--dry-run', action='store_true', 
            help="""Do a dry run with Snakemake: assemble but do not run the task graph.""")

    parser.add_argument('--prefix', action='store', 
            default='data/',
            help="""Set the working directory where all workflow files will be generated.""")


    args = parser.parse_args(sysargs)

    return parser, args



def ls_verb(parser, args):
    """
    List verb.
    With no arguments, list all valid workflows.
    With one argument, use argument as workflow name.

    Check if workflow name is valid, and print all the 
    rules that workflow defines.
    """
    if len(args.verb)==1:

        # taco ls just prints available workflows

        if not os.path.isdir('rules'):

            die('Could not find rules directory',parser)

        else:

            available_workflows = next(os.walk('rules/'))[1]

            print("Available workflows:\n")
            print("\n".join(["\t{}\n".format(z) for z in available_workflows]))
            print("To list available rules, run:\n")
            print("\t{} ls <workflow>\n".format(_program))

            sys.exit(0)

    elif len(args.verb)==2:
        # taco ls <workflow> lists rules in that workflow

        workflow = args.verb[1]

        snakefile = os.path.join('rules',workflow,'Snakefile')
        if os.path.isfile(snakefile):

            config = dict(data_dir=args.prefix,
                          clean=args.clean)

            status = snakemake.snakemake(snakefile, 
                                         config=config,
                                         listrules=True)

        else:
            die('Could not find Snakefile in workflow directory rules/{}'.format(workflow),parser)

    else:
        die('Too many arguments',parser)



def workflow_verb(parser, args):
    """
    Workflow verb.

    This looks in the rules/ directory to find
    all valid workflows, checks the workflow exists,
    and runs the workflow.
    """
    workflow_verb = args.verb[0]

    if not os.path.isdir('rules'):
        die('Could not find a rules/ directory.',parser)

    available_workflows = next(os.walk('rules/'))[1]

    if workflow_verb not in available_workflows:
        # rules dir exists but workflow not found
        die('Could not find workflow {} in list of available workflows.'.format(workflow_verb),parser)

    snakefile = os.path.join('rules',workflow_verb,'Snakefile')

    if not os.path.isfile(snakefile):
        die('Could not find Snakekfile {} in directory'.format(snakefile),parser)


    # Load Workfow Parameters.
    # 
    # Load the JSON/YAML file with workflow parameters,
    # and populate the Snakemake configuration dict.

    paramsfile = None
    smk_config = {}


    # Option 1:
    # Taco infers directory structure
    # Requires one *config*{json,yaml} and one *param*{json,yaml}

    def infer_file(shortname,longname):
        """Use this to infer workflow config/param files"""

        # Look for *params*{json,yaml,yml}
        # or *config*{json,yaml,yml}
        files =  glob.glob("*%s*json"%(shortname))
        files += glob.glob("*%s*yaml"%(shortname))
        files += glob.glob("*%s*yml"%(shortname))

        raise_err = len(files)!=1
        if len(files)>1:
            howmany = 'more than one file'
        else:
            howmany = 'no files'
        if raise_err:
            err = 'Tried to infer workflow %s file '%(longname)
            err += 'but found %s matching pattern: '%(howmany)
            err += '*%s*{json,yaml,yml}'%(shortname)
            die(err,parser)

        if len(files)>1:
            return files[0]


    # Parameters file is passed on directly to Snakemake

    if args.params is None:
        paramsfile = infer_file('params','parameters')
    else:
        paramsfile = args.params[0]
        _, ext = os.path.splitext(paramsfile)
        valid_extensions = ['json','yaml','yml']
        if ext.lower() not in valid_extensions:
            err = 'Unrecognized file format for params file: %s'%(ext)
            hint = 'Expected one of these: '%(", ".join(valid_extensions))
            die(err=err,
                hint=hint,
                parser=parser)

    if not os.path.isfile(paramsfile):
        die('The workflow parameters file {} is not a valid file'.format(paramsfile),parser)


    # Config file is used to figure out how to call Snakemake

    if args.config is None:
        configfile = infer_file('config','configuration')
    else:
        configfile = args.config[0]
        _, ext = os.path.splitext(configfile)
        valid_extensions = ['json','yaml','yml']
        if ext.lower() not in valid_extensions:
            err = 'Unrecognized file format for config file: %s'%(ext)
            hint = 'Expected one of these: '%(", ".join(valid_extensions))
            die(err=err,
                hint=hint,
                parser=parser)

    if not os.path.isfile(configfile):
        die('The workflow configuration file {} is not a valid file'.format(configfile),parser)
    else:
        _, ext = os.path.splitext(configfile)
        if ext in ['yaml','yml']:
            config_dictionary = yaml.load(open(workflowfile,'r'))
        elif ext in ['json']:
            config_dictionary = json.load(open(workflowfile,'r'))

    try:
        targets = config_dictionary['workflow_targets']
        if(type(targets)!=type([])):
            targets = [targets]

    except KeyError:
        die(err='Could not find key "workflow_targets" in workflow configuration.',
            hint='Make sure the parser and config files are not swapped.',
            parser=parser)

    config = dict(data_dir='data/',
                  clean=args.clean)


    print('--------')
    print('taco workflow details:')
    print('\tsnakefile: {}'.format(snakefile))
    print('\tconfig: {}'.format(workflowfile))
    print('\tparams: {}'.format(paramsfile))
    print('\ttargets: {}'.format(targets))
    print('\tbootstrap configuration: {}'.format(config))
    print('--------')

    status = snakemake.snakemake(snakefile, 
                                 configfile=paramsfile,
                                 targets=targets, 
                                 printshellcmds=True,
                                 lock=False,
                                 dryrun=args.dry_run, 
                                 forceall=args.force,
                                 config=config)


    if status: # translate "success" into shell exit code of 0
        return 0
    else:
        print("")
        print("Error: Failed to call Snakemake API")
        print("You might have requested an output file or rule that does not exist.")
        print("Try adding the data directory location as a prefix to your file names.")
        print("")
        print("config['data_dir'] = %s"%(config['data_dir']))
        print("")
        return 1



def die(err,parser,hint=None):
    parser.print_help()
    sys.stderr.write('\n\nERROR: %s\n\n'%(err))
    if(hint is not None):
        sys.stderr.write('\n\nHINT: %s\n\n'%(err))
    sys.exit(-1)


if __name__ == '__main__':
    main()

