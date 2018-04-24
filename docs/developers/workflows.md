# Adding New Taco Workflows

If you wish to extend or modify taco by 
adding a new workflow, you can do so,
but it's important to plan it out first!

Each Snakemake workflow is composed of 
a set of loosely-interconnected rules 
sharing parameters and handling pieces 
of the whole workflow.

The workflow lives in a directory 
in `rules` that is named after the 
workflow. For example, to add a new
workflow called `foobar`:

```
rules/
    foobar/
    taxonomic_classification/
    read_filtering/
    functional_annotation/
    ...
```

Each rule or group of rules lives in a 
.rule file. All rule files have access
to the entire configuration dictionary,
which stores all workflow parameters.

Suppose our new workflow `foobar` had 
three distinct steps: `buz`, `fuz`, and `wuz`.
Then we would create a rule file for each,
and the `foobar/` rules directory structure
would be:

```
rules/
    foobar/
        buz.rule
        fuz.rule
        wuz.rule
        foobar.settings
```

Additionally, we need to set parameters for the workflow.

Each workflow has access to the "master" Snakemake
parameters dictionary. 

In addition, each workflow defines its own parameters dictionary
to store parameters specific to that workflow.

This parameters dictionary is stored under a key that is the name 
of the workflow.

For example, if each of our three workflow steps took 
parameters, here is how we would organize the 
workflow's default parameters dictionary:

```
{
    ...

    'foobar' : {

        'buz' : {
            'buz_param_1' : 1,
            'buz_param_2' : 'alpha'
        },

        'fuz' : {
            'fuz_param_1' : 50,
            'fuz_param_2' : 51,
            'fuz_param_3' : False
        },

        'wuz' : {
            'wuz_param_1' : 9.99,
            'wuz_param_2' : 9.98,
            'wuz_param_3' : 9.97,
            'wuz_param_4' : 9.96
        }
    }
    ...
}
```

The `foobar.settings` file must set this 
in a way that will not overwrite defaults;
hence this business:

```
from snakemake.utils import update_config

if(not config['clean']):

    # Note: don't include http:// or https://
    config_default = { 
                        ... 
                     }

    update_config(config_default, config)
    config = config_default
```


