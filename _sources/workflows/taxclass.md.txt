# Taxonomic Classification Walkthrough

This walkthrough documents the taxonomic classification workflow.

## List of Rules

To see available rules, run:

```
$ ./taco ls
```

TODO: implement this:

```
$ ./taco ls             # list available workflows
$ ./taco ls readfilt    # list available rules in workflow readfilt
```

Add the rule you want to run to the workflow configuration file.

A list of rules is given below.

Note that the readme files mentioned here 
are located in the same directory as the 
.rule and .settings files used by Snakemake,
and share a filename with the rule they document.

```text
pull_biocontainers

    Pull the required versions of containers from quay.io.

    See biocontainers.md

download_sourmash_sbts

    Download the sourmash SBTs from spacegraphcats.

    See sourmash_sbt.md

unpack_sourmash_sbts

    Unpack the sourmash SBTs from spacegraphcats.

    See sourmash_sbt.md

calculate_signatures

    Calculate signatures from trimmed data using sourmash.

    See calculate_signatures.md

download_trimmed_data

    Download the trimmed data from OSF.
    The trimmed data parameters
    consist of a dictionary of
    `*.fq.gz` files and corresponding URLs.

    See trimmed_data.md

unpack_kaiju

    Download and unpack the kaiju database.
    This is a large file and will take approx. 15-30 minutes.

    See kaiju.md

run_kaiju

    Run kaiju after downloading and unpacking the kaiju database.

    See kaiju.md

kaiju2krona

    Convert kaiju results to krona results,
    and generate a report.

    See kaiju2krona.md

kaiju2kronasummary

    Convert kaiju results to krona results,
    and generate a report.

    See kaiju2krona.md

filter_taxa_total

    Filter out taxa with low abundances by obtaining genera that
    comprise at least {pct} percent of the total reads
    (default: 1%)

    See filter_taxa.md

filter_taxa_class

    For comparison, take the genera that comprise
    at least {pct} percent of all of the classified reads
    (default: 1%)

    See filter_taxa.md

visualize_krona

    Visualize the results of the
    full and filtered taxonomic
    classifications using krona.

    See krona_visualization.md
```    

## List of Rule Files

```
rules/
    dahak/
        biocontainers.rule
        calculate_signatures.rule
        filter_taxa.rule
        kaiju.rule
        kaiju2krona.rule
        krona_visualization.rule
        sourmash_sbt.rule
        trimmed_data.rule
```


