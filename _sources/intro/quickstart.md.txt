# Quick Start

Run the taco command line tool like this:

```
$ ./taco <arguments>
```

dahak-taco requires two inputs from the user:

* **Workflow configuration file:** specifies the workflow rules
    to run and the names of the target input and output files.
    These rules are defined in `rules/dahak/*.rules`.

* **Workflow parameters file (optional):** specifies values for 
    workflow parameters. Parameters set in this
    parameters file will override parameters set
    in the `rules/dahak/*.settings` files.

These are both JSON files.

## Workflow Configuration File

The workflow configuration file 
must specify a key `workflow_target`.

The value must be a valid Snakemake rule
defined in one of the rule files at `rules/dahak/*.rules`.

The form of the workflow configuration file 
for running rules without file targets is:

```text
{
    "workflow_target" : <name of Snakemake rule>
}
```

and the form for using a filename-based target is:

```text
{
    "workflow_target" : <name of output file target>
}
```

You can also specify a list of workflow targets.
For example:

```text
{
    "workflow_targets" : <list of Snakemake rules>
}
```

or,


```text
{
    "workflow_targets" : <list of output file targets>
}
```

### Example Rule-Based Workflow Configuration File

Here is a simple example of a workflow configuration file
for running a rule that has no file targets (pulling containers).
This rule specifies the workflow target by specifying the 
rule name:

**`test-workflow.json`:**

```text
{
    "workflow_target" : "pull_biocontainers"
}
``` 

### Example File-Based Workflow Configuration File

Here is a simple example of a workflow configuration file
that runs rules based on filename targets:

**`test-workflow.json`:**

```text
{
    "workflow_targets" : ["XXXXXX_trim5_1.fq.gz",
                          "XXXXXX_trim5_2.fq..gz"]
}
``` 

## Workflow Parameters File

The workflow parameters control various parameters
that are used by the programs and containers run
by the Snakemake rules.

There is a configuration parameters dictionary 
common to all Snakemake rules 




contains parameter values
to control the workflow. These parameter values will override
default parameter values set in the `rules/` directory.

Parameters are any variables used in the Snakemake rules.
All Snakemake parameters are contained in a config dictionary
that contains dictionaries of parameters, typically grouped 
by workflow rule, application, or group of applications.

The default values 
All rules are set in `*.settings` files in the `rules/` directory.

Workflow parameters are 
The form of the workflow parameters JSON file is:

```text
{
    'workflow_name' : {
        'workflow_step' : {
            'param_name' : <param-value>,
            ...
        }
    }
}
```

Most parameters are listed under the app that uses them.
Some parameters are common to several tasks,
so they are assigned a key with a group name, like "reads".

### Example Workflow Parameters File

The following example parameters file adjusts the parameters for 
the rule to update biocontainers.

This is a simple parameter file overriding a single parameter,
the version of sourmash being utilized.

This overrides the default biocontainers setting of 
sourmash version `2.0.0a3--py36_0`, set in 
`rules/dahak/biocontainers.settings`.

**`test-params.json`:**

```text
{
    "biocontainers" : {
        "sourmash" : "2.0.0a2--py36_0"
    }
}
```

## Running Taco

To run taco, pass it two arguments on the command line.
The first argument is the name of the workflow,
the second argument is the name of the paramters file.

Both arguments should be the path to a JSON file
(absolute or relative) and exclude the JSON suffix.

For example, to run the two JSON files in the example above,

```text
$ ./taco test-workflow test-params
```

To run workflows contained in a `configs/` directory, run:

```text
$ ./taco configs/test-workflow configs/test-params
```

To do a dry run only, add the `-n` or `--dry-run` flag:

```text
$ ./taco -n test-workflow test-params
```

## Running the Example Workflow

Following the example above, we run the example workflow
by specifying the test workflow configuration file 
and the test workflow parameters file:

```text
$ ./taco test-workflow test-params
```

(Note that a parameters file is optional.)

This will run the pull biocontainers rule.

## Listing Available Actions

### Listing Workflows

You can list available taco workflows
using the `taco ls` command with no 
additional arguments:

```text
$ ./taco ls
```

### Listing Workflow Rules

You can list all of the rules available 
for a given workflow by running `taco ls <workflow-name>`.
For example:

```text
$ ./taco 

