# fastqc dockerfile 

Date: 11 April 2018

Currently using this Dockerfile as a workaround to a problem with
fonts (of all things). Problem is with true type fonts not being
found in the container (happens when the report is complete and 
fastqc is generating its report).

Addressed in [this bioconda issue](https://github.com/bioconda/bioconda-recipes/issues/5026).

Resolved by adding 

```
sudo apt-get install ttf-dejavu
```

but [a PR to fix the issue](https://github.com/bioconda/bioconda-recipes/pull/8588) is in progress.

Build the docker image:

```
docker build -t dahak_fastqc .
```

Test out the image:

```
docker run -it dahak_fastqc fastqc -h
```

should print out fastqc help.
