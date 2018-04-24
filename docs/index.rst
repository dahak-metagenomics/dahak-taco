==========================
dahak-taco documentation
==========================

dahak-taco is an experimental command-line interface
for running dahak workflows using Snakemake.

(insert icholy/ttygif here.)

To get started with taco,
and run your first workflow task,
see the :ref:`getting-started-label`
section.

If you're hungry for more dahak workflows,
skip to the :ref:`walkthroughs-label` 
section.

If you are already up and running 
with taco and are looking for 
information about the rules and their 
parameters, check out the 
:ref:`detailed-api-label` section.

If you are extending taco by adding new
rules, workflows, or documentation, see 
the :ref:`for-developers-label` section.


.. _getting-started-label:

Getting Started
==================

taco is a command line utility that wraps
Snakemake rules to run complex workflows.

These sections will cover what taco is
and get you up and running with your 
first taco workflow.

.. toctree::
   :maxdepth: 1
   :caption: Getting Started:

   intro/intro
   intro/quickstart


.. _walkthroughs-label:

Workflow Walkthroughs
=======================

taco is a lightweight wrapper around Snakemake tasks.
Kind of like a corn tortilla.

The Snakemake rules and parameters are organized 
by workflow in the ``rules/`` directory 
of this repository.

The walkthroughs below show examples
of how to run each workflow.

.. toctree::
   :maxdepth: 1
   :caption: Workflow Walkthroughs:

   walkthrus/awssetup
   walkthrus/readfilt



.. _detailed-api-label:

Workflow Parameters
==========================

Each workflow takes a parameters dictionary.
This section details the structure and keys
that are defined and used in the parameter 
dictionary.

.. toctree::
   :maxdepth: 1
   :caption: Read Filtering Workflow API:

   read_filtering

.. _for-developers-label:

For Developers
=====================

The sections below explain how taco works,
so you know how to modify taco to suit your needs.

There are also sections for adding or modifying
Snakemake rules, and for adding new workflows.

taco provides a set of workflows with default 
parameters that should work for many use cases.

However, to extend taco, or just understand
what it is doing, take a look at the innards of taco:

.. toctree::
   :maxdepth: 1
   :caption: For Developers:

   developers/howitworks
   developers/snakemakerules
   developers/workflows
   developers/documentation

