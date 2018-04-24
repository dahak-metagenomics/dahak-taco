# How Taco Works

## The Tao of Taco

taco is a lightweight wrapper around Snakemake tasks.
Kind of like a corn tortilla.

* All code is located in the `taco` executable script
* It is a short and simple command line interface implemented with argparser
* Snakemake is called via its Python API. 
* The user specifies which snakemake rule to call, and any parameters to use.

## User Input

User input required to run taco:

* Workflow config json file calls rules defined in `rules/dahak/*.rules`
* Parameters json file overrides parameters defined in `rules/dahak/*.settings`

See [Introduction](intro.md) for a user-oriented introduction
to workflow configuration and parameters.


## Parameter Presets (Not Implemented)

We want to define a few command line options
that will be passed through the Snakemake 
API (via a configuration dictionary)
to provide parameter presets.

```
$ taco <workflow-name> \
    --workflow-preset=heavy \
    <config-json-file> \
    <params-json-file>
```


## Setting Variables from Command Line (Not Implemented)

(Not implemented yet.)

Setting variables:

For the user's convenience, we want to provide the user a way to 
change/set parameter values on the command line. 

Provide a command line flag for simpler/common options.
This is flat, so you have to hard-code how the command line options
map to the particular JSON entry you want it to change.

```
$ taco <workflow-name> \
    --quality=2,30,50 \
    --custom-param=custom_value \
    <config-json-file> \
    <params-json-file>
```

