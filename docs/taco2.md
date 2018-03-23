# dahak-taco

dahak-taco is an experimental 
command line interface for 
running dahak workflows.

## Installation

dahak-taco is an executable script
that requires Conda, Snakemake,
and (optionally) Singularity to run.

Installation scripts for software needed 
for dahak-taco are in the `scripts/` folder.

## Command-Line Quick Start

To get started with dahak-taco, 
you will need to provide a workflow
configuration file and a parameters file.

The workflow configuration file
will specify what task to perform
on which files. The parameters
file specifies values to use 
for various workflow parameters.

Both files are JSON files.

### Example workflow configuration file

Here is a simple example of a workflow 
configuration file that pulls containers
from a URL (no output filenames involved):

```
{
    "workflow_target" : "pull_biocontainers"
}
```

This is stored in ``my-workflow.son``

### Example parameters file

Here is a simple parameters file that adjusts
the version of one of the containers being
pulled in the workflow task defined above:

```
{
    "biocontainers" : {
        "sourmash" : "2.0.0a2--py36_0"
    }
}
```

This is stored in ``my-params.json``

### Performing a task

To perform the workflow task using 

```
$ ./taco my-workflow my-params
```

### Performing another task

```
$ ./taco another-workflow another-task
```

### Overriding parameters

We implement command line arguments
for the most common parameters,
but full access requires using 
the parameters JSON file.

