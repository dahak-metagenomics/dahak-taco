# Rule: `kaiju2krona`

Convert kaiju results to krona results,
and generate a report.

TODO: use `kaijukrona_output` as an example of the "take care of all the details" approach.

## Simple workflow configuration

Simple workflow configuration:

```
$ cat kaiju2krona.json
{
    'workflow_target' : 'kaiju2krona'
}

Run the workflow:

```
$ ./taco -d kaiju2krona # dry run

$ ./taco kaiju2krona 
```

## Override parameters example

Override parameters examples:

(Note: kaiju2krona does not have any parameters itself,
but utilizes kaiju parameters.)

## Details

This rule is defined in `rules/taxonomic_classification/kaiju2krona.rule`


-----


# Rule: `kaiju2kronasummary`

Convert kaiju results to krona results,
and generate a report.

## Simple workflow configuration

Simple workflow configuration:

```
$ cat kaiju2kronasummary.json
{
    'workflow_target' : 'kaiju2kronasummary'
}

Run the workflow:

```
$ ./taco -d kaiju2kronasummary # dry run

$ ./taco kaiju2kronasummary
```

## Override parameters example

Override parameters examples:

(Note: kaiju2kronasummary does not have any parameters itself,
but utilizes kaiju parameters.)

## Details

This rule is defined in `rules/taxonomic_classification/kaiju2krona.rule`

