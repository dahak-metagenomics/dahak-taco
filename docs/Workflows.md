# Workflows

## Workflow Repositories

To create a new workflow or set of workflows, 
create a new repository to hold all the files 
for the workflow.

You will need a `rules/` folder, as well as a folder for
configuration files and parameter files.

The taco tool is then run from that directory, and runs
the workflows defined in that directory.

Here is an example repository layout for 
a repository containing two related workflows:

```
taco-my-awesome-workflow/
        
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

        apples-workflow/
            apples_config.json
            apples_params.json

        bananas-workflow/
            banana_config.json
            banana_params.json

        green-bananas-workflow/
            green_banana_config.json
            green_banana_params.json

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

Each of these components is discussed in more detail below,
but first we cover how to get up and running with an existing
workflow.


## Running a Workflow

When you run `taco` you can specify several verbs.
The `ls` verb will list available workflows, which it 
does by looking for folders in the `rules/` directory
(relative to the current directory where `taco` was run)
that contain Snakemake workflows:

```
taco ls
```

To list rules in a particular workflow, give the name of the 
workflow to the `ls` verb:

```
taco ls <workflow-name>
```

To run the workflow, use the workflow name as the verb:

```
taco <workflow-name> [OPTIONS]
```

When this command is executed, `taco` loads the 
`Snakefile` (and subsequently all workflow rules)
in the `rules/<workflow-name>/` directory.
The Snakefile will first load the user-provided
workflow parameters, then fill in any parameters
the user did not provide with the default values.

`taco` then uses the configuration file provided in 
the options to determine what targets to make,
and from that determines what rules to run.


## Workflow Components

All workflow repositories must include:

* Rules
* Workflow configuration files
* Workflow parameter files
* Documentation

The rules are required to define the workflow,
and the configuration and parameter files are 
required to guide the user on how to use the 
workflow.

Optionally, if your workflow requires it you can
also include:

* Docker images


### Rules

Workflows are defined in a folder called `rules/`.

The `rules/` directory contains one folder per workflow.
Each workflow is defined by `rules/<workflow-name>/Snakefile`,
and workflows should include the following:

* `Snakefile` - this will consist mainly of `include:` statements
* `*.rule` files - these define the Snakemake rules
* `*.settings` files - usually one per workflow, these define default values 
    for all workflow parameters (and also serve as documentation for workflow
    parameter values)

The user should specify the workflow name as the first
verb on the command line, then pass any flags that modify
the workflow behavior. For example:

```
$ taco read_filtering (--config-json|--config-yaml) (--params-json|--params-yaml)
```

(More on the config and params flags below.)

This command will run the Snakemake API with the Snakefile found in `rules/read_filtering` 
(relative to the current directory where `taco` was run). It uses the target specified by 
the user's workflow configuration file to figure out what rules to run, and runs them using
the parameters in the user's parameters file.


### Workflow Configuration File

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

#### Example Rule-Based Workflow Configuration File

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

#### Example File-Based Workflow Configuration File

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

### Workflow Parameters File

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
    "<workflow-name>" : {
        "<rule-name>" : {
            "<param-name>" : <param-value>,
            "<param-list>" : [<value1>, ...],
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

#### Example Workflow Parameters File

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

## Docker and Singularity

### Docker Images

Most taco workflows utilize singularity to run docker containers
as part of the workflows. Docker containers are usually specified
by URL, but if a biocontainer or Dockerhub image is broken, a local
image must be used. 

For this reason, some workflows will include their own
Dockerfiles. This is not recommended, but serves as a temporary fix.

To use a custom docker image in a taco workflow,
add a `docker` directory, and add a subdirectory
for the utility you are adding. For example, if
we are adding a simple alpine widget called `acme_widget`,
we would create `docker/acme_widget/` and add the 
Dockerfile to `docker/acme_widget/Dockerfile`.

We must also set up the configuration files and 
parameters to utilize local docker images.
This is largely workflow dependent, but 
a good pattern to implement this is to include
a configuration dictionary for each application
(such as `acme_widget`) that specifies whether 
to use a dockerhub/quay.io container image 
or a local container image:

```
acme_widget:
  use_local: true
  local: my_acme_widget_image
```

This assumes you ran 

```
docker build -t my_acme_widget_image .
```

in the `docker/acme_widget/Dockerfile` directory.

## Singularity

(Notes on singularity?)

