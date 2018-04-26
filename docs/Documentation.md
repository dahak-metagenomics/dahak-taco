# Documentation

This document covers the `taco` documentation,
how to improve it, how to build it, and how to 
update the Github Pages/ReadTheDocs pages for
`taco` documentation.

## Building

To build the documentation, you will need [mkdocs](http://www.mkdocs.org/).

```
pip install mkdocs
```

You will also need to check out the `mkdocs-material-dib` submodule
for the mkdocs documentation theme. 

To include submodules when running the clone command:

```
git clone --recursive <url>
```

To clone submodules in an existing repository, run:

```
git submodule update --init
```

Once that's finished, you can run the following command
from the current directory to build the documentation:

```
mkdocs build
```

This generates all static content in the `site/` directory.
To serve the documentation using a simple local HTTP server,
run:

```
mkdocs serve
```

## Updating Github Pages

See the [Setting Up Push-to-Deploy on Github Pages](https://github.com/dib-lab/mkdocs-material-dib#set-up-push-to-deploy-on-github-pages)
section of the [mkdocs-material-dib](https://github.com/dib-lab/mkdocs-material-dib)
documentation for instructions.



