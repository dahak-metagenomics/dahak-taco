# Snakemake Rules

A brief summary of how Snakemake rules are implemented and organized.

We follow the conventions set in the [snakemake-rules](https://github.com/percyfal/snakemake-rules)
repository, and groups all rules into `.rule` files and all parameters into
`.settings` files.

## Rule Files

Rule files are, unsurprisingly, 
contained in the `rules/` directory,
in `.rule` files. 

To list all rules, use the `taco ls` command:

```
$ ./taco ls
```

TODO: fix this mess. Use snakemake -l to generate docs, use taco ls 
to present a cleaned up version of the information.
Will require grep and cut and etc.

## Parameter Files

Parameter files live in the same location and share the same name
as their corresponding rule files, but have a `.settings` suffix.

These files have a default set of configuration parameters defined.
They read the configuration parameter set after the Snakefile 
has been initialized (and the user has set configuration parameters).

The `.settings` files _only_ set configuration parameter values 
if a value has not yet been assigned to that parameter.

## Documentation of Snakemake Rules

Due to the dependency chain and the 
sharing of parameter sets, it is 
difficult to automate documentation of 
Snakemake rules. 


To compromise, Snakemake rules are documented
in the docstring of the Snakemake rule. 
For example:

```
rule do_stuff:
    """
    Useful information about the .settings files
    that do_stuff imports, or parameter values
    that are important for the do_stuff rule,
    can be added here.
    """

    ...
```

However, we can take this a step further 
and write the docstrings directly in Markdown,
allowing us to atuomate documentation generation 
in Markdown (and handed off to Sphinx).

For example:

```
rule do_stuff:
    """
## Snakemake Rule: `do_stuff`

Short Description: The `do_stuff` rule does stuff.

Long Description: The `do_stuff` rule calls the thing
that does the other thing that pulls the widget that
pushes the button that runs the thing that does the thing.

To run this rule with default parameter values:

(&c.)

To run this rule with customized input/output file names:

(&c.)
    """

    ...
```

This is the most convenient place to define this information.
Furthermore, when we run the Snakemake command to list all 
rules, it will print this documentation along with the rules:

```
$ snakemake -l
```

(This currently requires a bit of cleanup, working on a 
sed/awk one-liner.)














