# Tests

`taco` tests use the `unittest` module
(same underlying test framework that nose uses,
but without the nose wrapper).

All tests are located in the `tests/` directory
of the repository. They can be run through `setup.py`:

```
python setup.py test
```

The scope of the `taco` unit tests is to focus on 
testing basic functionality in taco - mainly checking
the use of different verbs and command line flags.

