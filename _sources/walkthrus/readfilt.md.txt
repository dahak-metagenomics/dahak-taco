# Read Filtering Walkthrough

This walkthrough covers a read filtering workflow. Specifically, we will:

* **(Optional)** Prepare a beefy worker node to run a 
    dahak workflow by installing required software 
    (dahak-yeti).

* Download raw sequence data from OSF data store (wget).

* Assess the quality of the pre-filtered reads (fastqc)

* Trim and filter the reads based on a quality threshold (trimmomatic)

* Assess the quality of the post-filtered reads (fastqc)

This workflow specifically covers the use of taco.
See the [walkthroughs dir of the dahak repo](https://github.com/dahak-metagenomics/dahak/tree/master/workflows/read_filtering)
for the original shell-based walkthrough.

## (Optional) Preparing Worker Node

dahak-taco is intended to be a multi-platform
tool (HPC or cloud), but for the sake of the walkthrough
we will briefly cover the setup process using an AWS node.

Log into the AWS console and select a region 
(`us-west-2` Oregon is good for spot instances).

### Amazon Machine Image

Select the stock Ubuntu 16.04 LTS image 
from the list of AMIs.
This has the AMI ID:

```
ami-4e79ed36
```

### Node Type

The hardware depends highly on the worfklow
(more results soon from benchmarking of workflows),
but for all walkthroughs we utilize one of the following:

* `m5.2xlarge` (8 vCPUs, 32 GB RAM) 
* `m5.4xlarge` (16 vCPUs, 64 GB RAM)

Select `m5.2xlarge` for the read filtering walkthrough.

### Configuring Instance Details

On the configure instance details:

* Check "Request Spot Instances" box and set your desired price
    * Typical price for 2xlarge is 14 cents per hour
    * Typical price for 4xlarge is 28 cents per hour

* Click the Advanced Details bar at the bottom

* Copy the following into the user data text box:

```
#!/bin/bash
bash <( curl https://raw.githubusercontent.com/charlesreid1/dahak-yeti/master/cloud_init/cloud_init.sh )
```

![dahak-yeti user data setup screenshot.](user-data-screenshot.png)

* The pipe-to-bash one-liner will run the cloud init script 
    in the [dahak-yeti](https://github.com/dahak-metagenomics/dahak-yeti) repo

### Volumes

A 256 GB hard disk (EBS, the default) should be sufficient.

### Logging Into Instance

When you create the node it should set up a private key
to use to SSH into the worker node.

The init script will add a few minutes to the worker node's 
startup time. It will run scripts, install files, set configurations,
and run a lot of magic.

Once the startup step has completed, you can SSH to the
worker node, and you will have the following installed:

* pyenv
* miniconda3-4.30 installed with pyenv
* snakemake installed with conda
* opinionated dotfiles (`.bashrc`, `.bash_profile`, `.vimrc`, etc.)
* a colorful pink prompt

![dahak-yeti promp after user login.](yeti-screenshot.png)



