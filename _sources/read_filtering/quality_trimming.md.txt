# Rule: `quality_trimming`

Trim reads from the sequencer by dropping low-quality reads.

## Simple workflow configuration

The trimming rule takes two .fq.gz files
and an adapter file as inputs,
and outputs two trimmed .fq.gz files
and two "se" files.

This rule is not generally run on its own,
but is run as part of the post-trimming
quality assessment.

## Override parameters example

Configuration parameters for the `read_trimming`
workflow are contained in a parameters dictionary
stored under the `read_trimming` key:

```
config_default = {
    'read_trimming' : {
        ...
    }
}
```

(See below for more detailed example.)

The principal role of the `quality_trimming` rule 
is to perform trimming based on a threshold 
minimum quality required for each read.

The two most important configuration parameters
are `pre_trimming_pattern` and `post_trimming_pattern`,
which determine the forms of the input and output file names
with wildcards.

Example from `read_filtering.settings`:

```
config_default = {
    ...

    'read_filtering' : {
        ...

        'read_patterns' : {
            'pre_trimming_pattern'  : '{sample}_{direction}.fq.gz',
            'post_trimming_pattern' : '{sample}_trim{qual}_{direction}.fq.gz'
        }
    }
}
```

These can be set to match the format of the data files 
specified in the related parameter, `read_files`:

```
config_default = {
    ...

    'read_filtering' : {
        ...

        'read_files' : {
            'XXXXXX_1.fq.gz' : 'https://files.osf.io/v1/resources/dm938/providers/osfstorage/59f0f9156c613b026430dbc7',
            'XXXXXX_2.fq.gz' : 'https://files.osf.io/v1/resources/dm938/providers/osfstorage/59f0fc7fb83f69026076be47'
        }
    }
}
```

## Details

This rule is defined in `rules/read_filtering/quality_trimming.rule`

