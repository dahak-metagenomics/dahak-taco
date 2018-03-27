# dahak-taco

taco is an experimental command line interface for dahak workflows. 

See the [dahak-taco documentation](https://charlesreid1.github.io/dahak-taco/).

The documentation for workflow rules
are contained as markdown in the docstrings
in each rule file. (This is the most convenient place
to document information about each rule.) 

To create the documentation, run the snakemake
list rules command, which will include 
the docstrings for each rule:

```
$ snakemake -l -s Snakefile.workflow1 > workflow1_documentation.md
```

