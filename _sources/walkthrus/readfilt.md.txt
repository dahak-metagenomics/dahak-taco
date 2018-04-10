# Read Filtering Walkthrough

This walkthrough covers a read filtering workflow. 

In this document we will:

* Download raw sequence data from OSF data store (wget).

* Assess the quality of the pre-filtered reads (fastqc)

* Trim and filter the reads based on a quality threshold (trimmomatic)

* Assess the quality of the post-filtered reads (fastqc)

This workflow specifically covers the use of taco.
See the [walkthroughs dir of the dahak repo](https://github.com/dahak-metagenomics/dahak/tree/master/workflows/read_filtering)
for the original shell-based walkthrough.

## Setup

This node assumes you have the following software:

* Python
* Conda
* Snakemake
* Singularity

See [INSTALLING](/INSTALLING.md) for more info.

If you do not have an environment set up, the 
[Worker Node Setup Walkthrough](setup.md)
covers setting up a worker node on AWS.

## Clone The Repo

Start by cloning a copy of dahak-taco:

```
$ git clone https://github.com/dahak-metagenomics/dahak-taco.git
$ cd dahak-taco/
```

As mentioned in [INSTALLING](/INSTALLING.md),
there is nothing to install for taco itself.

## Start the Workflow

For the read filtering walkthrough we will be downloading
two `*.fq.gz` files, assessing their quality,
and trimming them based on the quality of the reads.

The workflow has four steps:

* Download the data
* Assess the quality before trimming
* Trim the data
* Assess the quality after trimming

### Step 1: Rule: Download the Data

Our three required inputs are:

* Workflow name (`read_filtering`)
* Workflow configuration file (in `goodies/readfilt1config.json`)
* Workflow parameters file (in `goodies/readfilt1params.json`)

Here is the workflow configuration file we will use.
The workflow targets it specifies are two files with 
unprocessed sequence reads.

(These files are the inputs to the rest of the 
read filtering workflow.)

```
$ cat goodies/readfilt1config.json
{
    "short_description": "Read Filtering Walkthrough 1 - Configuration",
    "workflow_targets" : ["data/SRR606249_1.fq.gz",
                          "data/SRR606249_2.fq.gz"]
}
```

Next, we have our workflow parameters file.
This parameters file should define any parameters
used for the single step we're executing.
In our case, we have to tell Snakemake 
where to download the read files.
This parameters file defines a long list of files,
but rules are defined on a file-by-file basis
so we only downlod the files we need:

```
$ cat goodies/readfilt1params.json
{
    "short_description": "Read Filtering Walkthrough 1 Parameters",
    "read_filtering" : {
        "read_patterns" : {
            "pre_trimming_pattern"  : "{sample}_{direction}.fq.gz",
        },
        "read_files" : {
            "SRR606249_1.fq.gz" :           "files.osf.io/v1/resources/dm938/providers/osfstorage/59f0f9156c613b026430dbc7",
            "SRR606249_2.fq.gz" :           "files.osf.io/v1/resources/dm938/providers/osfstorage/59f0fc7fb83f69026076be47",
            "SRR606249_subset10_1.fq.gz" :  "files.osf.io/v1/resources/dm938/providers/osfstorage/59f10134b83f69026377611b",
            "SRR606249_subset10_2.fq.gz" :  "files.osf.io/v1/resources/dm938/providers/osfstorage/59f101f26c613b026330e53a",
            "SRR606249_subset25_1.fq.gz" :  "files.osf.io/v1/resources/dm938/providers/osfstorage/59f1039a594d900263120c38",
            "SRR606249_subset25_2.fq.gz" :  "files.osf.io/v1/resources/dm938/providers/osfstorage/59f104ed594d90026411f486",
            "SRR606249_subset50_1.fq.gz" :  "files.osf.io/v1/resources/dm938/providers/osfstorage/59f1082d6c613b026430e5cf",
            "SRR606249_subset50_2.fq.gz" :  "files.osf.io/v1/resources/dm938/providers/osfstorage/59f10ac6594d900262123e77"
        }
    }
}
```

Both of these JSON files are contained in the 
`goodies/` directory of the repo.

The `read_patterns` parameter is optional and the
default value is shown here. This pattern is used
to create the download wildcard rule, so the files 
that make up the `read_files` keys must match that 
pattern or they will not be downloadable.

To run the workflow defined by this workflow,
config file, and parameters file, run taco as follows:

Dry run first with the `-n` flag:

```
$ ./taco -n read_filtering \
    goodies/readfilt1config.json \
    goodies/readfilt1params.json
```

Then the real deal:

```
$ ./taco -n read_filtering \
    goodies/readfilt1config.json \
    goodies/readfilt1params.json
```


### Step 2: Rule: Pre-Trim Quality Assessment

The second step uses `fastq` to assess the 
quality of the sequencer reads before any
trimming occurs.

The file suffix for files whose quality has been
assessed by fastqc is specified in the config file,
or can be left as the default `_fastqc`.

Here is the config file for the second step,
which is the pre-trim quality assessment.

```
$ cat goodies/readfilt2config.json
{
    "short_description": "Read Filtering Walkthrough 2 - Pre-Trim Quality Assessment - Configuration",
    "workflow_targets" : ["data/SRR606249_1_fastqc.zip",
                          "data/SRR606249_2_fastqc.zip"]
}
```

While the second step of the workflow should use a 
second config file, the parameters file should 
include all the parameters from the prior step,
since Snakemake will still be running those workflow steps.

Here is the parameters file:

```
$ cat goodies/readfilt2params.json
{
    "short_description": "Read Filtering Walkthrough 2 - Pre-Trim Quality Assessment - Parameters",
    "read_filtering" : {
        "quality_assessment" : {
            "fastqc_suffix" : "_fastqc"
        },
        "read_patterns" : {
            "pre_trimming_pattern"  : "{sample}_{direction}.fq.gz",
        },
        "read_files" : {
            ...
        }
    }
}
```

To run the workflow defined by this workflow,
config file, and parameters file, run taco as follows:

Dry run first with the `-n` flag:

```
$ ./taco -n read_filtering \
    goodies/readfilt2config.json \
    goodies/readfilt2params.json
```

Then the real deal:

```
$ ./taco read_filtering \
    goodies/readfilt2config.json \
    goodies/readfilt2params.json
```



### Step 3: Rule: Trim Reads

Step 3 uses trimmomatic to trim the reads based on quality.

This step requires us to output reads to a new trimmed filename.
We have to change the pre-trimming filename pattern,
which is too general: `{sample}_{direction}.fq.gz`
will match nearly every `post_trimming_pattern` we choose.

We should change the pattern parameters to include 
either a prefix or a suffix:

```
    "pre_trimming_pattern"  :  "{sample}_{direction}_reads.fq.gz"
    "post_trimming_pattern"  : "{sample}_{direction}_trim{qual}.fq.gz"
```

Because we changed the target filenames for steps 1 and 2,
this will cause steps 1 and 2 to re-run.

This step also requires us to add an adapter file for 
trimmomatic to use. This works like the read files: 
we specify a target filename and a URL for the data.

The following step 3 config file explicitly specifies
targets for steps 1 and 2, in addition to step 3:

```
$ cat goodies/readfilt3config.json
{
    "short_description": "Read Filtering Walkthrough 2 - Pre-Trim Quality Assessment - Configuration",
    "workflow_targets" : ["data/SRR606249_1_reads.fq.gz",
                          "data/SRR606249_2_reads.fq.gz",
                          "data/SRR606249_1_reads_fastqc.zip",
                          "data/SRR606249_2_reads_fastqc.zip",
                          "data/TruSeq2-PE.fa",
                          "data/SRR606249_1_trim2.fq.gz",
                          "data/SRR606249_2_trim2.fq.gz"]
}
```

The parameters file contains updated parameters
(most options are not required, but this illustrates
what controls the user has over file names):

```
{
    "short_description": "Read Filtering Walkthrough 3 - Trimming - Parameters",
    "read_filtering" : {
        "quality_assessment" : {
            "fastqc_suffix" : "_fastqc"
        },
        "quality_trimming" : {
            "trim_suffix" : "_se"
        },
        "read_patterns" : {
            "pre_trimming_pattern"  : "{sample}_{direction}_reads.fq.gz",
            "post_trimming_pattern" : "{sample}_{direction}_trim{qual}.fq.gz",
            "adapter_pattern" :       "{adapter}.fa"
        },
        "read_files" : {
            ...
        },
        "adapter_files" : {
            "TruSeq2-PE.fa" : "http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-semi-2015-03-04/TruSeq2-PE.fa"
        }
```

Dry run first with the `-n` flag:

```
$ ./taco -n read_filtering \
    goodies/readfilt3config.json \
    goodies/readfilt3params.json
```

Then the real deal:

```
$ ./taco read_filtering \
    goodies/readfilt3config.json \
    goodies/readfilt3params.json
```


### Step 4: Rule: Post-Trim Quality Assessment

