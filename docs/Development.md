# Development

## Branches and Tags

There are two main branches for development in taco:
an active development branch that may break,
and an infrequently updated stable branch that 
points to the latest tested and verified version
of taco.

We utilize a two-track convention with branches - 
one development branch and one stable branch: 

* `master` (unstable) - this points to the latest commit on the 
    development branch of taco

* `stable` (stable) - this points to the latest commit on the 
    stable branch of taco

Branches for each release version also exist.
We create a branch for each version release 
to enable version-specific maintenance commits.
Release branches also follow the two-track method.
Release branches are named:

* `release/v0.0` (stable) - this contains all commits specific to
    release version 0.0 of taco

* `release/v0.0beta` (unstable) - this contains unstable development code
    for _preparing_ for release version 0.0 of taco (beta version)

The release branches use only the major and minor numbers,
but tags are used for each major, minor, and patch number.
The convention for naming tags in taco is the letter `v` 
followed by the version (major, minor, and patch) `v0.0.0`.

All tags for a major and minor version X.Y will point to 
commits on the `release/vX.Y` branch.

## Workflow

The normal workflow is to create a new branch 
to add features or fix features, and merge commits 
from that branch into `master`, then into 
`stable`, and eventually on into a versioned release.

### Adding New Features

To add new features, create a new branch using the `master` 
branch as a source, and make your commits on this branch.
When you're ready, run tests on the branch to ensure the 
modified code works as expected. Merge this code into
the `master` branch.

Once the code has been tested, checked for backwards 
compatibility, linted, minted, stamped, licensed, etc., 
it can be merged into the `stable` branch.

### Creating New Version

When you have commits in `stable` and are ready to
release them as a new version, create a new 
pre-release branch `release/v0.0beta` from the 
appropriate `stable` commit.

(If the features you want to add to a new version of taco 
are not in the `stable` branch yet, start by getting them 
into `stable`.)

You should *not* be doing regular development on the 
beta branches, but some hot-fix or workaround commits 
may be required, hence the unstable label. 

Once `release/v0.0beta` has been tested and is ready
for release, create a new branch `release/v0.0` 
for the stable release of version 0.0 of taco.

