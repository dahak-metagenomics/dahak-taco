# Introduction: dahak-taco

dahak-taco is an experimental 
command line interface for 
running dahak workflows.

dahak-taco is hosted in Github
at [https://github.com/dahak-metagenomics/dahak-taco](https://github.com/dahak-metagenomics/dahak-taco).

## Installation

dahak-taco is an executable command-line script.

Create a local clone using git:

```text
$ git clone https://github.com/dahak-metagenomics/dahak-taco.git
```

## How dahak-taco Works

dahak-taco wraps a Snakemake file with a simpler command line interface.

To run dahak-taco, you must have Python and Snakemake installed.

Singularity is not currently required but may be in the future.

## Getting Required Software 

Required software:

* Conda
* Snakemake
* Singularity (optional)

**Installing:** Installation scripts for software needed 
for dahak-taco may be found in the `scripts/` directory
in the repo:

```text
$ ls dahak-taco/scripts/
install_pyenv.py
install_singularity.py
install_snakemake.py
```

You must be root to install singularity.

You may install pyenv and Snakemake as a user only.

**Testing:** To test your environment is working,
run the following command using your version of Python:

```text
$ python -c 'import snakemake'
```

## How To Use Taco

The file `taco` contains the command line tool,
so run it directly:

```
$ ./taco <arguments>
```

This will provide helpful information at the command line. 

Keep reading for a description of what 
information taco requires to run.

## Quick Start

dahak-taco requires two inputs from the user:

* **Workflow configuration file:** specifies the workflow rules
    to run and the names of the target input and output files.
    These rules are defined in `rules/dahak/*.rules`.

* **Workflow parameters file:** specifies values for 
    workflow parameters. Parmaeters set in this
    parameters file will override parameters set
    in the `rules/dahak/*.settings` files.

These are both JSON files.

### Workflow Configuration File

The workflow configuration file 
must specify a key `workflow_target`.

The value must be a valid Snakemake rule
defined in one of the rule files at `rules/dahak/*.rules`.

The form of the workflow configuration file is:

```text
{
    'workflow_target' : <name of Snakemake rule>
}
```

### Example Workflow Configuration File

Here is a simple example of a workflow 
configuration file that pulls containers
from a URL (no output filenames involved):

**`test-workflow.json`:**

```text
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

```text
{
    'app 1 name' : <dict of app 1 parameters>,
    'app 2 name' : <dict of app 2 parameters>,
    ...
    'group 1 name' : <dict of grouped parameters 1>,
    'group 2 name' : <dict of grouped parameters 2>,
    ...
}
```

Most parameters are listed under the app that uses them.
Some parameters are common to a large number of tasks,
so are defined under a group like "reads".

### Example Workflow Parameters File

The following parameters file adjusts parameters for 
the biocontainers rule.

Here is a simple parameters file that adjusts
the version of one of the containers being
pulled in the workflow task defined above:

**`test-params.json`:**

```text
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

```text
./taco test-workflow test-params
```

To run workflows contained in a `configs/` directory, run:

```text
./taco configs/test-workflow configs/test-params
```

To do a dry run only, add the `-n` or `--dry-run` flag:

```text
./taco -n test-workflow test-params
```

### Running the Example Workflow

Following the example above, we run the example workflow
by specifying the test workflow configuration file 
and the test workflow parameters file:

```
./taco test-workflow test-params
```

(Note that a parameters file is optional.)

This will run the pull biocontainers rule.

## Listing Snakemake Rules

You can also list available snakemake rules
using the `dahak ls` command:

```text
$ ./taco ls
```

This is equivalent to the following snakemake command:

```text
$ snakemake -l
```

