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

   walkthrus/setup
   walkthrus/readfilt



.. _detailed-api-label:

Detailed Workflow API
==========================

Each workflow takes a set of parameters.
The pages listed below give information 
about default parameters for each workflow,
and show short examples of how to customize
each rule.

.. toctree::
   :maxdepth: 1
   :caption: Read Filtering Workflow API:

   read_filtering/read_filtering
   read_filtering/fetch_reads
   read_filtering/pre_post_assessment
   read_filtering/quality_trimming

.. toctree::
   :maxdepth: 1
   :caption: Taxonomic Classification Workflow API:

   taxonomic_classification/taxonomic_classification
   taxonomic_classification/biocontainers
   taxonomic_classification/calculate_signatures
   taxonomic_classification/filter_taxa
   taxonomic_classification/kaiju
   taxonomic_classification/kaiju2krona
   taxonomic_classification/krona_visualization
   taxonomic_classification/sourmash_sbt
   taxonomic_classification/trimmed_data


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

