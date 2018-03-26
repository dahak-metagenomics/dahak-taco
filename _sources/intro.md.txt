# Introduction: dahak-taco

dahak-taco is an experimental 
command line interface for 
running dahak workflows.

## Installation

dahak-taco is an executable command-line script.

### Required Software

Requirements:

* Conda
* Snakemake
* Singularity (optional)

### Scripts for Installing Required Software

Installation scripts for software needed 
for dahak-taco are in the `scripts/` folder:

```
$ ls scripts/
install_pyenv.py
install_singularity.py
install_snakemake.py
```

You can test that your environment is working correctly
by running your version of python and an 
`import snakemake` command:

```
python -c 'import snakemake'
```

### Where Is Taco

The file `taco` contains the command line tool,
so run it directly:

```
$ ./taco <arguments>
```

## Quick Start

dahak-taco requires two inputs from the user:

* Workflow configuration file - specifies the workflow rules
    to run and the names of the target input and output files.
    These rules are defined in `rules/dahak/*.rules`.

* Workflow parameters file - specifies values for 
    workflow parameters. Parmaeters set in this
    parameters file will override parameters set
    in the `rules/dahak/*.settings` files.

These are both JSON files.

### Workflow Configuration File

The workflow configuration file 
must specify a key `workflow_target`.

The value must be a valid Snakemake rule
defined in one of the rule files at `rules/dahak/*.rules`.

### Example Workflow Configuration File

Here is a simple example of a workflow 
configuration file that pulls containers
from a URL (no output filenames involved):

**`test-workflow.json`:**

```
{
    "workflow_target" : "pull_biocontainers"
}
``` 

### Workflow Parameters File

The workflow parameters file contains parameter values
to control the workflow. These parameter values will override
parameters set in the settings files at `rules/dahak/*.settings`.

Parameters are any variables used in the Snakemake rules.
All Snakemake parameters are contained in a config dictionary
that contains dictionaries of parameters, typically grouped 
by workflow rule, application, or group of applications.

The form of the workflow parameters JSON file is:

```
{
    'rule 1 name' : <dict of rule 1 parameters>,
    'rule 2 name' : <dict of rule 2 parameters>,
    ...
    'app 1 name' : <dict of app 1 parameters>,
    'app 2 name' : <dict of app 2 parameters>,
    ...
    'group 1 name' : <dict of grouped parameters 1>,
    'group 2 name' : <dict of grouped parameters 2>,
    ...
}
```

Some parameters are named according to the app or rule 
that uses them. Others are used by several rules and 
have a more generic group name.

### Example Workflow Parameters File

The following parameters file adjusts parameters for 
the biocontainers rule.

Here is a simple parameters file that adjusts
the version of one of the containers being
pulled in the workflow task defined above:

**`test-params.json`:**

```
{
    "biocontainers" : {
        "sourmash" : "2.0.0a2--py36_0"
    }
}
```

(Note that this overrides the default 
sourmash version of `2.0.0a3--py36_0`
defined in `rules/dahak/biocontainers.settings`.

### Running

To run taco, pass it two arguments on the command line.
The first argument is the name of the workflow,
the second argument is the name of the paramters file.

Both arguments should be the path to a JSON file
(absolute or relative) and exclude the JSON suffix.

For example, to run the two JSON files in the 
example above,

```
./taco test-workflow test-params
```

To run workflows contained in a `configs/` directory, run:

```
./taco configs/test-workflow configs/test-params
```

### Running the Example Workflow

Following the example above, we run the example workflow
by specifying the test workflow configuration file 
and the test workflow parameters file:

```
./taco test-workflow test-params
```

This will run the pull biocontainers rule.

## Other Commands

To see what rules are possible, you can 
use the `dahak ls` command by running:

```
$ dahak ls
```

