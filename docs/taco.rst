==================
dahak-taco
==================

dahak-taco is an experimental 
command line interface for 
running dahak workflows.

Installation
=============

dahak-taco is an executable script
that requires Conda, Snakemake,
and (optionally) Singularity to run.

Installation scripts for software needed 
for dahak-taco are in the `scripts/` folder.

Command-Line Quick Start
============================

To get started with dahak-taco, 
you will need to provide a workflow
configuration file and a parameters file.

The workflow configuration file
will specify what task to perform
on which files. The parameters
file specifies values to use 
for various workflow parameters.

Both files are JSON files.

Example workflow configuration file
---------------------------------------

.. code::
    {
        "workflow_target" : "pull_biocontainers"
    }

Example parameters file
------------------------

.. code::
    {
        "biocontainers" : {
            "sourmash" : "2.0.0a2--py36_0"
        }
    }

Performing a task
-------------------------

.. code::
    $ ./taco my-workflow my-params

Performing another task
-------------------------------------

.. code::
    $ ./taco another-workflow another-task

Overriding parameters
--------------------------

We implement command line arguments
for the most common parameters,
but full access requires using 
the parameters JSON file.


