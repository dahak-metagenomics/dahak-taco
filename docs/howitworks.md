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

See [intro](/intro)

## Setting Variables (Not Implemented)

(Not implemented yet.)

Setting variables:

* For the user's convenience, we want to provide the user a way to 
    change/set parameter values on the command line. 

* We might provide a command line flag for simpler/common options.
    This is flat, so you have to hard-code how the command line options
    map to the particular JSON entry you want it to change.

```
$ taco --a1=something --b2=other test-workflow test-params
```

* Or we might do something like accept JSON from stdin,
    in addition to any other json files specified on the 
    command line. This could handle arbitrary nested 
    JSON, which is necessary for most settings.
 
```
$ cat my_special_settings.json
{ 'myapp' : { 'special_file_prefix' : 'abcd{kvalue}.out', 'kvalue' : 5 } }

$ cat my_special_settings.json | taco --var-stdin test-workflow test-params
```

