# Rule: `download_sourmash_sbts`

Download the sourmash SBTs from spacegraphcats.

## Simple workflow configuration

This rule should be called by the `unpack_sourmash_sbts` 
rule and should not be called directly.

## Details

This rule is defined in `rules/taxonomic_classification/sourmash_sbt.rule`.


-------


# Rule: `unpack_sourmash_sbts`

Download and unpack the sourmash SBTs from spacegraphcats.

The SBTs contain hashes from the microbial genomes
in the NCBI Databank and RefSeq databases.

## Simple workflow configuration

To run with default parameters:

```
$ cat download-sbt-workflow.json
{
    "workflow_target" : "download_sourmash_sbts"
}

$ ./taco -n unpack-sbt-workflow # dry run

$ ./taco download-sbt-workflow
```


## Override parameters example

We can modify parameters for the calculate signatures workflow.

If we examine the `calculate_signatures` rule file at 
`rules/taxonomic_classification/calculate_signatures.rule` we see that three
settings files are used:

* read group settings (group parameters for any task involving reading sequences)
* calculate signature rule settings (rule-specific settings for calculating signatures)
* biocontainer app settings (container URLs and versions)

We can override any parameters in those files 
to change how the `calculate_signatures` workflow
works.



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

$ ./taco calc-sigs calc-sigs-params
```



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

$ ./taco calc-sigs calc-sigs-params
```

## Details

This rule is defined in `rules/taxonomic_classification/sourmash_sbt.rule`.

