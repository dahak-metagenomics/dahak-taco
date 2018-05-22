# Installation 

`taco` is installed using `setup.py`, and will be 
installed as a command-line utility on the system.
When we are finished you will be able to run the 
command 

```
$ taco --help
```

and see a `taco` help message.

## Requirements

`taco` requires the following software be installed:

* Python 3
* Conda
* Snakemake
* Singularity or Docker

To check that you are using Python 3, run:

```text
$ /usr/bin/env python --version
```

To test that Snakemake can be imported from Python, run:

```text
$ /usr/bin/env python -c 'import snakemake'
```

To check your version of singularity, run:

```text
$ which singularity
```

Scripts to install the above packages can be found
in the [`scripts/`](https://github.com/dahak-metagenomics/dahak-taco/tree/master/scripts) 
directory of dahak-taco.

## Clone 

Start by cloning a local copy of the repository:

```
git clone https://github.com/dahak-metagenomics/dahak-taco
```

By default, this will clone the `stable` branch.

To specify a particular branch, use the `-b` flag:

```
git clone -b master https://github.com/dahak-metagenomics/dahak-taco
```

To go to a particular tag, clone the repository first, then
check out the tag:

```
git clone https://github.com/dahak-metagenomics/dahak-taco
cd dahak-taco/
git checkout v1.0.0beta
```


## Build and Install

The next step is to build and install the `taco` source code using `setup.py`.
To install `taco` as a system-level executable, run:

```
$ python setup.py build install
```

To install `taco` as a user (recommended):

```
$ python setup.py install --user
```

Or install it into a virtual environment using either the 
setup.py or pip method:

```
$ virtualenv vp
$ source vp/bin/activate

# either:

$ vp/bin/pip install dahak_taco

# or:

$ vp/bin/python setup.py build install
```

This will install the taco command line utility as an 
executable program in Python's `bin` location. This 
location may or may not be on your path, and varies
depending on your Python environment, but should be in

```
$PYTHONHOME/bin
```

This path should be on your `$PATH` for you to be able to 
call `taco` from the command line.

## Run Tests

To run tests:

```
python setup.py test
```

## Full Circle

Now you can run the help command:

```
$ taco --help
```

Now let's move on to usage.
