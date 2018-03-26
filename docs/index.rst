.. dahak-taco documentation master file, created by
   sphinx-quickstart on Thu Mar 22 16:07:28 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==========================
dahak-taco documentation
==========================

dahak-taco is an experimental command-line interface
for running dahak workflows using Snakemake.

Getting Started
==================

To get started with dahak-taco,
and run your first workflow task,
see :doc:`intro`.

To figure out what taco is doing
and what it requires, see :doc:`howitworks`.

If you're hungry for more dahak workflows,
skip to the next section.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   intro
   howitworks
   snakemakerules

Workflows
==================

The main purpose of taco is to run 
dahak workflows by calling Snakemake
rules contained in the ``rules`` directory.

Here are a few walkthroughs of 
common dahak workflows:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   taxclass
   assembly
   functionalinference

