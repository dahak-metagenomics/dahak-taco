# Changelog

All notable changes to <package name> are documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0).

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

# [Unreleased Changes]

### Added 

### Changed

### Deprecated

### Removed

### Fixed

- Bug: when user-provided parameters are not correctly specified,
    dahak-taco silently uses default values without informing user
- Solution: implement YAML/JSON validation, tell user all possible parameters
    and which parameters were not specified

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

### Deprecated

### Removed

### Fixed
