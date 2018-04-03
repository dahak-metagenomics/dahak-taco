.. dahak-taco documentation master file, created by
   sphinx-quickstart on Thu Mar 22 16:07:28 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==========================
dahak-taco documentation
==========================

dahak-taco is an experimental command-line interface
for running dahak workflows using Snakemake.

(insert icholy/ttygif here.)

Getting Started
==================

To get started with dahak-taco,
and run your first workflow task,
see :doc:`intro/intro`.

If you're hungry for more dahak workflows,
skip to the next section.

.. toctree::
   :maxdepth: 1
   :caption: Getting Started:

   intro/intro
   intro/quickstart

Workflow Walkthroughs
=======================

dahak-taco is a lightweight wrapper around Snakemake tasks.
Kind of like a corn tortilla.

The Snakemake API is called to run rules contained in the 
``rules`` directory.

Here are a few walkthroughs of 
common dahak workflows:

.. toctree::
   :maxdepth: 1
   :caption: Workflow Walkthroughs:

   workflows/readfilt
   workflows/taxclass
   workflows/assembly

Under The Hood
=====================

dahak-taco provides a set of workflows 
with default parameters that should work
for many use cases.

However, to extend dahak-taco, or just understand
what it is doing, take a look at the innards of taco:

.. toctree::
   :maxdepth: 1
   :caption: Under the Hood:

   underthehood/howitworks
   underthehood/snakemakerules
