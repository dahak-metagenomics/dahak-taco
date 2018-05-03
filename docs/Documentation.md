# Documentation

This document covers the `taco` documentation,
how to improve it, how to build it, and how to 
update the Github Pages/ReadTheDocs pages for
`taco` documentation.


## What You Need

This documentation uses [mkdocs](http://www.mkdocs.org/) and a variation
on the [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) theme
called [mkdocs-material-dib](https://github.com/dib-lab/mkdocs-material-dib).


## Building

To build the documentation, you will need to install mkdocs: 

```
pip install mkdocs
```

The `mkdocs-material-dib` theme is in this repository as a submodule,
so you will need to clone a copy of the submodule.

To include submodules when cloning the taco repository:

```
git clone --recursive <url>
```

To clone the submodule in an already-cloned repository, run:

```
git submodule update --init
```

Once that's finished, you can run the following command
from the current directory to build the documentation:

```
mkdocs build
```

This generates all static content in the `site/` directory.
To serve the documentation using a simple local HTTP server, run:

```
mkdocs serve
```


## Updating Github Pages

See the [Setting Up Push-to-Deploy on Github Pages](https://github.com/dib-lab/mkdocs-material-dib#set-up-push-to-deploy-on-github-pages)
section of the [mkdocs-material-dib](https://github.com/dib-lab/mkdocs-material-dib)
documentation for instructions.

