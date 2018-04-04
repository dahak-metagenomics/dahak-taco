# Rule: `rule_name`

Visualize the results of the
full and filtered taxonomic
classifications using krona.

TODO: No parameters for krona visualization are implemented at this time.

## Simple workflow configuration

Simple workflow configuration:

```
$ cat krona-viz.json
{
    'workflow_target' : 'visualize_krona'
}
```

Run the workflow:

```
$ ./taco -n krona-viz krona-viz-params # dry run

$ ./taco krona-viz krona-viz-params
```

## Override parameters example

Override parameters example:

```
$ cat krona-viz-params.json
{
    'biocontainers' : {
        'kaiju' : {
            'version' : '1.5.0--pl5.22.0_0'
        }
    }
}

$ ./taco krona-viz krona-viz-params
```

## Details

This rule is defined in `rules/taxonomic_classification/krona_visualization.rule`

