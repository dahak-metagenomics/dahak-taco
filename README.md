# dahak-taco

taco is an experimental command line interface for dahak workflows. 

## Quick Start

Create a workflow configuration JSON file,
which contains rules and filenames,
and a parameters JSon file,
which contains parameter values.

For example, to run the `pull_biocontainers` rule,
define the workflow file:

```
{
    "workflow_target" : "pull_biocontainers"
}
```

$adjust any parameters in the parameter JSON file
(also see `.settings` files in `rules/` subdirectory):

```
config = {
    'biocontainers' : {
        'sourmash' : {
            'version' : '2.0.0a2--py36_0'
        }
    }
}
```

Then run them via taco:

```
./taco test-workflow test-params
```



import snakemake
ModuleNotFoundError: No module named 'snakemake'






