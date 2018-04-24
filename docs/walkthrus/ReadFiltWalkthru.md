# Read Filtering Walkthrough

This walkthrough covers a read filtering workflow. 

In this document we will:

* Download raw sequence data from OSF data store (wget).

* Assess the quality of the pre-filtered reads (fastqc)

* Trim and filter the reads based on a quality threshold (trimmomatic)

* Assess the quality of the post-filtered reads (fastqc)

* Interleave post-filtered reads (khmer) 

This workflow covers the use of taco to run the workflow.

See the [walkthroughs dir of the dahak repo](https://github.com/dahak-metagenomics/dahak/tree/master/workflows/read_filtering)
for the original shell-based walkthrough.

## Setup

This node assumes you have the following software:

* Python
* Conda
* Snakemake
* Singularity

See [Installing](/intro/Installing.md) for more info.

If you do not have an environment set up, the 
[Worker Node Setup Walkthrough](AWS_Setup.md)
covers setting up a worker node on AWS.

## Clone The Repo

Start by cloning a copy of dahak-taco:

```
$ git clone https://github.com/dahak-metagenomics/dahak-taco.git
$ cd dahak-taco/
```

As mentioned in [Installing](/intro/Installing.md),
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

## Part 1: Download Data

In Part 1 we'll specify a filename as a target
to download read data.

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

```text
$ cat goodies/readfilt1params.json
{
    "short_description": "Read Filtering Walkthrough 1 - Fetching Reads - Parameters",
    "read_filtering" : {
        "read_files" : {
            "SRR606249_1.fq.gz" :           "files.osf.io/v1/resources/dm938/providers/osfstorage/59f0f9156c613b026430dbc7",
            "SRR606249_2.fq.gz" :           "files.osf.io/v1/resources/dm938/providers/osfstorage/59f0fc7fb83f69026076be47",
            "SRR606249_subset10_1.fq.gz" :  "files.osf.io/v1/resources/dm938/providers/osfstorage/59f10134b83f69026377611b",
            "SRR606249_subset10_2.fq.gz" :  "files.osf.io/v1/resources/dm938/providers/osfstorage/59f101f26c613b026330e53a",
            "SRR606249_subset25_1.fq.gz" :  "files.osf.io/v1/resources/dm938/providers/osfstorage/59f1039a594d900263120c38",
            "SRR606249_subset25_2.fq.gz" :  "files.osf.io/v1/resources/dm938/providers/osfstorage/59f104ed594d90026411f486",
            "SRR606249_subset50_1.fq.gz" :  "files.osf.io/v1/resources/dm938/providers/osfstorage/59f1082d6c613b026430e5cf",
            "SRR606249_subset50_2.fq.gz" :  "files.osf.io/v1/resources/dm938/providers/osfstorage/59f10ac6594d900262123e77"
        },
        "read_patterns" : {
            "pre_trimming_pattern"  : "{sample}_{direction}.fq.gz"
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

```text
$ ./taco -n read_filtering \
    goodies/readfilt1config.json \
    goodies/readfilt1params.json
```

Then the real deal:

```text
$ ./taco -n read_filtering \
    goodies/readfilt1config.json \
    goodies/readfilt1params.json
```


### Part 2: Perform Pre-Trim Quality Assessment

In Part 2 we'll perform a pre-trimming quality assessment
by specifying filename targets.

The `fastqc` utility is used to assess the quality
of the sequencer reads before any trimming occurs.

The file suffix for files whose quality has been
assessed by fastqc is specified in the config file,
or can be left as the default `_fastqc`.

Here is the config file for the second step,
which is the pre-trim quality assessment.

```text
$ cat goodies/readfilt2config.json
{
    "short_description": "Read Filtering Walkthrough 1 - Fetching Reads - Configuration",
    "workflow_targets" : ["data/SRR606249_1.fq.gz",
                          "data/SRR606249_2.fq.gz"]
}
```

While the second step of the workflow should use a 
second config file, the parameters file should 
include all the parameters from the prior step,
since Snakemake will still be running those workflow steps.

Here is the parameters file:

```text
$ cat goodies/readfilt2params.json
{
    "short_description": "Read Filtering Walkthrough 2 - Pre-Trim Quality Assessment - Parameters",
    "biocontainers" : {
        "fastqc" : {
            "use_local" : false,
            "quayurl" : "quay.io/biocontainers/fastqc",
            "version" : "0.11.7--pl5.22.0_2"
        }
    },
    "read_filtering" : {
        "read_patterns" : {
            "pre_trimming_pattern"  : "{sample}_{direction}_reads.fq.gz"
        },
        "quality_assessment" : { 
            "fastqc_suffix" : "fastqc"
        },
        "read_files" : {
            ...
        }
    }
}
```

This uses the pre-trimming pattern to match filenames
containing read files to assess.

To run the workflow defined by this workflow name,
config file, and parameters file, run taco as follows:

Dry run first with the `-n` flag:

```text
$ ./taco -n read_filtering \
    goodies/readfilt2config.json \
    goodies/readfilt2params.json
```

Then the real deal:

```text
$ ./taco read_filtering \
    goodies/readfilt2config.json \
    goodies/readfilt2params.json
```


## Part 3: Trim Reads

In Part 3 we will use trimmomatic to trim reads based on quality.
(This will require us to re-run the prior steps.)

In Part 3, we will output the trimmed reads to a new file.
To do this, we must change the pre-trimming filename pattern,
which is too general: `{sample}_{direction}.fq.gz`
will match nearly every `post_trimming_pattern` we choose.

We should change the pattern parameters to include 
either a prefix or a suffix:

```text
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

```text
$ cat goodies/readfilt3config.json
{
    "short_description": "Read Filtering Walkthrough 3 - Trimming - Configuration",
    "workflow_targets":  ["data/TruSeq2-PE.fa",
                          "data/SRR606249_1_reads.fq.gz",
                          "data/SRR606249_2_reads.fq.gz",
                          "data/SRR606249_1_reads_fastqc.zip",
                          "data/SRR606249_2_reads_fastqc.zip",
                          "data/SRR606249_1_trim2.fq.gz",
                          "data/SRR606249_2_trim2.fq.gz"]
}
```

The parameters file contains updated parameters
(most options are not required, but this illustrates
what controls the user has over file names):

```text
$ cat goodies/readfilt3params.json
{
    "short_description": "Read Filtering Walkthrough 3 - Trimming - Parameters",
    "biocontainers" : {
        "trimmomatic" : {
            "use_local" : false,
            "quayurl" : "quay.io/biocontainers/trimmomatic",
            "version" : "0.36--5"
        },
        "fastqc" : {
            "use_local" : false,
            "quayurl" : "quay.io/biocontainers/fastqc",
            "version" : "0.11.7--pl5.22.0_2"
        }
    },
    "read_filtering" : {
        "read_patterns" : {
            "pre_trimming_pattern"  : "{sample}_{direction}_reads.fq.gz",
            "post_trimming_pattern" : "{sample}_{direction}_trim{qual}.fq.gz"
        },
        "quality_assessment" : { 
            "fastqc_suffix" : "fastqc"
        },
        "quality_trimming" : {
            "trim_suffix" : "se"
        },
        "adapter_file" : {
            "name" : "TruSeq2-PE.fa",
            "url"  : "http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-semi-2015-03-04/TruSeq2-PE.fa"
        },
        "read_files" : {
            ...
        }
    }
}
```

Note the `read_files` file names have been adjusted to match
the `pre_trimming_pattern`.

Dry run first with the `-n` flag:

```text
$ ./taco -n read_filtering \
    goodies/readfilt3config.json \
    goodies/readfilt3params.json
```

Then the real deal:

```text
$ ./taco read_filtering \
    goodies/readfilt3config.json \
    goodies/readfilt3params.json
```


## Part 3 (Modified): Trim Reads with Custom Docker Container

Each step that utilizes a biocontainer from quay.io 
can also be configured to use a local Docker image
as well. 

**CAVEATS:** 

* This feature does not currently work for workflows
    involving multiple machines (the container image
    is not built and must already be available).
* This workflow (use of local, customized docker files)
    is intended as a last resort, or for development 
    purposes only.

Start by building a `fastqc` docker container to use in lieu
of the quay.io docker container defined in the default 
config dictionary. From the taco repository:

```text
cd docker_kludge/fastqc/
docker -t dahak_conda .
cd ../../
```

This builds a container image called `dahak_conda`
using the Dockerfile in the given directory.

Now add a `biocontainers` section to the parameters 
dictionary. In the fastqc section, specify the name of the 
local container and specify that taco should use a 
local container.

We use the same config file as before, so that we run the 
same workflow steps, but now the workflow is run using a 
local docker container.

Here is the new file `readfilt3params_localdocker.json`:

```text
$ cat readfilt3params_localdocker.json
{
    "short_description": "Read Filtering Walkthrough 3 Modified - Trimming - Parameters",
    "biocontainers" : {
        "trimmomatic" : {
            "use_local" : false,
            "quayurl" : "quay.io/biocontainers/trimmomatic",
            "version" : "0.36--5"
        },
        "fastqc" : {
            "local" : "dahak_fastqc",
            "use_local" : true
        }
    },
    "read_filtering" : {
        ...
    }
}
```

And here is the command to run the workflow:

```text

$ # Dry run

$ ./taco -n read_filtering \
    goodies/readfilt3config.json \
    goodies/readfilt3params_localdocker.json

$ # Real thing:

$ ./taco -n read_filtering \
    goodies/readfilt3config.json \
    goodies/readfilt3params_localdocker.json
```


### Steps 4 and 5: Rule: Post-Trim Quality Assessment

In steps 4 and 5 we request the output file from the quality 
assessment pipeline. 

In step 4, the first quality trimming, we'll use a quality value of 2.

In step 5, the second quality trimming, we'll use a quality value of 30.

The config file requests trimmed reads with a quality value of 2,
done using trimmomatic, and a fastqc quality-assessed output 
file (fastqc.zip files).

```text
$ cat goodies/readfilt4config.json
{
    "short_description": "Read Filtering Walkthrough 4 - Quality Filtering at 2 - Configuration",
    "workflow_targets" : ["data/SRR606249_1_trim2.fq.gz",
                          "data/SRR606249_2_trim2.fq.gz",
                          "data/SRR606249_1_trim2_fastqc.zip",
                          "data/SRR606249_2_trim2_fastqc.zip"]
}


$ cat goodies/readfilt5config.json
{
    "short_description": "Read Filtering Walkthrough 5 - Quality Filtering at 30 - Configuration",
    "workflow_targets" : ["data/SRR606249_1_trim30.fq.gz",
                          "data/SRR606249_2_trim30.fq.gz",
                          "data/SRR606249_1_trim30_fastqc.zip",
                          "data/SRR606249_2_trim30_fastqc.zip"]
}
```

Next, the parameters file requires the user to 
specify a few additional parameters 

```text
$ cat goodies/readfilt4params.json
{
    "short_description": "Read Filtering Walkthrough 4 - Quality Filtering - Parameters",
    "biocontainers" : {
        ...
    },
    "read_filtering" : {
        "read_patterns" : {
            "pre_trimming_pattern"  : "{sample}_{direction}_reads.fq.gz",
            "post_trimming_pattern" : "{sample}_{direction}_trim{qual}.fq.gz"
        },
        "quality_assessment" : { 
            "fastqc_suffix" : "fastqc"
        },
        "quality_trimming" : {
            "trim_suffix" : "se"
        },
        "adapter_file" : {
            "name" : "TruSeq2-PE.fa",
            "url"  : "http://dib-training.ucdavis.edu.s3.amazonaws.com/mRNAseq-semi-2015-03-04/TruSeq2-PE.fa"
        },
        "read_files" : {
            ...
        }
    }
}
```

Note that the parameters file for steps 4 and 5 will look identical, 
since both run the same workflow and the only change is in the quality
value (which is only specified by the filename).

Now execute the commands that will run the workflow:

```text

$ # Dry run

$ ./taco -n read_filtering \
    goodies/readfilt4config.json \
    goodies/readfilt4params.json

$ ./taco -n read_filtering \
    goodies/readfilt5config.json \
    goodies/readfilt5params.json



$ # Real thing:

$ ./taco -n read_filtering \
    goodies/readfilt4config.json \
    goodies/readfilt4params.json

$ ./taco -n read_filtering \
    goodies/readfilt5config.json \
    goodies/readfilt5params.json
```

### Step 6: Interleaving Trimmed Reads 

The last step is to use khmer to interleave
trimmed reads after running trimmomatic and
the `quality_trimming` rule.

The interleaving step takes two input files,
the trimmed reads we want to use, 
requires one additional parameter,
which is the filename suffix we want 
paired-end reads to have 
(for example, `pe`).

The config file uses this when specifying the target file:

```text
$ cat goodies/readfilt6config.json
{
    "short_description": "Read Filtering Walkthrough 6 - Interleaving Trimmed Reads - Configuration",
    "workflow_targets" : ["data/SRR606249_pe_trim2.fq.gz",
                          "data/SRR606249_pe_trim2.fq.gz",
                          "data/SRR606249_pe_trim30.fq.gz",
                          "data/SRR606249_pe_trim30.fq.gz"]
}
```

and the params file:

```text
$ cat goodies/readfilt6params.json
{
    "short_description": "Read Filtering Walkthrough 6 - Interleaving Trimmed Reads - Parameters",
    "biocontainers" : {
        "trimmomatic" : {
            ...
        },
        "fastqc" : {
            ...
        },
        "khmer" : {
            "use_local" : false,
            "quayurl" : "quay.io/biocontainers/khmer",
            "version" : "2.1.2--py35_0"
        }
    },
    "read_filtering" : {
        ...
        "interleaving" : {
            "interleave_suffix" : "pe"
        },
        ...
    }
}
```

```text
$ # Dry run

$ ./taco -n read_filtering \
    goodies/readfilt6config.json \
    goodies/readfilt6params.json



$ # Real thing:

$ ./taco -n read_filtering \
    goodies/readfilt6config.json \
    goodies/readfilt6params.json
```



