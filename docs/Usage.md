# Usage

The basic idea behind `taco` is to pass it a verb, and 
modify the interpretation of the verb using command line flags.

The user will defines their Snakemake workflows in a way that 
keeps them general and utilizes user-provided parameters. 
`taco` then reads these workflows, determines what rules exist
and what rules were specified by the user, and runs the workflows
using the user-provided parameters.

Remember, you can always get help by running:

```
$ taco --help
```

## Verbs

Run the taco command line tool like this:

```
$ ./taco <verb> --arguments
```

taco has two main actions:

* `taco ls [<worfklow>]` - lists the available workflows, or the available rules in a given workflow

* `taco <worfklow>` - runs the specified workflow

Each workflow must specify a set of 
workflow configuration variables 
(names of files or Snakemake rules to run)
and workflow parameters (parameters used 
by the workflows themselves). These control
the details of the workflow.

## Flags

The principal way to modify taco workflows 
is to use external YAML or JSON files.

To specify the configuration file, which 
tells taco which files to create or which
rules to run, use:

* **`(--config-json | --config-yaml)`** - flags specifying 
    the path to the JSON or YAML file to use for the 
    workflow configuration.

To specify the parameters file, which 
controls the settings and details of 
each workflow step, use:

* **`(--params-json | --params-yaml)`** - flags specifying 
    the path to the JSON or YAML file to use for the 
    workflow parameters.


