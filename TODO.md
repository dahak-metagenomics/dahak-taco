## priorities

* finish walkthru
* read trim workflow

* clear up ambiguity about data/ prefix.
* does the user specify it or not? clean this up.
    * right now:
    * params, nope.
    * config and rule targets, yup.


## requirements

docker vs singularity
* we have pull biocontainers rule, for example
* not strictly necessary, since if the container is not pulled, it gets pulled
* barring that, we can use `singularity:` directive in Snakefiles


## taco cli

* print a list of common rules (all rules?) with output
* implement a better ls functionality
    * `dahak ls` lists workflows
    * `dahak ls workflow` lists rules
* Add command line options to change options shared by all workflows/rules
* <s>Explain how to change other rules and settings</s> (see API documentation)

## rules

* Implement file name and file extension validation (if needed)
    * should this happen *before* or *within* the rule?
    * validate file existence *within* the rule
    * we want the user to know which rule caused the problem

* Tab completion

## documentation

* Mention `data_dir` parameter and "where's my stuff"
* Mention logs, output, and troubleshooting information

## walkthroughs



