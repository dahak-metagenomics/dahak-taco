# dahak-taco documentation

`taco` is an experimental command-line interface
for running [dahak](https://github.com/dahak-metagenomics/dahak)
workflows using Snakemake.

(insert icholy/ttygif here.)


## Getting Started

`taco` is a lightweight wrapper around Snakemake tasks.
Kind of like a corn tortilla.

These sections will cover how to get up and running with `taco`.

[Installation](Installation.md) - how to install `taco`

[Usage](Usage.md) - basic usage of `taco`

[Workflows](Workflows.md) - what are `taco` workflows, 
how do you run them, and what do they include?

[Tests](Tests.md) - how to run `taco` unit tests 


## Workflows

The actual taco workflow is defined using Snakemake rules,
and these files should live in their own repository, separate
from `taco`.

Each repository can define a single workflow, or multiple workflows.

Several example `taco` workflow repositories are available:

* [taco-simple](https://dahak-metagenomics.github.io/taco-simple) - 
    illustrates the implementation of several "hello world" style taco workflows.
* [taco-read-filtering](https://dahak-metagenomics.github.io/taco-read-filtering) - 
    implements a read filtering taco workflow. 
* [taco-taxonomic-classification](https://dahak-metagenomics.github.io/taco-taxonomic-classification) - 
    implements a taxonomic classification taco workflow. 

Each repository provides documentation and a Quick Start guide.

## Cloud Platforms

We include instructions for getting up and running with `taco` on various cloud platforms.
This is a great application of the `taco-simple` workflow.

* [AWS Setup](AWSSetup.md)
* HPC - TBA


## Configuration and Parameter Sets

`taco` takes two input files: a workflow configuration file,
which specifies the workflow targets, and a workflow
parameters file, which specifies parameters to control
the workflow.

Workflow configuration and parameter files are workflow-dependent
and live in workflow repositories.

Individual configuration files or parameter sets
are workflow-dependent, and are defined or included
in the repository that defines that workflow.

For a simple example of how configuration and parameter 
files are used, see the [taco-simple](https://github.com/dahak-metagenomics/taco-simple)
repository, which contains several "hello world" style
`taco` workflows.


## Advanced Topics

For instructions on building, modifying, and improving
the documentation for `taco`, see 
[Documentation](Documentation.md).

If you are interested in creating a new workflow,
see [DevWorkflows.md](DevWorkflows.md). Also see 
the [taco-simple](https://github.com/dahak-metagenomics/taco-simple) 
repository, which illustrates simple "hello world" style 
workflows using `taco` best practices.

For more information about the development workflow,
branches, tags, and the release process, 
see [Development](Development.md).

