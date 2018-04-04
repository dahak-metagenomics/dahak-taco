# Rule: `unpack_kaiju`

Download and unpack the kaiju database.
This is a large file and will take approx. 15-30 minutes.

## Simple workflow configuration

Note: you should probably run the `run_kaiju` rule instead of the `unpack_kaiju` rule.

Simple workflow configuration:

```
$ cat fetch-kaiju.json
{
    'workflow_target' : 'unpack_kaiju'
}
```

Run the workflow:

```
$ ./taco -d fetch-kaiju # dry run

$ ./taco fetch-kaiju 
```

## Override parameters example

Override parameters examples:

```
$ cat fetch-kaiju-params.json
{
    'kaiju' : {
        'dmp1' : 'nodes.dmp',
        'dmp2' : 'names.dmp',
        'fmi'  : 'kaiju_db_nr_euk.fmi',
        'tar'  : 'kaiju_index_nr_euk.tgz',
        'url'  : 'http://kaiju.binf.ku.dk/database',
        'out'  : '{base}.kaiju_output.trim{ntrim}.out'
    }
}

$ cat fetch-kaiju.json
{
    'workflow_target' : 'unpack_kaiju'
}

$ ./taco -d fetch-kaiju fetch-kaiju-params # dry run

$ ./taco fetch-kaiju fetch-kaiju-params
```

## Details

This rule is defined in `rules/dahak/kaiju.rule`.

This rule includes `reads.settings`, `biocontainers.settings`, `kaiju.settings`.





# Rule: `run_kaiju`

Run kaiju after downloading and unpacking the kaiju database. 

## Simple workflow configuration

Simple workflow configuration:

```
$ cat run-kaiju.json
{
    'workflow_target' : 'run_kaiju'
}
```

Run the workflow:

```
$ ./taco -d run-kaiju # dry run

$ ./taco run-kaiju 
```

## Override parameters example

Override parameters examples:

```
$ cat run-kaiju-params.json
{
    'kaiju' : {
        'dmp1' : 'nodes.dmp',
        'dmp2' : 'names.dmp',
        'fmi'  : 'kaiju_db_nr_euk.fmi',
        'tar'  : 'kaiju_index_nr_euk.tgz',
        'url'  : 'http://kaiju.binf.ku.dk/database',
        'out'  : '{base}.kaiju_output.trim{ntrim}.out'
    }
}
```

## Details

This rule is defined in `rules/dahak/kaiju.rule`.

This rule includes `reads.settings`, `biocontainers.settings`, `kaiju.settings`.


