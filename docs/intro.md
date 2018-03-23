# Introduction: dahak-taco

dahak-taco is an experimental 
command line interface for 
running dahak workflows.

## Installation

dahak-taco is an executable script
that requires Conda, Snakemake,
and (optionally) Singularity to run.

Installation scripts for software needed 
for dahak-taco are in the `scripts/` folder:

```
$ ls scripts/
install_pyenv.py
install_singularity.py
install_snakemake.py
```

## Quick Start

To use dahak-taco, you need two things:

* Workflow configuration file - specifies the workflow rules
    to run and the names of the target input and output files.
* Workflow parameters file - specifies values for 
    workflow parameters. Parmaeters set in this
    parameters file will override parameters set
    in the `rules/dahak/*.settings` files.

These files are both JSON files.

The configuration file must specify
a value for the key `workflow_target`, 
and the value must be a defined
Snakemake rule.

### Example workflow configuration file

Here is a simple example of a workflow 
configuration file that pulls containers
from a URL (no output filenames involved):::

```
{
    "workflow_target" : "pull_biocontainers"
}
``` 

This is stored in `test-workflow.json`.

### Example parameters file

Here is a simple parameters file that adjusts
the version of one of the containers being
pulled in the workflow task defined above:::

```
{
    "biocontainers" : {
        "sourmash" : "2.0.0a2--py36_0"
    }
}
```

(Note that this overrides the default 
sourmash version of `2.0.0a3--py36_0`
defined in `rules/dahak/biocontainers.settings`.

This is stored in `test-params.json`.

### Run taco

Now that we have our two JSON config files
in `test-workflow.json` and `test-params.json`,
we are ready to run the test workflow.

Start with a dry run using the `-n` flag:

```
./taco -n test-workflow test-params
```

and the real thing:

```
./taco test-workflow test-params
```

This test workflow performs 
docker pull commands, and does 
not require setting any input or 
output files. 

Note that you can also put your 
workflow files in a separate directory,
e.g., in the `configs/` directory:

```
$ ./taco configs/test-workflow.json configs/test-params.json
```

