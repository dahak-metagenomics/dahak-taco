# dahak-taco documentation

dahak-taco is an experimental command-line interface
for running dahak workflows using Snakemake.

(insert icholy/ttygif here.)

To get started with taco,
and run your first workflow task,
see the **Getting Started** Section below.

If you're hungry for more dahak workflows,
skip to the **Walkthroughs Section** below.

If you are already up and running 
with taco and are looking for 
information about the rules and their 
parameters, check out the 
**API Section** below.

If you are extending taco by adding new
rules, workflows, or documentation, see 
the **Developers Section**.


## Getting Started

taco is a command line utility that wraps
Snakemake rules to run complex workflows.

These sections will cover what taco is
and get you up and running with your 
first taco workflow.

[Installation and Usage](InstallationUsage.md)

[Quick Start](Quickstart.md)


## Workflows

`taco` is a lightweight wrapper around Snakemake tasks.
Kind of like a corn tortilla.

The actual taco workflow is defined using Snakemake rules,
and these files should live in their own repository seaprate
from dahak-taco.

Each repository can define a single workflow, or multiple workflows.

Several example `taco` workflow repositories are available:

* [taco-simple](https://github.com/dahak-metagenomics/taco-simple) - 
    illustrates the implementation of several "hello world" style taco workflows
* [taco-read-filtering](https://github.com/dahak-metagenomics/taco-read-filtering) - 
    implements a read filtering taco workflow.
* [taco-taxonomic-classification](https://github.com/dahak-metagenomics/taco-taxonomic-classification) - 
    implements a taxonomic classification taco workflow.

## Cloud Platforms

We include instructions for running workflows using `taco` 
on various cloud platforms.

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
the documentation for dahak-taco, see 
[Documentation](Documentation.md).

If you are interested in creating a new workflow,
start with the [taco-simple](https://github.com/dahak-metagenomics/taco-simple) 
repository, which illustrates how to create
rule files to define multiple workflows 
and how to utilize user-provided parameters.

For more information about the development workflow,
branches, tags, and the release process, see [Development](Development.md).

