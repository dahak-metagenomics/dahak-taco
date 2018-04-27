# Installation 

`taco` is installed using `setup.py`, and will be 
installed as a command-line utility on the system.
When we are finished you will be able to run the 
command 

```
$ taco --help
```

and see a `taco` help message.

## Clone 

Start by cloning a local copy of the repository:

```
git clone https://github.com/dahak-metagenomics/dahak-taco
```

You can specify a particular tag or branch with the 
clone command, or use the default `stable` branch.


## Build and Install

The next step is to build and install the `taco` source code
using `setup.py`:

```
$ python setup.py build
```

If you want to install taco as a system level module, run:

```
$ python setup.py install
```

If you want to install it as a user (recommended):

```
$ python setup.py install --user

$ python setup.py install --user --prefix=    # <-- this is required on mac
```

This will install the taco command line utility as an 
executable program in the Python `bin` location. This 
location may or may not be on your path, and varies
depending on your Python environment, but should be in

```
$PYTHONHOME/bin
```

This should be on your `$PATH` for you to be able to 
call `taco` from the command line.

## Run Tests

To run tests:

```
python setup.py test
```

