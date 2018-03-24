# Taxonomic Classification Walkthrough

Covering taxonomic classification.

See [dahak - taxonomic classification workflow](https://github.com/dahak-metagenomics/dahak/tree/master/workflows/taxonomic_classification).

## Running Taxonomic Classification Workflows

Start by selecting which rule from the workflow you want to run.
Then, check the relevant `.settings` file in the `rules/` directory
to see what parameters you can adjust.

### pull biocontainers

Start with a simple example of a single workflow step
with no input or output files. To run the
`pull_biocontainers` workflow:

```
$ cat pull-biocontainers-workflow.json
{
    "workflow_target" : "pull_biocontainers"
}
```

Now run the workflow (include `-n` to do a dry run):

```
$ ./taco pull-biocontainers-workflow
```

If we wanted to modify any parameters,
we could add configuration paramters
to `pull-biocontainers-params.json`
that match the parameters for this rule.
Note that the rule is defined in 
`rules/dahak/biocontainers.rule`
and the corresponding default settings
are defined in `rules/dahak/biocontainers.settings`.

```
$ cat pull-biocontainers-params.json
{
    'biocontainers' : {
        'sourmash' : {
            'version' : '2.0.0a2--py36_0'
        }
    }
}

```

Now run the workflow, specifying both the workflow
and parameter configuration files on the command line
(include `-n` to do a dry run):

```
$ ./taco pull-biocontainers-workflow pull-biocontainers-params
```

### download/unpack sourmash SBTs

Like the above step, this has no inputs or outputs 
and is not a particularly interesting rule.

This step downloads SBTs containing hashes
from the microbial genomes in the NCBI Databank
and RefSeq databases.

```
$ cat unpack-sbt-workflow.json
{
    "workflow_target" : "unpack_sourmash_sbts"
}

$ ./taco unpack-sbt-workflow
```

This calls the `unpack_sourmash_sbts` rule,
which in turn calls the `download_sourmash_sbts` rule.

### calculate signatures

To run the calculate signatures rule,
the user can specify the target rule 
`calculate_signatures` without any parameters
to use the default values:

```
$ cat calc-sigs.json
{
    "workflow_target" : "calculate_signatures"
}

$ ./taco calc-sigs
```

However, this workflow has a number of additional options 
that users can set.

(TODO: More on changing parameter values...)

## Rules

### List of Rules

```
pull_biocontainers
    
    - Pull the latest version of sourmash, kaiju, and krona
    - Version numbers are set in biocontainers.settings
    - To call this rule, ask for the file .pulled_containers
    
download_sourmash_sbts
    
    Downoad the sourmash SBTs from spacegraphcats

    To call this rule, request sourmash SBT json file for the specified database.
    
unpack_sourmash_sbts
    
    Unpack the sourmash SBTs
    
calculate_signatures
    
    Calculate signatures from trimmed data using sourmash
    
download_trimmed_data
    
    Download the trimmed data from OSF

    To call this rule, request the files listed in trimmed_data.dat
    
unpack_kaiju
    
    Download and unpack the kaiju database.
    
run_kaiju
    
    Run kaiju
    
kaiju2krona
    
    Convert kaiju results to krona results,
    and generate a report.
    
kaiju2kronasummary
    
    Convert kaiju results to krona results,
    and generate a report.
    
filter_taxa_total
    
    Filter out taxa with low abundances by obtaining genera that
    comprise at least {pct} percent of the total reads
    (default: 1%)
    
filter_taxa_class
    
    For comparison, take the genera that comprise
    at least {pct} percent of all of the classified reads
    (default: 1%)
    
visualize_krona
    
    Visualize the results of the
    full and filtered taxonomic
    classifications using krona.
```    

### List of Rule Files

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

