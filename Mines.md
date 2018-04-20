# Land Mines in Snakemake

## overview

this document covers some of the issues with snakemake.

the main problem is that snakemake's vocabulary is only designed
for mostly-hard-coded filenames and workflows. It provides a 
rigid structure, limited Python functionality, and a structure
that is difficult to work around (specifically, it evaluates
non-rule code first, then evaluates rule code).

There are many caveats (this feature works, but only this context;
you can do this, but only if you do that).

Snakemake is also filename-centric, which makes 
generalizing workflows difficult. It seems crazy to 
make the entire workflow control happen through 
filenames, and it makes it hard to test.


## details

one difference between make and snakemake is that you can't define
generic rules that perform a set of commands, or rules that call rules.
It comes back to the fact that Snakemake is filename-centric.

For example, I can't have a rule that calls another rule.

This is some minor league stuff. It also makes Snakemake really hard to 
test and to generalize.

The workflow is also designed around long and abstract chains of filenames
that are hard to reason about - especially if you are using some software package
and don't know what kind of files it is going to generate. 

Again, everything fixates on filenames.

## the `{}` characters

There are many complications with `{}` and parameters and wildcards.
Sometimes parameters are available by name, sometimes they are only
available as param.name.

## configuration

We ran into a problem with setting a default configuration file.

if the user misconfigures their config file, e.g., they put something 
in the wrong level of the hierarchy, snakemake will silently replace
all the values with the defaults, and the user may not notice it is not
running their workflow.

On the flip side, if you don't use defaults, there's the problem that
the program may ask for parameters the user will not use.

The core issue here is that non-Snakemake Python code is evaluated first,
separately from the rules, then the rules are evaluated. That means that 
when you are validating parameters, you have no idea what workflow
the user is running, so it is impossible to validate parameters.

You basically have to hope that the user knows what they're doing,
and can diagnose any problems.

From `pre_post_assessment.rule`:

```
A terrible last-minute discovery: 
variables that are just above a rule
are not evaluated just before that rule.

That means the variable holding the name of 
the docker image to use should not be shared 
across rule files (otherwise you get the wrong
container names).

Resolved by using unique variable names,
for each container name,
in each separate rule file.
```

## external functions

Problems with using an external function 
to get OSF data file URLs.

This led to another revelantion: Snakemake has no
debug capabilities. If a rule is failing, you get to
figure out where in the rule things are going wrong.

This problem was with a broken rule that was using 
an external function to validate HTTP resources.
However, there was a problem 

```
            InputFunctionException in line 18 of /home/ubuntu/dahak-taco/rules/read_filtering/fetch_reads.rule:
            KeyError: 'data/SRR606249_2.fq.gz'
            Wildcards:
            sample=SRR606249
            direction=2
```

The error message doesn't hae any useful information.
The line it points to, the line where the error occurs, 
is the line where we define the rule, like 

```
rule: myrule
```

There is no information about what is wrong, except what rule.

It's likely mixing wildcards, functions, and HTTP 
is bad, but it's unclear. Yet another obstacle/slowdown.

## importing does not work

More problems around importing functions.

It is desirable to factor the program so that common functions 
(such as dealing with biocontainers) are defined once.
Normally you would have a `utility.py` that would define
any utility functions, and you would import this from
`taco` and it would be available to Snakemake.

However, there's a catch: it's only available to non-Snakemake
Python code. Once you hit the rules, any functions you have 
imported will disappear, because the rules are essentially living
in a totally different Snakemake namespace/context.

Steps:
* define a function in a file called util.py
* import functions from util.py in taco
* the functions are (should be) available to all sub-calling functions

are they available?
* outside of Snakemake rules, they are
* however, they cannot be used inside snakemake rules
* other limitations - not clear what's going on - but the functions 
    are not available in all rule files.

## two passes through rule files

Snakemake takes two passes through each rule file.

The first time through, it evaluates non-Snakemake Python code.
The functions imported in taco are passed into the rule files
just fine.

The second time through the rule files, Snakemake has created 
a totally new python context, the Snakemake rules are evaluated, 
and the functions imported in are not available.

## more shenanigans 

The unsavory solution to the unsolvable problem above is to put a duplicate copy
of utils.py in each folder. 

Forced to use Python 2 syntax `from utils import my_function` 

This syntax still works in Python 3

## core problem

In the end, these problems all revolve around inflexibility and limited vocabulary.

The solutions are inelegant and require duplicating code, isolating pieces of the program,
making nicely-integrated easy-to-read Snakemake rules impossible.

The problem of having to validate the workflow parameters without knowing 
anything about the workflow being run is the death blow to making Snakemake 
generalize and makes the whole Snakefile logic extremely hairy.

## more weirdness

Let's say we don't want to complain if the user doesn't define parameters 
in the parameter dictionary. Then we just set them equal to empty strings "".
Okay, fine, except that some of the rules take multiple arguments,
so the input essentially becomes `["","","",""]` and Snakemake complains
that rules have duplicate input arguments.

Setting the input/output files to None instead of empty strings results in 
exceptions, so that's out.

The fix? More hard-coded kludges to check if any rules taking lists of input 
or output files consist of only empty strings, and if so, replce them with a 
single empty string.

This is maddening.

## exceptions all the way down

After a painful 2 hours implementing the above, validating each parameter,
raising an exception if it was not okay, it finally ended up we were throwing
exceptions for steps we weren't even running.

The solution? We leave the exception-checking in, and expect the user defines
every single parameter for every single step of this workflow.

Forget about letting the user run one or two steps of the 
five or six total in the workflow. The user is going to have to run
all-or-nothing.

If we provide a sensible default set of parameters, this shouldn't be 
too much of an issue - the user says, use these default parameter values,
and override a couple of them for the one or two steps I'm actually running.

However, the user still isn't getting the information they need, 
which is, what parameters can they/do they define?

## stop being so helpful

The underlying difficulty comes from trying to be too helpful/flexible.

As mentioned above, expect the user will define every parameter needed 
for every step of the workflow, even if they aren't running those steps.
Help the user out by providing sets of default parameters they can use.

## more notes on generalization difficulties

We are trying to use a generalized approach
that utilizes parameters for the input/output 
targets of the rule. That requires us to extract
parameters from the config dictionary and 
slice and dice them for the rules.

This extra work must happen outside of the rule,
because the slicing and dicing gives us all 
portions of the rule: the input files, the output 
targets, the singularity container to use,
the shell command, etc.

But if it happens outside the rule,
that means we are validating parameters
for a rule before we even know if we are 
running that rule.

If we aren't running that rule,
then when that rule runs its 
validation check of the parameters ,
it will fail, but that's okay because
we aren't running that rule.

But if we are running that rule,
the validation check failing would be
very bad, and we would want to inform the 
user of what changes they need to make.

But there's no way to do that, because
_the rule and the parameter validation are isolated._
This means the only time we can validate parameters 
is when we are totally in the dark about what 
we're doing.

This design is _extremely_ problematic for testing.

It also makes it _very_ difficult to help the user when 
parameter validation fails, which means,
we probably need to write a separate tool
to validate JSON or YAML files.

We'll have to end up implementing external validation
of the JSON/YAML input files (again, without any context
about what rules the user will be running in the workflow.)

