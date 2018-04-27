# Scripts

This directory contains scripts to install
the software required by dahak-taco.

In order of execution, these are:

* `install_pyenv.py` - install pyenv, which enables 
    fine-grained control over Python and Conda versions.
    This will install pyenv to `~/.pyenv/bin`, this directory
    should be on your path

* `activate_conda.py` - install and activate the latest 
    version of miniconda. This assumes `pyenv` is on your path.

* `install_snakemake.py` - use miniconda to install the 
    latest version of miniconda.

* `install_docker.py` - install docker for the user ubuntu.

* `install_singularity.py` - install singularity for the user ubuntu

Run these scripts through Python:

```
python <script-name>.py
```

