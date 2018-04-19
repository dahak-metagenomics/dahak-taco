# Land Mines in Snakemake

## overview

the problem with snakemake is that it provides the user with
a very limited vocabulary and a limited subset of Python 
functionality. 

This makes it extremely difficult to "break out" of the 
rigid structure Snakemake sets up.

Further complicating the many caveats 
(this feature works, that feature doesn't;
you can do this, but only if you do that) 
is the fact that Snakemake is fixated on filenames.

This is a poor choice for a number of reasons. 
The workflow control happens entirely through filenames,
which seems crazy.



## details

The way rules are defined, and the fact that
you cannot define generic rules that perform a task.

For example, I can't have a rule that calls another rule.

This is some minor league stuff. If Snakemake can't handle
rules that call other rules, or handle calling rules by name,
instead of by target file, that makes it a lot less useful 
than make, and much more difficult to generalize.

Snakemake also forces the user to design the workflow
around long, abstract chains of filenames and workflow steps.
Again, everything fixates on filenames.


------

The many, many problems with `{}` and parameters and wildcards

----

The default config problem:
* if you misconfigure your configure file,
* the keys won't match what the program is looking for
* but if default keys are defined, it will seamlessly pick those up
* the problem is, you have no idea your original config file did not validate


From `pre_post_assessment.rule`:

```
A horrible last-minute discovery: 
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


-----

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

This error message is useless because the line it 
points to, as the line where the error occurs, 
is the line where we define the rule, like 

```
rule: myrule
```

So, basically no information about what's wrong
other than the name of the rule.

It's likely mixing wildcards, functions, and HTTP 
is bad, but it's unclear, and yet again it will just
waste a whole bunch of time to track this down.
a conditional this-doesn't-wor


------

Here is the latest error:
* you define a function in a file called util.py
* you import functions from util.py in taco
* the functions are (hsould be) available to all sub-calling functions

are they available?
* in a few of the rule files, they ARE
* however, they are not available in all rule files at any time

two passes:
* there seems to be two passes through each rule file happening 
* the first time through, the function is inherited from taco just fine
* the second time through, the function is NOT inherited from taco
* but, honestly, who knows???

further investigation:
* when you say "from .utils import func1, func2" in a snakemake file,
* you do not have access to func1 or func2
* apparently the problem is, you're living in snakemake namespace
* the solution is, you "from utils import func1, func2"
* what the hell? this is not even python-compliant.

not even going to keep wasting my time.
* the solution is stupid, but it's all we have left.
* hard-code a copy of every function in every workflow.
* import every function in every rule file.
* let someone else sort out this dumpster fire.

What does all of this mean?
* there is NO WAY to have separate snakefiles and workflows import common code
* this is absurd, how does a program do such a poor job of generalizing

Why snakemake wastes your time:
* You spend hours chasing down problems caused by features that are broken
* Or, at best, not as straightforward as advertised
* The documentation leaves out many really, really, really important caveats and details
* You should have more of these questions answered by the documentation 
* Instead, you get to spend hours "discovering" non-working features yourself










