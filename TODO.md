## priorities


### parameter validation

more enormous headaches.
* we are trying to validate parameters
* but how do we do that, if we're forced to validate everything?
* we're forced to go through validation for parameters we don't even use
* the flip side is we don't validate anything, and then the user 
    is forced to puzzle through what went wrong or why a rule failed.

validation solution:
* validate everything. 
* the problem with validating everything is the user may be asked to provide
    parameters for steps they are not interested in carrying out.
    that's where two other features step in.
* the first feature is the `taco validation` verb
    * make sure your config file isn't out of sorts,
    * print out all possible keys and what keys you have specified
    * (ideally) what keys a given default setting would define
    * this is starting to get complicated.
* the second feature is parameter presets
    * you can specify a preset on the command line
    * this will nail down all those extra params you didn't care about


### documentation

developers guide:
* making new rules
* creating a default parameter set


### yaml

switch input from json to yaml

important:
* create an input config validator
* this adds yet another action to dahak...
* which one is easier?
    * yaml validator?
    * yaml -> json, json validator?

What else?
* get the read filtering workflow back up an running
* tag the next release 
* add a changelog
* add a test suite with goodies 
* the idiotic problem of not being able to import things...

prefix:
* clear up ambiguity about data/ prefix.
* does the user specify it in filenames, or not? clear this up.
    * right now:
    * in the params dictionary, the user does not specify `data/` prefix.
    * config and rule targets, yes, the user must specify `data/` prefix.


notifications
* email at the end
* ubuntu sendmail container
* php + mail() (apache not necesary, should be able to 
    run a php mail script from the command line)
* https://www.abeautifulsite.net/configuring-sendmail-on-ubuntu-1404


## taco cli

* add common parser: [link](https://github.com/dcppc/dcppc-bot/pull/4/files#diff-d51593b709dedb0cfd088f88515df1a2R180)

* improve the command line interface

```
Usage:
taco <action> [OPTIONS]

    Actions:
        
        taco help           Print long help message
        taco ls             List workflows 
        taco ls <workflow>  List rules in workflow <workflow>
        taco validate       Validate input JSON/YAML
        taco <workflow>     Run workflow <workflow>
```

### `taco ls`

To list all workflows that are available:

```
taco ls
```

Once you decide on a workflow, you can list all rules
in that workflow and get a brief description of each:

```
taco ls --help

taco ls

taco ls <workflow>
```

### `taco validate`

This takes an optional config and/or params argument and validates it.

```
taco validate --help

taco validate --config=goodies/w1config.json

taco validate --params=goodies/w1config.json

taco validate \
    --config=goodies/w1config.json \
    --params=goodies/w1params.json
```

### `taco <workflow>`

The meat of the taco, the workflows take two arguments:
the config file and the params file.

Here are some example usages of the workflow commands:

```
taco workflow1 --help

taco workflow1 --config=goodies/w1config.json \
               --params=goodies/w1config.json
```

### parameter presets

We also want to provide the user with some 
command line arguments to change some common
options or use a preconfigured set of parameters.

Preconfigured parameters would be flags that 
activate a particular default configuration/parameters
dictionary. In the corresponding `.settings` file of the 
workflow, each preset should be defined, and the 
appropriate default selected when the Snakemake API
is run.

Presets can't define every parameter, though, 
so the user must provide a config and params file
regardless of the preset.

```
taco workflow1 --config=goodies/w1config.json \
               --params=goodies/w1config.json \
               --preset=turbo

taco workflow1 --config=goodies/w1config.json \
               --params=goodies/w1config.json \
               --preset=nitro
```


## when finished

* when workflows are complete:
    * dump out a log copy of the complete config dictionary the user used
    * email a message specifying workflow is complete

## rules


* Tab completion

## documentation

Users:

* Mention `data_dir` parameter and "where's my stuff"
* Mention logs, output, and troubleshooting information
* How to change other rules and settings

Dev:

* Add new rule
* Structuring rules
* docker singularity biocontainers bioconda


## walkthrus

Read filtering walkthrough:
* Revisit
* Rewrite:
    * We have to define all the parameters
    * We can define one preset to demonstrate how to do it


## done

done:
* <s>finish read trim workflow</s>
* <s>finish read trim walkthru</s>
* <s>custom dockerfile/image in place of quay url</s>

<s>uh oh... huge problem.
* scenario: we provided values, but not at the right place
* the dict keys we defined are never used
* the default dict keys are used instead
* add a --clean option so we don't use any default parameters
* only useful for testing.</s>

more:
* <s>make the program more robust to errors or misconfiguration</s> (see --clean)

<s>requirements (see scripts/ folder, or [dahak-yeti](https://github.com/charlesreid1/dahak-yeti)):
* fix pyenv installation script
* fix conda installation script 
* fix snakemake installation script
* fix singularity installation script</s>

Yet another thing we can't do, because Snakemake:
* <s>Common tasks/rules: common workflow folder? (e.g., pull biocontainers rule)</s>
* <s>Tried putting utils in a common workflow dir. FAILED TO IMPORT</s> 
* <s>Tried putting utils in the workflow dir. FAILED TO IMPORT</s>
* Literally the only thing that works is making a copy of utils.py in every single workflow directory. 
* The problem 

more:
* <s>start a (very long) list of all the land mines I discovered in Snakemake</s>


* <s>file name and extension and parameter validation: implement where needed
    * validation should occur *within* the rule
    * we want the user to know which rule caused the problem</s>

"Validation should occur *within* the rule" is precisely the heart of the problem:
Snakemake separately evalutes non-rule Python code, then evaluates rules.
If you validate inside a rule, you can't validate inputs, outputs, singularity containers,
or anything else but the `run` block.




