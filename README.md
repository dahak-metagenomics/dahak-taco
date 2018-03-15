# dahak-taco

taco is an experimental command line interface for dahak workflows. 

when it is no longer experimental, we will `s/taco/dahak/`.

## Example Interfaces

taco is experimental.

some discussion occurring on dahak, [issue #61](https://github.com/dahak-metagenomics/dahak/issues/61#issuecomment-373041670).

User inputs:
* Input files, obvs.
* Parameter sets - the parameters with which I'm analyzing the data set
* Data sets - the files I am analyzing

Example:

```
# run a simple trim 
taco trim-reads mydata

# run a simple trim with "lenient" preset for parameters
taco trim-reads lenient mydata

# run a simple trim
# lenient parameters
# override quality cutoff 
taco trim-reads lenient mydata --qual-cutoff 30
```

## Tools

The [argparse](https://docs.python.org/3/library/argparse.html) 
library provides a nice way to create a sophisticated command line interface.

The [argcomplete](https://github.com/kislyuk/argcomplete) library
provides bash completion that integrates with Python and argparse.

## Principle: Helpful Output

One of the principles of command line utilities is, the user should 
get enough information from the command line interface to know 
what they should do, and the program should provide helpful error
messages and show help when things fail. 

(Start coding at the help functions. Define the structure.)

An example of how the program might provide helpful output to the user
to help guide them as to how to perform various workflows:

```
[user@host] $ taco trim-reads

              _            _                _     
    o O O  __| |   __ _   | |_     __ _    | |__  
   o      / _` |  / _` |  | ' \   / _` |   | / /  
  TS__[O] \__,_|  \__,_|  |_||_|  \__,_|   |_\_\  
 {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'


Task: Trim Reads
Description: This task uses trimmomatic and fastqc to trim sequence data.

Error: exactly one of (--fasta1 --fasta2 | --fasta-url) must be used.

Usage: dahak-cli --trim-reads (--fasta1=PATH_TO_FASTA1 --fasta2=PATH_TO_FASTA2 | --fasta-url=FASTA_URL)

    Optional flags: --output-file=PATH_TO_OUTPUT
```

