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

We will perform each step separatel,
then all steps together, to illustrate.

### Step 1: Download the Data

Our three required inputs are:

* Workflow name (`read_filtering`)
* Workflow configuration file
* Workflow parameters file

Here is the workflow configuration file we will use.
The workflow targets it specifies are two files with 
unprocessed sequence reads.

(These files are the inputs to the rest of the 
read filtering workflow.)

```
$ cat read_filtering_walkthru_1_config.json
{
    "workflow_targets" : ["data/SRR606249_1.fq.gz",
                          "data/SRR606249_2.fq.gz"]
}
```

Next, we have our workflow parameters file.
This parameters file should define any parameters
used for the single step we're executing.
In our case, we have to tell Snakemake 
where to download the read files:

```
$ cat read_filtering_walkthru_1_params.json
{
    "read_filtering" : {
        "read_files" : {
            "SRR606249_1.fq.gz" : "files.osf.io/v1/resources/dm938/providers/osfstorage/59f0f9156c613b026430dbc7",
            "SRR606249_2.fq.gz" : "files.osf.io/v1/resources/dm938/providers/osfstorage/59f0fc7fb83f69026076be47"
        }
    }
}
```

Both of these JSON files are contained in the 
`goodies/` directory of the repo.

To run the workflow that downloads these two
read files, run taco as follows:

Dry run first with the `-n` flag:

```
$ ./taco -n read_filtering \
    goodies/read_filtering_walkthru_1_config.json \
    goodies/read_filtering_walkthru_1_params.json
```

Then the real deal:

```
$ ./taco -n read_filtering \
    goodies/read_filtering_walkthru_1_config.json \
    goodies/read_filtering_walkthru_1_params.json
```


