# Installation and Usage 

`taco` is a command-line utility that runs Snakemake workflows. 
This document covers how to install and use taco.


## Installation Instructions

`taco` is installed using `setup.py`, and will be 
installed as a command-line utility on the system.
When we are finished you will be able to run the 
command 

```
$ taco --help
```

and see a `taco` help message.

### Clone 

Start by cloning a local copy of the repository:

```
git clone https://github.com/dahak-metagenomics/dahak-taco
```

You can specify a particular tag or branch with the 
clone command, or use the default `stable` branch.


### Build and Install

The next step is to build and install the `taco` source code
using `setup.py`:

```
$ python setup.py build
```

If you want to install taco as a system level module, run:

```
$ python setup.py install
```

If you want to install it as a user (recommended):

```
$ python setup.py install --user

$ python setup.py install --user --prefix=    # <-- this is required on mac
```

This will install the taco command line utility as an 
executable program in the Python `bin` location. This 
location may or may not be on your path, and varies
depending on your Python environment, but should be in

```
$PYTHONHOME/bin
```

This should be on your `$PATH` for you to be able to 
call `taco` from the command line.

## Usage

The basic idea behind `taco` is to pass it a verb, and 
modify the interpretation of the verb using command line flags.

The user will defines their Snakemake workflows in a way that 
keeps them general and utilizes user-provided parameters. 
`taco` then reads these workflows, determines what rules exist
and what rules were specified by the user, and runs the workflows
using the user-provided parameters.

### Verbs

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

## Rules

Workflows are defined in a folder called `rules/`.

The `rules/` directory contains one folder per workflow.

Each workflow directory contains rules in `*.rule` files
and default parameters in `*.settings` files, as well as 
a Snakefile that is imported by taco and that should 
in turn include each rule and settings file used by 
that workflow.


## Docker and Singularity

Most taco workflows utilize singularity to run docker containers
as part of the workflows. Docker containers are usually specified
by URL, but if a biocontainer or Dockerhub image is broken, a local
image must be used. 

For this reason, some workflows will include their own
Dockerfiles. This is not recommended and should serve 
only as a temporary fix.


## Workflow Repository

To create a new set of workflows, create a new repository.

You will need a `rules/` folder, as well as a folder for
configuration files and parameter files.

The taco tool is then run from that directory, and runs
the workflows defined in that directory.

Here is an example repository layout for 
a repository containing two related workflows:

```
taco-my-cool-workflow/
        
        rules/
            workflowA/
                Snakefile
                purple.rule
                blue.rule
                green.rule
                workflowA.settings

            workflowB/
                Snakefile
                apple.rule
                orange.rule
                banana.rule
                workflowB.settings

        workflow-config/
            config_make_apples.json
            config_make_blue_apples.json
            config_make_bananas.json
            config_make_green_bananas.json

        workflow-params/
            params_lite.json
            params_medium.json
            params_heavy.json

        docker/
            utility_one/
                Dockerfile
            utility_two/
                Dockerfile
            utility_three/
                Dockerfile
```



## Workflow Name

Each workflow is defined by a Snakefile that includes
a set of rules for each step of the workflow
and a dictionary of parameter values. 

Each workflow is in its own directory in the 
[`rules/`](https://github.com/dahak-metagenomics/dahak-taco/tree/master/rules)
directory of this repository and must have 
a Snakefile.

The user should specify the workflow name as the first
verb on the command line, then pass any flags that modify
the workflow behavior. For example:

```
$ taco read_filtering (--config-json|--config-yaml) (--params-json|--params-yaml)
```

This command will run the Snakemake API with the Snakefile found in `rules/read_filtering` 
(relative to the current directory where `taco` was run). It uses the target specified by 
the user's workflow configuration file to figure out what rules to run, and runs them using
the parameters in the user's parameters file.


## Workflow Configuration File

The workflow configuration file 
contains a dictionary of configuration values.

The workflow configuration file
must specify a list of workflow targets
assigned to the key `workflow_targets`.

The value must be a valid Snakemake rule
defined in one of the rule files at `rules/<workflow-name>/*.rules`.

The form of the workflow configuration file 
for running rules that have no file targets is
to specify the name of the rule:

**JSON:**

```text
{
    "workflow_targets" : <list of Snakemake rules>
}


{
    "workflow_targets" : <list of output file targets>
}
```

**YAML:**

```text
workflow_targets:
  - list
  - of 
  - target
  - files

-----------

workflow_targets:
  - list
  - of
  - target
  - rules
```

### Example Rule-Based Workflow Configuration File

Here is a simple example of a workflow configuration file
for running a rule that has no file targets (pulling containers).
This rule specifies the workflow target by specifying the 
rule name:

**JSON:**

```text
{
    "workflow_targets" : ["pull_biocontainers"]
}
``` 

**YAML:**

```text
workflow_targets:
  - pull_biocontainers
```

### Example File-Based Workflow Configuration File

Here is a simple example of a workflow configuration file
that runs rules based on filename targets (in this example,
the output of a trimming process):

**JSON:**

```text
{
    "workflow_targets" : ["XXXXXX_trim5_1.fq.gz",
                          "XXXXXX_trim5_2.fq.gz"]
}
``` 

**YAML:**

```text
workflow_targets: 
  - XXXXXX_trim5_1.fq.gz
  - XXXXXX_trim5_2.fq.gz
``` 

## Workflow Parameters File

The workflow parameters control various parameters
that are used by the programs and containers run
by the Snakemake rules.

Each workflow defines a set of default parameter values
in a `.settings` file that lives next to the `Snakefile`
and `*.rule` files.

However, the user can set these parameter values in the 
workflow parameters file, and these values set by the user 
will override the default values.

The workflow parameters control how the workflow proceeds.

The workflow configuration controls the starting and ending points.

The form of the workflow parameters JSON file is:

**JSON:**

```text
{
    '<workflow-name>' : {
        '<rule-name>' : {
            '<param-name>' : <param-value>,
            '<param-list>' : [<value1>, ...],
            ...
        }
    }
}
```


**YAML:**

```text
my_workflow_name:

  my_rule_name_1:
    my_param_name_1: "my_param_value"
    my_param_name_2: 10

  my_rule_name_2:
    my_param_name_3: "another_param_value"
    my_param_name_4: 100
```

Most parameters are listed under the name of the application
that uses it, but some parameters have more generic names because
they are common to multiple tasks.

### Example Workflow Parameters File

The following example parameters file adjusts the parameters for 
the rule to update biocontainers.

This is a simple parameter file overriding a single parameter,
the version of sourmash being utilized.

This overrides the default biocontainers setting of 
sourmash version `2.0.0a3--py36_0`, set in 
`rules/dahak/biocontainers.settings`.

**JSON:**

```text
{
    "biocontainers" : {
        "trimmomatic" : {
            "use_local" : false,
            "quayurl" : "quay.io/biocontainers/trimmomatic",
            "version" : "0.36--5"
        }
    }
}
```

**YAML:**

```text
biocontainers:
  trimmomatic:
    quayurl: "quay.io/biocontainers/trimmomatic"
    version: '0.36--5"
    use_local: false
```

## Running Taco

To run taco, pass it three arguments on the command line:

* Name of the workflow
* Relative path to workflow configuration file
* Relative path to workflow parameters file

Both arguments should be the path to a JSON file
(absolute or relative) and exclude the JSON suffix.

### Running an Example

To run the two JSON files in the example above,
which are contained in the `goodies/` directory 
and which are the first steps in the taxonomic classification 
workflow, we would run:

```text
$ ./taco taxonomic_classification goodies/test-conf.json goodies/test-params.json
```

(The `.json` extension can be included or excluded.)

To do a dry run only, add the `-n` or `--dry-run` flag:

```text
$ ./taco -n taxonomic_classification goodies/test-conf goodies/test-params
```

This will run the `pull_biocontainers` rule.

## Listing Available Actions

### Listing Workflows

You can list available taco workflows
using the `taco ls` command with no 
additional arguments:

```text
$ ./taco ls
```

### Listing Workflow Rules

(Not available)

You can list all of the rules available 
for a given workflow by running `taco ls <workflow-name>`.
For example:

```text
$ ./taco ls read_filtering
```

