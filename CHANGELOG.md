# Changelog

All notable changes to <package name> are documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0).

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

# [Unreleased Changes]

### Added 

### Changed

- Abstraction for taco has been updated to facilitate testing.
    We are now separating the workflow details from taco itself.
    The taco utility is a wrapper that's imported and run from the
    Python package namespace; it uses local folders and files
    to determine what workflow to run.
- This structure becomes more logical when we think about the
    alternative: bundling Snakefiles, storing them in memory,
    dumping the contents of each varible to a temporary file 
    structure, running Snakemake from the temporary file struture,
    moving data files, DEAR GOD PLEASE DONT MAKE ME DO THIS.

### Deprecated

### Removed

- Standalone taco script

### Fixed

- Add setup.py to make this a pip-installable, 
    semantically-versioned, testable, cross-platform
    package.
- Update the command line interface syntax to handle 
    verbs and command line options in a more logical fashion.

# [0.2] - 2018-04-19

### Added

- Revisiting read filtering to fix parameters
- Added tests (for now, dry runs)

### Fixed

# [0.1] - 2018-04-18

### Added 

- Completed read filtering workflow
- Added ability to use custom Dockerfile
- Previous work: implementing rules files for read filtering,
    implementing taco command line, adding documentation, etc.

### Changed

- Added `use_local` parameter (boolean: use a local docker image?)
- Added `local` parameter (name of local docker image to use)

# [List of Change Categories]

### Added 

### Changed

### Deprecated

### Removed

### Fixed

