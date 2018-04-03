# Rule: `calculate_signatures`

Calculate signatures from trimmed data using sourmash.

## Simple workflow configuration

Simple workflow configuration:

```
$ cat calculate-signatures-workflow.json
{
    'workflow_target' : 'calculate_signatures'
}
```

Run the workflow:

```
$ ./taco -n calculate-signatures-workflow calculate-signatures-params # dry run

$ ./taco calculate-signatures-workflow calculate-signatures-params
```

## Override parameters example

Override parameters examples:

**Example 1:** Change the name of the forward and reverse read files.

```
$ cat calc-sigs-params.json
{
    "reads" : {
        "fq_fwd" : "{base}_1.trim{ntrim}.fq.gz",
        "fq_rev" : "{base}_2.trim{ntrim}.fq.gz"
    }
}

$ cat calc-sigs.json
{
    "workflow_target" : "calculate_signatures"
}

$ ./taco -n calc-sigs calc-sigs-params # dry run

$ ./taco calc-sigs calc-sigs-params
```

**Example 2:** Change the k values used to calculate signatures.

```
$ cat calc-sigs-params.json
{
    "calculate_signatures" : {
        "kvalues" : [21, 31, 51, 101]
    }
}

$ cat calc-sigs.json
{
    "workflow_target" : "calculate_signatures"
}

$ ./taco -n calc-sigs calc-sigs-params # dry run

$ ./taco calc-sigs calc-sigs-params
```

**Example 3:** Change the sequence and merge file naming schema.

```
$ cat calc-sigs-params.json
{
    "calculate_signatures" : {
        "sig_name" : "{base}.trim{ntrim}.scaled{scale}.k{kvalues_fname}.sig"
    }
}
```

NOTE: `kvalues_fname` is a variable created when the rule is run,
and is the result of `"_".join(config['calculate_signatures']['kvalues'])`.

TODO: improve the abstraction.

**Example 4:** Implement all three of the above parameter changes.

```
$ cat calc-sigs-params.json
{
    "reads" : {
        "fq_fwd" : "{base}_1.trim{ntrim}.fq.gz",
        "fq_rev" : "{base}_2.trim{ntrim}.fq.gz"
    },
    "calculate_signatures" : {
        "kvalues" : [21, 31, 51, 101],
        "sig_name" : "{base}.trim{ntrim}.scaled{scale}.k{kvalues_fname}.sig"
    }
}

$ cat calc-sigs.json
{
    "workflow_target" : "calculate_signatures"
}

$ ./taco -n calc-sigs calc-sigs-params # dry run

$ ./taco calc-sigs calc-sigs-params
```

## Details

This rule is defined in `rules/dahak/calculate_signatures.rule`.

This rule includes `reads.settings`, `biocontainers.settings`, `calculate_signatures.settings`.

