# dahak-taco

taco is an experimental command line interface for dahak workflows. 

## Quick Start

Create a workflow configuration JSON file,
which contains rules and filenames,
and a parameters JSon file,
which contains parameter values.

For example, to run the `pull_biocontainers` rule,
define the workflow file:

**`test-workflow.json:`**

```
{
    "workflow_target" : "pull_biocontainers"
}
```

Adjust any parameters in the parameter JSON file
(see the `.settings` files in `rules/` subdirectory):

**`test-params.json:`**

```
{
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

## Documentation

To get started, see the [docs/](/docs/) directory.

