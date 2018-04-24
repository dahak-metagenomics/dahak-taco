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

[Quickstart](Quickstart.md)


## Workflow Walkthroughs

(in progress)

taco is a lightweight wrapper around Snakemake tasks.
Kind of like a corn tortilla.

In the quickstart, we showed how to create a repository
for a set of workflows. Below, we link to repositories
with useful workflows and walkthroughs.

[AWS Setup](SetupAWS.md)

[Read Filtering Walkthrough](https://dahak-metagenomics.github.io/taco-read-filtering)


## Configuration and Parameter Sets

(in progress)

Individual configuration files or parameter sets
are workflow-dependent, and are defined or included
in the repository that defines that workflow.

The following are some example taco workflows
with configuration and parameter sets included:

* [taco-simple](https://github.com/dahak-metagenomics/taco-simple) - illustrates
    a simple workflow that prints messages
* [taco-read-filtering](https://github.com/dahak-metagenomics/taco-read-filtering) - illustrates
    a read filtering workflow.
* [taco-taxonomic-classification](https://github.com/dahak-metagenomics/taco-taxonomic-classification) - illustrates
    a taxonomic classification workflow.


## For Developers

(in progress)

Documentation on these pages describe how taco works
so that you can modify it to suit your needs. 

Currently covered are snakemake rules and defining 
new workflows.

[Snakemake Rules](SnakemakeRules.md)

[Workflows](Workflows.md)

