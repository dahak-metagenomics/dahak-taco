# Introduction: dahak-taco

dahak-taco is an experimental 
command line interface for 
running dahak workflows.

dahak-taco is hosted in Github
at [https://github.com/dahak-metagenomics/dahak-taco](https://github.com/dahak-metagenomics/dahak-taco).

## Installation

dahak-taco is an executable command-line script.

Create a local clone using git:

```text
$ git clone https://github.com/dahak-metagenomics/dahak-taco.git
```

## Software Requirements

dahak-taco wraps a Snakemake file with a simpler command line interface.

To run dahak-taco, you must have Python 3 and Snakemake installed.

Singularity is not currently required, but may be in the future.

## Getting Required Software 

Required software:

* Conda
* Snakemake
* Singularity (optional)

**Installing:** Installation scripts for software needed 
for dahak-taco may be found in the `scripts/` directory
in the repo:

```text
$ ls dahak-taco/scripts/
install_pyenv.py
install_singularity.py
install_snakemake.py
```

You must be root to install singularity.

You may install pyenv and Snakemake as a user only.

**Testing:** To test your environment is working,
run the following command using your version of Python:

```text
$ python -c 'import snakemake'
```

## How To Use Taco

The file `taco` contains the command line tool,
so run it directly:

```
$ ./taco <arguments>
```

This will provide helpful information at the command line. 

Keep reading for a description of what 
information taco requires to run.

Next: [Quick Start](quickstart.md)

