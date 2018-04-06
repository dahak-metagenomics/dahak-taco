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

## documentation

* Mention `data_dir` parameter and "where's my stuff"
* Mention logs, output, and troubleshooting information
