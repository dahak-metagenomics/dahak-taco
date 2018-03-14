# dahak-taco

taco is a command line interface for dahak workflows. 

Pick your ingredients and dig in!

```
              _            _                _     
    o O O  __| |   __ _   | |_     __ _    | |__  
   o      / _` |  / _` |  | ' \   / _` |   | / /  
  TS__[O] \__,_|  \__,_|  |_||_|  \__,_|   |_\_\  
 {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'

```

[ascii logo](http://patorjk.com/software/taag/#p=display&f=Train&t=dahak%0A)

## Example Interfaces

taco is experimental.

Here are some proposed behaviors:

### Subcommands

One example of how dahak might be implemented is to 
use subcommands:

```
taco taxclass A.txt B.txt \
    --optional1=/path/to/C.txt \
    --optional2=/path/to/D.txt \
    --do-this --not-that
```

### All Flags

An alternative method would be to pass flags
to a binary (and indicate which workflow 
to take with flags, possibly multiple binaries).

This workflow is entirely fictional:

```
taco --do-taxclass --do-sequence-trimming --do-annotations \
        --input-fq=A.fq.gz,B.fq.fz      \
        --kaiju-url=http://example.com  \
        --output-contigs=contigs.out    \
        --output-labels=labels.out      \
        --k-value=10                    \
        --trim-last=50                  \
        --nrounds=100
```


### Helpful Output

An example of how the program might provide helpful output to the user
to help guide them as to how to perform various workflows:

```
[user@host] $ dahak-taco --trim-reads

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

