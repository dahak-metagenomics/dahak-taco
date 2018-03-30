# Rule: `pull_biocontainers`

Pull the required versions of containers from quay.io.

## Simple workflow configuration

Simple workflow configuration file:

```
$ cat pull-biocontainers-workflow.json
{
    'workflow_target' : 'pull_biocontainers'
}
```

Run the workflow:

```
$ ./taco -n pull-biocontainers-workflow # dry run

$ ./taco pull-biocontainers-workflow
```

## Override parameters example

Override parameters example:

```
$ cat pull-biocontainers-params.json
{
    'biocontainers' : {
        'sourmash' : {
            'version' : '2.0.0a2--py36_0'
        }
    }
}

$ ./taco pull-biocontainers-workflow pull-biocontainers-params
```

## Details

This rule is defined in `rules/dahak/biocontainers.rule`.

This rule includes `biocontainers.settings`.

