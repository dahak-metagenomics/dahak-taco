# Snakemake Rules

A brief summary of how Snakemake rules are implemented and organized.

We follow the conventions set in the [snakemake-rules](https://github.com/percyfal/snakemake-rules)
repository, and groups all rules into `.rule` files and all parameters into
`.settings` files.

For a couple of simple workflows illustrating
how to assemble Snakemake rules that `taco` 
can utilize (i.e., that uses information 
from the user's config and params file),
see the [simple-taco](https://github.com/dahak-metagenomics/simple-taco)
taco workflow repository.

## Workflows 

The workflows define a set of tasks.
Each workflow is a sub-directory in the `rules/` 
directory.

## Rule Files

Rule files define how steps in the workflow proceed.
They preprocess configuration variables.
Rules are defined in `.rule` files
in the workflow directory.

## Default Parameter Files

The default parameter dictionary is contained
in a `.settings` file in the workflow directory.
These will _NOT_ overwrite any parameters
that have already been set by the user in their
JSON parameter file.

## Validation of Parameters

Because we don't know what workflow is being run
when we process the parameters, we can't do much
parameter validation.

Currently, we do not throw an exception 
when a parameter is undefined by the user,
we either silently use the default value 
(default behavior) or we silently set to 
an empty string (using `--clean` or `-c`
flag).

