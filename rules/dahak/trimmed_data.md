# Rule: `download_trimmed_data`

Download the trimmed data from OSF.
The trimmed data parameters 
consist of a dictionary of 
`*.fq.gz` files and corresponding URLs.

## Simple workflow configuration

Simple workflow configuration:

```
$ cat get-trimmed-data.json
{
    'workflow_target' : 'download_trimmed_data'
}
```

Run the workflow:

```
$ ./taco -n get-trimmed-data
```

## Override parameters example

Run the workflow with custom, overriding parameters:

```
$ cat get-trimmed-data.json
{
    'workflow_target' : 'download_trimmed_data'
}

$ cat get-trimmed-data-params.json
{
    'trimmed_data' : {
        'filename.trim1.fq.gz' : <url-for-trim1>,
        'filename.trim2.fq.gz' : <url-for-trim2>
    }
}

$ ./taco -n get-trimmed-data get-trimmed-data-params
```

## Details

This rule is defined in `rules/dahak/trimmed_data.rule`.

This rule includes the files `trimmed_data.settings`.

