# Changelog

All notable changes to <package name> are documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0).

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.0beta] - 2018-04-27

### Added

- Revamped documentation

- Added unit tests (run with nose, or nose collector via setup.py)
    - tests for success (uses taco-simple workflow repository)
    - tests for failure (incorrect usage)

- Tests can be run with `python setup.py test`

### Removed

- `goodies/` - not used, see [taco-simple](https://github.com/dahak-metagenomics/taco-simple)

## [0.3] - 2018-04-24

### Changed

- Abstraction for taco has been updated to facilitate testing.
    We are now separating the workflow details from taco itself.

- taco utility is now a command line tool, installed with setup.py 

- Workflows should now exist locally, taco anticipates a particular
    directory structure and will raise exceptions if things aren't
    in place

- This structure becomes more logical when we think about the
    alternative: bundling everything together requries dealing with
    in-memory Snakefiles, creating a temporary folder on disk to 
    extract and run, etc. Yikes.

### Removed

- Standalone taco script

- Docker files (moved to workflow repositories)

- Rule files (moved to workflow repositories)

### Fixed

- Add setup.py to make this a pip-installable, 
    semantically-versioned, testable, cross-platform
    package.
- Update the command line interface syntax to handle 
    verbs and command line options in a more logical fashion.

## [0.2] - 2018-04-19

### Added

- Revisiting read filtering to fix parameters
- Added tests (for now, dry runs)

### Fixed

## [0.1] - 2018-04-18

### Added 

- Completed read filtering workflow
- Added ability to use custom Dockerfile
- Previous work: implementing rules files for read filtering,
    implementing taco command line, adding documentation, etc.

### Changed

- Added `use_local` parameter (boolean: use a local docker image?)
- Added `local` parameter (name of local docker image to use)

## [List of Change Categories]

### Added 

### Changed

### Deprecated

### Removed

### Fixed

