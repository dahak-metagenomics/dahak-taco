## Installing

taco is an executable script, so there is nothing to install
for taco specifically - you can just download and run taco.
(However, taco requires other software be installed; see below.)

### Requirements

* Python 3
* Conda (Miniconda recommended)
* Snakemake
* Singularity

### Optional

* Docker



## Resolving Requirements

### Install Scripts

Scripts to install the above packages can be found
in the [`scripts/`](https://github.com/dahak-metagenomics/dahak-taco/tree/master/scripts) 
directory of dahak-taco.

### Testing Requirements are Installed

To check that you are using Python 3, run:

```text
$ /usr/bin/env python --version
```

To test that Snakemake can be imported from Python, run:

```text
$ /usr/bin/env python -c 'import snakemake'
```



## Getting Taco

To get taco, clone a local copy using git:

```text
$ git clone https://github.com/dahak-metagenomics/dahak-taco.git 
$ cd dahak-taco/
$ ./taco --help
```

