# Quick Start

The basic idea behind taco is to 
pass it an action and modify basic
behavior with command line flags.

```
$ ./taco <action> --arguments
```

In this section we'll get started
with a simple workflow to illustrate
how to use taco.


## Workflow Repository

To create a new set of workflows, create a new repository.
To illustrate how to run taco, we will use a single workflow 
with two steps.

Here is the repository layout for our simple example:

```
taco-simple/

        rules/
            my_simple_workflow/
                Snakefile
                step1.rule
                workflow_A.settings

        workflow-config/
            configA.json
            configB.json

        workflow-params/
            paramsA.json
            paramsB.json
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
verb on the command line. For example:

```
$ taco read_filtering <workflow-config-file> <workflow-params-file>
```

will load the Snakefile in `rules/read_filtering/` 
and will make avaiable all read filtering rules.


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

**`goodies/test-conf.json`:**

```text
{
    "workflow_targets" : ["pull_biocontainers"]
}
``` 

### Example File-Based Workflow Configuration File

Here is a simple example of a workflow configuration file
that runs rules based on filename targets (in this example,
the output of a trimming process):

**`goodies/test-conf.json`:**

```text
{
    "workflow_targets" : ["XXXXXX_trim5_1.fq.gz",
                          "XXXXXX_trim5_2.fq.gz"]
}
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

```text
{
    '<workflow-name>' : {
        '<rule-name>' : {
            '<param-name>' : <param-value>,
            ...
        }
    }
}
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

**`goodies/test-params.json`:**

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

