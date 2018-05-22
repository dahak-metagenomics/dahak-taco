## General Usage

The basic idea behind `taco` is to pass it a command verb:

```
$ taco <verb>
```

and modify the behavior with command line flags:

```
$ taco <verb> [--FLAGS]
```

Workflows are defined in their own repositories using specially-structured
Snakemake rules. These keep the rules general enough to be usable by taco
and usable by others.

See [taco-simple](https://github.com/dahak-metagenomics/taco-simple) for
an example.


## Workflow Usage

The main purpose of taco is to run workflows. 

A taco workflow is a repository that defines one or more 
taco workflows using a specified directory structure.
Each workflow is a subdirectory in the `rules/` directory.

The taco command line tool is run from the taco workflow
repository using the verb-with-flags pattern. 


### Listing Workflows

Before you run a workflow, you probably want to list the 
available workflows. For that, use the `ls` verb:

```
$ taco ls 
```

Optionally, pass it the name of a workflow to 
list all rules in the specified workflow:

```
$ taco ls [<workflow>]
```

To run a workflow, the verb should be the name of the workflow.


### Running Workflows

For example, in the [taco-simple](https://github.com/dahak-megatenomics/taco-simple)
repository, we have the following workflow directory layout:

```
taco-simple/

        # Run taco from here

        rules/
            workflow1/
                Snakefile
                hello.rule
                time.rule
                goodbye.rule
                ...

        README.md
        ...
```

To run this workflow, we would run `taco workflow1` from inside 
the `taco-simple/` directory.

The user writes Snakemake workflows to generalize them and keep them
usable by taco. taco will read each workflow and determine which rules
exist, and decide which rules to run for the user.

Remember, you can always get help by running:

```
$ taco --help
```


## Workflow Configuration and Parameter Files

A **workflow configuration file** specifies details about 
which rules and which workflows to run.

The configuration file is where you tell taco what files
you want to produce.

A **workflow parameters file** specifies parameters to 
set for each step of the workflow, and are often broken
up by workflow step.

The parameters file is where you tell taco how you want
your files to be produced.

Both workflow configuration and workflow parameter files
must be in either JSON or YAML format.


### Method 1: Infer Config and Param Files

The first method to specify your workflow configuration
and parameter files is to let taco infer their location.
This requires the following be true:

* There is one and only one file with `config` or 
    `configuration` in the name that is either a 
    JSON file or a YAML file

* There is one and only one file with `params` or 
    `parameters` in the name that is either a 
    JSON file or a YAML file

Pass a directory containing your workflow config
and params files to taco and it will take care of
the rest:

```
$ taco workflow1 my-workflow-files
```


### Method 2: Be Explicit

The second option to specify workflow configuration
and parameter files is to be explicit using command 
line flags. Specifically, use the `--config` 
and `--params` flags:

```
$ taco workflow1 --config=my-workflow-files/config.yaml --params=my-workflow-files/params.yaml
```


## Paths

By default, `taco` will create a working directory 
called `data/` in your current working directory,
and it will put all generated files in that directory.

You can change this location using the `--prefix` 
command line option. For example, to make a big mess
in the current directory, you could leave prefix empty
and run taco like this:

```
$ taco --prefix= ...
```

You can specify relative paths:

```
$ taco --prefix=my-workflow-scratch ...
```

or absolute paths:

```
taco --prefix=/tmp/my-workflow-scratch ...
```

