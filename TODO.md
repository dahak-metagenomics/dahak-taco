## priorities

uh oh...
* scenario: we provided values, but not at the right place
* the dict keys we defined are never used
* the default dict keys are used instead



* clear up ambiguity about data/ prefix.
* does the user specify it in filenames, or not? clear this up.
    * right now:
    * in the params dictionary, the user does not specify `data/` prefix.
    * config and rule targets, yes, the user must specify `data/` prefix.


## requirements

docker and singularity
* singularity directive in Snakefiles

## taco cli

* add common parser: [link](https://github.com/dcppc/dcppc-bot/pull/4/files#diff-d51593b709dedb0cfd088f88515df1a2R180)

* improve workflow

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

* Add command line options 
    * snakemake force flag
    * snakemake options flags:
    * change options shared by all workflows/rules

* When the user runs a workflow, dump out a copy of the config dictionary with the log/other

## rules

* Implement file name/extension validation where needed
    * validation should occur *within* the rule
    * we want the user to know which rule caused the problem

* Common tasks/rules: common workflow folder? (e.g., pull biocontainers rule)

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

* <s>finish read trim workflow</s>
* <s>finish read trim walkthru</s>
* <s>custom dockerfile/image in place of quay url</s>

