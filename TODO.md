## priorities


more enormous problems.
* we are trying to validate parameters
* but how do we do that, if we're forced to validate everything?
* we're forced to go through validation for parameters we don't even use


important:
* create an input config validator
* this adds yet another action to dahak...

* get the read filtering workflow back up an running
* tag the next release 
* add a changelog
* add a test suite with goodies (really idiotic problem, I can't import stuff from `../somedir/<here>`a)

* clear up ambiguity about data/ prefix.
* does the user specify it in filenames, or not? clear this up.
    * right now:
    * in the params dictionary, the user does not specify `data/` prefix.
    * config and rule targets, yes, the user must specify `data/` prefix.

* email at the end


## taco cli

* add common parser: [link](https://github.com/dcppc/dcppc-bot/pull/4/files#diff-d51593b709dedb0cfd088f88515df1a2R180)

* improve the command line interface

```
taco ls

taco workflow1 --config=goodies/w1config.json --params=goodies/w1params.json

taco --workflow=workflow1 --config=goodies/w1config.json --params=goodies/w1params.json
```

getting help:

```
dahak # (print short help)
dahak help # (print long help)
dahak --help # (print long help)
```

listing workflows/rules:

```
dahak ls # (list available workflows)
dahak ls <workflow> # (list available rules in workflow)
```

## when finished

* when workflows are complete:
    * dump out a log copy of the complete config dictionary the user used
    * email a message specifying workflow is complete

## rules

* Implement file name/extension validation where needed
    * validation should occur *within* the rule
    * we want the user to know which rule caused the problem

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

Read filtering walkthru:
* Gauge detail level - too much? not enough?
* Still more detail that could be added


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





